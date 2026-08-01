---
name: rohit-master-intel-scan
description: "Weekly signal scan across Reddit, news, YouTube, and Google PAA plus your own platform performance data. Synthesizes scored TopicCards that gate every downstream content skill in this plugin."
---

## Purpose

Fans out across your configured signal sources in parallel, synthesizes the results into
scored TopicCards, and writes the top candidates to your content database as Draft
records. Every other skill in this plugin reads its topic input from here.

## Setup required

Configure `customization/my-content-sources.json` before first use:
- `signal_sources` -- which channels you actually monitor and their scope
- `notion.content_assets_db_id` -- where Draft records get written (optional; skips
  Notion write if left blank)
- `scoring` -- weights used to rank candidates

## Process

1. Fan out across each configured source in parallel -- pull recent, relevant activity
2. Score each candidate signal against your configured weights
3. Synthesize into TopicCards: title, source, summary, composite score
4. Rank and select the top candidates (target: up to 5 per run)
5. Write `topic-cards.json` locally; write Draft records to your content DB if configured

## Output

`topic-cards.json` at the plugin working directory, plus Draft records in your content
database, ranked by composite score.

## Rules

- Never fabricate a signal -- every TopicCard traces to a real source result
- Flag low-confidence signals rather than inflating their score
- No em dashes in any output
