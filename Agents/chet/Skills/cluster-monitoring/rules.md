# Cluster Monitoring -- Rules

- Never send external communications or contact anyone -- outreach is owned by whatever
  part of your own process handles it once a cluster advances, not this skill
- Don't apply your own scoring model here -- individual signal scoring happens upstream,
  before signals reach this skill; this skill qualifies clusters, not raw signals
- Flag, don't remove -- decisions to remove a cluster from your tracking system are
  yours to make, not this skill's to make automatically
- Don't source new signals from the open web here, and don't write to your raw signal
  inbox -- that's `Skills/cluster-discovery/`'s job (or your own signal-sourcing
  process); this skill only sweeps what's already there
- If a cluster already has a capability match from `cluster-discovery`, don't overwrite
  it with a generic sector-based guess -- the capability-first match is more specific and
  takes precedence
- No em dashes in any output

## Relationship to other sources
This skill is source-agnostic -- it sweeps whatever is already sitting in your signal
inbox, regardless of which process wrote it there. It doesn't source anything itself and
doesn't apply its own scoring model. Sequence: something sources and scores signals
first (your own process, or `Skills/mandate-mapping` / `Skills/community-grant-radar` if
you're using those), then this skill runs to decide advancement.
