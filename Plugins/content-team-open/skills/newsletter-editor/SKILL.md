---
name: "Newsletter Editor"
description: "Selects the strongest signal from Intel Scanner's output, translates it through your methodology framework, and generates WARM and COLD draft editions ready for platform posting."
---

## Purpose

Turns the week's top-ranked TopicCard into two newsletter drafts calibrated to different
audience temperatures: WARM for engaged subscribers, COLD for new/unengaged ones. Owner
reviews tone before send; this skill handles structure and copy.

## Setup required

Configure `customization/my-content-sources.json` before first use:
- `newsletter_platform` -- your platform name and ID
- `notion.content_assets_db_id` -- where content records get logged

## Process

1. Read `topic-cards.json` from Intel Scanner's most recent run
2. Select the highest-scoring eligible signal
3. Translate the signal through your methodology framework into a narrative arc
4. Generate the WARM edition -- assumes context, deeper insight, direct CTA
5. Generate the COLD edition -- more framing, lighter CTA, subscription hook
6. Post both as drafts to your configured newsletter platform

## Output

Two draft editions (WARM and COLD) posted to your newsletter platform, plus a local
Markdown backup at `output/{week}/`.

## Rules

- WARM and COLD must differ in framing, not just greeting -- COLD earns the context WARM
  assumes
- Never post live -- drafts only, owner sends
- No em dashes in any output
