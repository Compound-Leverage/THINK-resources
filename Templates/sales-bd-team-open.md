# Sales BD Team (sales-bd-team-open) - Deliverable Templates

Blank versions of the documents Lori, Alex, and Sarah produce. Use these directly (fill in
your own data by hand) or as the reference format the plugin's outputs should match. Every
`[bracket]` is a placeholder.

---

### Lori - Lead Scout

Field names below match the CSV schema in her SKILL.md. One row per qualified candidate.

```
Leads/[segment]/leads_[YYYY-MM-DD].csv

name,org,signal_source,intent_score,routing_flag
[Contact name],[Org name],[Which configured signal source this came from],[Score per your scoring_dimensions],[qualified_flag / monitor_flag / disqualified_flag]
```

---

### Alex - BD Research

One record per enriched candidate, before it's written to your pipeline and contacts
databases.

```
Enriched Prospect Record: [Org name]
Contact: [Name, title]
ICP profile matched: [profile_id from customization/my-icp-profile.json, or "no match"]
Signal source: [Where the intent signal originated -- passed from Lead Scout]
Company size: [Employee count or revenue band]
Contact info: [Email, phone -- from your enrichment tool]
Enrichment tool used: [Clay or equivalent]
Missing fields flagged: [list, or "none" -- never guessed]
Routed to: [Deals Pipeline / Contacts / Orgs db]
```

---

### Sarah - BD Execution

One record per prospect touched, covering the score, the send (or hold), and the deal
admin that follows.

```
Outreach Record: [Prospect name / Org]
Segment: [segment name]
Scores: fit [1-5] / win_probability [1-5] / economic_value [1-5] / timeline_realism [1-5] / strategic_leverage [1-5]
Approval gate: [New segment -- held for owner approval / Approved segment -- autonomous send]
Send-from: [name] <[email]>
CC: [cc_addresses from customization/my-outreach-config.json]
Sent: [date/time, or "Held for approval"]
Follow-up cadence applied: [step number, days_after_initial]
Deal record: [Created / Updated] in [your CRM] -- Stage: [stage]
Activity logged: [summary of touches this record covers]
Escalation flagged: [trigger matched from escalation_triggers, or "none"]
```

---

## Questions

Contact [marvin@compoundleverage.co](mailto:marvin@compoundleverage.co) or visit [compoundleverage.com](https://compoundleverage.com).
