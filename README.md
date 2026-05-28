# Auto Changelog Action 🚀

[![GitHub Release](https://img.shields.io/github/v/release/SCL339/auto-changelog-action?style=flat-square&logo=github)](https://github.com/SCL339/auto-changelog-action/releases)
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-Auto%20Changelog-blue?style=flat-square&logo=githubactions)](https://github.com/marketplace/actions/auto-changelog-action)
[![MIT License](https://img.shields.io/github/license/SCL339/auto-changelog-action?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)

A GitHub Action that **automatically generates a beautiful, well-organized CHANGELOG.md** from your merged pull requests. It groups changes by label (features, bug fixes, dependencies, etc.) and includes PR numbers, authors, and links.

> ✨ Part of the [SCL339](https://github.com/SCL339) open-source ecosystem.

---

## Features ✨

- **Label-based grouping** — Automatically groups PRs by labels (feature, bug, dependencies, etc.)
- **Sane defaults** — Works out of the box with zero configuration
- **Customizable** — Configure grouping labels, sort order, output path, and more
- **Beautiful output** — Emoji headings, markdown links, and clean formatting
- **CI/CD ready** — Runs in seconds as part of any workflow

## Usage 📦

### Basic

Add this step to your GitHub Actions workflow:

```yaml
name: Generate Changelog

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: write
  pull-requests: read

jobs:
  changelog:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: SCL339/auto-changelog-action@v1.0.0
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          output-file: CHANGELOG.md
      - uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: 'docs: update CHANGELOG.md'
          file_pattern: CHANGELOG.md
```

### Full Example with All Options

```yaml
- uses: SCL339/auto-changelog-action@v1.0.0
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    output-file: docs/CHANGELOG.md
    header: |
      # Changelog
      
      All notable changes to this project.
    unreleased-label: '## [Unreleased]'
    include-pr-numbers: 'true'
    sort-by: 'label'
    max-entries: '50'
    group-labels: |
      {
        "feature": "🚀 Features",
        "enhancement": "✨ Enhancements",
        "bug": "🐛 Bug Fixes",
        "documentation": "📖 Documentation",
        "dependencies": "📦 Dependencies",
        "breaking": "⚠️ Breaking Changes",
        "chore": "🔧 Maintenance"
      }
```

## Inputs ⚙️

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `github-token` | GitHub token with PR read access | No | `${{ github.token }}` |
| `output-file` | Path for the generated changelog | No | `CHANGELOG.md` |
| `header` | Custom header text for the changelog | No | `# Changelog\n\n...` |
| `unreleased-label` | Heading for unreleased changes | No | `## [Unreleased]` |
| `include-pr-numbers` | Whether to include PR numbers | No | `true` |
| `group-labels` | JSON map of label → heading | No | *(see above)* |
| `sort-by` | Sort by `label` or `date` | No | `label` |
| `max-entries` | Max PRs to include (0 = all) | No | `0` |

## Label to Heading Mapping 🏷️

Default mapping (override with `group-labels`):

| Label | Heading |
|-------|---------|
| `feature` | 🚀 Features |
| `enhancement` | ✨ Enhancements |
| `bug` | 🐛 Bug Fixes |
| `documentation` | 📖 Documentation |
| `dependencies` | 📦 Dependencies |
| `breaking` | ⚠️ Breaking Changes |
| `chore` | 🔧 Maintenance |

Any PR without a matching label goes under **"Other"**.

## Example Output 📄

```markdown
# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### 🚀 Features
- Add dark mode support [#42](https://github.com/owner/repo/pull/42) (@octocat)
- New search endpoint [#38](https://github.com/owner/repo/pull/38) (@octocat)

### 🐛 Bug Fixes
- Fix null pointer in login flow [#35](https://github.com/owner/repo/pull/35) (@octocat)

### 📦 Dependencies
- Bump actions/setup-python from 4 to 5 [#33](https://github.com/owner/repo/pull/33) (@dependabot)
```

## Related Projects 🔗

Check out other [SCL339](https://github.com/SCL339) tools:

- [md-slides](https://github.com/SCL339/md-slides) — Markdown-to-HTML presentation tool (slidev-lite)
- [pr-labeler-action](https://github.com/SCL339/pr-labeler-action) — Auto-label PRs based on changed file paths

## Development 🛠️

```bash
git clone https://github.com/SCL339/auto-changelog-action.git
cd auto-changelog-action
# The action is Python-based — no build step needed
# Test locally:
python3 entrypoint.py --token $GITHUB_TOKEN --repo SCL339/auto-changelog-action
```

## License 📄

MIT — see [LICENSE](LICENSE) for details.
