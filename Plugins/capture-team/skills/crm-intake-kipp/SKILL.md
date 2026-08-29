---
name: crm-intake-kipp
description: "Enriches incoming org and contact records, classifies each by your ICP profile, and creates or updates CRM entries. Processes new inbound leads, intelligence inbox entries, and prospect lists."
---

## Purpose

Runs a daily (or on-demand) sweep of new candidates from Chet (or any inbound source),
qualifies each one against your organization's own criteria, and writes clean, scored,
prioritized records into your CRM. "ICP" is one kind of qualification profile — the same
underlying process supports GovCon eligibility/capability alignment, grant eligibility/
program alignment, or business-development ICP fit, depending on what you configure.

## Setup required

Connect your own CRM (Notion, Airtable, HubSpot, Salesforce, or whatever you
already use) and enrichment tool via their MCP connectors, or however you
already access them in this session. Configure
`customization/my-capture-config.json` before first use:
- `icp_profiles` -- your qualification profiles. Define criteria for whatever pursuit type
  you're qualifying against: business-development ICP (industry, company size, capacity
  gap, buying signal), GovCon (capability alignment, NAICS/certifications, past
  performance, mandatory requirements, contract size, geography, deadline), or
  grant/funding (organization eligibility, program alignment, funder priorities, geography,
  award amount, deadline, matching requirements) -- the fields are yours to define;
  nothing is hard-coded to one pursuit type
- `routing_flags` -- how classified records get flagged
- `notion.*_db_id` -- your Contacts, Orgs, and Deals Pipeline database IDs
  (shown as Notion fields for illustration -- rename/restructure to match
  whatever CRM you actually use)
- `enrichment.provider` and `enrichment.api_key_env_var` -- your enrichment tool

## Process

1. Pull new records from your inbound queue (Chet's candidates, intelligence inbox
   entries, unlinked pipeline prospects, warm inbound leads)
2. Enrich each via your configured provider
3. Classify against `icp_profiles`, apply the matching `routing_flags` value -- score
   strength of fit, don't force a binary yes/no
4. Create or update the Contacts and Orgs records; link to Deals Pipeline where
   applicable
5. Produce an intake report summarizing the sweep, prioritized by fit strength and any
   deadline/timing information available

## Output

Contacts and Organizations records in your CRM. Deals Pipeline updated with
decision-maker links. Intake report at the end of each sweep, prioritized so you can see
where to spend limited pursuit capacity first.

## Rules

- Never overwrite an existing manually-edited field with an enrichment guess -- flag
  the conflict instead
- Every record gets a routing flag -- nothing is left unclassified
- Never convert missing or unknown qualification data into a "no fit" result -- flag
  what's missing and route for human review instead of assuming the worst case
- Don't fabricate qualification criteria (NAICS codes, eligibility rules, funder
  priorities) that aren't in your configuration
- No em dashes in any output
