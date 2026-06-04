# Mandate Search Agent - Claude Skill Package

**Version:** 2.0.0 (Fully Configurable)
**Created:** 2025-10-25
**For:** Any organization seeking funding opportunities (grants, contracts, RFPs)

---

## 🎯 What This Skill Does

**Finds funding opportunities customized to YOUR business** - any industry, any geography, any organization type.

**How it works:** You ask Claude to search, and Claude uses **interactive web search** (no automation or actors).

1. **Searches** on-demand using Claude's web search capabilities
2. **Scores** opportunities 0-100 based on YOUR priorities
3. **Routes** with action tags based on YOUR thresholds
4. **Generates** intelligence reports tailored to YOUR needs
5. **Tracks** trends in YOUR focus areas

**Important:** This is conversational and interactive - you initiate searches, Claude responds in real-time using web search tools.

---

## ✨ Key Feature: Fully Configurable

**This skill adapts to YOUR business:**

- 🗺️ **Your Geography:** Any states, regions, or countries
- 🏭 **Your Industry:** Manufacturing, healthcare, IT, consulting, nonprofit, etc.
- 🎯 **Your Focus:** Workforce development, economic development, entrepreneurship, etc.
- 💰 **Your Capacity:** Minimum funding, sweet spot range, match capability
- ⚖️ **Your Priorities:** Customize scoring weights to match your strategy

**Works for:**
- Training providers
- Economic development consultants
- Industry associations
- Nonprofit organizations
- Community colleges
- Workforce boards
- Small businesses seeking grants
- Any organization pursuing funding

---

## 🚀 Quick Start

### Step 1: Set Up Your Configuration

**Before using the skill, customize it for your business:**

1. Open `CONFIG-TEMPLATE.md`
2. Fill in your:
   - Business profile and services
   - Target states/regions (any geography!)
   - Industry focus areas
   - Custom keywords
   - Funding thresholds
   - Scoring preferences
3. Save as `CONFIG.md` in the skill folder

**⏱️ Setup takes 10-15 minutes** but saves hours of irrelevant searches!

### Step 2: Upload to Claude

1. **ZIP the folder:**
   ```
   mandate-search-skill/
   ├── Skill.md
   ├── SKILL-generic.md
   ├── CONFIG.md  (your configuration!)
   ├── CONFIG-TEMPLATE.md
   ├── CONFIG-COMMUNITY-PRESET.md
   ├── REFERENCE.md
   ├── search-criteria.md
   ├── target-regions.md
   ├── scoring-examples.md
   ├── output-templates.md
   ├── README.md
   ├── SKILLS-SUMMARY.md
   ├── SKOOL-SUMMARY.html
   └── SETUP-GUIDE.md
   ```

2. **Upload to Claude:**
   - Go to Settings → Capabilities → Skills
   - Click "Upload Skill" and select ZIP
   - Enable the Skill

3. **Test it:**
   ```
   "Search for funding opportunities in my target regions"
   "Help me set up my configuration"
   ```

---

## 📋 Files in This Package

### Configuration Files
- **CONFIG-TEMPLATE.md** - Template with examples for all business types
- **CONFIG-COMMUNITY-PRESET.md** - Generic preset with placeholders for easy customization
- **CONFIG.md** - YOUR configuration (create from template or preset)

### Core Skill Files
- **Skill.md** - Main skill file (reads your CONFIG.md)
- **SKILL-generic.md** - Version for OpenAI GPTs, other platforms

### Reference Files
- **REFERENCE.md** - Detailed workflow and best practices
- **search-criteria.md** - Default keywords (supplement with yours)
- **target-regions.md** - Default agencies (supplement with yours)
- **scoring-examples.md** - Sample opportunities with scoring
- **output-templates.md** - JSON and markdown report templates

### Documentation Files
- **README.md** - This file - complete overview
- **SKILLS-SUMMARY.md** - Quick reference card
- **SKOOL-SUMMARY.html** - Beautiful HTML version for sharing
- **SETUP-GUIDE.md** - Step-by-step setup instructions

---

## 💡 Configuration Examples

### Example 1: California Training Provider
```yaml
primary_states: [California]
primary_keywords: [workforce training, technical skills, job placement]
minimum_funding: $25,000
sweet_spot_range: $50,000 - $250,000
```

### Example 2: Multi-State Economic Development Consultant
```yaml
primary_states: [North Carolina, South Carolina, Georgia, Virginia]
regions: [Appalachian region]
primary_keywords: [economic development, entrepreneurship, regional planning]
minimum_funding: $100,000
sweet_spot_range: $250,000 - $1,000,000
```

### Example 3: Manufacturing Industry Association
```yaml
primary_states: [Illinois, Indiana, Wisconsin, Michigan]
primary_keywords: [manufacturing, Industry 4.0, AI workforce, automation]
minimum_funding: $500,000
sweet_spot_range: $1,000,000 - $5,000,000
```

### Example 4: Texas Nonprofit
```yaml
primary_states: [Texas]
primary_keywords: [disadvantaged workers, job training, career pathways]
minimum_funding: $50,000
sweet_spot_range: $100,000 - $500,000
```

**See CONFIG-TEMPLATE.md for complete examples and all configuration options!**

---

## 🎓 How It Works

### Interactive Web Search (Not Automated)

**This skill uses Claude's web search tools - no background automation or actors:**

1. **You Ask:** "Search for funding opportunities in Texas"
2. **Claude Searches:** Uses WebSearch tool to query Grants.gov, state sites, agency pages
3. **Claude Analyzes:** Filters by your CONFIG.md, scores opportunities
4. **Claude Reports:** Presents findings with intelligence briefs

**Each search is interactive and initiated by you in conversation with Claude.**

### 1. Pre-RFP Signal Detection
Finds opportunities **before they become competitive RFPs:**
- Legislative bills with appropriation language
- Budget proposals with new funding
- Agency strategic plans (unfunded priorities)
- Listening sessions and stakeholder engagement
- Expiring appropriations

### 2. Intelligent Scoring (0-100)
Scores based on YOUR priorities:
- **Funding Size:** Based on your preferences
- **Timeline:** Optimal positioning windows
- **Competition Level:** Unsolicited = highest score
- **Geography Match:** Your target states

### 3. Smart Routing Tags
- **white-paper-ready** (80+): Write thought leadership, position early
- **proposal-ready** (70+): Active RFP, develop proposal
- **nurture-needed** (50-69): Build relationships
- **monitor-only** (<50): Archive for reference

### 4. Custom Intelligence Reports
- Individual opportunity briefs
- Weekly digests
- Monthly trend analysis
- High-priority alerts (your thresholds)

---

## 📖 Usage Examples

### Initial Setup
```
"Help me set up my Mandate Search Agent configuration"
"I need to configure this for my business in [state]"
```

### Search & Discovery
```
"Search for opportunities in my target regions"
"Find pre-RFP opportunities I can position for"
"Check for new opportunities this week"
"Look for opportunities in [specific industry/topic]"
```

### Scoring & Evaluation
```
"Score this opportunity: [URL or description]"
"Evaluate this based on my business profile"
"Compare these 3 opportunities"
```

### Reports & Analysis
```
"Generate intelligence brief for top 5 opportunities"
"Create my weekly digest"
"Show all white-paper-ready opportunities"
"What funding trends are emerging in my focus areas?"
"Show opportunities matching my sweet spot"
```

---

## 🔧 Customization Options

Your CONFIG.md controls everything:

**Business Profile:**
- Organization type, services, expertise
- Industry focus areas
- Target populations
- Differentiators

**Geographic Scope:**
- Primary states/regions
- Adjacent areas to monitor
- Federal program preferences

**Search Criteria:**
- Custom keywords for your industry
- Exclusion terms
- Minimum/maximum funding
- Sweet spot range

**Scoring Preferences:**
- Weight allocation (must total 100)
- Routing tag thresholds
- Alert triggers

**Capacity & Constraints:**
- Lead vs. subcontractor
- Partnership capabilities
- Match/cost-share capacity
- Max concurrent projects

**Intelligence Sources:**
- Federal, state, regional sources
- Industry-specific sources
- Custom sources you provide

---

## 🌟 Why This Skill Is Valuable

### Saves Time
- ❌ No more manual searching across dozens of websites
- ❌ No more reviewing irrelevant opportunities
- ✅ Pre-filtered to YOUR profile automatically

### Finds Hidden Opportunities
- 🔍 Catches pre-RFP signals others miss
- 🔍 Monitors legislative activity for upcoming funding
- 🔍 Identifies expiring appropriations

### Strategic Positioning
- 📝 White paper recommendations for pre-RFP opportunities
- 🎯 Score-based prioritization
- 📊 Trend analysis to anticipate future opportunities

### Fully Customized
- 🎨 Your geography, your industry, your capacity
- 🎨 Your keywords, your thresholds, your priorities
- 🎨 Works for ANY organization type

---

## 📦 Progressive Disclosure Architecture

This skill follows Claude Skills best practices:

**Level 1: Metadata**
- Claude reads name and description to determine if skill applies

**Level 2: Skill.md + CONFIG.md**
- If relevant, reads your configuration and core instructions

**Level 3: Reference Files**
- Accesses detailed information only when needed

**Result:** Efficient, fast, and scales well with multiple skills

---

## 🔄 Version History

**Version 2.0.0 (2025-10-25) - Configurable Release**
- ✅ Full configuration system via CONFIG.md
- ✅ Works for any geography, industry, organization type
- ✅ Customizable scoring weights and thresholds
- ✅ Custom keywords and sources
- ✅ Template with examples for multiple business types

**Version 1.0.0 (2025-10-25) - Initial Release**
- Fixed to DE, MD, PA, VA, DC
- Workforce/economic development only

---

## 🤝 Perfect for Community Sharing

**This skill is designed to be shared with your community:**

✅ Each user creates their own CONFIG.md
✅ Works for any business type or geography
✅ Includes template with extensive examples
✅ Clear setup instructions (10-15 minutes)
✅ No coding required - just fill in a template

**Share with:**
- Your consulting clients
- Your community members
- Your network/association members
- Your training program participants

---

## 🚀 Get Started Now

### For Claude Skills:
1. **Fill out CONFIG-TEMPLATE.md** with your information
2. **Save as CONFIG.md**
3. **ZIP the folder** (including your CONFIG.md)
4. **Upload to Claude** → Settings → Capabilities → Skills
5. **Test:** `"Search for opportunities in my target regions"`

### For OpenAI GPTs:
1. **Fill out CONFIG-TEMPLATE.md**
2. **Use SKILL-generic.md** as system prompt
3. **Upload all .md files** as knowledge base
4. **Test** with your configured geography/industry

---

## 💬 Support

**Questions about configuration?**
- See CONFIG-TEMPLATE.md for detailed examples
- Review REFERENCE.md for implementation details
- Check scoring-examples.md for scoring guidance

**Questions about usage?**
- Run: `"Help me use my Mandate Search Agent"`
- Claude will guide you based on your configuration

---

## ⭐ Key Takeaway

**This is NOT a one-size-fits-all skill.**

It's a **configurable framework** that adapts to:
- ✅ YOUR geography (any states/regions)
- ✅ YOUR industry (any focus areas)
- ✅ YOUR capacity (any funding range)
- ✅ YOUR priorities (custom scoring)

**Take 10-15 minutes to configure it, then enjoy hours of automated, relevant opportunity intelligence!**

---

**Ready to configure your Mandate Search Agent? Open CONFIG-TEMPLATE.md and let's get started!** 🎯
