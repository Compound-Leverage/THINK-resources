# Proposal Team (proposal-team-open) - Deliverable Templates

Blank versions of the documents Maya, Chase, Priya, Porter, Quinn, Diego, and Blair
produce. Use these directly (fill in your own data by hand) or as the reference format
the plugin's outputs should match. Every `[bracket]` is a placeholder.

---

### Maya - Pipeline Status

Maya's status check on where a deal sits across the 7-phase workflow. Produce this any
time you ask for a check-in, and at the end of a full pipeline run.

```
Proposal Pipeline Status - [Prospect name]
Date: [date]

| Phase | Owner | Status | Gate outcome | Date completed |
|---|---|---|---|---|
| 1. Intake | Maya | [Not started / In progress / Complete] | [n/a] | [date] |
| 2. Research | Chase | [Not started / In progress / Complete] | [GO / CONDITIONAL GO / NO-GO] | [date] |
| 3. Assessment | Priya | [Not started / In progress / Complete] | [Approved / Revise] | [date] |
| 4. Strategy | Porter | [Not started / In progress / Complete] | [Approved / Revise] | [date] |
| 5. Draft | Quinn | [Not started / In progress / Complete] | [Approved / Revise] | [date] |
| 6. QA | Diego | [Not started / In progress / Complete] | [PASS / WARNING / FAIL] | [date] |
| 7. Output | Maya | [Not started / In progress / Complete] | [n/a] | [date] |

Current gate awaiting your approval: [phase name, or "none"]
Blockers: [list, or "none"]
```

---

### Chase - Discovery Brief

One brief per opportunity. Feeds Priya, Porter, and Quinn - don't advance past a NO-GO.

```
Discovery Brief - [Client name]
Date: [date]

## Client Profile
[Company overview, size, recent developments, competitive position]

## Recent Developments (Proposal Implications)
[Development] - [why it matters to this proposal]

## Quantified Pain Points
[Pain point] - [evidence / quantification]

## Stakeholder Profiles
| Name | Title | Likely priority |
|---|---|---|
| [Name] | [Title] | [Priority] |

## Compliance / Regulatory Context
[Applicable regulations, risk areas, upcoming deadlines]

## Fit Score
[0-10] - [rationale]

## Recommendation
[GO / CONDITIONAL GO / NO-GO] - [rationale]

## Open Information Gaps
[What couldn't be found - never filled with an assumption]

Red flags: [litigation, layoffs, financial distress, or "none found"]
```

---

### Priya - Assessment Package

Requires `customization/my-pricing-model.json` and `customization/my-company-profile.json`
filled in. Feeds Porter and Quinn.

```
Assessment Package - [Client name]
Date: [date]

## Classification
Deal type: [type]
Offering type: [type]
Complexity: [Low / Medium / High]
Confidence level: [Low / Medium / High]

## Capability Fit
| Requirement | Our capability | Fit score (0-10) | Gap? |
|---|---|---|---|
| [Requirement] | [Capability] | [Score] | [Gap description, or "none"] |

Overall fit score: [0-10]

## Gap Analysis
[Gap] - [Mitigation]

## ROI Model
Baseline: [labor cost / volume / risk exposure, from the Discovery Brief]
Estimated savings (conservative, hard savings only): [amount]
Soft benefits (labeled separately): [list]
Break-even: [months]
Year 1 ROI: [percentage]
Assumptions: [every assumption documented]

## Pricing Configuration
Components: [component_id(s) from my-pricing-model.json]
Package: [package name, or "custom"]
Investment range: [low] - [high]
Success fee (if enabled): [percentage] / [basis] / cap [amount]

## Risk Assessment
[Risk] - [severity] - [mitigation]
```

---

### Porter - Strategy Package

Requires `customization/my-case-studies.json` filled in. Feeds Quinn.

```
Strategy Package - [Client name]
Date: [date]

## Competitive Positioning
Known/likely competitors: [list, or "unknown"]
Counter-positioning: [our positioning - no competitor named negatively]

## Win Themes
| Theme (Capability / Value / Approach / Risk / Partnership) | Mapped section(s) | Emphasis level | Language guidance |
|---|---|---|---|
| [Theme] | [Section] | [High / Medium / Low] | [Guidance] |

## Case Study Selection
| Case study | Match score (0-10) | Snippet |
|---|---|---|
| [Name] | [Score] | [Snippet] |

## Elevator Pitch
[2-3 sentences]

## Proposal Guidance
Sections to emphasize: [list]
Risks to address: [list]
```

---

### Quinn - Proposal Draft

Requires `customization/my-brand-guidelines.md` filled in. Section structure below is the
standard set - swap in the Government/Commercial/Simple/SOW template structure if your
deal calls for a different one.

```
[Client Name] - Proposal
Template: [Government / Commercial / Simple / SOW]
Date: [date]

## Executive Summary
[Problem first, 1-2 pages - write this section last]

## Understanding of Needs
[Client's stated and inferred requirements]

## Proposed Solution
[Solution mapped to win themes from the Strategy Package]

## Implementation Plan
[Phases, milestones, timeline]

## Project Team
[Names/roles, from customization/my-company-profile.json]

## Investment
[Pricing table, from the Assessment Package]

## Terms and Conditions
[Payment terms, standard terms]

## Past Performance
[Selected case studies]

Placeholders remaining: [list any [PLACEHOLDER: ...] markers, or "none"]
```

---

### Diego - QA Report

Never rewrites content - findings and fix instructions only.

```
QA Report - [Client name] Proposal
Date: [date]
Review depth: [Quick (consistency only) / Standard (all 4 checks) / Deep (all 4 + detailed feedback)]

Overall status: [PASS / WARNING / FAIL]

| Check | Result | Findings (exact section + citation) |
|---|---|---|
| Requirements | [Pass / Warning / Fail] | [Finding, or "none"] |
| Consistency | [Pass / Warning / Fail] | [Finding, or "none"] |
| Compliance | [Pass / Warning / Fail] | [Finding, or "none"] |
| Methodology | [Pass / Warning / Fail] | [Finding, or "none"] |

## Critical Issues (must fix before final review)
[Section] - [Issue] - [Fix instruction]

## Warnings (judgment call)
[Section] - [Issue]

Subjective findings: [labeled explicitly, or "none"]
```

---

### Blair - Funder Proposal

Requires `customization/my-bid-sizing.json` and `customization/my-case-studies.json`
filled in. For grant/funder-type deals only - commercial/general deals run through the
Maya pipeline above instead. Your approval required before any outreach.

```
[Funder Name] - Funder Proposal
Funder category: [category_id from my-bid-sizing.json]
Date: [date]

## Funder Alignment
[How this proposal speaks to what this funder category cares about]

## Proof Points
[Completed, quantified outcome] - [source case study]

## Bid Sizing
Bid basis: [percentage / flat_range]
Calculation: [allocation x percentage_range, or the flat_range value used]
Bid amount: [amount]

## Decision Timeline
Deadline: [date]
Next contact date: [date]
Decision criteria: [what the funder is evaluating on]

Approval status: [Pending your approval / Approved for outreach]
```

---

## Questions

Contact [marvin@compoundleverage.co](mailto:marvin@compoundleverage.co) or visit [compoundleverage.com](https://compoundleverage.com).
