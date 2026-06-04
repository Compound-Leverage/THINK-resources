# Assessment Prompts Reference

## Overview

These prompts guide Phase 3 (Assessment) - classifying the opportunity, mapping capabilities, and configuring pricing.

---

## Opportunity Classification Prompt

### Context
Classify this opportunity to determine the appropriate template, tone, and structure.

### Input Required
- Discovery Brief
- Client type
- Procurement process
- Requirements list

### Classification Tasks

**Deal Type Classification**
Evaluate against each type:

| Deal Type | Key Indicators | Match? |
|-----------|----------------|--------|
| GOVERNMENT | Public sector, formal RFP, compliance requirements | Y/N |
| COMMERCIAL | Private sector, ROI-focused, flexible process | Y/N |
| PARTNERSHIP | Joint venture, shared risk/reward, collaboration | Y/N |
| SIMPLE/SOW | Straightforward scope, quick turnaround | Y/N |

**Offering Type Classification**
Evaluate what's being proposed:

| Offering | Key Indicators | Match? |
|----------|----------------|--------|
| CONSULTING | Strategic guidance, no implementation | Y/N |
| IMPLEMENTATION | Build and deploy, measurable outcomes | Y/N |
| TRAINING | Skills transfer, team enablement | Y/N |
| FULL ENGAGEMENT | End-to-end, strategy through outcomes | Y/N |

**Complexity Assessment**

| Factor | Low | Medium | High |
|--------|-----|--------|------|
| Requirements count | <5 | 5-10 | >10 |
| Stakeholders | 1-2 | 3-5 | >5 |
| Integration points | 0-1 | 2-3 | >3 |
| Timeline pressure | Flexible | Normal | Tight |
| Compliance burden | None | Standard | Heavy |

### Output Format
```json
{
  "classification": {
    "deal_type": "[GOVERNMENT | COMMERCIAL | PARTNERSHIP | SIMPLE]",
    "deal_type_confidence": 0.X,
    "offering_type": "[CONSULTING | IMPLEMENTATION | TRAINING | FULL]",
    "offering_components": [],
    "complexity": "[LOW | MEDIUM | HIGH]"
  },
  "template_selected": "[template name]",
  "page_target": {"min": X, "max": X},
  "tone": "[FORMAL | PROFESSIONAL | COLLABORATIVE | CONCISE]",
  "sections_required": []
}
```

---

## Capability Mapping Prompt

### Context
Map client requirements to your capabilities to assess fit and identify gaps.

### Input Required
- Requirements list (from discovery)
- Your company profile (capabilities)
- Your service offerings

### Mapping Tasks

**For each requirement:**

1. **Identify the requirement**
   - ID: [Unique identifier]
   - Description: [What they need]
   - Priority: [CRITICAL | HIGH | MEDIUM | LOW]
   - Source: [Where this came from]

2. **Map to capability**
   - Matching capability: [Your capability that addresses this]
   - Fit level: [STRONG | MODERATE | WEAK | GAP]
   - Evidence: [How you've done this before]

3. **Identify proposal section**
   - Section: [Which proposal section will address this]
   - Approach: [How you'll present the solution]

### Fit Scoring

| Fit Level | Criteria | Score |
|-----------|----------|-------|
| STRONG | Direct experience, proven capability | 9-10 |
| MODERATE | Related experience, capable with effort | 7-8 |
| WEAK | Limited experience, stretch | 5-6 |
| GAP | No capability, need partner/mitigation | 1-4 |

### Output Format
```json
{
  "requirements_mapped": [
    {
      "requirement_id": "",
      "description": "",
      "priority": "",
      "maps_to_capability": "",
      "maps_to_section": "",
      "fit": "",
      "evidence": "",
      "mitigation": ""
    }
  ],
  "overall_fit": {
    "score": X,
    "level": "[STRONG | MODERATE | WEAK]",
    "strengths": [],
    "gaps": [],
    "mitigations": []
  }
}
```

---

## ROI Modeling Prompt

### Context
Calculate ROI to build the business case for the investment.

### Input Required
- Client pain points (quantified)
- Current state costs
- Proposed solution
- Your pricing model

### ROI Calculation Tasks

**1. Establish Baseline (Current State)**

| Cost Category | Calculation | Amount |
|---------------|-------------|--------|
| Labor hours/week | [Hours] × [$/hr] × 52 | $[Annual] |
| Error/rework costs | [Frequency] × [Cost each] | $[Annual] |
| Opportunity costs | [What's not happening] | $[Annual] |
| Compliance risk | [Probability] × [Impact] | $[Exposure] |
| **Total Current Cost** | | **$[Annual]** |

**2. Project Future State**

| Improvement Area | Current | Projected | Savings |
|------------------|---------|-----------|---------|
| Hours reduction | [X] hrs/week | [Y] hrs/week | [X-Y] hrs × $rate |
| Error reduction | [X]% error rate | [Y]% error rate | $[savings] |
| Speed improvement | [X] days/cycle | [Y] days/cycle | $[value] |
| **Total Annual Savings** | | | **$[Amount]** |

**3. Calculate ROI**

```
Investment Required: $[Amount]
Annual Savings: $[Amount]
Break-even Month: Investment ÷ (Monthly Savings) = Month [X]
Year 1 ROI: (Savings - Investment) ÷ Investment × 100 = [X]%
3-Year Value: (Savings × 3) - Investment = $[Amount]
```

### Output Format
```json
{
  "baseline": {
    "labor_cost_annual": X,
    "error_cost_annual": X,
    "opportunity_cost_annual": X,
    "total_annual_cost": X
  },
  "projected": {
    "labor_savings": X,
    "error_savings": X,
    "speed_value": X,
    "total_annual_savings": X
  },
  "roi": {
    "investment_required": X,
    "break_even_month": X,
    "year_1_roi_percent": X,
    "year_1_net_value": X,
    "three_year_value": X
  }
}
```

---

## Pricing Configuration Prompt

### Context
Configure pricing based on opportunity classification and scope.

### Input Required
- Deal type
- Offering type
- Complexity
- Your pricing model
- ROI calculations

### Pricing Tasks

**1. Select Components**

Based on offering type, select which components apply:

| Component | Include? | Base Price | Adjusted Price |
|-----------|----------|------------|----------------|
| [Component 1] | Y/N | $[Base] | $[Adjusted] |
| [Component 2] | Y/N | $[Base] | $[Adjusted] |
| [Component 3] | Y/N | $[Base] | $[Adjusted] |

**2. Apply Adjustments**

| Adjustment Factor | Reason | Amount |
|-------------------|--------|--------|
| Complexity | [LOW/MED/HIGH] | +/- [%] |
| Timeline | [Normal/Accelerated] | +/- [%] |
| Volume/Scale | [Small/Med/Large] | +/- [%] |
| Strategic | [Reason if applicable] | +/- $[Amount] |

**3. Configure Success Fee (if applicable)**

| Parameter | Value |
|-----------|-------|
| Basis | [What triggers success fee] |
| Percentage | [X]% |
| Cap | $[Amount] |
| Minimum | $[Amount] |

**4. Set Payment Terms**

| Milestone | Percentage | Amount | Timing |
|-----------|------------|--------|--------|
| [Milestone 1] | [X]% | $[Amount] | [When] |
| [Milestone 2] | [X]% | $[Amount] | [When] |
| [Milestone 3] | [X]% | $[Amount] | [When] |

### Output Format
```json
{
  "pricing": {
    "components": [
      {"name": "", "base_price": X, "adjusted_price": X, "included": true}
    ],
    "adjustments": [
      {"factor": "", "amount": X, "reason": ""}
    ],
    "base_total": X,
    "success_fee": {
      "enabled": true,
      "percentage": X,
      "cap": X,
      "basis": ""
    },
    "total_range": {"min": X, "max": X},
    "payment_terms": [
      {"milestone": "", "percentage": X, "amount": X, "timing": ""}
    ]
  }
}
```

---

## Assessment Package Template

Synthesize all assessment outputs into this format:

```
ASSESSMENT PACKAGE

Opportunity: [Name]
Date: [Date]

CLASSIFICATION
• Deal Type: [Type]
• Offering Type: [Type]
• Complexity: [Level]
• Template: [Selected template]

CAPABILITY FIT
• Overall Score: [X/10]
• Strengths: [What we nail]
• Gaps: [What needs mitigation]

ROI MODEL
• Current Annual Cost: $[Amount]
• Projected Annual Savings: $[Amount]
• Break-even: Month [X]
• Year 1 ROI: [X]%

PRICING RECOMMENDATION
• Base Investment: $[Amount]
• Success Fee Potential: $[Amount]
• Total Range: $[Min] - $[Max]

RISK ASSESSMENT
• Overall Risk: [LOW | MEDIUM | HIGH]
• Key Risks: [List]
• Mitigations: [List]

QUESTIONS FOR HUMAN
1. [ROI assumption to validate]
2. [Pricing question]
3. [Scope clarification]

READY FOR STRATEGY PHASE: [YES | NEED ANSWERS]
```

---

*End of Assessment Prompts Reference*
