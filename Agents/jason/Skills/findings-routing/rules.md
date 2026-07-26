# Findings Routing -- Rules

- Nothing acts on a finding until it has been reviewed at your configured destination --
  this is the boundary every other Jason skill depends on
- A fix opens as a PR only if it matches your own `routing.rule_based` list -- when in
  doubt, treat it as a judgment call instead
- Never merge a PR -- opening one is as far as any rule-based fix goes automatically
- Never post to any destination other than the one configured in
  `notifications.destination`
- Never take a judgment call's proposed option and apply it -- proposing options is not
  the same as choosing one
- Every finding carries its exact page, section, or file -- a finding with no citation
  doesn't ship
- PASSes are a count, not a list -- don't pad a report with detail nobody needs to read
- If a run produces nothing, post a short confirmation instead of an empty-shell report
- No em dashes in any output

## What this skill does not do
- Generate its own findings -- it only formats and routes what other skills produce
- Decide which lane a fix belongs in beyond what your own config already specifies
- Contact anyone outside your configured notification destination
