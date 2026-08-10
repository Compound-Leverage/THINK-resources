---
name: bd-execution-sarah
description: "Scores leads, builds outreach emails, sends from your configured address, handles deal admin, and tracks activity. Owner approves the prospect profile once; this skill runs autonomously after."
---

## Purpose

Takes BD Research's enriched records, scores them, drafts outreach, and -- once you've
approved the prospect profile for a segment -- sends and logs activity without further
manual steps.

## Setup required

Configure both files before first use:
- `customization/my-outreach-config.json` -- send-from address, CC rules, approval
  gate, follow-up cadence, escalation triggers
- `customization/my-company-profile.json` -- your company info and differentiators,
  used in outreach copy (copy this from the Proposal Team plugin's schema if you've
  already filled that one in)

## Process

1. Score each enriched record against `my-icp-profile.json`'s scoring dimensions
2. Draft an HTML outreach email using your `my-company-profile.json` differentiators
3. Check `approval_gate` -- if this is a new segment, hold for owner approval before
   first send
4. Send from the configured address, CC the configured addresses
5. Write deal and activity records to your CRM
6. Apply `follow_up_cadence` for subsequent touches

## Output

HTML outreach email (owner reviews before first send to a new segment), deal records
written to your CRM, and activity logged.

## Rules

- Never send to a new segment without the one-time approval this file's approval gate
  requires
- Escalate to owner immediately on any trigger in `escalation_triggers`
- No em dashes in any output
