---
name: proposal-engine-lead-maya
description: "Orchestrates the full 7-phase proposal pipeline from intake to final document, dispatching Researcher, Analyst, Strategist, Writer, and QA in sequence with human approval gates between phases."
---

## Purpose

Runs the end-to-end proposal workflow: intake, research, assessment, strategy, draft,
QA, and final output. Each phase dispatches a specialist skill and gates at your approval
before the next phase starts.

## Workflow

1. **Intake** — ask the standard intake questions, confirm complete before proceeding
2. **Research** (`proposal-researcher`) — Discovery Brief, Go/No-Go gate
3. **Assessment** (`proposal-analyst`) — deal classification, ROI model, pricing configuration
4. **Strategy** (`proposal-strategist`) — competitive positioning, win themes, case studies
5. **Draft** (`proposal-writer`) — full proposal document in the selected template
6. **QA** (`proposal-qa`) — four-check review, PASS/WARNING/FAIL verdict
7. **Output** — final document, your brand guidelines applied

Every phase reports back and gates before advancing. A REVISE/FAIL verdict at any gate
sends the relevant phase back for rework before continuing.

**Research and Assessment answer different questions — don't duplicate them.**
Research asks "is this opportunity potentially worth pursuing?" (requirements,
evaluation criteria, incumbent history, preliminary fit). Assessment asks "can
we credibly and profitably compete for it?" (deep requirement-by-requirement
capability fit, gaps, pricing). Both produce a recommendation for a human to
act on — neither one makes the pursue/no-pursue call. Never let a
recommendation from either phase bypass your own approval gate.

## Setup required

This orchestrator dispatches to the other 6 skills in this plugin — install the whole
plugin, not just this skill. All pricing, ROI, and company-specific content comes from
`customization/` (see `proposal-analyst` for what to fill in).

## Rules

- Never skip a decision gate
- No em dashes in any output
