# Site Audit -- Rules

- Redirect chain collapse and removing a redirect for a source that never existed are
  rule-based -- hand off to `Skills/findings-routing/` for a PR
- A redirect conflict (source file still exists) or a dead destination (ambiguous
  correct target) is a judgment call -- propose your best guess, never act on it
- Uptime and broken-link checks flag 4xx/5xx only -- a 3xx is informational, not a flag
- Performance checks flag code-level patterns only -- this skill does not run a
  Lighthouse audit or claim to measure real user performance
- SEO and LLM-discoverability checks judge presence and structure, never copy quality --
  whether title/description text is good is a brand decision, not this skill's call
- Secondary-property audits sample recent content only (your configured sample size and
  window) -- never re-audit the full archive on every run
- Search console monitoring never auto-resolves a manual action or mobile usability
  issue -- both always route to manual review
- Broken-link checks are internal-only by default -- external link rot is a separate,
  optional cadence, not bundled into every run
- No em dashes in any output

## What this skill does not do
- Rewrite H1s or judge copy quality -- see `Skills/content-qa/`
- Scan for credentials or committed secrets -- see `Skills/security-audit/`
- Take any action beyond what `routing.rule_based` in your config explicitly allows
