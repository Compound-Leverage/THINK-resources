# Stalled Record Audit -- Template

Produced by the periodic audit step in `Skills/crm-intake/workflow.md` (Step 7) --
not a substitute for the per-sweep intake report in `Templates/kipp-crm-intake.md`,
which stays the record of what happened on each daily run. This template is for the
separate, lower-frequency pass that catches records still stuck mid-intake.

```
Stalled Record Audit -- [date]

| Record | Source | Days in pipeline | Missing | Last attempted |
|---|---|---|---|---|
| [Org / contact name] | [inbound queue / list name] | [count, vs. audit.stalled_after_days] | [decision-maker link / ICP classification / both] | [date of last enrichment attempt] |

Records flagged this run: [count, or "none"]
Records resolved since last audit: [count, or "none"]
```
