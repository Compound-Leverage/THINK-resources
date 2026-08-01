# Eric, Infrastructure Lead (ops-team) -- Deliverable Templates

Blank version of the document Eric produces. Use it directly (fill in your own data by
hand) or as the reference format the plugin's output should match. Every `[bracket]` is
a placeholder.

---

### Infra/Deploy Audit Report

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

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit [compoundleverage.com](https://compoundleverage.com).
