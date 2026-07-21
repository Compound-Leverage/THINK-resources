---
name: lead-discovery
description: Automate lead qualification for government contractors and economic development organizations. Scores opportunities across 5 dimensions and surfaces weekly decision-ready prospects from procurement sources, grant databases, and funding announcements.
---

# Lead Discovery and Prioritization Module

## Skill Overview
Automates lead qualification for government contractors, economic development organizations, and consulting firms to surface weekly decision-ready opportunities. Reduces manual review time by 70%+ by eliminating scanning and interpretation work.

## Trigger Patterns
Use this skill when the user:
- Needs to qualify leads from procurement sources (SAM.gov, state/local portals, grants databases)
- Wants automated weekly shortlists of high-probability opportunities
- Asks to evaluate RFPs, grants, budget disclosures, or hiring signals
- Requests lead scoring across multiple dimensions
- Needs to filter out low-fit or exploratory opportunities
- Wants prioritized action recommendations

## Core Methodology

### Input Requirements
Qualified leads must have ALL of:
- **Time-bound need**: Deadline or procurement timeline
- **Intent signal**: RFP, grant, budget filing, hiring announcement, compliance deadline
- **Business tie**: Connected to revenue, compliance, or operational necessity
- **AI-addressable work**: Manual processes suitable for Digital Employee implementation

### Disqualifiers (Auto-exclude)
- Exploratory only (no commitment signal)
- No timeline or deadline
- No decision authority identified
- Tool shopping without implementation intent
- Capability gap >40%
- Ethics risk (surveillance, manipulation, deceptive practices)
- Impossible timeline (<2 weeks for complex implementation)

### Source Hierarchy
**Primary (High Signal)**
- SAM.gov RFPs and contract awards
- State/local procurement portals
- County business filings
- Lis pendens (foreclosure/legal filings indicating need)
- Federal/state grants databases
- Workforce development budget disclosures

**Secondary (Requires Trigger)**
- Budget announcements + hiring
- Organizational restructuring + compliance deadline
- Technology modernization + RFP language
- Real estate/Zillow data (only with foreclosure/distress signal)

### Scoring Dimensions (1-5 scale)

**1. Fit** (Does capability match need?)
- 5: Perfect alignment, zero gaps
- 4: Minor gaps, addressable with existing components
- 3: Moderate adaptation needed
- 2: Significant development required
- 1: Fundamental mismatch

**2. Win Probability** (Can we credibly win?)
- 5: Incumbent or exclusive relationship
- 4: Strong position, limited competition
- 3: Competitive but viable
- 2: Crowded field, weak position
- 1: Long-shot or impossible

**3. Economic Value** (Revenue potential)
- 5: $100K+
- 4: $50-100K
- 3: $25-50K
- 2: $10-25K
- 1: <$10K

**4. Timeline Realism** (Can we deliver?)
- 5: 6+ weeks for complex, ample for simple
- 4: 4-6 weeks
- 3: 2-4 weeks (tight but feasible)
- 2: <2 weeks (high risk)
- 1: Impossible given scope

**5. Strategic Leverage** (Long-term value)
- 5: Category leadership opportunity (conference keynote, case study, market positioning)
- 4: Strong reference potential (named testimonial, public win)
- 3: Good portfolio addition
- 2: Transactional, limited upside
- 1: No strategic value or reputation risk

### Decision Rules

**Include** if:
- Aggregate score ≥12
- No dimension = 1
- No disqualifiers present

**Exclude** if:
- Aggregate score <12
- Any dimension = 1
- Disqualifier present

**Monitor** if:
- Insufficient data to score
- Missing key details but potential exists
- Timeline unclear but opportunity interesting

### Output Format

For each included lead:
```
Organization: [Name]
Opportunity: [Title]
Summary: [2-3 sentence plain-English description]
Fit: [Why this matches capabilities]
Scoring: [5 dimensions with justifications]
Risks: [Concerns or gaps to address]
Recommended Action: Pursue | Delegate Outreach | Monitor
Deadline: [Date]
Value: [Estimated amount]
Source: [URL]
```

Weekly batch target: 5-10 qualified leads

### Assumptions Handling
When data is incomplete but inferrable from context:
- Make reasonable assumption
- Flag it clearly: "Assumption: [detail] based on [reasoning]"
- Lower confidence scores appropriately

When data is uninferrable:
- Output as "Monitor" decision
- Note: "Insufficient data: [what's missing]"
- Don't guess or speculate

## Success Metrics
- Time reduction: 70%+ less manual review
- Pursue rate: >60% of surfaced leads worth outreach
- Conversion: Track to qualified conversation (90-day window)

## Out of Scope
This module does NOT:
- Update CRM systems
- Send outreach emails
- Write proposals
- Manage relationships
- Handle negotiation
- Execute follow-up sequences

## Usage Example

**Input**: Maryland workforce development RFP for AI training program, $75K, 8-week timeline, requires curriculum development and cohort facilitation

**Output**:
- Decision: Include
- Fit: 5 (THINK methodology perfect match)
- Win: 4 (Bowie State partnership demonstrates capability)
- Value: 4 ($75K)
- Timeline: 5 (8 weeks ample)
- Leverage: 5 (HBCU partnership expansion, conference content)
- Aggregate: 23
- Recommended Action: Pursue
- Risks: None material
- Next Step: Schedule intake call with procurement officer

## Implementation Notes

This skill provides the specification and methodology. Actual implementation requires choosing a delivery mechanism:
- Notion database + automation
- Email digest
- JSON API endpoint
- Google Sheets integration

The skill focuses on qualification logic, not execution infrastructure.
