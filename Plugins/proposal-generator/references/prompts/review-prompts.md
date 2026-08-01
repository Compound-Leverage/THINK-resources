# Review Prompts Reference

## Overview

These prompts guide Phase 6 (QA) - validating the proposal before delivery.

---

## Requirements Coverage Check

### Purpose
Ensure every client requirement is addressed in the proposal.

### Process

1. **Extract requirements list** from discovery/assessment
2. **Scan proposal** for each requirement
3. **Verify traceability** - requirement linked to section

### Check Table

| Req ID | Requirement | Addressed? | Section | Coverage |
|--------|-------------|------------|---------|----------|
| R1 | [Description] | Y/N | [Section #] | [Full/Partial/Missing] |
| R2 | [Description] | Y/N | [Section #] | [Full/Partial/Missing] |

### Output
```json
{
  "check": "requirements_coverage",
  "status": "[PASS | WARNING | FAIL]",
  "total_requirements": X,
  "requirements_addressed": X,
  "requirements_missing": [],
  "traceability": [
    {"requirement": "", "section": "", "coverage": ""}
  ]
}
```

### Pass Criteria
- PASS: 100% of requirements addressed
- WARNING: 90-99% addressed (minor gaps)
- FAIL: <90% addressed

---

## Consistency Check

### Purpose
Ensure numbers, dates, and facts are consistent throughout.

### Check Areas

**1. Investment Figures**
- Scan all mentions of pricing
- Compare values across sections
- Flag any discrepancies

**2. Timeline**
- Check all date/duration mentions
- Verify phases add up correctly
- Confirm milestones consistent

**3. Team/Resources**
- Verify team members consistent
- Check hours/allocation numbers
- Confirm roles match org chart

**4. ROI Numbers**
- Check baseline figures consistent
- Verify savings calculations
- Confirm break-even aligns

### Check Table

| Item | Location 1 | Location 2 | Match? |
|------|------------|------------|--------|
| Total Investment | Exec Summary: $X | Pricing Section: $Y | Y/N |
| Timeline | Exec Summary: X weeks | Work Plan: Y weeks | Y/N |
| Break-even | Pricing: Month X | ROI: Month Y | Y/N |

### Output
```json
{
  "check": "consistency",
  "status": "[PASS | WARNING | FAIL]",
  "items_checked": X,
  "discrepancies_found": [
    {
      "item": "",
      "location_1": {"section": "", "value": ""},
      "location_2": {"section": "", "value": ""},
      "resolution": ""
    }
  ]
}
```

### Pass Criteria
- PASS: Zero discrepancies
- WARNING: Minor discrepancies (rounding, etc.)
- FAIL: Any material discrepancy

---

## Compliance Check

### Purpose
Ensure proposal meets all compliance requirements.

### Check Areas

**1. Brand Guidelines**
- Voice and tone appropriate
- Terminology consistent
- Formatting follows standards

**2. Legal Requirements**
- Required disclaimers present
- Terms appropriate for deal type
- No sensitive information exposed

**3. Deal-Type Specific**

For GOVERNMENT deals:
- [ ] Section 6.4 (Data Security & Compliance) present
- [ ] Required compliance frameworks addressed
- [ ] Certifications appendix complete
- [ ] Section numbering matches RFP

For COMMERCIAL deals:
- [ ] Professional tone maintained
- [ ] ROI clearly presented
- [ ] Terms appropriate for commercial

For PARTNERSHIP deals:
- [ ] Mutual benefit evident
- [ ] Shared governance clear
- [ ] Risk sharing appropriate

### Output
```json
{
  "check": "compliance",
  "status": "[PASS | WARNING | FAIL]",
  "brand_compliance": "[PASS | FAIL]",
  "legal_compliance": "[PASS | FAIL]",
  "deal_type_compliance": "[PASS | FAIL]",
  "issues": [
    {"area": "", "issue": "", "severity": "", "fix": ""}
  ]
}
```

### Pass Criteria
- PASS: All compliance areas met
- WARNING: Minor non-critical issues
- FAIL: Missing required sections or material issues

---

## Quality Check

### Purpose
Ensure proposal meets quality standards.

### Check Areas

**1. Win Themes**
- Are themes present in Executive Summary?
- Are themes threaded throughout sections?
- Is positioning consistent?

**2. Methodology Application**
- Is methodology correctly referenced (if applicable)?
- Are framework phases logical?
- Is methodology jargon-free?

**3. Writing Quality**
- Short sentences (15 words avg)?
- "You" language predominant?
- Client benefit leads each section?
- No vague claims (all quantified)?

**4. Completeness**
- All sections from outline present?
- No empty placeholders?
- Page count within target?
- All appendices complete?

### Scoring

| Quality Area | Score | Notes |
|--------------|-------|-------|
| Win Themes | [1-10] | [Notes] |
| Methodology | [1-10] | [Notes] |
| Writing | [1-10] | [Notes] |
| Completeness | [1-10] | [Notes] |
| **Overall** | **[X/10]** | |

### Output
```json
{
  "check": "quality",
  "status": "[PASS | WARNING | FAIL]",
  "scores": {
    "win_themes": X,
    "methodology": X,
    "writing": X,
    "completeness": X,
    "overall": X
  },
  "improvements_suggested": []
}
```

### Pass Criteria
- PASS: Overall score 8+
- WARNING: Overall score 6-7
- FAIL: Overall score <6

---

## Tone Check

### Purpose
Ensure tone matches deal type expectations.

### Tone Standards by Deal Type

| Deal Type | Expected Tone | Red Flags |
|-----------|---------------|-----------|
| GOVERNMENT | Formal, compliance-focused | Casual language, missing sections |
| COMMERCIAL | Professional, outcome-focused | Too formal, jargon-heavy |
| PARTNERSHIP | Collaborative, mutual benefit | One-sided language |
| SIMPLE/SOW | Concise, direct | Overblown language |

### Check Process
1. Sample 3-5 paragraphs from different sections
2. Evaluate against tone standards
3. Flag inconsistencies

### Output
```json
{
  "check": "tone",
  "status": "[PASS | WARNING | FAIL]",
  "deal_type": "",
  "expected_tone": "",
  "tone_consistent": true,
  "issues": []
}
```

---

## Final QA Report Template

```
QA REPORT

Proposal: [Name]
Date: [Date]
Reviewer: [System/Human]

OVERALL STATUS: [PASS | WARNING | FAIL]

CHECK RESULTS:
┌─────────────────────┬─────────┬─────────────────────────┐
│ Check               │ Status  │ Notes                   │
├─────────────────────┼─────────┼─────────────────────────┤
│ Requirements        │ [Status]│ [X/X addressed]         │
│ Consistency         │ [Status]│ [X discrepancies]       │
│ Compliance          │ [Status]│ [Notes]                 │
│ Quality             │ [Status]│ [Score X/10]            │
│ Tone                │ [Status]│ [Notes]                 │
└─────────────────────┴─────────┴─────────────────────────┘

CRITICAL ISSUES (Must Fix):
• [Issue 1] - [Fix required]

WARNINGS (Should Fix):
• [Issue 1] - [Recommendation]

RECOMMENDATIONS:
• [Recommendation 1]

READY FOR DELIVERY: [YES | NO - fix issues first]
```

---

## QA Decision Logic

```
IF all checks PASS:
  → Ready for delivery
  → Generate final document

IF any check has WARNING:
  → Present to human for decision
  → Human can override or request fix
  → Document justification if override

IF any check has FAIL:
  → NOT ready for delivery
  → List specific failures
  → Route back to appropriate phase:
    - Requirements fail → Back to Strategy/Draft
    - Consistency fail → Back to Draft
    - Compliance fail → Back to Draft
    - Quality fail → Back to Draft
    - Tone fail → Back to Draft
```

---

*End of Review Prompts Reference*
