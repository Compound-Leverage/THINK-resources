---
name: justin-linkedin-content
description: "Generates a full week of LinkedIn posts across your active personas -- personal brand, company page, product/program -- from the current signal stack."
---

## Purpose

Selects the best eligible topic per persona from your signal stack, applies each
persona's voice rules, and delivers a combined Markdown queue ready to schedule for the
week.

## Setup required

Configure `customization/my-content-sources.json` before first use:
- `linkedin_personas.personas` -- each persona, its posting day, and posts-per-week
- `icp_voice_profiles` -- reused for voice differentiation across personas

## Process

1. Read `topic-cards.json` for eligible topics
2. For each configured persona, select a topic and check eligibility threshold
3. Apply that persona's voice and format rules
4. Generate the post(s) for that persona
5. Combine into a single queue file, grouped by persona and posting day

## Output

Combined Markdown queue file at `output/{week}/LI_Queue_{week}.md`, posts grouped by
persona and day.

## Rules

- One topic never appears twice across personas in the same week unless deliberately
  cross-posted with distinct framing
- Match each persona's configured posts-per-week -- do not over- or under-produce
- No em dashes in any output
