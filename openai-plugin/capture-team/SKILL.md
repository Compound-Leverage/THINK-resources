---
name: capture-team
description: "THINK School AI Capture Team, by Compound Leverage: an AI Team of three Digital Employees (Chet, Kipp, Ben) that finds named groups worth pursuing, enriches and classifies inbound leads against your ICP, and turns signals into client-ready intelligence briefs. Use when you need to discover clusters or opportunities carrying a capacity gap, process new inbound contacts and organizations into your CRM with ICP scoring, or convert raw signals into a polished brief document. Bring your own CRM, enrichment tool, and document storage -- nothing is pre-wired to a specific vendor."
---

## Capture Team

Three specialized roles, each with a distinct job. Load the matching reference
file for the task at hand -- don't load more than one at a time unless the
request genuinely spans more than one role.

- **Cluster discovery** (find named, bounded groups worth pursuing) -- load
  `references/chet.md`
- **CRM intake** (enrich and classify inbound records) -- load
  `references/kipp.md`
- **Signal delivery** (turn signals into client-ready briefs) -- load
  `references/ben.md`

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
