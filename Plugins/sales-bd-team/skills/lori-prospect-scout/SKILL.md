---
name: lori-prospect-scout
description: "Finds individuals showing active demand signals for what you deliver, targeting intent over profile match. Pulls from public sources and feeds qualified, scored leads to BD Research and BD Execution."
---

## Purpose

Scans public sources for people actively signaling demand -- not just people who fit
your profile on paper. Produces a scored CSV that BD Research enriches and BD Execution
acts on.

## Setup required

Configure `customization/my-icp-profile.json` before first use:
- `icp_profiles` -- your ICP definition(s) and required signals
- `disqualifiers.auto_exclude` -- criteria that auto-exclude a candidate
- `signal_sources` -- where you actually look (forums, event registrations, org sites,
  newsletter click signals, etc.)

## Process

1. Pull recent activity across your configured signal sources
2. Check each candidate against your `icp_profiles` signals-required list
3. Apply `disqualifiers.auto_exclude` -- drop anything that matches
4. Score remaining candidates using `scoring_dimensions`
5. Write qualified leads to CSV with a routing flag

## Output

Leads CSV at `Leads/[segment]/leads_YYYY-MM-DD.csv` with name, org, signal source,
intent score, and routing flag.

## Rules

- Intent signal required -- profile match alone is not enough to qualify
- Never guess a missing required field -- mark it as a gap, don't infer it
- No em dashes in any output
