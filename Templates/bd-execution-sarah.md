# Sarah - BD Execution (sales-bd-team) -- Deliverable Templates

Blank version of the document Sarah produces. Use this directly (fill in your own data by
hand) or as the reference format the plugin's output should match. Every `[bracket]` is a
placeholder.

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

**Approval gate reminder:** never send real outreach from this record without a human
reviewing the draft first, unless the segment is already an approved segment per
`customization/my-outreach-config.json`.

---

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit [compoundleverage.com](https://compoundleverage.com).
