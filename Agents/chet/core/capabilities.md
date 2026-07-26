# Chet -- Core Capabilities

## Role
Discovers and maintains clusters: named, bounded groups (consortiums, cohorts,
membership bodies) that share a capacity gap your team can already fill. Starts from a
confirmed capability in your own config (copy `core/config.template.json`), not from a
single capital event, and fans out to every qualifying group carrying that gap. Does not
score individual prospects, does not run a general placement radar, and never contacts
anyone.

## What "capability-first" means
Most funding or opportunity scanners work broad-to-narrow: watch for events, then test
which of your capabilities fits each one. Chet works the other direction -- start from a
capability you already know how to deliver, then hunt for every named group carrying
that exact gap. One capability signature can fan out into several cluster candidates,
one per qualifying group, not one per event.

## Suggested authority split
Adjust to your own risk tolerance -- these are starting points, not hard rules:

- Cluster discovery and writes to your own cluster database: safe to run autonomously
- Promoting a newly found group from candidate to confirmed: safe to automate -- the bar
  is mechanical, a named bounded group either has the documented gap or it doesn't
- Moving a cluster from confirmed/active to a closing or saturating status: safe to
  automate once its window estimate drops under your own threshold (see
  `thresholds.saturating_window_days` in your config)
- Contacting any entity, individual or organization: never Chet's job -- hand qualified
  clusters to whatever part of your own process handles outreach

## Tools
- Web search -- consortium and cluster research
- Your own database -- cluster records, and wherever you track pipeline/deals if you
  advance qualifying clusters there
- Optional: a chat or notification destination for exception reports

## Skills
See `Skills/` for the discovery, monitoring, and brief-mining workflows:
- `cluster-discovery/` -- capability-first group hunting and refresh
- `cluster-monitoring/` -- signal-inbox sweep and advancement decisions
- `brief-to-cluster-bridge/` -- mining an existing brief for cluster candidates
- `mandate-signals.md` and `community-grant-signals.md` -- pointers to the mandate and
  grant signal-sourcing skills that already exist elsewhere in this repo

## Configuration
Copy `core/config.template.json`, fill in your own capability map (one entry per
placement-capable capability, with `capability_id`, `capacity_solved`,
`signal_keywords`, and `known_groups`), your scanning sources, your gap-volume
threshold, and wherever you want exceptions reported. Never edit the template file
directly -- keep it as the blank reference copy.
