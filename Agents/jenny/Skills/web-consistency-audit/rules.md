# Web Consistency Audit -- Rules

- Never push a fix directly, rule-based fixes go into your own PR flow, a human
  merges
- Never silently fix a judgment call, route it through
  `Skills/style-guide-proposal/` instead
- Check against your own style guide's actual documented patterns, don't invent a
  rule that isn't written down somewhere you can point to
- If nothing deviates, report that plainly rather than manufacturing a finding to
  justify the run
- No em dashes in any output

## What this skill does not do
- Write or push code itself
- Decide whether a pattern gap becomes a new design-system rule, that's
  `Skills/style-guide-proposal/`'s call, routed to you
- Audit produced marketing assets (thumbnails, decks, social graphics), that's
  `Skills/brand-asset-audit/`
