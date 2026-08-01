# Discovery Prompts Reference

## Overview

These prompts guide research during Phase 2 (Research). Run them in parallel for comprehensive discovery.

---

## Client Research Prompt

### Context
You are researching a prospective client to inform a proposal. Gather factual, verifiable information.

### Input Required
- Company Name: [NAME]
- Industry: [INDUSTRY]
- Website: [URL]
- LinkedIn: [URL if available]

### Research Tasks

**Company Overview**
1. What does this company do? (core business, products/services)
2. How long have they been in business?
3. What is their approximate size? (employees, revenue if public)
4. Where are they headquartered? Other locations?

**Recent News & Events**
1. Any recent press releases or announcements?
2. Leadership changes in past 12 months?
3. Mergers, acquisitions, or major partnerships?
4. Any public challenges or controversies?

**Business Context**
1. Who are their primary customers?
2. Who are their main competitors?
3. What market position do they hold? (leader, challenger, niche)
4. Any visible growth or contraction signals?

**Technology Signals**
1. What technologies do they mention on their site?
2. Any job postings that reveal tech stack or initiatives?
3. Any public case studies or tech partnerships?

### Output Format
```json
{
  "company_overview": {
    "description": "",
    "founded": "",
    "size": "",
    "locations": []
  },
  "recent_developments": [],
  "business_context": {
    "customers": "",
    "competitors": [],
    "market_position": ""
  },
  "technology_signals": [],
  "key_findings": [],
  "proposal_implications": []
}
```

---

## Industry Analysis Prompt

### Context
You are analyzing the industry context for a prospective client to identify trends, benchmarks, and positioning opportunities.

### Input Required
- Industry: [INDUSTRY]
- Sub-sector: [SUB-SECTOR]
- Client Type: [TYPE]

### Research Tasks

**Industry Trends**
1. What are the top 3-5 trends affecting this industry?
2. What technology shifts are happening? (AI adoption, automation, etc.)
3. What operational challenges are common?
4. What's driving growth or contraction?

**Benchmarks & Standards**
1. What are typical operational metrics? (time-to-X, cost per X, etc.)
2. What efficiency benchmarks exist?
3. What does "good" look like in this industry?
4. What are common KPIs tracked?

**Competitive Landscape**
1. Who are the major players?
2. What differentiates leaders from laggards?
3. What solutions are commonly adopted?
4. What vendors/partners are prevalent?

**Regulatory Environment**
1. What regulations affect this industry?
2. Any upcoming compliance deadlines?
3. What frameworks are commonly required?
4. What are the consequences of non-compliance?

### Output Format
```json
{
  "industry_trends": [
    {"trend": "", "relevance_to_client": "", "our_positioning": ""}
  ],
  "benchmarks": {
    "operational_metrics": [],
    "efficiency_standards": [],
    "common_kpis": []
  },
  "competitive_landscape": {
    "major_players": [],
    "differentiation_factors": [],
    "common_solutions": []
  },
  "regulatory_environment": {
    "key_regulations": [],
    "compliance_frameworks": [],
    "upcoming_deadlines": []
  },
  "proposal_implications": []
}
```

---

## Stakeholder Intelligence Prompt

### Context
You are researching key stakeholders to understand decision-making dynamics and relationship opportunities.

### Input Required
- Company: [NAME]
- Known Stakeholders: [LIST]
- Deal Type: [TYPE]
- Estimated Value: [AMOUNT]

### Research Tasks

**Decision-Making Structure**
1. Who are the likely decision-makers for this type of purchase?
2. What is the typical approval chain?
3. Who controls budget?
4. Who are technical vs. business evaluators?

**Key Individuals**
For each known stakeholder:
1. What is their background? (LinkedIn, bio)
2. What is their tenure at the company?
3. What are their likely priorities?
4. What communication style do they prefer?
5. Any public content they've created?

**Organizational Dynamics**
1. What is the company culture? (formal, agile, hierarchical, flat)
2. How do they typically buy? (RFP, negotiated, procurement)
3. What is their risk tolerance?
4. What past purchases/projects are visible?

**Relationship Mapping**
1. Do we have any existing connections?
2. Are there mutual contacts?
3. What partners do they work with that we know?

### Output Format
```json
{
  "decision_structure": {
    "decision_makers": [],
    "approval_chain": "",
    "budget_holder": "",
    "evaluator_types": []
  },
  "key_individuals": [
    {
      "name": "",
      "title": "",
      "role_in_decision": "",
      "priorities": [],
      "communication_style": ""
    }
  ],
  "organizational_dynamics": {
    "culture": "",
    "buying_process": "",
    "risk_tolerance": ""
  },
  "relationship_opportunities": [],
  "engagement_strategy": []
}
```

---

## Compliance & Regulatory Prompt

### Context
You are researching compliance requirements for a client engagement.

### Input Required
- Industry: [INDUSTRY]
- Client Type: [TYPE]
- Deal Type: [TYPE]
- Known Requirements: [LIST]

### Research Tasks

**Applicable Frameworks**
1. What compliance frameworks apply?
   - Federal: NIST 800-53, FedRAMP, FISMA, CMMC
   - Industry: HIPAA, PCI-DSS, SOX, GDPR
   - Sector-specific: EEOC, OFCCP, FAR/DFARS
2. What certification levels are required?
3. What audit requirements exist?

**Data & Privacy**
1. What data classification applies? (CUI, PII, PHI, etc.)
2. What data handling requirements exist?
3. What privacy regulations apply?

**Security Requirements**
1. What security controls are required?
2. What access control requirements exist?
3. What logging/audit trail requirements exist?

**Risk Factors**
1. What are the consequences of non-compliance?
2. What are common compliance gaps?
3. What recent enforcement actions are relevant?

### Output Format
```json
{
  "applicable_frameworks": [
    {
      "framework": "",
      "applicability": "required | recommended | optional",
      "certification_level": ""
    }
  ],
  "data_requirements": {
    "classification": "",
    "handling_requirements": [],
    "privacy_regulations": []
  },
  "security_requirements": {
    "controls_required": [],
    "audit_trail": ""
  },
  "proposal_sections_affected": [],
  "recommendations": []
}
```

---

## Technology Landscape Prompt

### Context
You are researching the technology landscape to understand integration points and technical constraints.

### Input Required
- Company: [NAME]
- Industry: [INDUSTRY]
- Known Systems: [LIST]
- Technical Requirements: [LIST]

### Research Tasks

**Current Technology Stack**
1. What core systems does the client use? (ATS, CRM, ERP, etc.)
2. What cloud platforms are they on?
3. What integration technologies are common?
4. What data platforms are in use?

**Vendor Ecosystem**
1. Who are the major vendors in this space?
2. What are typical vendor combinations?
3. What integration patterns are common?

**Integration Considerations**
1. What APIs are available for known systems?
2. What data formats are standard?
3. What authentication methods are required?
4. What are common integration challenges?

**Technology Trends**
1. What technologies are being adopted in this sector?
2. What AI/automation adoption is happening?
3. What skills are in demand?

### Output Format
```json
{
  "current_stack_assessment": {
    "core_systems": [],
    "cloud_platforms": [],
    "integration_technologies": []
  },
  "vendor_ecosystem": {
    "major_vendors": [],
    "common_combinations": [],
    "integration_patterns": []
  },
  "integration_considerations": {
    "available_apis": [],
    "common_challenges": []
  },
  "proposal_implications": [],
  "technical_risks": []
}
```

---

## Discovery Brief Template

After running all discovery prompts, synthesize into this format:

```
DISCOVERY BRIEF

Client: [Name]
Date: [Date]
Fit Score: [X/10]

KEY FINDINGS
• [Finding 1 - quantified]
• [Finding 2 - quantified]
• [Finding 3 - quantified]

PAIN POINTS IDENTIFIED
• [Pain 1 - specific, quantified if possible]
• [Pain 2 - specific, quantified if possible]

RED FLAGS
• [Concern 1]
• [Concern 2]

INFORMATION GAPS
• [What couldn't be found]

QUESTIONS FOR HUMAN
1. [Question needing input]
2. [Strategic question]

RECOMMENDATION: [GO / CONDITIONAL GO / NO-GO]
RATIONALE: [Why]
```

---

*End of Discovery Prompts Reference*
