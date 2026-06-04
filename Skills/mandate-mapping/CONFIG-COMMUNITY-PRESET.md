# Mandate Search Agent - Community Preset Configuration

**Purpose:** Ready-to-use configuration with GENERIC placeholders you can easily customize
**Setup Time:** 10-15 minutes to fill in YOUR specifics

---

## ✏️ How to Use This File

This file is **pre-filled with placeholders** - just replace the bracketed items with YOUR information:

1. Find all `[PLACEHOLDER]` items
2. Replace with YOUR actual information
3. Save as `CONFIG.md`
4. Upload to Claude

**Example:**
- Replace `[YOUR_STATE]` with `California` or `Texas` or your state
- Replace `[YOUR_INDUSTRY]` with `Manufacturing` or `Healthcare` or your industry
- Replace `[YOUR_MIN_FUNDING]` with `$25,000` or your threshold

---

## Your Business Profile

### Organization Information
```yaml
organization_name: [YOUR_ORGANIZATION_NAME]
business_type: [Consulting / Training Provider / Nonprofit / Association / Economic Development / Other]
primary_services:
  - [Service 1]
  - [Service 2]
  - [Service 3]
```

**Examples:**
- `organization_name: Pacific Skills Training`
- `business_type: Workforce Training Provider`
- `primary_services: [Technical training, Career coaching, Job placement]`

---

## Focus Areas

### Industries/Sectors You Serve
**Check all that apply to YOU:**
```yaml
industries:
  - [ ] Workforce Development
  - [ ] Economic Development
  - [ ] Manufacturing
  - [ ] Healthcare
  - [ ] Information Technology
  - [ ] Construction
  - [ ] Hospitality/Tourism
  - [ ] Energy/Utilities
  - [ ] Agriculture
  - [ ] Other: [YOUR_INDUSTRY]
```

### Target Populations
**Check all populations YOU serve:**
```yaml
populations:
  - [ ] Dislocated/Displaced Workers
  - [ ] Youth (16-24)
  - [ ] Veterans
  - [ ] Justice-Involved Individuals
  - [ ] Low-Income Workers
  - [ ] Rural Communities
  - [ ] Urban Communities
  - [ ] Older Workers (55+)
  - [ ] Immigrants/Refugees
  - [ ] Individuals with Disabilities
  - [ ] Other: [YOUR_POPULATION]
```

### Special Focus Areas
**Check YOUR areas of expertise:**
```yaml
focus_areas:
  - [ ] AI/Automation Impact
  - [ ] Digital Transformation
  - [ ] Apprenticeships
  - [ ] Skills Training
  - [ ] Career Pathways
  - [ ] Entrepreneurship
  - [ ] Small Business Support
  - [ ] Other: [YOUR_FOCUS]
```

---

## Geographic Configuration

### Primary Target States/Regions

**Replace with YOUR states/regions:**

```yaml
primary_states:
  - [YOUR_STATE_1]
  - [YOUR_STATE_2]
  - [YOUR_STATE_3]

adjacent_states:  # Optional
  - [ADJACENT_STATE_1]
  - [ADJACENT_STATE_2]

regions:  # Optional: specific metro areas or regions
  - [YOUR_REGION_1]
  - [YOUR_REGION_2]
```

**Examples:**
```yaml
# Single State Example
primary_states:
  - California

# Multi-State Example
primary_states:
  - North Carolina
  - South Carolina
  - Georgia
  - Virginia

# Regional Example
regions:
  - San Francisco Bay Area
  - Southern California
```

### Federal Programs
```yaml
include_federal_programs: [Yes/No]
federal_focus: [Programs available in your states / National programs / Both]
```

---

## Keywords & Search Terms

### Primary Keywords (Your Industry/Focus)

**Replace with keywords for YOUR industry:**
```yaml
primary_keywords:
  - [KEYWORD_1]
  - [KEYWORD_2]
  - [KEYWORD_3]
  - [KEYWORD_4]
  - [KEYWORD_5]
  - [KEYWORD_6]
```

**Examples by Industry:**

**Manufacturing:**
```yaml
primary_keywords:
  - advanced manufacturing
  - Industry 4.0
  - supply chain
  - automation
  - robotics training
  - lean manufacturing
```

**Healthcare:**
```yaml
primary_keywords:
  - healthcare workforce
  - nursing shortage
  - allied health
  - medical training
  - behavioral health
  - patient care training
```

**Technology:**
```yaml
primary_keywords:
  - IT workforce
  - cybersecurity training
  - software development
  - data analytics
  - cloud computing
  - tech skills
```

**Economic Development:**
```yaml
primary_keywords:
  - economic development
  - business development
  - entrepreneurship
  - startup support
  - small business
  - regional planning
```

### Exclusion Keywords

**Add terms that indicate opportunities NOT relevant to you:**
```yaml
exclude_keywords:
  - [EXCLUSION_1]
  - [EXCLUSION_2]
  - [EXCLUSION_3]
```

**Common exclusions:**
```yaml
exclude_keywords:
  - K-12 only
  - pure research
  - international development
  - [YOUR_EXCLUSION]
```

---

## Funding Preferences

### Minimum Funding Threshold
```yaml
minimum_funding: $[YOUR_MINIMUM]
```

**Guidance:**
- Small organization: `$10,000` - `$25,000`
- Medium organization: `$50,000` - `$100,000`
- Large organization: `$100,000+`

**Your choice:** `minimum_funding: $[YOUR_MIN_FUNDING]`

### Funding Size Preferences

```yaml
sweet_spot_range: $[YOUR_MIN] - $[YOUR_MAX]
```

**Examples:**
- Small org: `$50,000 - $250,000`
- Medium org: `$100,000 - $750,000`
- Large org: `$500,000 - $5,000,000`

**Your choice:** `sweet_spot_range: $[YOUR_SWEET_SPOT]`

---

## Scoring Customization

### Scoring Weight Preferences

**Replace with YOUR priorities (must total 100):**

```yaml
scoring_weights:
  funding_size: [YOUR_WEIGHT_0-50]          # Default: 40
  timeline: [YOUR_WEIGHT_0-30]              # Default: 20
  competition_level: [YOUR_WEIGHT_0-30]     # Default: 20
  geography_match: [YOUR_WEIGHT_0-30]       # Default: 20
```

**Default (balanced):**
```yaml
scoring_weights:
  funding_size: 40
  timeline: 20
  competition_level: 20
  geography_match: 20
```

**Prioritize easy wins:**
```yaml
scoring_weights:
  funding_size: 30
  timeline: 25          # More time to prepare
  competition_level: 30 # Favor less competition
  geography_match: 15
```

**Prioritize large opportunities:**
```yaml
scoring_weights:
  funding_size: 50      # Size most important
  timeline: 15
  competition_level: 15
  geography_match: 20
```

**Your choice:** (must total 100)

### Routing Tag Thresholds

**Standard thresholds (adjust if needed):**
```yaml
routing_thresholds:
  white_paper_ready: [75-90]   # Default: 80
  proposal_ready: [65-79]      # Default: 70
  nurture_needed: [45-64]      # Default: 50
```

---

## Capacity & Constraints

### Organizational Capacity

**Replace with YOUR actual capacity:**

```yaml
capacity:
  can_lead_projects: [Yes/No]
  can_be_subcontractor: [Yes/No]
  max_concurrent_projects: [NUMBER]
  geographic_presence: [Local / Statewide / Regional / National]
```

**Example:**
```yaml
capacity:
  can_lead_projects: Yes
  can_be_subcontractor: Yes
  max_concurrent_projects: 3
  geographic_presence: Statewide
```

### Partnership Preferences

**List YOUR existing or desired partners:**
```yaml
partnerships:
  community_colleges: [Yes/No]
    partners: [PARTNER_1, PARTNER_2]

  workforce_boards: [Yes/No]
    partners: [PARTNER_1, PARTNER_2]

  industry_associations: [Yes/No]
    partners: [PARTNER_1, PARTNER_2]

  employers: [Yes/No]
    partners: [PARTNER_1, PARTNER_2]

  other_training_providers: [Yes/No]
    partners: [PARTNER_1, PARTNER_2]
```

**Example:**
```yaml
partnerships:
  community_colleges: Yes
    partners: [Lone Star College, Houston Community College]

  employers: Yes
    partners: [Local manufacturing companies]
```

### Match/Cost-Share Capability

```yaml
cost_share:
  can_provide_cash_match: [Yes/No]
  max_match_percentage: [0-100%]
  can_provide_in_kind_match: [Yes/No]
```

**Example:**
```yaml
cost_share:
  can_provide_cash_match: Yes
  max_match_percentage: 25%
  can_provide_in_kind_match: Yes
```

---

## Intelligence Sources

### Which sources should the skill monitor for you?

**Check sources relevant to YOUR work:**

```yaml
federal_sources:
  - [ ] Grants.gov
  - [ ] Federal agency announcements (DOL, EDA, SBA, etc.)
  - [ ] Federal Register

state_sources:
  - [ ] State legislature bill trackers
  - [ ] Governor/executive office press releases
  - [ ] State workforce development boards
  - [ ] State economic development agencies
  - [ ] State budget documents

regional_local_sources:
  - [ ] Regional planning councils
  - [ ] Local workforce areas
  - [ ] Economic development organizations
  - [ ] Chamber of commerce announcements

foundation_sources:
  - [ ] Private foundation programs
  - [ ] Corporate foundation programs
  - [ ] Community foundation programs

industry_sources:
  - [ ] Industry association announcements
  - [ ] Trade publication RFPs
  - [ ] Sector partnership initiatives
```

### Custom Sources

**Add specific sources unique to YOUR network:**
```yaml
custom_sources:
  - name: [YOUR_SOURCE_NAME]
    url: [URL]
    check_frequency: [Daily/Weekly/Monthly]

  - name: [YOUR_SOURCE_NAME_2]
    url: [URL]
    check_frequency: [Daily/Weekly/Monthly]
```

---

## Reporting Preferences

### Alert Preferences

**Set YOUR alert thresholds:**
```yaml
alert_triggers:
  minimum_score: [75-95]              # Alert for scores above this
  minimum_funding: $[YOUR_AMOUNT]     # Alert for funding above this
  unsolicited_opportunities: [Yes/No] # Alert for pre-RFP signals
  urgent_deadlines: [NUMBER] days     # Alert if deadline within X days
```

**Example:**
```yaml
alert_triggers:
  minimum_score: 85
  minimum_funding: $500,000
  unsolicited_opportunities: Yes
  urgent_deadlines: 30 days
```

### Report Frequency

```yaml
reports:
  daily_alerts: [Yes/No]
  weekly_digest: [Yes/No] - [Day of week]
  monthly_analysis: [Yes/No]
```

**Example:**
```yaml
reports:
  daily_alerts: No
  weekly_digest: Yes - Monday
  monthly_analysis: Yes
```

---

## Strategic Priorities

### White Paper Topics

**List YOUR thought leadership topics:**
```yaml
white_paper_expertise:
  - [YOUR_TOPIC_1]
  - [YOUR_TOPIC_2]
  - [YOUR_TOPIC_3]
```

**Examples:**
```yaml
white_paper_expertise:
  - AI workforce displacement in manufacturing
  - Regional skills gap solutions
  - Innovative apprenticeship models
```

### Past Performance

**Add YOUR credentials:**
```yaml
past_performance:
  - program: [PROGRAM_NAME]
    funder: [AGENCY]
    amount: $[AMOUNT]
    year: [YEAR]
    outcomes: [BRIEF_DESCRIPTION]

  - program: [PROGRAM_NAME_2]
    funder: [AGENCY_2]
    amount: $[AMOUNT]
    year: [YEAR]
    outcomes: [BRIEF_DESCRIPTION]
```

---

## Success Criteria

### What defines a "good opportunity" for YOUR organization?

**Replace with YOUR ideal opportunity profile:**

```yaml
ideal_opportunity:
  funding_range: $[YOUR_MIN] - $[YOUR_MAX]
  project_duration: [NUMBER] months
  competition_level: [Unsolicited / Limited / Set-aside / Open]
  timeline_to_deadline: [NUMBER] months
  match_requirement: [None / Up to X% / Flexible]
  participant_numbers: [NUMBER] participants
```

**Example:**
```yaml
ideal_opportunity:
  funding_range: $100,000 - $500,000
  project_duration: 12-24 months
  competition_level: Limited preferred
  timeline_to_deadline: 3-6 months
  match_requirement: Up to 25%
  participant_numbers: 100-300 participants
```

---

## Additional Context

### Unique Differentiators

**What makes YOUR organization stand out?**
```yaml
differentiators:
  - [YOUR_UNIQUE_CAPABILITY_1]
  - [YOUR_UNIQUE_APPROACH_2]
  - [YOUR_SPECIAL_EXPERTISE_3]
```

### Current Gaps/Needs

**What capabilities would YOU need to build?**
```yaml
capability_gaps:
  - [YOUR_GAP_1]
  - [YOUR_GAP_2]
```

---

## Notes & Special Instructions

```yaml
special_notes: |
  [Add any special preferences or instructions for Claude here]
```

---

## Configuration Version

```yaml
config_version: 2.0.0
last_updated: [YYYY-MM-DD]
updated_by: [YOUR_NAME]
```

---

## 🚀 Quick Setup Checklist

**Before saving as CONFIG.md, replace all placeholders:**

- [ ] Organization name and business type
- [ ] Check all focus areas that apply
- [ ] Add YOUR states/regions
- [ ] Add YOUR industry keywords (5-10 minimum)
- [ ] Add exclusion keywords
- [ ] Set YOUR minimum funding threshold
- [ ] Set YOUR sweet spot range
- [ ] Adjust scoring weights if needed (must total 100)
- [ ] Set YOUR capacity constraints
- [ ] List YOUR partners
- [ ] Set YOUR match capability
- [ ] Check intelligence sources to monitor
- [ ] Set YOUR alert thresholds
- [ ] Add YOUR white paper topics
- [ ] Add YOUR past performance (2-3 examples)
- [ ] Define YOUR ideal opportunity
- [ ] List YOUR differentiators
- [ ] Note any capability gaps

**Once complete:**
1. Save this file as `CONFIG.md`
2. ZIP your skill folder (include CONFIG.md)
3. Upload to Claude → Settings → Capabilities → Skills
4. Test: `"Search for opportunities in my target regions"`

---

## 📝 Placeholder Reference Guide

Quick find-and-replace guide:

| Placeholder | Replace With | Example |
|-------------|--------------|---------|
| `[YOUR_ORGANIZATION_NAME]` | Your actual organization name | `Pacific Skills Training` |
| `[YOUR_STATE_1]` | Your primary state | `California` |
| `[KEYWORD_1]` | Industry keyword | `workforce training` |
| `[YOUR_MIN_FUNDING]` | Minimum amount | `$50,000` |
| `[YOUR_SWEET_SPOT]` | Funding range | `$100,000 - $500,000` |
| `[YOUR_WEIGHT]` | Scoring weight | `40` (for funding size) |
| `[Yes/No]` | Choose one | `Yes` or `No` |
| `[NUMBER]` | Insert number | `3` (for max projects) |

---

**This preset is ready for YOU to customize - just fill in the placeholders!**
