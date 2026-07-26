# Capture Team (capture-team-open) -- Deliverable Templates

Blank versions of the documents Chet, Kipp, and Ben produce. Use these directly (fill in
your own data by hand) or as the reference format the plugin's outputs should match. Every
`[bracket]` is a placeholder.

---

### Chet -- Cluster Candidate Record

One record per qualifying group. Don't collapse multiple groups into one record.

```
Cluster Candidate: [Group name]
Capability matched: [capability_id / capacity_solved]
Member entities: [count] -- [list or link to membership roster]
Buyer identity: [who holds hiring/contracting authority]
Budget confirmation: [Confirmed line item / Inferred -- cite source]
Gap volume: [count of member entities showing the signal pattern]
Window estimate: [date or range until the gap goes public or gets staffed elsewhere]
Status: [New / Monitoring / Ready for outreach / Archived]
Source: [where this group was found]
```

---

### Kipp -- Intake Report

Produced at the end of each sweep. One row per record processed.

```
Intake Sweep -- [date]

| Record | Source | Enrichment applied | ICP profile matched | Routing flag | CRM action |
|---|---|---|---|---|---|
| [Org / contact name] | [inbound queue / list name] | [fields enriched] | [profile_id or "no match"] | [qualified_flag / unqualified_flag / escalation_flag] | [Created / Updated / Linked to deal] |

Conflicts flagged (manually-edited field vs. enrichment guess): [list, or "none"]
Records left unclassified: [should always be 0 -- investigate if not]
```

---

### Ben -- Client-Ready Brief

Section headers below match `brief_structure.sections` in
`customization/my-capture-config.json` -- replace with your own if you've customized them.

```
[Client Name] -- Intelligence Brief
Date: [date]
Source signal(s): [link(s) to signal inbox entries this brief traces back to]

## Executive Summary
[2-3 sentences: what happened, why it matters to this client, what to do]

## Signal Detail
[What was detected, when, and from which source -- every claim traces to a real signal]

## Market Context
[Why this signal matters now -- competitive, regulatory, or funding backdrop]

## Recommended Actions
[Specific next step(s), ranked by urgency]

---
Exceptions flagged: [missing data, ambiguous signal, or "none"]
```

---

## Questions

Contact [marvin@compoundleverage.co](mailto:marvin@compoundleverage.co) or visit [compoundleverage.com](https://compoundleverage.com).
