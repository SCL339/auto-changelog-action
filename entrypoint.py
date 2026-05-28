#!/usr/bin/env python3
"""
Auto Changelog Action — Generates a beautiful CHANGELOG.md from merged PRs.

Queries the GitHub API for merged pull requests, groups them by label,
and outputs a formatted changelog. Designed to run as a GitHub Composite Action.
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime
from collections import OrderedDict


def parse_args():
    parser = argparse.ArgumentParser(description="Generate a CHANGELOG from merged PRs")
    parser.add_argument("--token", required=True, help="GitHub token")
    parser.add_argument("--output", default="CHANGELOG.md", help="Output file path")
    parser.add_argument("--repo", required=True, help="Repository (owner/repo)")
    parser.add_argument("--header", default="# Changelog\n\nAll notable changes to this project will be documented in this file.")
    parser.add_argument("--unreleased", default="## [Unreleased]")
    parser.add_argument("--include-pr-numbers", default="true", choices=["true", "false"])
    parser.add_argument("--group-labels", default='{"feature":"🚀 Features","enhancement":"✨ Enhancements","bug":"🐛 Bug Fixes","documentation":"📖 Documentation","dependencies":"📦 Dependencies","breaking":"⚠️ Breaking Changes","chore":"🔧 Maintenance"}')
    parser.add_argument("--sort-by", default="label", choices=["label", "date"])
    parser.add_argument("--max-entries", default="0")
    return parser.parse_args()


def github_request(url, token):
    """Make an authenticated GitHub API request with pagination."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "auto-changelog-action/1.0",
    }
    all_data = []
    per_page = 100

    while url:
        sep = "&" if "?" in url else "?"
        page_url = f"{url}{sep}per_page={per_page}"
        req = urllib.request.Request(page_url, headers=headers)
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode())
                if isinstance(data, list):
                    all_data.extend(data)
                else:
                    return data
        except urllib.error.HTTPError as e:
            print(f"::error::GitHub API error {e.code} for {url}: {e.read().decode()}", file=sys.stderr)
            sys.exit(1)

        # Check for next page
        link_header = resp.headers.get("Link", "")
        next_url = None
        for part in link_header.split(","):
            if 'rel="next"' in part:
                next_url = part.split(";")[0].strip().strip("<>")
        url = next_url

    return all_data


def generate_changelog(prs, group_labels_map, include_pr_numbers, sort_by, max_entries):
    """Group PRs by label and format the changelog."""
    # Build grouped entries
    groups = OrderedDict()
    for label_key in ["breaking", "feature", "enhancement", "bug", "documentation", "dependencies", "chore"]:
        if label_key in group_labels_map:
            groups[label_key] = []

    other_label = "Other"
    groups[other_label] = []

    label_keys = {v.lower(): k for k, v in group_labels_map.items()}
    label_keys.update({k.lower(): k for k in group_labels_map})

    prs_to_process = prs
    if max_entries > 0:
        prs_to_process = prs[:max_entries]

    for pr in prs_to_process:
        pr_labels = [lbl["name"].lower() for lbl in pr.get("labels", [])]
        assigned = False
        for key in label_keys:
            if key in pr_labels:
                canonical = label_keys[key]
                if canonical in group_labels_map:
                    groups.setdefault(canonical, [])
                    groups[canonical].append(pr)
                else:
                    groups.setdefault(canonical, [])
                    groups[canonical].append(pr)
                assigned = True
                break
        if not assigned:
            groups[other_label].append(pr)

    # Sort within groups
    for key in groups:
        if sort_by == "date":
            groups[key].sort(key=lambda p: p.get("merged_at", ""), reverse=True)
        else:
            groups[key].sort(key=lambda p: p.get("title", ""))

    # Format
    lines = []
    group_order = ["breaking", "feature", "enhancement", "bug", "documentation", "dependencies", "chore", other_label]

    for group_key in group_order:
        if group_key not in groups or not groups[group_key]:
            continue

        heading = group_labels_map.get(group_key, group_key)
        lines.append(f"\n### {heading}\n")
        for pr in groups[group_key]:
            title = pr.get("title", "Untitled")
            number = pr.get("number", "")
            pr_url = pr.get("html_url", f"https://github.com/{pr.get('base', {}).get('repo', {}).get('full_name', '')}/pull/{number}")
            author = pr.get("user", {}).get("login", "unknown")
            if include_pr_numbers:
                lines.append(f"- {title} [#{number}]({pr_url}) (@{author})")
            else:
                lines.append(f"- {title} (@{author})")

    return "\n".join(lines)


def main():
    args = parse_args()

    # Parse group labels JSON
    try:
        group_labels_map = json.loads(args.group_labels)
    except json.JSONDecodeError:
        print("::error::Invalid JSON for group-labels input", file=sys.stderr)
        sys.exit(1)

    max_entries = int(args.max_entries)
    include_pr_numbers = args.include_pr_numbers.lower() == "true"

    # Fetch merged PRs
    api_url = f"https://api.github.com/repos/{args.repo}/pulls"
    print(f"::debug::Fetching merged PRs from {api_url}", file=sys.stderr)

    params = "state=closed&sort=updated&direction=desc"
    all_prs = github_request(f"{api_url}?{params}", args.token)

    # Filter to merged PRs only
    merged_prs = [pr for pr in all_prs if pr.get("merged_at")]
    print(f"::debug::Found {len(merged_prs)} merged PRs", file=sys.stderr)

    if not merged_prs:
        print("::notice::No merged PRs found. Creating empty changelog.")
        with open(args.output, "w") as f:
            f.write(args.header.replace("\\n", "\n"))
            f.write(f"\n\n{args.unreleased}\n\n")
            f.write("No changes yet.\n")
        print(f"::notice::Created {args.output}")
        return

    # Generate changelog content
    changelog_body = generate_changelog(merged_prs, group_labels_map, include_pr_numbers, args.sort_by, max_entries)

    # Write output
    today = datetime.utcnow().strftime("%Y-%m-%d")
    unreleased_section = f"\n{args.unreleased}\n\n"
    unreleased_section += changelog_body

    full_content = args.header.replace("\\n", "\n")
    full_content += f"\n\n{unreleased_section}\n"

    with open(args.output, "w") as f:
        f.write(full_content)

    print(f"::notice::Changelog written to {args.output}")


if __name__ == "__main__":
    main()
