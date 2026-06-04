---
name: mandate-search-agent
description: Monitors and scores funding opportunities based on your business profile, geographic focus, and industry preferences. Finds pre-RFP signals for strategic positioning.
metadata:
  version: 2.0.0
  configurable: true
---

# Mandate Search Agent

## Overview

This Skill monitors and scores funding opportunities customized to YOUR business profile, geographic focus, and industry preferences. It works for any organization seeking grants, contracts, or funding opportunities.

**Primary Focus:** Identify pre-RFP signals (legislative activity, budget proposals, agency planning) to enable proactive positioning through white papers and unsolicited proposals—before opportunities become competitive RFPs.

**Fully Configurable:** Customize for your specific states, industries, keywords, and organizational capacity.

## First-Time Setup Required

**Before using this Skill, set up your configuration:**

1. Copy `CONFIG-TEMPLATE.md` to create your `CONFIG.md`
2. Fill in your:
   - Business profile and services
   - Target states/regions
   - Industry focus areas
   - Keywords and search terms
   - Funding thresholds
   - Scoring preferences
3. Save as `CONFIG.md` in the skill folder

**Quick Setup Command:**
```
"Help me set up my Mandate Search Agent configuration"
```

Claude will guide you through the setup process.

## When to Use This Skill

Use this Skill when the user requests:
- Searching for funding opportunities in your configured regions/industries
- Scoring/evaluating a specific grant or funding opportunity
- Generating intelligence briefs on opportunities
- Analyzing funding trends or patterns
- Finding pre-RFP positioning opportunities
- Creating weekly or monthly opportunity reports

**Example prompts that trigger this Skill:**
- "Search for funding opportunities in [your configured region]"
- "Score this grant opportunity for me"
- "Generate a weekly digest of opportunities"
- "What are the top white-paper-ready opportunities?"
- "Analyze funding trends in [your industry/region]"
- "Find pre-RFP opportunities I can position for"

## Core Capabilities

### 1. Search & Discovery (On-Demand Web Search)
When you ask, Claude uses **web search tools** to find funding opportunities matching YOUR configured criteria.

**How it works:**
- You request: "Search for opportunities in [my region/topic]"
- Claude uses web search to query relevant sources in real-time
- Results are filtered by your CONFIG.md preferences
- Returns opportunities matching your profile

**No automated scraping or background actors** - this is interactive web search powered by Claude's built-in capabilities.

**Searches based on your CONFIG.md:**
- Your target states/regions
- Your industry focus areas
- Your custom keywords
- Your minimum funding thresholds

### 2. Scoring (0-100 Scale)
Score each opportunity based on YOUR priorities:

**Default scoring (customizable in CONFIG.md):**
- **Funding Size (40 pts):** Based on your funding preferences
- **Timeline (20 pts):** 6-12mo = 20, 3-6mo = 15, <3mo = 10, >12mo = 5
- **Competition (20 pts):** Unsolicited = 20, Limited = 15, Set-aside = 10, Open = 5
- **Geography (20 pts):** Your target states = 20, Adjacent = 10, Federal = 5

**Adjust weights in CONFIG.md** to match your priorities (must total 100).

### 3. Routing Tags
Automatically categorize opportunities:
- **white-paper-ready** (80+): Pre-RFP signals requiring thought leadership
- **proposal-ready** (70+): Active RFPs requiring proposals
- **nurture-needed** (50-69): Relationship building opportunities
- **monitor-only** (<50): Low priority, archive only

**Thresholds are customizable** in CONFIG.md.

### 4. Intelligence Reporting
Generate structured reports:
- Individual opportunity intelligence briefs
- Weekly digests (all opportunities found)
- Monthly trend analysis
- High-priority alerts (customized to your thresholds)

## Quick Reference

**Configuration-Driven:** All parameters come from your CONFIG.md file

**Output Formats:** JSON records and Markdown reports (see `output-templates.md`)

**Scoring Examples:** See `scoring-examples.md` for sample opportunities

**Search Keywords:** Default library in `search-criteria.md` + YOUR custom keywords

**Agency Sources:** Default sources in `target-regions.md` + YOUR custom sources

## Workflow (Interactive, On-Demand)

**When you ask Claude to search for opportunities:**

1. **Read CONFIG.md** to understand your business profile and preferences
2. **Web Search** - Claude uses web search tools to query:
   - Grants.gov with your keywords and geography
   - State agency websites for your target states
   - Federal program announcements
   - Legislative tracking sites
3. **Filter** results by your relevance criteria and exclusions
4. **Score** each opportunity (0-100) using your scoring weights
5. **Tag** with routing classification based on your thresholds
6. **Generate** intelligence brief if meets your alert criteria
7. **Report** findings in requested format

**This is conversational and interactive** - no background automation. You ask, Claude searches and analyzes.

## Key Features

- **Interactive Web Search:** On-demand searches using Claude's web search capabilities (no automation)
- **Fully Configurable:** Works for any industry, geography, or business type
- **Pre-RFP Detection:** Finds legislative bills, budget proposals, agency planning signals
- **Strategic Scoring:** Prioritizes opportunities matching YOUR strengths and capacity
- **Multi-Source Intelligence:** Searches federal, state, regional, local, and industry sources
- **Structured Output:** JSON + Markdown formats for easy integration

**Important:** This skill requires you to initiate searches. Claude responds in real-time using web search tools. It does NOT automatically monitor sources in the background.

## Configuration Options

Your CONFIG.md controls:

**Business Profile:**
- Organization type and services
- Industry focus areas
- Target populations
- Special expertise

**Geographic Scope:**
- Primary target states/regions
- Adjacent states to monitor
- Federal program preferences

**Search Criteria:**
- Custom keywords for your industry
- Exclusion terms
- Minimum funding thresholds
- Sweet spot funding range

**Scoring Preferences:**
- Scoring weight allocation
- Routing tag thresholds
- Alert triggers

**Capacity & Constraints:**
- Lead vs. subcontractor preferences
- Partnership capabilities
- Match/cost-share capacity
- Max concurrent projects

**Intelligence Sources:**
- Which federal sources to monitor
- State sources for your geography
- Industry-specific sources
- Custom sources you provide

## Resources

This Skill includes supporting reference files:

**Configuration:**
- `CONFIG-TEMPLATE.md` - Template to create your configuration
- `CONFIG.md` - YOUR configuration (create from template)

**Reference Files:**
- `REFERENCE.md` - Detailed workflow, intelligence signals, and best practices
- `search-criteria.md` - Default keyword library (supplement with your keywords)
- `target-regions.md` - Default agency directories (supplement with your sources)
- `scoring-examples.md` - Sample opportunities with detailed scoring rationale
- `output-templates.md` - JSON schemas and Markdown report templates

Claude will access these files as needed when executing searches, scoring opportunities, or generating reports.

## Usage Examples

**Initial Setup:**
```
"Help me set up my Mandate Search Agent configuration"
"I need to configure this for my business in California"
```

**Search Commands:**
```
"Search for opportunities in my target regions"
"Find pre-RFP opportunities I can position for"
"Check for new opportunities this week"
```

**Scoring Commands:**
```
"Score this opportunity: [URL or description]"
"Evaluate this based on my business profile"
```

**Report Commands:**
```
"Generate intelligence brief for top 5 opportunities"
"Create my weekly digest"
"Show all white-paper-ready opportunities for me"
```

**Analysis Commands:**
```
"What funding trends are emerging in my focus areas?"
"Compare opportunities across my target states"
"Show opportunities matching my sweet spot"
```

## Configuration Examples

**Small Training Provider (Single State):**
- Target: California
- Focus: Technical skills training
- Min funding: $25K
- Sweet spot: $50K-$250K

**Economic Development Consultant (Multi-State):**
- Target: NC, SC, GA, VA (Appalachian region)
- Focus: Regional planning, entrepreneurship
- Min funding: $100K
- Sweet spot: $250K-$1M

**Industry Association (Regional):**
- Target: IL, IN, WI, MI (Great Lakes)
- Focus: Manufacturing, Industry 4.0, AI workforce
- Min funding: $500K
- Sweet spot: $1M-$5M

**Nonprofit Workforce Provider:**
- Target: TX (statewide)
- Focus: Disadvantaged workers, job placement
- Min funding: $50K
- Sweet spot: $100K-$500K

---

**Note:** This Skill adapts to YOUR configuration. Without a CONFIG.md file, it will use default settings (DE, PA, MD, VA, DC / workforce & economic development focus). To get full value, complete your configuration!

**Ready to start? Run:** `"Help me set up my Mandate Search Agent configuration"`
