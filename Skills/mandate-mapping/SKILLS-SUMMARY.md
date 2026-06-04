# Mandate Search Agent - Skills Summary

**Version:** 2.0.0 (Fully Configurable)
**For:** Any organization seeking funding opportunities (grants, contracts, RFPs)

---

## 🎯 What This Skill Does

**Finds funding opportunities customized to YOUR business** - any industry, any geography, any organization type.

### How It Works
You ask Claude to search → Claude uses **interactive web search** → Claude analyzes and presents findings

**Key Point:** This is conversational and on-demand. No automation, no actors, no background scraping. You initiate searches, Claude responds in real-time.

### What It Delivers
1. **Searches** on-demand using Claude's web search capabilities
2. **Scores** opportunities 0-100 based on YOUR priorities
3. **Routes** with action tags (white-paper-ready, proposal-ready, nurture-needed, monitor-only)
4. **Generates** intelligence reports tailored to YOUR needs
5. **Tracks** trends in YOUR focus areas

---

## ✨ Why This Is Powerful

### Fully Configurable
- 🗺️ **Your Geography:** Any states, regions, or countries
- 🏭 **Your Industry:** Manufacturing, healthcare, IT, consulting, nonprofit, etc.
- 🎯 **Your Focus:** Workforce development, economic development, entrepreneurship, etc.
- 💰 **Your Capacity:** Minimum funding, sweet spot range, match capability
- ⚖️ **Your Priorities:** Customize scoring weights to match your strategy

### Works For
- Training providers
- Economic development consultants
- Industry associations
- Nonprofit organizations
- Community colleges
- Workforce boards
- Small businesses seeking grants
- **Any organization pursuing funding**

---

## 🔍 Key Innovation: Pre-RFP Signal Detection

Finds opportunities **BEFORE they become competitive RFPs:**

- 📜 Legislative bills with appropriation language
- 💵 Budget proposals with new funding
- 📋 Agency strategic plans (unfunded priorities)
- 👥 Listening sessions and stakeholder engagement
- ⏰ Expiring appropriations

**Result:** Position yourself as a thought leader before competition begins!

---

## 🎓 How Scoring Works (0-100 Scale)

Every opportunity is scored based on YOUR configured priorities:

| Factor | Default Points | What It Means |
|--------|---------------|---------------|
| **Funding Size** | 40 | Based on your funding preferences |
| **Timeline** | 20 | 6-12 months = optimal positioning |
| **Competition** | 20 | Unsolicited = highest score |
| **Geography** | 20 | Your target states = max points |

**Weights are customizable** - adjust to match your priorities (must total 100).

---

## 🏷️ Smart Routing Tags

Opportunities are automatically categorized:

- **white-paper-ready (80+):** Pre-RFP signal → Write thought leadership, position early
- **proposal-ready (70+):** Active RFP → Develop full proposal
- **nurture-needed (50-69):** Build relationships and partnerships
- **monitor-only (<50):** Archive for future reference

---

## ⚙️ Setup (10-15 Minutes)

### Step 1: Configure for Your Business
1. Open `CONFIG-TEMPLATE.md`
2. Fill in your:
   - Business profile and services
   - Target states/regions
   - Industry focus areas
   - Custom keywords
   - Funding thresholds
   - Scoring preferences
3. Save as `CONFIG.md`

### Step 2: Upload to Claude
1. ZIP the folder (include your `CONFIG.md`)
2. Upload to Claude → Settings → Capabilities → Skills
3. Enable the skill

### Step 3: Test It
```
"Search for funding opportunities in my target regions"
```

**That's it!** No coding required.

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

---

## 📖 Usage Examples

### Search Commands
```
"Search for opportunities in my target regions"
"Find pre-RFP opportunities I can position for"
"Check for new workforce AI funding in Texas"
"Look for opportunities in manufacturing automation"
```

### Scoring Commands
```
"Score this opportunity: [URL or description]"
"Evaluate this based on my business profile"
"Compare these 3 opportunities"
```

### Report Commands
```
"Generate intelligence brief for top 5 opportunities"
"Create my weekly digest"
"Show all white-paper-ready opportunities"
"What funding trends are emerging in my focus areas?"
"Show opportunities matching my sweet spot"
```

---

## 🌟 What Makes This Valuable

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

## 📦 What's Included

| File | Purpose |
|------|---------|
| **Skill.md** | Main skill file (reads your CONFIG.md) |
| **SKILL-generic.md** | Version for OpenAI GPTs, other platforms |
| **CONFIG-TEMPLATE.md** | Template with examples for all business types |
| **CONFIG-COMMUNITY-PRESET.md** | Generic preset with placeholders for easy customization |
| **CONFIG.md** | YOUR configuration (you create from template or preset) |
| **REFERENCE.md** | Detailed workflow and best practices |
| **search-criteria.md** | Default keywords (supplement with yours) |
| **target-regions.md** | Default agencies (supplement with yours) |
| **scoring-examples.md** | Sample opportunities with scoring |
| **output-templates.md** | JSON and markdown report templates |
| **README.md** | Complete overview and quick start |
| **SKILLS-SUMMARY.md** | This file - quick reference |
| **SKOOL-SUMMARY.html** | Beautiful HTML version for sharing |
| **SETUP-GUIDE.md** | Step-by-step setup instructions |

---

## 🤝 Perfect for Community Sharing

**This skill is designed to be shared:**

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

## 🚀 Get Started

### For Claude Skills:
1. Fill out `CONFIG-TEMPLATE.md` with your information
2. Save as `CONFIG.md`
3. ZIP the folder (including your CONFIG.md)
4. Upload to Claude → Settings → Capabilities → Skills
5. Test: `"Search for opportunities in my target regions"`

### For OpenAI GPTs:
1. Fill out `CONFIG-TEMPLATE.md`
2. Use `SKILL-generic.md` as system prompt
3. Upload all .md files as knowledge base
4. Test with your configured geography/industry

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

## 💬 Support

**Questions about configuration?**
- See `CONFIG-TEMPLATE.md` for detailed examples
- Review `REFERENCE.md` for implementation details
- Check `scoring-examples.md` for scoring guidance

**Questions about usage?**
- Run: `"Help me use my Mandate Search Agent"`
- Claude will guide you based on your configuration

---

## 📝 Quick Reference Card

**Command Shortcuts:**

| What You Want | What To Say |
|---------------|-------------|
| Find opportunities | "Search for opportunities in [topic/region]" |
| Score an opportunity | "Score this: [URL/description]" |
| Get your digest | "Create my weekly digest" |
| Find early signals | "Find white-paper-ready opportunities" |
| Analyze trends | "What trends are emerging in [your industry]?" |
| Setup help | "Help me configure my Mandate Search Agent" |

---

**Version:** 2.0.0
**Last Updated:** 2025-10-25
**Works with:** Claude Skills, OpenAI GPTs, other LLM platforms
