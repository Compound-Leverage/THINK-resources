---
name: "Signal Delivery"
description: "Synthesizes capital event or market signals into client-ready intelligence briefs. Reads your signal inbox, applies structured analysis, and produces brief documents clients can act on immediately."
---

## Purpose

Converts raw signals sitting in your intelligence inbox into a polished, client-ready
brief document -- the fulfillment-side counterpart to the Content Team's internal
intelligence briefs.

## Setup required

Configure `customization/my-fulfillment-config.json` before first use:
- `notion.signal_inbox_db_id` -- your source signal database
- `delivery.google_drive_folder_id` -- where finished briefs get stored
- `brief_structure.sections` -- your section headers

## Process

1. Read new/unactioned signals from your configured signal inbox
2. Apply structured analysis -- what the signal means, why it matters, what to do
3. Draft the brief using your configured section structure
4. Write the document to your configured delivery destination
5. Post a summary to owner with any exception flags

## Output

Brief document written to your configured storage destination. Summary posted to owner
with exception flags.

## Rules

- Every claim in the brief traces back to a signal in the inbox -- no invented context
- Flag exceptions (missing data, ambiguous signal) rather than guessing past them
- No em dashes in any output
