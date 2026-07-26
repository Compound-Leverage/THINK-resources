# Performance Audit -- Workflow

Runs a Lighthouse (or equivalent) pass against your production site, scores Core Web
Vitals, and routes fixes. Performance regressions are an infrastructure problem -- they
ship in deploys and get fixed in deploys.

## Pages to audit

Use `performance_thresholds.priority_pages` from your filled-in config. A reasonable
default order:
1. Homepage
2. Your primary conversion page
3. Any page flagged in a recent design or QA review
4. Representative pages for your other main sections

## Step 1: Run the check

```bash
npx lighthouse [YOUR SITE URL] --output json --chrome-flags="--headless" --only-categories=performance,accessibility,seo
```

Or use your CDN provider's own web analytics via its API/MCP if available.

Target scores come from `performance_thresholds` in your config
(`lighthouse_performance_min`, `lighthouse_accessibility_min`, `lighthouse_seo_min`).

## Step 2: Core Web Vitals

| Metric | Good | Needs work | Poor |
|---|---|---|---|
| LCP | < 2.5s | 2.5-4s | > 4s |
| CLS | < 0.1 | 0.1-0.25 | > 0.25 |
| INP | < 200ms | 200-500ms | > 500ms |
| FCP | < 1.8s | 1.8-3s | > 3s |

Compare against your own `performance_thresholds` values, not just the generic bands
above -- your config's numbers win if they're stricter.

## Step 3: Common fixes and routing

| Issue | Fix | Routing |
|---|---|---|
| Missing cache headers on static assets | Update your headers config | PR to staging |
| Images not using a modern format or missing width/height | Update image attributes | PR to staging |
| Render-blocking JS (non-critical) | Add `defer` or `type="module"` | PR to staging |
| LCP over your threshold on a priority page | Investigate and report | Notify with analysis |
| CLS over your threshold on any page | Investigate and report | Notify with analysis |
| Any priority page scoring well below target | Notify immediately | |

## Step 4: Cache headers check

Verify your headers config (e.g. a `_headers` file, or your provider's cache-rules
equivalent) matches `caching_rules` in your config:

```
/assets/*
  Cache-Control: public, max-age=31536000, immutable

/*.js
  Cache-Control: public, max-age=31536000, immutable

/*.css
  Cache-Control: public, max-age=31536000, immutable
```

If missing or incorrect, open a PR to staging with the corrected config.

## Output
See `Templates/eric-infrastructure.md`'s Infra/Deploy Audit Report for the combined
output format this and the other audit skills share.

**Notification rule:** post to your notification destination only if something needs
attention or a PR was opened. If every score clears its target and nothing was fixed,
log the run and post nothing, per `notifications.silent_on_zero_findings` in your
config. Zero-finding audits are silent.
