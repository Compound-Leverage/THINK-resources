---
name: brief-writer-josh
description: "Produces Leader and Strategist editions of a weekly intelligence brief from top-scoring TopicCards, applying a proof gate and two-audience ICP voice extraction."
---

## Purpose

Takes the top-scoring topic cards, applies your configured proof gate, extracts voice
for two distinct audiences, and delivers publication-ready briefs. Flags org-buyer
topics for downstream pipeline use (BD Team skills, if installed).

## Setup required

Configure `customization/my-content-sources.json` before first use:
- `scoring.proof_gate_threshold` -- minimum score a topic needs to be brief-eligible
- `icp_voice_profiles` -- your Leader (org-buyer) and Strategist (practitioner) audiences
- `notion.content_assets_db_id` -- where Draft records get written

## Process

1. Read `topic-cards.json`, filter to cards meeting the proof gate threshold
2. Extract voice for the Leader edition (org-buyer audience)
3. Extract voice for the Strategist edition (practitioner audience)
4. Draft both briefs
5. Flag any org-buyer-relevant topic to `org-buyer-flags.json` for downstream use
6. Write Draft records to your content database

## Output

Leader and Strategist brief Markdown files, `org-buyer-flags.json`, and Draft records in
your content database.

## Rules

- Nothing below the proof gate threshold reaches either brief
- Leader and Strategist editions differ in framing and depth, not just length
- No em dashes in any output
