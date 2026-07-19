---
name: "Blog Writer"
description: "Generates long-form blog posts from Intel Scanner's signal output. Produces one practitioner-focused post and one org-buyer post per cycle, each in a distinct ICP voice."
---

## Purpose

Converts a signal or topic into two long-form posts calibrated to your two configured
ICP voices, so a single signal serves both an individual practitioner reader and an
org-scale buyer reader without either draft reading generic.

## Setup required

Configure `customization/my-content-sources.json` before first use:
- `icp_voice_profiles.practitioner` and `icp_voice_profiles.org_buyer` -- define both
  audiences and their voice notes
- `notion.content_assets_db_id` -- where Draft records get written

## Process

1. Select the signal or topic (from `topic-cards.json` or direct input)
2. Extract ICP voice for both configured profiles -- vocabulary, priorities, tone
3. Draft the practitioner-ICP post
4. Draft the org-buyer-ICP post
5. Write both as Draft records to your content database

## Output

Two Markdown post files at `output/{week}/` (practitioner ICP + org-buyer ICP), plus
Draft records in your content database.

## Rules

- Each post reads as written for its ICP, not the same post twice with a different
  intro
- End each post with the CTA style configured for that ICP
- No em dashes in any output
