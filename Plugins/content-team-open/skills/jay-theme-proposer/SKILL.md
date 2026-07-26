---
name: jay-theme-proposer
description: "Generates 3 data-driven monthly content theme proposals anchored to your active signal clusters and current offer, for owner review and approval before the content month begins."
---

## Purpose

Runs at month-end to propose next month's content themes so the whole content pipeline
has a shared anchor. Produces exactly 3 options (A, B, C), each with a composite score,
and writes them as Pending records awaiting approval.

## Setup required

Configure `customization/my-content-sources.json` before first use:
- `notion.theme_proposals_db_id` -- where Pending records get written
- `scoring` -- signal strength, offer alignment, and audience fit weights

## Process

1. Determine the target month
2. Filter recent topic cards and engagement signals to the strongest clusters
3. Generate 3 distinct theme proposals, each scored against your configured weights
4. Write all 3 as Pending records to your theme proposals database

## Output

3 Pending records (A, B, C) in your theme proposals database for the target month,
awaiting owner approval.

## Rules

- The 3 proposals must be genuinely distinct, not variations of the same idea
- Every proposal cites the signal cluster(s) it's anchored to
- No em dashes in any output
