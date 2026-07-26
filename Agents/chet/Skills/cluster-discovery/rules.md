# Cluster Discovery -- Rules

- Never score or contact individual entities within a group -- Chet writes clusters, not
  individual leads or events
- Don't re-derive dependency for a group whose existence is already documented
- Skip a paused or closed group entirely -- no re-mining, no discovery expansion
- Mine per qualifying group, not per individual event or entity
- Every group clearing your gap-volume threshold gets its own candidate record -- never
  collapse multiple groups into one
- A signal that doesn't match any mapped capability, seen once, isn't enough to log --
  seen more than once, log it as a build candidate instead of forcing a cluster
- When a policy-driven signal produces one matching group, check for a second, distinct
  group before treating the search as done -- one root event can create more than one
  real cluster
- No em dashes in any output

## What this skill does not do
- Score individual prospects or organizations
- Contact anyone, directly or on your behalf
- Re-implement mandate/compliance signal sourcing, which already exists as its own
  public skill -- see `Agents/chet/Skills/mandate-signals.md` pointing to
  `Skills/mandate-mapping`
- Re-implement grant/funding signal sourcing, which already exists as its own public
  skill -- see `Agents/chet/Skills/community-grant-signals.md` pointing to
  `Skills/community-grant-radar`

This skill consumes signals from wherever you're sourcing them; it doesn't re-derive how
to find mandate or grant signals in the first place.
