---
name: proposal-generator-open
description: Generate institutional proposals for high-value deals ($25K-$150K+) using a structured 7-phase methodology with strategic positioning before writing. Includes AI-powered customization, real-time feedback, and multi-version management.
---

# Proposal Generator Skill

## Purpose

Generate winning proposals for high-value deals ($25K-$150K+) using a structured methodology that forces strategic thinking BEFORE writing. The tool ensures you:
1. Understand the opportunity before proposing
2. Position competitively before drafting
3. Follow proven frameworks before customizing
4. Review systematically before submitting

---

## Before You Start: Configuration Required

This skill requires YOUR company data to generate proposals. You MUST complete the customization files before first use:

| File | What to Add | Update Frequency |
|------|-------------|------------------|
| `customization/my-company-profile.json` | Your company info, team, differentiators | Quarterly |
| `customization/my-pricing-model.json` | Your products, pricing, packages | Quarterly |
| `customization/my-case-studies.json` | Your past performance, testimonials | After each win |
| `customization/my-brand-guidelines.md` | Your voice, colors, messaging rules | Annually |

**Without these files completed, the skill cannot generate personalized proposals.**

---

## Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                    7-PHASE PROPOSAL WORKFLOW                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  Phase 1: INTAKE        → Gather opportunity information             │
│           ↓             → Human confirms completeness                │
│  Phase 2: RESEARCH      → Client/industry discovery                  │
│           ↓             → Go/No-Go decision gate                     │
│  Phase 3: ASSESSMENT    → Classify, model ROI, configure price       │
│           ↓             → Human approves assessment                  │
│  Phase 4: STRATEGY      → Position, themes, case studies             │
│           ↓             → Human approves strategy                    │
│  Phase 5: DRAFT         → Write all sections                         │
│           ↓             → Human reviews draft                        │
│  Phase 6: QA            → Check requirements, consistency            │
│           ↓             → Human approves or fixes                    │
│  Phase 7: OUTPUT        → Generate final document                    │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Intake

### Trigger Command
```
run proposal [Client Name]
```
or
```
new proposal [Client Name]
```

### Discovery Questions (REQUIRED before proceeding)

You MUST answer these questions before the system will proceed:

| # | Question | Why It Matters |
|---|----------|----------------|
| 1 | Client website URL | Research starting point |
| 2 | Industry/sector | Template and tone selection |
| 3 | Proposal due date | Timeline and urgency |
| 4 | How did this opportunity come to us? | Positioning strategy |
| 5 | Any existing intel? (meeting notes, RFP, emails) | Context for research |
| 6 | Specific focus areas or constraints? | Scope boundaries |
| 7 | Known competitors for this deal? | Competitive positioning |
| 8 | Budget signals or range? | Pricing configuration |

### Output
- `intake.json` with all answers captured
- Proposal folder created

### Gate
**Human confirms information is complete → Proceed to Research**

---

## Phase 2: Research

### Tasks Performed
1. **Client Research** - Company overview, size, recent news, technology signals
2. **Industry Analysis** - Trends, benchmarks, regulatory environment
3. **Stakeholder Intelligence** - Decision makers, priorities, concerns
4. **Pain Point Identification** - Quantified problems, connection to your solution

### Output: Discovery Brief
```
Client: [Name]
Fit Score: [X/10]

Key Findings:
• [Pain point 1 - quantified]
• [Pain point 2 - quantified]
• [Key opportunity]

Red Flags (if any):
• [Concerns]

Information Gaps:
• [What couldn't be found]

Questions for Human:
1. [Question needing input]
2. [Strategic question]

Recommendation: [GO / CONDITIONAL GO / NO-GO]
Rationale: [Why]
```

### Gate
**Human decides Go/No-Go → If GO, proceed to Assessment**

---

## Phase 3: Assessment

### Tasks Performed
1. **Classify Opportunity**
   - Deal type selection (see Framework Selection below)
   - Offering type selection
   - Complexity assessment

2. **Map Capabilities**
   - Match client requirements to your capabilities
   - Identify gaps and mitigations
   - Score overall fit

3. **Model ROI**
   - Identify client's current costs/pain
   - Project savings from your solution
   - Calculate break-even and ROI

4. **Configure Pricing**
   - Select appropriate package/components from your pricing model
   - Apply discounts or adjustments
   - Structure success fee if applicable

### Framework Selection: Deal Types

| Deal Type | When to Use | Template | Pages |
|-----------|-------------|----------|-------|
| **GOVERNMENT** | RFPs, public sector, compliance-heavy | `government-style` | 20-30 |
| **COMMERCIAL** | Private sector, ROI-focused | `commercial-style` | 12-15 |
| **PARTNERSHIP** | Joint ventures, collaborations | `partnership-style` | 10-15 |
| **SIMPLE/SOW** | Straightforward scopes, quick turnaround | `simple-style` | 3-8 |

### Framework Selection: Offering Types

| Offering Type | Components | Typical Range |
|---------------|------------|---------------|
| **CONSULTING** | Strategy + Advisory | $30K-$75K |
| **IMPLEMENTATION** | Strategy + Build + Deploy | $40K-$100K |
| **TRAINING** | Methodology + Enablement | $15K-$35K |
| **FULL ENGAGEMENT** | All components | $50K-$150K+ |

### Output: Assessment Package
```
CLASSIFICATION:
• Deal Type: [Type]
• Offering: [Components]
• Complexity: [Low/Medium/High]

CAPABILITY FIT:
• Fit Score: [X/10]
• Strong Matches: [What you nail]
• Gaps: [What needs mitigation]

ROI MODEL:
• Baseline Cost: $[Amount] annually
• Projected Savings: $[Amount] annually
• Break-even: Month [X]
• Year 1 ROI: [X]%

PRICING:
• Base Investment: $[Amount]
• Success Fee: [If applicable]
• Total Range: $[Min] - $[Max]

Questions for Human:
1. [ROI assumption to validate]
2. [Pricing question]
```

### Gate
**Human approves assessment → Proceed to Strategy**

---

## Phase 4: Strategy

### Tasks Performed
1. **Competitive Analysis**
   - Identify likely competitors
   - Analyze their strengths/weaknesses
   - Develop counter-positioning

2. **Win Theme Development**
   - Extract 3-5 compelling themes from discovery
   - Map themes to proposal sections

3. **Case Study Matching**
   - Match relevant past performance from your case studies
   - Rank by fit to this opportunity

### Output: Strategy Package
```
COMPETITIVE POSITIONING:
• Lead With: [Primary differentiator]
• Key Competitors: [Names]
• Our Counter: [How we win]

WIN THEMES:
1. [Theme 1 - e.g., "Speed to Value"]
2. [Theme 2 - e.g., "Outcome-Aligned"]
3. [Theme 3 - e.g., "Low Risk"]

CASE STUDIES SELECTED:
• [Case 1] - Match: [X/10]
• [Case 2] - Match: [X/10]

ELEVATOR PITCH:
"[2-3 sentence pitch]"

Recommended Template: [Government/Commercial/Simple]
```

### Gate
**Human approves strategy + selects template → Proceed to Draft**

---

## Phase 5: Draft

### Sections Generated (varies by template)

**Government Style:**
1. Executive Summary
2. Understanding of Requirements
3. Technical Approach
4. Management Approach
5. Past Performance
6. Staffing Plan
7. Price Proposal
8. Appendices

**Commercial Style:**
1. Executive Summary
2. The Challenge You're Facing
3. Our Approach
4. Your Investment
5. Why [Your Company]
6. Next Steps

**Simple/SOW Style:**
1. Scope of Work
2. Deliverables
3. Timeline
4. Investment
5. Assumptions
6. Acceptance

### Writing Guidelines Applied
- Lead each section with client benefit
- Thread win themes throughout
- Use your configured brand voice
- Include tables for data, narrative for story
- Mark placeholders clearly: `[PLACEHOLDER: What's needed]`

### Output: Draft Package
```
DRAFT SUMMARY:
• Total Sections: [X]
• Word Count: ~[X,XXX]

PLACEHOLDERS TO FILL:
• [Placeholder 1] - [What's needed]
• [Placeholder 2] - [What's needed]

AREAS NEEDING REVIEW:
• [Section] - [Why]
```

### Gate
**Human reviews draft → Proceed to QA**

---

## Phase 6: QA

### Checks Performed

| Check | What It Validates |
|-------|-------------------|
| **Requirements** | All client requirements addressed |
| **Consistency** | Numbers match throughout, timeline consistent |
| **Compliance** | Brand guidelines followed, legal terms appropriate |
| **Quality** | Win themes threaded, methodology applied, professional tone |

### Output: QA Report
```
OVERALL STATUS: [PASS / WARNING / FAIL]

CHECK RESULTS:
• Requirements: [Pass/Warning/Fail]
• Consistency: [Pass/Warning/Fail]
• Compliance: [Pass/Warning/Fail]
• Quality: [Pass/Warning/Fail]

ISSUES FOUND:
Critical:
• [Issue] - [Fix required]

Warnings:
• [Issue] - [Recommendation]

MUST FIX:
• [Item]

SHOULD FIX:
• [Item]
```

### Gate
**Human decides: Fix issues → Back to Draft, OR Approve → Output**

---

## Phase 7: Output

### Final Deliverables
- `proposal_final.md` - Markdown version
- `proposal_final.docx` - Word document (if requested)
- `proposal_final.pdf` - PDF version (if requested)
- Submission checklist

### Completion
```
PROPOSAL COMPLETE

File: [Path to final document]
Due: [Date]

Remaining Tasks:
☐ Fill any remaining placeholders
☐ Final human proofread
☐ Export to submission format
☐ Submit by [deadline]
```

---

## Commands Reference

| Command | What It Does |
|---------|--------------|
| `run proposal [client]` | Start new proposal |
| `status` | Show current phase |
| `go` | Approve Go decision |
| `approved` | Approve current phase |
| `proceed` | Move to next phase |
| `revise [feedback]` | Request revision |

---

## Input Options

The system accepts 3 input formats:

| Input Type | What You Provide | Best For |
|------------|------------------|----------|
| **Structured Markdown** | Organized sections with Client, Requirements, Timeline | When you have organized notes |
| **Unstructured Paste** | Meeting notes, email threads, synthesis | When information is scattered |
| **Direct Answers** | Respond to intake questions | When starting fresh |

---

## Customization: What You Can Change

### ✅ ADD (Encouraged)
- Your own case studies
- Additional win themes
- Custom sections to templates
- Industry-specific terminology
- New offering types

### ❌ DON'T REPLACE
- The 7-phase workflow sequence
- The discovery questions
- The decision gates
- The QA checks

**The methodology is the tool. Customize the content, not the process.**

---

## Files in This Skill

```
proposal-generator/
├── SKILL.md                           # This file - main instructions
├── references/
│   ├── frameworks/
│   │   ├── deal-types.md              # Deal type definitions
│   │   ├── offering-types.md          # Offering definitions
│   │   └── methodology.md             # Strategic framework
│   ├── templates/
│   │   ├── government-style.md        # 20-30 page formal
│   │   ├── commercial-style.md        # 12-15 page ROI-focused
│   │   ├── partnership-style.md       # 10-15 page narrative
│   │   └── simple-sow.md              # 3-8 page SOW
│   └── prompts/
│       ├── discovery-prompts.md       # Research agent prompts
│       ├── assessment-prompts.md      # Classification prompts
│       ├── construction-prompts.md    # Writing prompts
│       └── review-prompts.md          # QA check prompts
├── customization/
│   ├── my-company-profile.json        # YOUR company data
│   ├── my-pricing-model.json          # YOUR pricing
│   ├── my-case-studies.json           # YOUR past performance
│   └── my-brand-guidelines.md         # YOUR voice/messaging
└── assets/
    └── Setup-Guide.pdf                # Platform setup instructions
```

---

## Tips for Best Results

### Give Good Inputs
- More context = better output
- Include quantified pain points when known
- Share any competitive intel
- Note stakeholder priorities

### Make Clear Decisions
- "Go" or "No-Go" - don't waffle
- Specific feedback: "Emphasize X more, less Y"
- Edit drafts directly when faster than describing

### Trust the Process
- Let each phase complete before reviewing
- Use the QA report - it catches things humans miss
- The methodology integration is automatic

### Know When to Override
- The system recommends, you decide
- Your client relationships matter
- Industry expertise trumps templates
- When in doubt, ask for options

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Research seems thin | Provide more starting info, request specific focus |
| ROI numbers feel wrong | Check baseline assumptions, adjust inputs |
| Themes don't resonate | Override with your own themes |
| Draft misses the mark | Provide specific section feedback |
| QA finds many issues | Normal for first draft - iterate |

---

*Proposal Generator Skill v1.0*
*Built on the THINK methodology*
