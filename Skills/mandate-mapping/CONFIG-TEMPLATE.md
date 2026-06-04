# Mandate Search Agent - Configuration Template

**Instructions:** Copy this template, fill in your information, and save as `CONFIG.md` in your skill folder. Claude will read your configuration to customize the search for your specific business needs.

---

## Your Business Profile

### Organization Information
```yaml
organization_name: [Your Company/Organization Name]
business_type: [Consulting, Training Provider, Economic Development, etc.]
primary_services: [List your main services/offerings]
```

### Focus Areas

**Industries/Sectors You Serve:**
- [ ] Workforce Development
- [ ] Economic Development
- [ ] Manufacturing
- [ ] Healthcare
- [ ] Information Technology
- [ ] Construction
- [ ] Hospitality/Tourism
- [ ] Energy/Utilities
- [ ] Agriculture
- [ ] Other: _______________

**Target Populations:**
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
- [ ] Other: _______________

**Special Focus Areas:**
- [ ] AI/Automation Impact
- [ ] Digital Transformation
- [ ] Apprenticeships
- [ ] Skills Training
- [ ] Career Pathways
- [ ] Entrepreneurship
- [ ] Small Business Support
- [ ] Other: _______________

---

## Geographic Configuration

### Primary Target States/Regions

**List your target geography (states, regions, or countries):**

```yaml
primary_states:
  - [State 1]
  - [State 2]
  - [State 3]

adjacent_states:  # Optional: nearby states to monitor
  - [Adjacent State 1]
  - [Adjacent State 2]

regions:  # Optional: specific regions or metro areas
  - [Region 1]
  - [Region 2]
```

**Example:**
```yaml
primary_states:
  - California
  - Nevada
  - Arizona

adjacent_states:
  - Oregon
  - New Mexico

regions:
  - San Francisco Bay Area
  - Southern California
  - Las Vegas Metro
```

### Federal Programs
```yaml
include_federal_programs: [Yes/No]
federal_focus: [Programs available in your states, National programs, Both]
```

---

## Keywords & Search Terms

### Primary Keywords (Your Industry/Focus)

**Add keywords specific to your business:**
```yaml
primary_keywords:
  - [keyword 1]
  - [keyword 2]
  - [keyword 3]
```

**Example for Manufacturing:**
```yaml
primary_keywords:
  - advanced manufacturing
  - Industry 4.0
  - supply chain
  - automation
  - robotics training
```

**Example for Healthcare:**
```yaml
primary_keywords:
  - healthcare workforce
  - nursing shortage
  - allied health
  - medical training
  - behavioral health
```

### Exclusion Keywords

**Terms that indicate opportunities NOT relevant to you:**
```yaml
exclude_keywords:
  - [keyword to exclude 1]
  - [keyword to exclude 2]
```

**Example:**
```yaml
exclude_keywords:
  - K-12 only
  - pure research
  - international development
  - law enforcement only
```

---

## Funding Preferences

### Minimum Funding Threshold
```yaml
minimum_funding: $[amount]  # Don't capture opportunities below this
```

**Recommended:**
- Small organization: $10,000 - $25,000
- Medium organization: $50,000 - $100,000
- Large organization: $100,000+

### Funding Size Preferences

**What funding ranges are you most competitive in?**
```yaml
sweet_spot_range: $[min] - $[max]
```

**Example:** `sweet_spot_range: $100,000 - $500,000`

---

## Scoring Customization

### Scoring Weight Preferences

**Default weights:** Funding 40, Timeline 20, Competition 20, Geography 20

**Adjust if your priorities differ:**

```yaml
scoring_weights:
  funding_size: [0-50 points]      # Default: 40
  timeline: [0-30 points]          # Default: 20
  competition_level: [0-30 points] # Default: 20
  geography_match: [0-30 points]   # Default: 20
```

**Must total 100 points**

**Example - Prioritizing Easy Wins:**
```yaml
scoring_weights:
  funding_size: 30      # Lower priority on size
  timeline: 25          # More time to prepare
  competition_level: 30 # Heavily favor less competition
  geography_match: 15   # Flexible on location
```

**Example - Prioritizing Large Opportunities:**
```yaml
scoring_weights:
  funding_size: 50      # Size is most important
  timeline: 15          # Less concerned about timeline
  competition_level: 15 # Willing to compete
  geography_match: 20   # Stick to target region
```

### Routing Tag Thresholds

**Default:** white-paper-ready (80+), proposal-ready (70+), nurture-needed (50-69), monitor-only (<50)

**Adjust if needed:**
```yaml
routing_thresholds:
  white_paper_ready: [75-90]   # Default: 80
  proposal_ready: [65-79]      # Default: 70
  nurture_needed: [45-64]      # Default: 50
```

---

## Capacity & Constraints

### Organizational Capacity

```yaml
capacity:
  can_lead_projects: [Yes/No]
  can_be_subcontractor: [Yes/No]
  max_concurrent_projects: [number]
  geographic_presence: [Local, Statewide, Regional, National]
```

### Partnership Preferences

**Do you have existing partners in these categories?**
```yaml
partnerships:
  community_colleges: [Yes/No - List names if yes]
  workforce_boards: [Yes/No - List names if yes]
  industry_associations: [Yes/No - List names if yes]
  employers: [Yes/No - Describe if yes]
  other_training_providers: [Yes/No - List names if yes]
```

### Match/Cost-Share Capability

```yaml
cost_share:
  can_provide_cash_match: [Yes/No]
  max_match_percentage: [0-100%]
  can_provide_in_kind_match: [Yes/No]
```

---

## Intelligence Sources

### Which sources should the skill monitor for you?

**Federal Sources:**
- [ ] Grants.gov
- [ ] Federal agency announcements (DOL, EDA, SBA, etc.)
- [ ] Federal Register

**State Sources (for your target states):**
- [ ] State legislature bill trackers
- [ ] Governor/executive office press releases
- [ ] State workforce development boards
- [ ] State economic development agencies
- [ ] State budget documents

**Regional/Local Sources:**
- [ ] Regional planning councils
- [ ] Local workforce areas
- [ ] Economic development organizations
- [ ] Chamber of commerce announcements

**Foundation Sources:**
- [ ] Private foundation programs
- [ ] Corporate foundation programs
- [ ] Community foundation programs

**Industry Sources:**
- [ ] Industry association announcements
- [ ] Trade publication RFPs
- [ ] Sector partnership initiatives

### Custom Sources

**Add any specific sources you want monitored:**
```yaml
custom_sources:
  - name: [Source Name]
    url: [URL]
    check_frequency: [Daily/Weekly/Monthly]

  - name: [Source Name 2]
    url: [URL]
    check_frequency: [Daily/Weekly/Monthly]
```

---

## Reporting Preferences

### Alert Preferences

**When should you receive immediate alerts?**
```yaml
alert_triggers:
  minimum_score: [75-95]          # Default: 85
  minimum_funding: $[amount]       # Default: $500,000
  unsolicited_opportunities: [Yes/No]  # Default: Yes
  urgent_deadlines: [X days]       # Alert if deadline within X days
```

### Report Frequency

```yaml
reports:
  daily_alerts: [Yes/No]
  weekly_digest: [Yes/No - Day of week: _____]
  monthly_analysis: [Yes/No]
```

### Report Distribution

```yaml
recipients:
  - name: [Name]
    email: [Email]
    role: [BD Manager, Grant Writer, etc.]

  - name: [Name 2]
    email: [Email]
    role: [Role]
```

---

## Strategic Priorities

### White Paper Topics

**What thought leadership topics are you positioned to write about?**
```yaml
white_paper_expertise:
  - [Topic 1: e.g., "Skills gap in manufacturing"]
  - [Topic 2: e.g., "AI workforce transition models"]
  - [Topic 3]
```

### Past Performance

**Do you have past awards/projects to reference?**
```yaml
past_performance:
  - program: [Program Name]
    funder: [Agency/Organization]
    amount: $[amount]
    year: [year]
    outcomes: [Brief description]
```

---

## Success Criteria

### What defines a "good opportunity" for your organization?

```yaml
ideal_opportunity:
  funding_range: $[min] - $[max]
  project_duration: [months]
  competition_level: [Unsolicited, Limited, Set-aside, Open]
  timeline_to_deadline: [3-6 months, 6-12 months, etc.]
  match_requirement: [None, Up to 25%, Flexible]
  participant_numbers: [approximate number you can serve]
```

---

## Additional Context

### Unique Differentiators

**What makes your organization stand out?**
```yaml
differentiators:
  - [Unique capability 1]
  - [Unique approach 2]
  - [Special expertise 3]
```

### Current Gaps/Needs

**What capabilities would you need to build to compete for certain opportunities?**
```yaml
capability_gaps:
  - [Gap 1: e.g., "Need healthcare sector partnerships"]
  - [Gap 2: e.g., "No presence in rural counties"]
```

---

## Notes & Special Instructions

**Any other information Claude should know:**
```yaml
special_notes: |
  [Add any additional context, preferences, or instructions here.

  Examples:
  - "Avoid opportunities requiring multi-state presence"
  - "Prioritize opportunities with employer co-investment"
  - "We're expanding into [state] next year, flag opportunities there"
  - "Focus on opportunities that include technology/equipment budgets"
  ]
```

---

## Configuration Version

```yaml
config_version: 1.0.0
last_updated: [YYYY-MM-DD]
updated_by: [Your Name]
```

---

## Quick Start Examples

### Example 1: Small Training Provider in California
```yaml
organization_name: Pacific Skills Training
business_type: Workforce Training Provider
primary_services: [Short-term technical training, Career coaching, Job placement]

primary_states: [California]
adjacent_states: [Nevada, Oregon]

primary_keywords:
  - workforce training
  - technical skills
  - career pathways
  - job placement

minimum_funding: $25,000
sweet_spot_range: $50,000 - $250,000

can_lead_projects: Yes
can_be_subcontractor: Yes
max_concurrent_projects: 3
```

### Example 2: Economic Development Consultant (Multi-State)
```yaml
organization_name: Regional Growth Advisors
business_type: Economic Development Consulting
primary_services: [Strategic planning, Grant writing, Program evaluation]

primary_states: [North Carolina, South Carolina, Georgia, Virginia]
regions: [Appalachian region, Rural South]

primary_keywords:
  - economic development
  - regional planning
  - business development
  - entrepreneurship

minimum_funding: $100,000
sweet_spot_range: $250,000 - $1,000,000

can_lead_projects: Yes
can_be_subcontractor: Yes
geographic_presence: Regional
```

### Example 3: Industry Association with AI Focus
```yaml
organization_name: Tech Industry Alliance
business_type: Industry Association
primary_services: [Member training, Advocacy, Research]

primary_states: [Illinois, Indiana, Wisconsin, Michigan]
regions: [Great Lakes region, Rust Belt]

primary_keywords:
  - AI workforce
  - automation
  - digital transformation
  - Industry 4.0
  - manufacturing technology

minimum_funding: $500,000
sweet_spot_range: $1,000,000 - $5,000,000

scoring_weights:
  funding_size: 45
  timeline: 20
  competition_level: 15
  geography_match: 20
```

---

**Save this file as `CONFIG.md` in your skill folder after filling it out!**
