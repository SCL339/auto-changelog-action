1|     1|     1|# Auto Changelog Action 🚀
     2|     2|     2|
     3|     3|     3|[![GitHub Release](https://img.shields.io/github/v/release/SCL339/auto-changelog-action?style=flat-square&logo=github)](https://github.com/SCL339/auto-changelog-action/releases)
     4|     4|     4|[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-Auto%20Changelog-blue?style=flat-square&logo=githubactions)](https://github.com/marketplace/actions/auto-changelog-action)
     5|     5|     5|[![MIT License](https://img.shields.io/github/license/SCL339/auto-changelog-action?style=flat-square)](LICENSE)
     6|     6|     6|[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)
     7|     7|     7|
     8|     8|     8|---
     9|     9|     9|
    10|    10|    10|
    11|    11|    11|- **Customizable** — Configure grouping labels, sort order, output path, and more
    12|    12|    12|- **Beautiful output** — Emoji headings, markdown links, and clean formatting
    13|    13|    13|- **CI/CD ready** — Runs in seconds as part of any workflow
    14|    14|    14|
    15|    15|    15|---
    16|    16|    16|
    17|    17|    17|
    18|    18|    18|  push:
    19|    19|    19|    branches: [main]
    20|    20|    20|  workflow_dispatch:
    21|    21|    21|
    22|    22|    22|permissions:
    23|    23|    23|  contents: write
    24|    24|    24|  pull-requests: read
    25|    25|    25|
    26|    26|    26|jobs:
    27|    27|    27|  changelog:
    28|    28|    28|    runs-on: ubuntu-latest
    29|    29|    29|    steps:
    30|    30|    30|      - uses: actions/checkout@v4
    31|    31|    31|      - uses: SCL339/auto-changelog-action@v1.0.0
    32|    32|    32|        with:
    33|    33|    33|          github-token: ${{ secrets.GITHUB_TOKEN }}
    34|    34|    34|          output-file: CHANGELOG.md
    35|    35|    35|      - uses: stefanzweifel/git-auto-commit-action@v5
    36|    36|    36|        with:
    37|    37|    37|          commit_message: 'docs: update CHANGELOG.md'
    38|    38|    38|          file_pattern: CHANGELOG.md
    39|    39|    39|```
    40|    40|    40|
    41|    41|    41|---
    42|    42|    42|
    43|    43|    43|
    44|    44|    44|- uses: SCL339/auto-changelog-action@v1.0.0
    45|    45|    45|  with:
    46|    46|    46|    github-token: ${{ secrets.GITHUB_TOKEN }}
    47|    47|    47|    output-file: docs/CHANGELOG.md
    48|    48|    48|    header: |
    49|    49|    49|      # Changelog
    50|    50|    50|      
    51|    51|    51|      All notable changes to this project.
    52|    52|    52|    unreleased-label: '## [Unreleased]'
    53|    53|    53|    include-pr-numbers: 'true'
    54|    54|    54|    sort-by: 'label'
    55|    55|    55|    max-entries: '50'
    56|    56|    56|    group-labels: |
    57|    57|    57|      {
    58|    58|    58|        "feature": "🚀 Features",
    59|    59|    59|        "enhancement": "✨ Enhancements",
    60|    60|    60|        "bug": "🐛 Bug Fixes",
    61|    61|    61|        "documentation": "📖 Documentation",
    62|    62|    62|        "dependencies": "📦 Dependencies",
    63|    63|    63|        "breaking": "⚠️ Breaking Changes",
    64|    64|    64|        "chore": "🔧 Maintenance"
    65|    65|    65|      }
    66|    66|    66|```
    67|    67|    67|
    68|    68|    68|---
    69|    69|    69|
    70|    70|    70|
    71|    71|    71||-------|-------------|----------|---------|
    72|    72|    72|| `github-token` | GitHub token with PR read access | No | `${{ github.token }}` |
    73|    73|    73|| `output-file` | Path for the generated changelog | No | `CHANGELOG.md` |
    74|    74|    74|| `header` | Custom header text for the changelog | No | `# Changelog\n\n...` |
    75|    75|    75|| `unreleased-label` | Heading for unreleased changes | No | `## [Unreleased]` |
    76|    76|    76|| `include-pr-numbers` | Whether to include PR numbers | No | `true` |
    77|    77|    77|| `group-labels` | JSON map of label → heading | No | *(see above)* |
    78|    78|    78|| `sort-by` | Sort by `label` or `date` | No | `label` |
    79|    79|    79|| `max-entries` | Max PRs to include (0 = all) | No | `0` |
    80|    80|    80|
    81|    81|    81|---
    82|    82|    82|
    83|    83|    83|
    84|    84|    84|| `enhancement` | ✨ Enhancements |
    85|    85|    85|| `bug` | 🐛 Bug Fixes |
    86|    86|    86|| `documentation` | 📖 Documentation |
    87|    87|    87|| `dependencies` | 📦 Dependencies |
    88|    88|    88|| `breaking` | ⚠️ Breaking Changes |
    89|    89|    89|| `chore` | 🔧 Maintenance |
    90|    90|    90|
    91|    91|    91|---
    92|    92|    92|
    93|    93|    93|
    94|    94|    94|# Changelog
    95|    95|    95|
    96|    96|    96|---
    97|    97|    97|
    98|    98|    98|
    99|    99|    99|- Add dark mode support [#42](https://github.com/owner/repo/pull/42) (@octocat)
   100|   100|   100|- New search endpoint [#38](https://github.com/owner/repo/pull/38) (@octocat)
   101|   101|   101|
   102|   102|   102|### 🐛 Bug Fixes
   103|   103|   103|- Fix null pointer in login flow [#35](https://github.com/owner/repo/pull/35) (@octocat)
   104|   104|   104|
   105|   105|   105|### 📦 Dependencies
   106|   106|   106|- Bump actions/setup-python from 4 to 5 [#33](https://github.com/owner/repo/pull/33) (@dependabot)
   107|   107|   107|```
   108|   108|   108|
   109|   109|   109|---
   110|   110|   110|
   111|   111|   111|action.git
   112|   112|   112|cd auto-changelog-action
   113|   113|   113|# The action is Python-based — no build step needed
   114|   114|   114|# Test locally:
   115|   115|   115|python3 entrypoint.py --token $GITHUB_TOKEN --repo SCL339/auto-changelog-action
   116|   116|   116|```
   117|   117|   117|
   118|   118|   118|---
   119|   119|   119|
   120|   120|   120|ARKER
   121|   121|   121|- 🚀 **Deploy your frontend** on [Vercel](https://vercel.com/?utm_source=scl339&utm_campaign=oss)
   122|   122|   122|- ⭐ **Star this repo** to help others discover it
   123|   123|   123|
   124|   124|   124|
   125|   125|   125|---
   126|   126|   126|
   127|   127|   127|
   128|   128|   128|

---

## 🤝 赞助支持 (Sponsor)

如果这个项目对你有帮助，可以请我喝杯咖啡 ☕

- 💖 **支付宝 (Alipay)**: `18559219554` | 邮箱联系: `530765059@qq.com`
- ☁️ **DigitalOcean 联盟链接**: [免费 $200 额度](https://www.digitalocean.com/?refcode=scl339-01&utm_campaign=Referral_Invite&utm_medium=opensource&utm_source=SCL339)
- ⭐ **在 GitHub 上点 Star** 帮助更多人发现这个项目

## 📄 License
