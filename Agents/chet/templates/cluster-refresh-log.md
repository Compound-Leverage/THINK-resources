# Cluster Refresh Log -- Template

Produced at the end of each `Skills/cluster-monitoring/` sweep (or a
`Skills/cluster-discovery/` refresh pass). One row per cluster touched this run -- not a
substitute for the individual Cluster Candidate Record, which stays the source of truth
per group.

```
Cluster Refresh -- [date]

| Group | Status before | Status after | Change | Reason |
|---|---|---|---|---|
| [Group name] | [Forming/Confirmed/Active/Saturating/Closed] | [same list] | [Refreshed / Advanced / Archived / Flagged] | [one line] |

Exceptions flagged for review: [list, or "none"]
Groups archived this run (window closed without conversion): [list, or "none"]
```
