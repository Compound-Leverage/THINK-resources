# Output Templates - JSON Schemas and Report Formats

## JSON Opportunity Record Schema

### Complete Opportunity Object

```json
{
  "opportunity_id": "string",
  "title": "string",
  "source": "string",
  "source_type": "string",
  "url": "string",
  "funding_amount": "string",
  "funding_amount_numeric": number,
  "geography": "string",
  "geography_type": "string",
  "score": number,
  "score_breakdown": {
    "funding": number,
    "timeline": number,
    "competition": number,
    "geography": number
  },
  "routing_tag": "string",
  "deadline": "string",
  "deadline_date": "YYYY-MM-DD",
  "stage": "string",
  "summary": "string",
  "target_orgs": ["array of strings"],
  "key_contacts": [
    {
      "name": "string",
      "title": "string",
      "organization": "string",
      "email": "string",
      "phone": "string"
    }
  ],
  "next_action": "string",
  "white_paper_angle": "string",
  "proposal_strategy": "string",
  "intelligence_brief_priority": "string",
  "keywords_matched": ["array of strings"],
  "industry_sectors": ["array of strings"],
  "target_populations": ["array of strings"],
  "partnership_requirements": "string",
  "match_requirements": "string",
  "eligibility_notes": "string",
  "past_awards": ["array of strings"],
  "competition_analysis": "string",
  "risk_factors": ["array of strings"],
  "similar_opportunities": ["array of opportunity_ids"],
  "date_discovered": "YYYY-MM-DD",
  "last_updated": "YYYY-MM-DD",
  "status": "string",
  "notes": "string"
}
```

### Field Definitions

**opportunity_id:** Unique identifier in format `[STATE]-[TYPE]-[YEAR]-[NUMBER]`
- STATE: DE, MD, PA, VA, DC, FED
- TYPE: WF (workforce), ED (economic dev), AI (AI-specific), MX (mixed)
- YEAR: Four digits
- NUMBER: Sequential three digits

**title:** Full opportunity title as published

**source:** Origin of opportunity (e.g., "Maryland Senate Bill 423", "DOL ETA Announcement")

**source_type:** Category of source
- Values: "legislation", "agency_announcement", "rfp", "governor_press_release", "budget_document", "strategic_plan", "grants_gov", "other"

**url:** Direct link to opportunity or source document

**funding_amount:** Funding as string (e.g., "$2.5M", "$250,000", "Up to $500K")

**funding_amount_numeric:** Numeric value for sorting/filtering (convert to dollars)

**geography:** State/region (e.g., "Maryland", "Pennsylvania", "Multi-state", "Federal")

**geography_type:** Classification
- Values: "target_state", "adjacent_state", "federal", "multi_state", "regional"

**score:** Total score 0-100

**score_breakdown:** Individual component scores
- funding: 0-40
- timeline: 0-20
- competition: 0-20
- geography: 0-20

**routing_tag:** Action classification
- Values: "white-paper-ready", "proposal-ready", "nurture-needed", "monitor-only"

**deadline:** Deadline as string (e.g., "March 15, 2026", "Rolling", "TBD")

**deadline_date:** ISO date format YYYY-MM-DD (or null if TBD)

**stage:** Opportunity lifecycle stage
- Values: "pre-funding-legislative", "pre-funding-planning", "pre-rfp", "active-rfp", "rolling", "anticipated"

**summary:** 2-4 sentence description of opportunity

**target_orgs:** List of agencies/organizations managing opportunity

**key_contacts:** Array of contact objects (name, title, organization, email, phone)

**next_action:** Specific recommended action with timeline

**white_paper_angle:** Suggested white paper topic/framing (for white-paper-ready)

**proposal_strategy:** High-level proposal approach (for proposal-ready)

**intelligence_brief_priority:** Priority level
- Values: "very_high", "high", "medium", "low"

**keywords_matched:** Keywords from search criteria that triggered this match

**industry_sectors:** Relevant industries
- Values: "manufacturing", "healthcare", "it", "construction", "hospitality", "energy", "logistics", "multiple"

**target_populations:** Populations served
- Values: "dislocated_workers", "youth", "veterans", "justice_involved", "rural", "urban", "low_income", "general"

**partnership_requirements:** Required or recommended partnerships

**match_requirements:** Match/cost-share requirements

**eligibility_notes:** Key eligibility criteria or restrictions

**past_awards:** Previous similar awards if known (organization names or links)

**competition_analysis:** Assessment of competitive landscape

**risk_factors:** Potential challenges or barriers

**similar_opportunities:** Links to related opportunity_ids in database

**date_discovered:** Date first identified

**last_updated:** Date record last modified

**status:** Current tracking status
- Values: "new", "monitoring", "pursuing", "submitted", "awarded", "declined", "closed"

**notes:** Free-form notes for internal use

---

## Example JSON Records

### Example 1: White Paper Ready Opportunity

```json
{
  "opportunity_id": "MD-WF-2025-001",
  "title": "Maryland AI Workforce Retraining Initiative",
  "source": "Maryland Senate Bill 423",
  "source_type": "legislation",
  "url": "https://mgaleg.maryland.gov/2025RS/bills/sb/sb0423.htm",
  "funding_amount": "$2.5M",
  "funding_amount_numeric": 2500000,
  "geography": "Maryland",
  "geography_type": "target_state",
  "score": 100,
  "score_breakdown": {
    "funding": 40,
    "timeline": 20,
    "competition": 20,
    "geography": 20
  },
  "routing_tag": "white-paper-ready",
  "deadline": "Program launch estimated Fall 2025",
  "deadline_date": "2025-10-01",
  "stage": "pre-funding-legislative",
  "summary": "Bill proposes $2.5M for FY2026 pilot program for retraining workers displaced or at risk of displacement due to AI and automation. Targets manufacturing and administrative sectors. Requires partnership between MD Department of Labor, community colleges, and employer consortia. Bill passed committee and awaiting Senate floor vote.",
  "target_orgs": [
    "Maryland Department of Labor",
    "Maryland Community College System",
    "Governor's Workforce Development Board"
  ],
  "key_contacts": [
    {
      "name": "TBD - Monitor bill for agency contact",
      "title": "Program Manager (to be assigned)",
      "organization": "MD Department of Labor",
      "email": "TBD",
      "phone": "TBD"
    }
  ],
  "next_action": "Draft white paper on AI displacement solutions for Maryland manufacturing sector within 30 days. Target MD Department of Labor, bill sponsors, and GWDB. Position as implementation thought leader before RFP released.",
  "white_paper_angle": "Skills-to-Jobs Framework: Proactive AI Displacement Response in Maryland Manufacturing",
  "proposal_strategy": "Position during pre-RFP phase; offer to serve as technical advisor or implementation partner",
  "intelligence_brief_priority": "very_high",
  "keywords_matched": [
    "workforce retraining",
    "AI",
    "automation",
    "displacement",
    "manufacturing",
    "appropriation",
    "partnership"
  ],
  "industry_sectors": [
    "manufacturing",
    "multiple"
  ],
  "target_populations": [
    "dislocated_workers",
    "at-risk_workers"
  ],
  "partnership_requirements": "Must include MD DOL, community college, and employer consortium",
  "match_requirements": "Not specified in bill language",
  "eligibility_notes": "Program design TBD; likely will be competitive grants or contracts once established",
  "past_awards": [],
  "competition_analysis": "Pre-RFP stage means competition not yet defined. Opportunity to influence program design and requirements. Likely 5-10 serious competitors once RFP released given Maryland workforce development landscape.",
  "risk_factors": [
    "Bill must pass Senate and House",
    "Governor must sign",
    "Funding must survive budget negotiations",
    "Timeline uncertain until enacted"
  ],
  "similar_opportunities": [],
  "date_discovered": "2025-10-23",
  "last_updated": "2025-10-23",
  "status": "monitoring",
  "notes": "Monitor bill progress weekly. Attend any public hearings. Begin drafting white paper outline. Identify Maryland manufacturing employers for potential partnership."
}
```

### Example 2: Proposal Ready Opportunity

```json
{
  "opportunity_id": "VA-ED-2025-012",
  "title": "GO Virginia Region 4 Talent Development Grant",
  "source": "GO Virginia Website",
  "source_type": "rfp",
  "url": "https://govirginia.org/region-4-grants/",
  "funding_amount": "Up to $300,000",
  "funding_amount_numeric": 300000,
  "geography": "Virginia Region 4 (Southwest)",
  "geography_type": "target_state",
  "score": 85,
  "score_breakdown": {
    "funding": 40,
    "timeline": 15,
    "competition": 10,
    "geography": 20
  },
  "routing_tag": "proposal-ready",
  "deadline": "January 15, 2026",
  "deadline_date": "2026-01-15",
  "stage": "active-rfp",
  "summary": "Competitive grant for workforce development projects supporting regional priority sectors (advanced manufacturing, IT, healthcare). Requires regional partnership including employer engagement. 1:1 matching funds required. Applications due in 90 days. Evaluation criteria focus on regional impact, sustainability, and employer commitment.",
  "target_orgs": [
    "GO Virginia Region 4 Council",
    "Virginia DHCD (administering agency)"
  ],
  "key_contacts": [
    {
      "name": "Sarah Johnson",
      "title": "Region 4 GO Virginia Program Manager",
      "organization": "Cumberland Plateau Planning District Commission",
      "email": "sjohnson@cppdcva.org",
      "phone": "276-555-0123"
    }
  ],
  "next_action": "Initiate proposal development immediately. By Day 7: Identify and contact regional partners (community college, workforce board, employers). By Day 14: Secure matching funds commitment. By Day 30: Complete draft proposal. By Day 60: Finalize and review. Submit by Day 83 (1 week buffer).",
  "white_paper_angle": "N/A - RFP stage",
  "proposal_strategy": "Focus on advanced manufacturing with AI/automation component. Leverage existing VCCS relationships. Target New River/Mount Rogers Community College as lead or partner. Secure 2-3 employer letters of commitment from regional manufacturers. Emphasize sustainability beyond grant period through employer contributions.",
  "intelligence_brief_priority": "high",
  "keywords_matched": [
    "workforce development",
    "advanced manufacturing",
    "IT",
    "regional partnership",
    "talent development"
  ],
  "industry_sectors": [
    "manufacturing",
    "it",
    "healthcare"
  ],
  "target_populations": [
    "general",
    "incumbent_workers"
  ],
  "partnership_requirements": "Regional partnership required. Must include employers. Community college or training provider partnership strongly recommended.",
  "match_requirements": "1:1 match required. Can be cash or in-kind. Employer contributions count toward match.",
  "eligibility_notes": "Lead applicant must be regional entity (workforce board, planning district, economic development organization, educational institution). Must serve Region 4 counties.",
  "past_awards": [
    "Previous Region 4 awardee: New River Community College manufacturing training (2023, $250K)",
    "Similar project: Region 2 healthcare pipeline (2024, $350K)"
  ],
  "competition_analysis": "Likely 10-15 applications for Region 4 funding. Past success rate approximately 30-40%. Proposals with strong employer engagement and clear sustainability plan score highest. Community college partnerships well-regarded.",
  "risk_factors": [
    "Tight 90-day timeline requires immediate action",
    "Match requirement may be barrier",
    "Must establish regional partnerships quickly",
    "Region 4 is rural/economically challenged - may impact employer match capacity"
  ],
  "similar_opportunities": [
    "VA-ED-2024-008"
  ],
  "date_discovered": "2025-10-18",
  "last_updated": "2025-10-20",
  "status": "evaluating",
  "notes": "Reached out to New River CC on 10/19 - interested in partnering. Need to contact Virginia Career Works West (Region 4 workforce board) and identify employer partners. Match requirement is key challenge to resolve."
}
```

### Example 3: Federal Opportunity

```json
{
  "opportunity_id": "FED-WF-2025-021",
  "title": "DOL Strengthening Community Colleges Training Grant (SCCTG)",
  "source": "Department of Labor Employment and Training Administration",
  "source_type": "grants_gov",
  "url": "https://grants.gov/view-opportunity.html?oppId=12345",
  "funding_amount": "$2M - $5M per award",
  "funding_amount_numeric": 3500000,
  "geography": "Federal (national competition)",
  "geography_type": "federal",
  "score": 90,
  "score_breakdown": {
    "funding": 40,
    "timeline": 20,
    "competition": 10,
    "geography": 20
  },
  "routing_tag": "proposal-ready",
  "deadline": "March 30, 2026",
  "deadline_date": "2026-03-30",
  "stage": "active-rfp",
  "summary": "Competitive grant for community college consortia to develop or expand workforce training programs in high-demand industries with emphasis on AI, advanced manufacturing, and healthcare. Multi-state consortia encouraged. Community college must be lead applicant. Requires employer partnerships and sustainability plan. 48-month project period. Anticipates 15-20 awards nationally.",
  "target_orgs": [
    "U.S. Department of Labor",
    "Employment and Training Administration"
  ],
  "key_contacts": [
    {
      "name": "Michael Chen",
      "title": "Grant Officer",
      "organization": "DOL ETA",
      "email": "chen.michael@dol.gov",
      "phone": "202-555-0198"
    }
  ],
  "next_action": "Attend technical assistance webinar (Nov 15, 2025). Identify community college partners in MD, VA, PA for multi-state consortium. Begin partnership MOU discussions. Monitor for frequently asked questions. Develop proposal outline by Dec 15. Draft complete by Feb 15. Finalize by March 15 (2-week buffer).",
  "white_paper_angle": "N/A - RFP stage",
  "proposal_strategy": "Multi-state consortium model across MD-VA-PA corridor. Focus on AI/automation impact on manufacturing workforce. Position community colleges as anchor institutions with us as workforce development content expert and training provider. Emphasize regional manufacturing sector needs and employer partnerships. Leverage existing relationships with Maryland, Virginia, Pennsylvania community college systems.",
  "intelligence_brief_priority": "very_high",
  "keywords_matched": [
    "community college",
    "workforce training",
    "high-demand industries",
    "AI",
    "advanced manufacturing",
    "healthcare",
    "multi-state",
    "consortia"
  ],
  "industry_sectors": [
    "manufacturing",
    "healthcare",
    "it"
  ],
  "target_populations": [
    "dislocated_workers",
    "incumbent_workers",
    "youth"
  ],
  "partnership_requirements": "Community college lead applicant required. Employer partnerships required. Consortia of multiple institutions encouraged. Workforce board partnership recommended.",
  "match_requirements": "No match required, but cost-sharing is viewed favorably in review criteria (up to 5 points)",
  "eligibility_notes": "Lead applicant must be public community college. Can partner with training providers, workforce boards, industry associations, employers. Geographic focus must be clearly defined.",
  "past_awards": [
    "Similar program 2023: Ohio consortium led by Sinclair CC ($4.2M)",
    "Similar program 2023: Texas consortium led by Austin CC ($3.8M)",
    "Mid-Atlantic example: Maryland/Virginia partnership (different program, 2022)"
  ],
  "competition_analysis": "Highly competitive - national competition with approximately 100-150 applications expected for 15-20 awards (10-15% success rate). Multi-state consortia historically perform well. Strong employer engagement critical. Previous DOL grantee experience helpful but not required. Evaluation criteria weight: Need (25%), Quality of program design (30%), Organizational capacity (25%), Budget (20%).",
  "risk_factors": [
    "Highly competitive national program",
    "Requires significant proposal development resources",
    "Community college must be lead (limits our role)",
    "Multi-state coordination complexity",
    "48-month commitment",
    "Federal compliance requirements"
  ],
  "similar_opportunities": [
    "FED-WF-2023-015",
    "FED-ED-2024-022"
  ],
  "date_discovered": "2025-10-22",
  "last_updated": "2025-10-25",
  "status": "pursuing",
  "notes": "Preliminary discussions with Montgomery College (MD), Northern Virginia CC (VA), and Community College of Philadelphia (PA). All expressed interest. Need to formalize consortium structure and determine lead institution. Registered for TA webinar on 11/15."
}
```

---

## Markdown Report Templates

### Template 1: Intelligence Brief (Individual Opportunity)

```markdown
# INTELLIGENCE BRIEF
## [Opportunity Title]

**Opportunity ID:** [ID]
**Date:** [Date]
**Priority:** [Very High / High / Medium / Low]
**Score:** [Score]/100
**Routing Tag:** [white-paper-ready / proposal-ready / nurture-needed]

---

## EXECUTIVE SUMMARY

[2-3 sentence high-level summary of opportunity and why it matters]

---

## OPPORTUNITY DETAILS

**Source:** [Source]
**URL:** [URL]
**Funding Amount:** [Amount]
**Geography:** [State/Region]
**Deadline:** [Deadline]
**Stage:** [Lifecycle stage]

---

## SCORING BREAKDOWN

| Category | Score | Max | Rationale |
|----------|-------|-----|-----------|
| Funding Size | [XX] | 40 | [Rationale] |
| Timeline | [XX] | 20 | [Rationale] |
| Competition | [XX] | 20 | [Rationale] |
| Geography | [XX] | 20 | [Rationale] |
| **TOTAL** | **[XXX]** | **100** | |

---

## DESCRIPTION

[Detailed description of the opportunity - 1-2 paragraphs]

### Key Features
- [Feature 1]
- [Feature 2]
- [Feature 3]

### Target Populations
- [Population 1]
- [Population 2]

### Industry Sectors
- [Sector 1]
- [Sector 2]

---

## STRATEGIC ANALYSIS

### Why This Matters
[Explanation of strategic importance]

### Competitive Landscape
[Analysis of likely competition and competitive positioning]

### Strategic Fit Assessment
[How this aligns with organizational capabilities and priorities]

---

## RECOMMENDED STRATEGY

### [White Paper Approach / Proposal Approach]

**Recommended Angle:** [Specific positioning]

**Key Messages:**
1. [Message 1]
2. [Message 2]
3. [Message 3]

**Target Audience:**
- [Audience 1]
- [Audience 2]

---

## PARTNERSHIP OPPORTUNITIES

**Required Partners:**
- [Partner type 1]: [Specific suggestions if known]
- [Partner type 2]: [Specific suggestions if known]

**Recommended Partners:**
- [Partner type 3]

**Teaming Strategy:** [Approach to partnership development]

---

## KEY CONTACTS & RELATIONSHIPS

| Name | Title | Organization | Contact Info | Relationship Status |
|------|-------|--------------|--------------|---------------------|
| [Name] | [Title] | [Org] | [Email/Phone] | [New/Existing/Target] |

---

## ACTION PLAN

### Immediate Actions (Next 7 Days)
1. [Action item with owner and date]
2. [Action item with owner and date]
3. [Action item with owner and date]

### Short-term Actions (Next 30 Days)
1. [Action item with owner and date]
2. [Action item with owner and date]

### Long-term Actions (30+ Days)
1. [Action item with owner and date]

---

## RISK FACTORS & MITIGATION

| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|---------------------|
| [Risk 1] | [H/M/L] | [H/M/L] | [Strategy] |
| [Risk 2] | [H/M/L] | [H/M/L] | [Strategy] |

---

## SIMILAR OPPORTUNITIES & PRECEDENTS

**Past Awards:**
- [Previous award example 1]
- [Previous award example 2]

**Related Opportunities:**
- [Opportunity ID]: [Brief description]

**Lessons Learned:**
[Key insights from similar opportunities]

---

## ATTACHMENTS & RESOURCES

- [Link to source document]
- [Link to related resource 1]
- [Link to related resource 2]

---

**Prepared by:** [Name]
**Intelligence Brief Version:** 1.0
**Distribution:** [Internal team list]
```

---

### Template 2: Weekly Digest

```markdown
# MANDATE SEARCH WEEKLY DIGEST
## Week of [Date Range]

**Report Date:** [Date]
**Reporting Period:** [Start Date] - [End Date]

---

## EXECUTIVE SUMMARY

**Total Opportunities Identified:** [Number]
**High-Priority Opportunities (Score 80+):** [Number]
**Total Potential Funding Value:** [Dollar amount]

**Geographic Distribution:**
- Delaware: [Number] opportunities
- Maryland: [Number] opportunities
- Pennsylvania: [Number] opportunities
- Virginia: [Number] opportunities
- District of Columbia: [Number] opportunities
- Federal/Multi-state: [Number] opportunities

**Routing Tag Distribution:**
- White Paper Ready: [Number]
- Proposal Ready: [Number]
- Nurture Needed: [Number]
- Monitor Only: [Number]

---

## TOP 5 OPPORTUNITIES THIS WEEK

### 1. [Opportunity Title] - Score: [XX]/100

**ID:** [ID] | **Tag:** [Tag] | **State:** [State] | **Funding:** [Amount]

[1-2 sentence description]

**Key Action:** [Immediate action required]
**Deadline:** [Deadline]

---

### 2. [Opportunity Title] - Score: [XX]/100

[Repeat structure]

---

### 3-5. [Continue for top 5]

---

## ALL OPPORTUNITIES BY STATE

### Delaware ([Number] total)

#### DE-XX-2025-XXX | [Title] | Score: [XX]
- **Funding:** [Amount]
- **Tag:** [Tag]
- **Deadline:** [Date]
- **Summary:** [1 sentence]
- **Action:** [Brief action]

[Repeat for each DE opportunity]

### Maryland ([Number] total)

[Repeat structure]

### Pennsylvania ([Number] total)

[Repeat structure]

### Virginia ([Number] total)

[Repeat structure]

### District of Columbia ([Number] total)

[Repeat structure]

### Federal / Multi-State ([Number] total)

[Repeat structure]

---

## OPPORTUNITIES BY ROUTING TAG

### White Paper Ready ([Number] opportunities)

**These require immediate thought leadership positioning:**

| ID | Title | State | Score | Funding | Action Deadline |
|----|-------|-------|-------|---------|-----------------|
| [ID] | [Title] | [State] | [Score] | [Amount] | [Date] |

### Proposal Ready ([Number] opportunities)

**These require proposal development:**

| ID | Title | State | Score | Funding | RFP Deadline |
|----|-------|-------|-------|---------|--------------|
| [ID] | [Title] | [State] | [Score] | [Amount] | [Date] |

### Nurture Needed ([Number] opportunities)

**These require relationship building:**

| ID | Title | State | Score | Funding | Status |
|----|-------|-------|-------|---------|--------|
| [ID] | [Title] | [State] | [Score] | [Amount] | [Status] |

---

## EMERGING TRENDS

**This Week's Observations:**

1. **[Trend 1]:** [Description of pattern noticed]

2. **[Trend 2]:** [Description]

3. **[Trend 3]:** [Description]

**Policy/Legislative Activity:**
- [Notable bill/policy development 1]
- [Notable bill/policy development 2]

---

## INTELLIGENCE ALERTS

**Urgent Items Requiring Immediate Attention:**

1. **[Alert Title]**
   - Opportunity: [ID]
   - Issue: [What requires attention]
   - Deadline: [Date]
   - Action Required: [What to do]

---

## UPCOMING DEADLINES (Next 30 Days)

| Date | Opportunity ID | Title | Type | Priority |
|------|----------------|-------|------|----------|
| [Date] | [ID] | [Title] | [RFP/Listening Session/etc] | [H/M/L] |

---

## COMPARISON TO PREVIOUS WEEK

| Metric | This Week | Last Week | Change |
|--------|-----------|-----------|--------|
| Total Opportunities | [N] | [N] | [+/- N] |
| Score 80+ | [N] | [N] | [+/- N] |
| White Paper Ready | [N] | [N] | [+/- N] |
| Proposal Ready | [N] | [N] | [+/- N] |
| Total Funding Value | [$X] | [$X] | [+/- $X] |

---

## ACTIONS IN PROGRESS

**Opportunities Currently Being Pursued:**

| ID | Title | Status | Next Milestone | Owner |
|----|-------|--------|----------------|-------|
| [ID] | [Title] | [Status] | [Milestone] | [Name] |

---

## RECOMMENDATIONS

**High Priority Actions for Coming Week:**

1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]

**Strategic Considerations:**
- [Strategic note 1]
- [Strategic note 2]

---

## APPENDIX: SEARCH PERFORMANCE

**Sources Monitored This Week:**
- Grants.gov: [Number] new postings reviewed
- State legislatures: [Number] bills tracked
- Agency announcements: [Number] reviewed
- Press releases: [Number] reviewed
- Workforce board sites: [Number] checked

**Search Effectiveness:**
- True positives: [Number]
- False positives filtered: [Number]
- Filter effectiveness: [Percentage]

---

**Report Prepared By:** Mandate Search Agent
**Next Report:** [Date]
**Questions/Feedback:** [Contact]
```

---

### Template 3: Quick Alert Format

```markdown
# OPPORTUNITY ALERT

## 🚨 [VERY HIGH / HIGH / MEDIUM] PRIORITY

**Date:** [Date]
**Opportunity ID:** [ID]

---

### [Opportunity Title]

**Score:** [XX]/100
**Routing Tag:** [Tag]
**Funding:** [Amount]
**State:** [State]

---

### QUICK SUMMARY

[2-3 sentences on what this is and why it matters]

---

### ACTION REQUIRED

**Deadline:** [Deadline]

**Immediate Next Steps:**
1. [Action 1] - Due: [Date]
2. [Action 2] - Due: [Date]
3. [Action 3] - Due: [Date]

**Owner:** [Person responsible]

---

### KEY DETAILS

- **Source:** [Source]
- **URL:** [URL]
- **Stage:** [Stage]
- **Partnerships:** [Required/recommended partnerships]

---

### WHY THIS IS HIGH PRIORITY

- [Reason 1]
- [Reason 2]
- [Reason 3]

---

**Full intelligence brief available:** [Link or ID reference]
**Questions:** Contact [Name]
```

---

### Template 4: Monthly Trend Analysis

```markdown
# MONTHLY MANDATE SEARCH TREND ANALYSIS
## [Month Year]

**Report Date:** [Date]
**Analysis Period:** [Start Date] - [End Date]

---

## EXECUTIVE SUMMARY

[High-level overview of the month - 1 paragraph]

**Key Findings:**
1. [Finding 1]
2. [Finding 2]
3. [Finding 3]

---

## MONTHLY STATISTICS

### Volume Metrics

| Metric | This Month | Last Month | Change | YTD |
|--------|------------|------------|--------|-----|
| Total Opportunities | [N] | [N] | [+/- N%] | [N] |
| Score 80+ | [N] | [N] | [+/- N%] | [N] |
| Score 70-79 | [N] | [N] | [+/- N%] | [N] |
| Score 50-69 | [N] | [N] | [+/- N%] | [N] |
| Total Funding Value | [$X] | [$X] | [+/- N%] | [$X] |
| Avg Funding Amount | [$X] | [$X] | [+/- N%] | [$X] |

### Geographic Distribution

| State | Opportunities | Total Funding | Avg Score | Top Sector |
|-------|---------------|---------------|-----------|------------|
| Delaware | [N] | [$X] | [XX] | [Sector] |
| Maryland | [N] | [$X] | [XX] | [Sector] |
| Pennsylvania | [N] | [$X] | [XX] | [Sector] |
| Virginia | [N] | [$X] | [XX] | [Sector] |
| DC | [N] | [$X] | [XX] | [Sector] |
| Federal | [N] | [$X] | [XX] | [Sector] |

### Routing Tag Distribution

| Tag | Count | Percentage | Avg Funding |
|-----|-------|------------|-------------|
| White Paper Ready | [N] | [X%] | [$X] |
| Proposal Ready | [N] | [X%] | [$X] |
| Nurture Needed | [N] | [X%] | [$X] |
| Monitor Only | [N] | [X%] | [$X] |

---

## TREND ANALYSIS

### 1. Funding Trends

**Total Funding Available:**
[Chart/description of funding trends over time]

**Key Observations:**
- [Observation 1]
- [Observation 2]

**Emerging Opportunities:**
- [Type of opportunity seeing increase]

**Declining Opportunities:**
- [Type of opportunity seeing decrease]

### 2. Geographic Trends

**Most Active State:** [State]
**Fastest Growing State:** [State]

**Analysis:**
[1-2 paragraphs on geographic patterns]

### 3. Industry Sector Trends

| Sector | Opportunities | % of Total | Trend |
|--------|---------------|------------|-------|
| Manufacturing | [N] | [X%] | [↑/↓/→] |
| Healthcare | [N] | [X%] | [↑/↓/→] |
| IT/Technology | [N] | [X%] | [↑/↓/→] |
| Construction | [N] | [X%] | [↑/↓/→] |
| Multiple/Other | [N] | [X%] | [↑/↓/→] |

**Analysis:**
[Paragraph on sector trends]

### 4. Target Population Trends

**Most Frequent Target Populations:**
1. [Population]: [N] opportunities
2. [Population]: [N] opportunities
3. [Population]: [N] opportunities

**Emerging Focus:**
[Description of new or growing focus areas]

---

## THEMATIC ANALYSIS

### Top Themes This Month

**1. [Theme 1 - e.g., "AI Workforce Displacement"]**

- Opportunities identified: [N]
- Total funding: [$X]
- States active: [List]

**Key Examples:**
- [Opportunity ID]: [Brief description]
- [Opportunity ID]: [Brief description]

**Strategic Implications:**
[Analysis of what this theme means for strategy]

**2. [Theme 2]**

[Repeat structure]

**3. [Theme 3]**

[Repeat structure]

---

## LEGISLATIVE & POLICY ACTIVITY

### State Legislative Highlights

**Delaware:**
[Summary of relevant activity or "No significant activity"]

**Maryland:**
[Summary]

**Pennsylvania:**
[Summary]

**Virginia:**
[Summary]

**DC:**
[Summary]

### Federal Policy Developments

[Summary of relevant federal policy/program developments]

---

## SOURCE PERFORMANCE ANALYSIS

### Most Productive Sources

| Source Type | Opportunities Found | Avg Score | Yield Rate |
|-------------|---------------------|-----------|------------|
| Grants.gov | [N] | [XX] | [X%] |
| State Legislation | [N] | [XX] | [X%] |
| Agency Announcements | [N] | [XX] | [X%] |
| Governor Press Releases | [N] | [XX] | [X%] |
| Workforce Boards | [N] | [XX] | [X%] |

### Quality Analysis

- **High-value sources (score 80+):** [List sources]
- **Underperforming sources:** [List sources]

**Recommendations:**
- [Recommendation for search strategy optimization]

---

## COMPETITIVE INTELLIGENCE

### Organizations Active in Target Opportunities

[If known from research/announcements]

**Frequently Appearing Organizations:**
1. [Organization name]
2. [Organization name]
3. [Organization name]

**Partnership Ecosystem Observations:**
[Analysis of partnership patterns seen in opportunities]

---

## PURSUIT STATUS UPDATE

### Opportunities Being Pursued

| ID | Title | Status | Next Milestone | Probability |
|----|-------|--------|----------------|-------------|
| [ID] | [Title] | [Status] | [Milestone] | [H/M/L] |

### Conversion Metrics

- Opportunities pursued: [N]
- Proposals submitted: [N]
- Awards received: [N]
- Win rate: [X%]

---

## FORECAST & PREDICTIONS

### Expected Upcoming Opportunities (Next 30-60 Days)

Based on legislative calendars, budget cycles, and agency announcements:

1. **[Predicted Opportunity]**
   - Expected source: [Source]
   - Estimated timing: [Timeframe]
   - Likely funding: [Amount range]
   - Confidence: [High/Medium/Low]

2. [Continue]

### Seasonal Patterns

[Analysis of cyclical patterns noticed - e.g., budget years, grant cycles]

---

## STRATEGIC RECOMMENDATIONS

### High-Priority Focus Areas

**For Next Month:**
1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]

### Partnership Development Priorities

[Recommendations for strategic partnership development]

### Geographic Focus Recommendations

[Recommendations for where to concentrate efforts]

### Capability Development Recommendations

[Recommendations for building capabilities to pursue certain opportunity types]

---

## SEARCH OPTIMIZATION

### Keywords to Add

- [New keyword 1]: [Rationale]
- [New keyword 2]: [Rationale]

### Keywords to Remove/Modify

- [Keyword]: [Reason]

### New Sources to Monitor

- [Source suggestion 1]
- [Source suggestion 2]

---

## APPENDIX

### All Opportunities by Score (80+)

| ID | Title | State | Score | Funding | Status |
|----|-------|-------|-------|---------|--------|
| [ID] | [Title] | [State] | [Score] | [Amount] | [Status] |

[List all score 80+ opportunities]

---

**Analysis Prepared By:** [Name]
**Next Monthly Report:** [Date]
**Feedback/Questions:** [Contact]
```

---

## API/Integration JSON Formats

### Bulk Export Format

```json
{
  "export_metadata": {
    "export_date": "YYYY-MM-DD",
    "export_type": "bulk_opportunities",
    "time_period": {
      "start_date": "YYYY-MM-DD",
      "end_date": "YYYY-MM-DD"
    },
    "filters_applied": {
      "min_score": 50,
      "states": ["MD", "VA", "PA", "DE", "DC"],
      "routing_tags": ["white-paper-ready", "proposal-ready"]
    },
    "total_records": 25
  },
  "opportunities": [
    {
      // Full opportunity object 1
    },
    {
      // Full opportunity object 2
    }
    // ... more opportunities
  ]
}
```

### Search Results Format

```json
{
  "search_metadata": {
    "query": "AI workforce Maryland",
    "search_date": "YYYY-MM-DD",
    "results_count": 5,
    "search_filters": {
      "states": ["MD"],
      "keywords": ["AI", "workforce"]
    }
  },
  "results": [
    {
      // Simplified opportunity object
      "opportunity_id": "MD-WF-2025-001",
      "title": "Title",
      "score": 100,
      "routing_tag": "white-paper-ready",
      "funding_amount": "$2.5M",
      "deadline_date": "2025-10-01",
      "summary": "Short summary",
      "url": "URL"
    }
  ]
}
```

---

**Version:** 1.0
**Last Updated:** 2025-10-25
