# Auto Changelog Action 🚀

[![GitHub Release](https://img.shields.io/github/v/release/SCL339/auto-changelog-action?style=flat-square&logo=github)](https://github.com/SCL339/auto-changelog-action/releases)
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-Auto%20Changelog-blue?style=flat-square&logo=githubactions)](https://github.com/marketplace/actions/auto-changelog-action)
[![MIT License](https://img.shields.io/github/license/SCL339/auto-changelog-action?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)

---

- **Customizable** — Configure grouping labels, sort order, output path, and more
- **Beautiful output** — Emoji headings, markdown links, and clean formatting
- **CI/CD ready** — Runs in seconds as part of any workflow

---

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

---

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

---

|-------|-------------|----------|---------|
| `github-token` | GitHub token with PR read access | No | `${{ github.token }}` |
| `output-file` | Path for the generated changelog | No | `CHANGELOG.md` |
| `header` | Custom header text for the changelog | No | `# Changelog\n\n...` |
| `unreleased-label` | Heading for unreleased changes | No | `## [Unreleased]` |
| `include-pr-numbers` | Whether to include PR numbers | No | `true` |
| `group-labels` | JSON map of label → heading | No | *(see above)* |
| `sort-by` | Sort by `label` or `date` | No | `label` |
| `max-entries` | Max PRs to include (0 = all) | No | `0` |

---

| `enhancement` | ✨ Enhancements |
| `bug` | 🐛 Bug Fixes |
| `documentation` | 📖 Documentation |
| `dependencies` | 📦 Dependencies |
| `breaking` | ⚠️ Breaking Changes |
| `chore` | 🔧 Maintenance |

---

# Changelog

---

- Add dark mode support [#42](https://github.com/owner/repo/pull/42) (@octocat)
- New search endpoint [#38](https://github.com/owner/repo/pull/38) (@octocat)

### 🐛 Bug Fixes
- Fix null pointer in login flow [#35](https://github.com/owner/repo/pull/35) (@octocat)

### 📦 Dependencies
- Bump actions/setup-python from 4 to 5 [#33](https://github.com/owner/repo/pull/33) (@dependabot)
```

---

action.git
cd auto-changelog-action
# The action is Python-based — no build step needed
# Test locally:
python3 entrypoint.py --token $GITHUB_TOKEN --repo SCL339/auto-changelog-action
```

---

- 🚀 **Deploy your frontend** on [Vercel](https://vercel.com/?utm_source=scl339&utm_campaign=oss)
- ⭐ **Star this repo** to help others discover it

---

---

## 🤝 赞助支持 (Sponsor)

如果这个项目对你有帮助，可以请我喝杯咖啡 ☕

- 💖 **支付宝 (Alipay)**: `18559219554` | 邮箱联系: `530765059@qq.com`
- ☁️ **DigitalOcean 联盟链接**: [免费 $200 额度](https://www.digitalocean.com/?refcode=scl339-01&utm_campaign=Referral_Invite&utm_medium=opensource&utm_source=SCL339)
- ⭐ **在 GitHub 上点 Star** 帮助更多人发现这个项目

## 📄 License