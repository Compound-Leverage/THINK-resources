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
- `qualification_profiles` -- your qualification profiles, one per pursuit type:
  `business_development`, `govcon`, or `grant_funding`. Each profile defines its own
  criteria set -- business-development ICP (industry, company size, capacity gap, buying
  signal), GovCon (capability alignment, NAICS/certifications, past performance, mandatory
  requirements, contract size, geography, deadline), or grant/funding (organization
  eligibility, program alignment, funder priorities, geography, award amount, deadline,
  matching requirements). Nothing is hard-coded to one pursuit type
- `routing_flags` -- how classified records get flagged
- `notion.*_db_id` -- your Contacts, Orgs, and Deals Pipeline database IDs
  (shown as Notion fields for illustration -- rename/restructure to match
  whatever CRM you actually use)
- `enrichment.provider` and `enrichment.api_key_env_var` -- your enrichment tool

## Process

1. Pull new records from your inbound queue (Chet's candidates, intelligence inbox
   entries, unlinked pipeline prospects, warm inbound leads)
2. Enrich each via your configured provider
3. Match the candidate to its `qualification_profiles` entry by pursuit type, then
   evaluate it criterion by criterion -- build a Qualification Evidence table (see below),
   don't collapse straight to a single score
4. Apply the matching `routing_flags` value based on the overall result
5. Create or update whichever records actually apply -- see Output below
6. Produce an intake report summarizing the sweep, prioritized by fit strength and any
   deadline/timing information available

## Qualification Evidence table

One row per criterion from the matched profile:

| Criterion | Result | Evidence | Gap/Unknown |
|---|---|---|---|

`Result` is one of: **Fit**, **Partial**, **Unsupported**, **Unknown** (missing
information — never convert Unknown into Unsupported; flag it and route for human review
instead), or **Risk** (used specifically for deadline/timing). When a deadline is
available for this candidate, always include a Deadline row: deadline date, days
remaining, and a timing-risk read (on track / tight / past realistic response window).

## Output

**Opportunity/Candidate Record** — the Qualification Evidence table plus the overall
routing flag, with optional relationships to whatever actually exists for this pursuit: an
organization, agency, or funder record; contacts; and a CRM opportunity/deal. Not every
qualified candidate needs a Contact or Organization record — a grant opportunity might
only need an Opportunity record with a funder name, while a business-development lead
might need the full Contact+Org+Deal chain. Create whichever records actually apply;
don't force a grant or solicitation into a CRM shape it doesn't fit.

Intake report at the end of each sweep, prioritized by fit strength and any deadline/
timing information available.

## Rules

- Never overwrite an existing manually-edited field with an enrichment guess -- flag
  the conflict instead
- Every record gets a routing flag -- nothing is left unclassified
- Never convert missing or unknown qualification data into a "no fit" result -- flag
  what's missing and route for human review instead of assuming the worst case
- Don't fabricate qualification criteria (NAICS codes, eligibility rules, funder
  priorities) that aren't in your configuration
- No em dashes in any output
