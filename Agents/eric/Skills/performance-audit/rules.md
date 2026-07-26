# Performance Audit -- Rules

- Compare against your own `performance_thresholds`, not a generic default, whenever your
  config sets a stricter number
- Header and image-attribute fixes go out as a PR to staging, never committed directly
- A Core Web Vitals regression with no clear one-line fix is a notify with analysis, not
  a guess-and-PR
- Zero-finding audits stay silent per `notifications.silent_on_zero_findings` -- don't
  post a status update just to confirm nothing happened
- No em dashes in any output
