---
name: "Proof Points"
description: "Extracts and packages proof points from active client engagements into 1-page case study narratives tagged for buyer relevance. Maintains a minimum inventory and feeds proposal work with ready-to-use evidence."
---

## Purpose

Turns real, completed engagement outcomes into 1-page case study narratives, tagged by
buyer type, so proposal and outreach work always has current evidence to draw on.

## Setup required

Configure `customization/my-proof-points-config.json` before first use:
- `notion.proof_points_db_id` -- where finished proof points get written
- `notion.source_db_ids` -- where completed engagement data lives
- `buyer_type_tags.tags` -- your buyer segments
- `minimum_inventory.threshold` -- alert threshold per tag

## Process

1. Read completed engagement records from your configured source database(s)
2. Extract challenge, solution, and quantified results per the configured
   `case_study_formula`
3. Tag each proof point against your `buyer_type_tags`
4. Write the record to your Proof Points database
5. Check current inventory per tag against `minimum_inventory.threshold` -- alert if
   below

## Output

New records in your Proof Points database with quantified outcomes, buyer-type tags,
and a case study narrative.

## Rules

- Only completed, quantified outcomes -- never a projected or in-progress result
- Quantify wherever the source data supports it; label anything qualitative-only as
  such
- No em dashes in any output
