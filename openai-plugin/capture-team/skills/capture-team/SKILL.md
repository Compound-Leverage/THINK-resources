---
name: capture-team
description: "THINK School AI Capture Team, by Compound Leverage: an AI Team of three specialized Digital Employees that helps you identify groups and opportunities worth pursuing, qualify organizations and contacts against your ICP, and turn market signals into client-ready intelligence briefs. Use it to discover potential markets and opportunities, research and qualify inbound organizations, or convert raw intelligence into actionable briefs. Bring your own CRM, enrichment tool, and document storage. Nothing is pre-wired to a specific vendor."
---

## Capture Team

Three specialized roles, each with a distinct job. Load the matching reference
file for the task at hand -- don't load more than one at a time unless the
request genuinely spans more than one role.

- **Opportunity discovery** (identify groups, markets, and opportunities
  worth pursuing) -- load `references/chet.md`
- **Lead qualification** (research, enrich, and classify organizations and
  contacts against your ICP) -- load `references/kipp.md`
- **Intelligence delivery** (turn signals and research into client-ready
  intelligence briefs) -- load `references/ben.md`

## Setup required

Configure `assets/my-capture-config.json` (fill in your own values -- it
ships with bracketed placeholders, not real data) before first use:
capability map, ICP profiles, routing flags, your CRM database structure,
enrichment provider, and delivery destination.

Connect your own CRM, enrichment tool, and document storage (Notion, Airtable,
Google Drive, OneDrive, whatever you already use) via their MCP connectors, or
however you already access them in this session. Nothing here requires a
specific vendor, and no Compound Leverage account or data is required.

## Rules (apply across all three roles)

- No em dashes in any output
- Flag gaps and exceptions rather than guessing past them
- Never invent data -- if something is missing, say so
