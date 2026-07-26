# Ops Team (ops-team-open): Deliverable Templates

Blank versions of the documents Eric, Jason, and Jenny produce. Use these directly (fill
in your own data by hand) or as the reference format the plugin's outputs should match.
Every `[bracket]` is a placeholder.

---

### Eric, Infra Lead: Infra/Deploy Audit Report

Produced on a deploy event or an on-demand/recurring audit.

```
Infra Audit: [date]
Deploy checked: [commit SHA / deploy ID, or "N/A, scheduled audit, no new deploy"]

Performance thresholds: [LCP / CLS / INP / bundle size vs. performance_thresholds]: [Pass / Regression, cite the delta]
Caching rules: [Pass / Flag, describe against caching_rules]
DNS state: [Pass / Flag, describe]
GitHub Actions: [failures or drift found, or "none"]

Config fix PRs opened to staging: [PR URL(s), or "none"]
Needs owner sign-off: [DNS change / production promotion / Worker or runtime logic change, describe, or "none"]
```

---

### Jason, QA Reviewer: Post-Deploy Audit Report

One row per finding. Cite the exact page/section, every time.

```
QA Audit: [date]
Pages checked: [count / list, or "full site"]

| Finding | Severity | Page/Section | Category | Action |
|---|---|---|---|---|
| [description] | [Critical / High / Medium / Low] | [exact page/section] | [Rule-based fix / Judgment call] | [PR URL / Flagged to owner] |

Changelog: [what was fixed, with PR links, or "none this run"]
Judgment calls flagged to owner: [list, or "none"]
```

---

### Jenny, Design Lead: Asset/Spec Handoff

Section headers below match the delivery types described in
`skills/jenny-head-of-design/SKILL.md`: asset delivery, web spec, or brand audit.

```
[Asset/Spec Name]: Design Handoff
Date: [date]
Brief or audit trigger: [link to the request this traces back to]

Type: [Asset delivered / Web spec / Brand audit]
Delivery: [Drive share link, or "N/A, spec or findings below"]

## Spec (if web spec)
[Markdown spec for dev handoff: layout, components, copy blocks, sizing]

## Brand audit findings (if audit)
[Off-brand items flagged, citing the exact asset or page, against my-brand-guidelines.md]

Proposed design-system changes: [describe, or "none"], routed to owner for approval before execution
```

---

## Questions

Contact [marvin@compoundleverage.co](mailto:marvin@compoundleverage.co) or visit [compoundleverage.com](https://compoundleverage.com).
