# Web Consistency Audit -- Workflow

Audits your live site, or a pending change to it, against your own style guide.
Flags deviations and routes rule-based fixes to your own PR flow, judgment calls to
you.

## Scope

Runs against either:
- Your live site, on a recurring cadence (see `hooks/hook-map.md`)
- A specific pull request diff, right before merge, typically triggered by
  `Skills/web-spec-handoff/` after a build step opens a PR

## What it checks

| Check | Rule |
|---|---|
| Inline style usage | Only where your own design system's documented patterns already use inline styles |
| CSS/class usage | No undocumented utility classes outside your own system |
| CTA count | One per page, unless your own guide documents an exception |
| CTA destination | Primary CTA points to `web.primary_cta_destination` from your config |
| Em dashes | None, anywhere |
| Typography/spacing tokens | Must match your own design system's tokens, not hardcoded values |
| Component reuse | Repeated patterns use existing components from `web.component_library_path`, not duplicated markup |

Add or adjust checks to match whatever your own style guide actually documents,
this table is a starting point, not a fixed list.

## Sampling rule

Check every product or lead-generation page on every run. Check utility pages on a
slower cadence (monthly is a reasonable default), your own judgment call.

## Output format

```
PAGE: [path]
DEVIATION: [what's wrong, citing the exact element or pattern]
PROPOSED FIX: [what would fix it] -> [routed to your PR flow, or flagged if it's a judgment call]
```

## Findings routing

- Rule-based deviations (wrong destination, deprecated class, hardcoded value
  instead of a token, an em dash): route straight into your own PR flow if you
  already trust that pattern, a human still merges
- Judgment calls (a pattern gap, an ambiguous deviation, something your style guide
  doesn't clearly cover): route to `Skills/style-guide-proposal/`, not a silent fix

## Output

A list of findings per the format above, plus routed fixes or proposals. If nothing
deviates, say so plainly rather than manufacturing a finding.
