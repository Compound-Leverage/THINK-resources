# Content QA -- Rules

- Classify every page before auditing it -- the H1 rule and proposal count both depend
  on page type
- Product pages get 2 proposed H1 options when flagged; utility pages get 1
- Never rewrite the value proposition, tone, audience, or offer -- proposals work within
  the page's existing direction
- Never propose a replacement H1 that contradicts the page's own subhead
- Copy-consistency only flags divergence from an approved line already on record in your
  site standards -- it does not judge new copy with no approved equivalent to compare
  against
- Whether copy is good is a brand decision, not this skill's call -- flag divergence,
  don't rewrite for quality
- Skip anything matching your config's `page_types.excluded_patterns` entirely -- no
  classification, no H1 audit, no copy check
- No em dashes in any output

## What this skill does not do
- Decide which H1 option ships -- that's a judgment call routed to you via
  `Skills/findings-routing/`
- Check technical SEO, redirects, or link health -- see `Skills/site-audit/`
- Invent a terminology table or brand voice rule -- both come from your own site
  standards file
