---
name: proposal-team
description: "Proposal Team: an AI Team of seven Digital Employees (Maya orchestrating Chase, Priya, Porter, Quinn, Diego, and Blair) that carries a qualified opportunity from research through a submission-ready proposal -- Go/No-Go research, capability-fit and pricing assessment, competitive positioning, drafting, QA, and a parallel grant/funder track. Use when you need to research and score a proposal opportunity, build competitive positioning and win themes, draft a submission-ready government or commercial proposal, run QA on a proposal draft, or develop a grant/funder pitch. Every stage stops for your approval before advancing. Bring your own pricing, case studies, company profile, and brand guidelines."
---

## Proposal Team

Maya orchestrates a 7-phase proposal pipeline, dispatching one specialist for
each phase with your approval gating between phases. Load the matching
reference file for the phase at hand -- don't load more than one at a time
unless the request genuinely spans more than one phase.

## Workflow

1. **Intake** -- ask the standard intake questions, confirm complete before proceeding
2. **Research** -- load `references/chase.md` for the Discovery Brief and Go/No-Go gate
3. **Assessment** -- load `references/priya.md` for deal classification, ROI model, pricing
4. **Strategy** -- load `references/porter.md` for competitive positioning and win themes
5. **Draft** -- load `references/quinn.md` for the full proposal document
6. **QA** -- load `references/diego.md` for the four-check review and PASS/WARNING/FAIL verdict
7. **Output** -- final document, your brand guidelines applied

Every phase reports back and gates before advancing. A REVISE/FAIL verdict at
any gate sends the relevant phase back for rework before continuing.

For grant and funder-type proposals specifically (not commercial or
government RFP work), load `references/blair.md` instead of the
Research-through-Draft chain above -- it's a separate, funder-specific track.

## Setup required

Configure the files in `assets/` before first use -- none are pre-filled with
real numbers or data:
- `my-company-profile.json` -- your company info, capabilities, differentiators, team
- `my-pricing-model.json` -- your products/services, pricing, ROI defaults
- `my-case-studies.json` -- your proof points for case study matching
- `my-brand-guidelines.md` -- your voice, terminology, and formatting rules
- `my-bid-sizing.json` -- your funder categories and bid-sizing rules (grant/funder track only)

## Rules (apply across all phases)

- Never skip a decision gate
- No em dashes in any output
- Never claim a capability or outcome not supported by the analyst's assessment
