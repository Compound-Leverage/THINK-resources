---
name: "Cal — Weekly Brief"
description: "Pulls from all active intelligence sources each week and synthesizes a single owner brief -- one page, overwritten weekly -- for full situational awareness with no reading required."
---

## Purpose

Runs last in the weekly content cycle. Reads everything the other skills in this plugin
(and, if installed, the BD Team and Fulfillment plugins) produced that week and
synthesizes it into one page.

## Setup required

Configure `customization/my-content-sources.json` before first use:
- `notion.signal_inbox_db_id` -- source for intelligence and deal activity, if you track
  it there
- Point this skill at whatever local weekly output paths you're using
  (`output/{week}/`)

## Process

1. Gather this week's local output files and configured Notion sources
2. Rank findings by priority -- what genuinely needs owner attention this week
3. Synthesize into a single-page brief: what happened, what's pending, what needs a
   decision
4. Overwrite the existing brief page -- never append

## Output

Single page, overwritten each week (Notion page if configured, otherwise local
Markdown). Owner gets a one-line summary when complete.

## Rules

- Always overwrite, never append -- old briefs are not archived by this skill
- Lead with what needs a decision, not a recap of everything that happened
- No em dashes in any output
