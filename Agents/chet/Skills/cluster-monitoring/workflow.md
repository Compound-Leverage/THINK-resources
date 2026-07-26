# Cluster Monitoring -- Workflow

Runs alongside (typically right after) `Skills/cluster-discovery/`. Where discovery
finds new groups, monitoring decides what to do with everything already sitting in your
tracking system -- refresh, advance, or flag.

## Conceptual frame
Clusters are not events -- they are trajectories. The goal is to notice when capacity is
concentrating around a shared gap before the opportunity window closes, not after. When
signals from multiple sources start pointing at the same sector, geography, or group in
a short window, that's usually a sign the positioning window is narrow and front-loaded.
This skill exists to catch that concentration early rather than reacting to it once it's
already obvious to everyone.

## What it does
1. Reads your current pipeline/deal state and existing cluster records
2. Sweeps your signal inbox (wherever you track incoming signals) for anything scored at
   or above your own qualification threshold (`qualification.cluster_score_threshold` in
   your config)
3. Groups signals by sector, geography, and funding/opportunity type, and updates
   cluster records -- skipping any cluster you've manually paused
4. Qualifies each cluster: does it contain a reachable contact, an open window, and a
   signal you can actually act on?
5. Auto-advances clusters that clear your qualification bar into your pipeline/deals
   system
6. Flags everything else for manual review with a one-line reason

## Qualification criteria (auto-advance threshold)
A reasonable starting point, controlled by `qualification` in your config: a cluster
auto-advances when all of the following are true --
- Cluster score at or above your threshold
- At least one reachable contact matching the cluster's sector, if you're checking
  `require_reachable_contact`
- An active window still open (not past the estimated close date), if you're checking
  `require_open_window`

Everything else gets flagged, not dropped.

## Detection signals worth watching for
- Multiple funding awards or announcements in the same sector within a short window
  (e.g. 90 days)
- Hiring or staffing concentration: several organizations in the same geography posting
  the same role type around the same time
- A funding announcement followed quickly by a formal opportunity (a compressed cycle is
  an urgency signal)
- The same sector or group appearing across more than one of your sources within a short
  window (cross-source corroboration)

## Recommending next action
When a cluster advances, note what kind of capacity gap it represents -- grant/signal
discovery, proposal or writing volume, outreach and follow-up, research-to-action
translation, or contact/CRM intake -- so whoever picks it up next in your own process
knows what to route it toward. This is a routing suggestion for your own downstream
workflow, not a placement score, and it should never override a capability match that
`cluster-discovery` already set for that cluster.

## Output
- Updated cluster records in your own database
- Advanced or created entries in your pipeline/deals system for qualifying clusters
- Flagged exceptions reported to wherever you want them (chat, email), with cluster
  name, score, and reason for the flag
