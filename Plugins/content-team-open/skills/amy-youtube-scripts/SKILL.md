---
name: amy-youtube-scripts
description: "Generates 4-5 minute YouTube video scripts targeting your primary ICP from a research file and the current weekly brief. Pure script output, no platform posting."
---

## Purpose

Parses your latest research input and weekly brief to produce a structured script:
title options, hook variants, a signal walkthrough, a practitioner takeaway, and a CTA
close. No Notion or platform interaction.

## Setup required

Configure `customization/my-content-sources.json` before first use:
- `icp_voice_profiles.practitioner` -- the primary ICP this skill writes for
- Point this skill at your research file path (pass it directly when invoking, or store
  a default path in your own notes -- this skill has no Notion dependency)

## Process

1. Parse the research file and/or weekly brief for the strongest storyline
2. Draft 2-3 title options
3. Draft 2-3 hook variants (first 15 seconds)
4. Write the signal walkthrough -- the body of the script
5. Write the practitioner takeaway -- what the viewer does with this
6. Write the CTA close

## Output

Markdown script file at `output/{week}/YouTube_Script_{week}.md` with title options,
hook variants, and full script body.

## Rules

- Script runs 4-5 minutes read aloud at a natural pace -- check length before finishing
- Hook must earn the next 10 seconds, not just state the topic
- No em dashes in any output
