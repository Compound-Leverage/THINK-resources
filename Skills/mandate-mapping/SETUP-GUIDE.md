# Mandate Search Agent - Complete Setup Guide

**Time Required:** 10-15 minutes
**Difficulty:** Easy - No coding required!

---

## 📋 What You'll Need

- [ ] The Mandate Search Agent skill package (all .md files)
- [ ] Claude account (or OpenAI GPT account)
- [ ] 10-15 minutes to fill in your configuration
- [ ] Basic info about your business (states, industry, funding preferences)

---

## 🚀 Setup Process Overview

1. **Configure** - Fill in CONFIG-COMMUNITY-PRESET.md with YOUR information
2. **Package** - ZIP your skill folder
3. **Upload** - Upload to Claude Skills
4. **Test** - Try it out!

**That's it!** Let's walk through each step.

---

## Step 1: Download & Extract the Skill Package

### What You Should Have:

```
mandate-search-skill/
├── Skill.md
├── SKILL-generic.md
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
└── SETUP-GUIDE.md (this file)
```

✅ **You're ready if you have all these files!**

---

## Step 2: Choose Your Configuration Method

### Option A: Quick Start (Use Preset)
**Best for:** Getting started fast, customize later
1. Open `CONFIG-COMMUNITY-PRESET.md`
2. Use find-and-replace to swap placeholders with YOUR info
3. Save as `CONFIG.md`

### Option B: Custom Start (Use Template)
**Best for:** Comprehensive customization from scratch
1. Open `CONFIG-TEMPLATE.md`
2. Review all examples and options
3. Fill in sections relevant to you
4. Save as `CONFIG.md`

**We recommend Option A for first-time users!**

---

## Step 3: Fill In Your Configuration (Detailed Walkthrough)

Let's use `CONFIG-COMMUNITY-PRESET.md` (Option A) for this guide.

### 3.1 Basic Business Information

**Find this section:**
```yaml
organization_name: [YOUR_ORGANIZATION_NAME]
business_type: [Consulting / Training Provider / Nonprofit / Association / Economic Development / Other]
```

**Replace with:**
```yaml
organization_name: Pacific Skills Training
business_type: Workforce Training Provider
```

### 3.2 Geographic Configuration

**Find this section:**
```yaml
primary_states:
  - [YOUR_STATE_1]
  - [YOUR_STATE_2]
  - [YOUR_STATE_3]
```

**Replace with YOUR states:**
```yaml
primary_states:
  - California
  - Nevada
  - Arizona
```

💡 **Tip:** List states where you actually operate or seek funding!

### 3.3 Industry Keywords

**Find this section:**
```yaml
primary_keywords:
  - [KEYWORD_1]
  - [KEYWORD_2]
  - [KEYWORD_3]
```

**Replace with YOUR industry keywords:**

**For Manufacturing:**
```yaml
primary_keywords:
  - advanced manufacturing
  - Industry 4.0
  - automation training
  - robotics
  - supply chain
  - lean manufacturing
```

**For Healthcare:**
```yaml
primary_keywords:
  - healthcare workforce
  - nursing
  - allied health
  - medical training
  - patient care
  - behavioral health
```

**For IT/Tech:**
```yaml
primary_keywords:
  - IT workforce
  - cybersecurity
  - software development
  - data analytics
  - cloud computing
  - digital skills
```

💡 **Tip:** Add 5-10 keywords that describe YOUR work!

### 3.4 Funding Preferences

**Find this section:**
```yaml
minimum_funding: $[YOUR_MINIMUM]
sweet_spot_range: $[YOUR_MIN] - $[YOUR_MAX]
```

**Replace with YOUR funding capacity:**

**Small Organization:**
```yaml
minimum_funding: $25,000
sweet_spot_range: $50,000 - $250,000
```

**Medium Organization:**
```yaml
minimum_funding: $50,000
sweet_spot_range: $100,000 - $750,000
```

**Large Organization:**
```yaml
minimum_funding: $100,000
sweet_spot_range: $500,000 - $5,000,000
```

💡 **Tip:** Be realistic about what you can actually manage!

### 3.5 Scoring Weights (Optional)

**Find this section:**
```yaml
scoring_weights:
  funding_size: [YOUR_WEIGHT]
  timeline: [YOUR_WEIGHT]
  competition_level: [YOUR_WEIGHT]
  geography_match: [YOUR_WEIGHT]
```

**Default (Balanced) - Leave as is:**
```yaml
scoring_weights:
  funding_size: 40
  timeline: 20
  competition_level: 20
  geography_match: 20
```

**OR customize to YOUR priorities:**

**Prefer Easy Wins:**
```yaml
scoring_weights:
  funding_size: 30
  timeline: 25
  competition_level: 30    # Higher = favor less competition
  geography_match: 15
```

**Prefer Large Opportunities:**
```yaml
scoring_weights:
  funding_size: 50         # Higher = favor larger grants
  timeline: 15
  competition_level: 15
  geography_match: 20
```

⚠️ **Must total 100 points!**

### 3.6 Organizational Capacity

**Find this section:**
```yaml
capacity:
  can_lead_projects: [Yes/No]
  can_be_subcontractor: [Yes/No]
  max_concurrent_projects: [NUMBER]
  geographic_presence: [Local / Statewide / Regional / National]
```

**Replace with YOUR actual capacity:**
```yaml
capacity:
  can_lead_projects: Yes
  can_be_subcontractor: Yes
  max_concurrent_projects: 3
  geographic_presence: Statewide
```

💡 **Tip:** Be honest! This helps Claude find opportunities you can actually handle.

### 3.7 Save Your Configuration

1. **File → Save As**
2. **Filename:** `CONFIG.md` (exactly this name!)
3. **Location:** Same folder as other skill files
4. **Format:** Plain text / Markdown

✅ **Your configuration is complete!**

---

## Step 4: Package Your Skill

### For Claude Skills:

**Option 1: Using Finder (Mac) or Explorer (Windows)**

1. Navigate to your `mandate-search-skill` folder
2. Select the folder (not the files inside!)
3. Right-click → Compress (Mac) or Send to → Compressed folder (Windows)
4. Rename the ZIP file: `mandate-search-agent.zip`

**Option 2: Using Command Line**

```bash
cd /path/to/parent-directory
zip -r mandate-search-agent.zip mandate-search-skill/
```

**✅ Correct Structure:**
```
mandate-search-agent.zip
└── mandate-search-skill/
    ├── Skill.md
    ├── SKILL-generic.md
    ├── CONFIG.md  (your configuration!)
    ├── CONFIG-TEMPLATE.md
    ├── CONFIG-COMMUNITY-PRESET.md
    ├── REFERENCE.md
    └── [all other .md and .html files]
```

**❌ Incorrect Structure:**
```
mandate-search-agent.zip
├── Skill.md  (files at root - WRONG!)
├── CONFIG.md
└── [files directly in ZIP]
```

---

## Step 5: Upload to Claude

### Upload Process:

1. **Open Claude** (claude.ai)

2. **Go to Settings**
   - Click your profile icon (bottom left)
   - Select "Settings"

3. **Navigate to Skills**
   - Click "Capabilities" in left sidebar
   - Click "Skills" tab

4. **Upload Your Skill**
   - Click "+ Upload Skill" button
   - Select your `mandate-search-agent.zip` file
   - Wait for upload (5-10 seconds)

5. **Enable the Skill**
   - Find "Mandate Search Agent" in your skills list
   - Toggle switch to "ON"

✅ **Your skill is installed!**

---

## Step 6: Test Your Skill

### First Test Commands:

**Test 1: Basic Search**
```
"Search for funding opportunities in my target regions"
```

**Expected:** Claude reads your CONFIG.md, performs web searches, presents opportunities

**Test 2: Score an Opportunity**
```
"Score this opportunity: [paste a grant URL or description]"
```

**Expected:** Claude scores it 0-100 based on your configured weights

**Test 3: Check Configuration**
```
"What are my configured target states and industries?"
```

**Expected:** Claude reads and summarizes your CONFIG.md

### If It Works:
✅ You're all set! Try more searches specific to your needs.

### If It Doesn't Work:
1. Check that CONFIG.md is in the ZIP
2. Check that ZIP structure is correct (folder as root)
3. Check that you enabled the skill in Settings
4. Try: "Help me use my Mandate Search Agent"

---

## Step 7: Using Your Skill

### Common Commands:

**Search & Discovery:**
```
"Find workforce AI funding in [your state]"
"Search for opportunities in manufacturing automation"
"Find pre-RFP opportunities I can position for"
"Check for new opportunities this week"
```

**Scoring & Evaluation:**
```
"Score this opportunity: [URL]"
"Evaluate this based on my business profile"
"Compare these 3 opportunities"
"What's the score breakdown for this?"
```

**Reports & Analysis:**
```
"Generate intelligence brief for top 5 opportunities"
"Create my weekly digest"
"Show all white-paper-ready opportunities"
"What trends are emerging in my industry?"
"Show opportunities matching my sweet spot"
```

**Configuration Help:**
```
"Help me update my configuration"
"What are my current settings?"
"How do I change my scoring weights?"
```

---

## 🎯 Quick Troubleshooting

### Problem: "Skill not found" or not triggering

**Solution:**
1. Check that skill is enabled in Settings → Capabilities → Skills
2. Try more specific command: "Use my Mandate Search Agent to find opportunities in [state]"
3. Check that CONFIG.md is in your ZIP file

### Problem: "Cannot read configuration"

**Solution:**
1. Check that file is named exactly `CONFIG.md` (case sensitive)
2. Check that it's in the root of the skill folder
3. Re-ZIP making sure folder structure is correct

### Problem: Getting irrelevant opportunities

**Solution:**
1. Review your keywords in CONFIG.md
2. Add more exclusion keywords
3. Adjust your minimum funding threshold
4. Be more specific in your search queries

### Problem: Scores don't make sense

**Solution:**
1. Review your scoring weights (must total 100)
2. Check examples in `scoring-examples.md`
3. Try: "Explain why this opportunity scored [XX]"

---

## 🔄 Updating Your Configuration

### To Update After Initial Setup:

1. **Edit CONFIG.md**
   - Make your changes
   - Save the file

2. **Re-ZIP the folder**
   - Include updated CONFIG.md
   - Keep same structure

3. **Re-upload to Claude**
   - Settings → Capabilities → Skills
   - Delete old version
   - Upload new ZIP
   - Enable the skill

4. **Test Changes**
   - Try a search to confirm new settings work

💡 **Tip:** Keep a backup of your CONFIG.md file outside the skill folder!

---

## 📚 Additional Resources

### For More Help:

- **CONFIG-TEMPLATE.md** - Comprehensive template with all options
- **REFERENCE.md** - Detailed workflow and best practices
- **scoring-examples.md** - 10 sample opportunities with scoring
- **SKILLS-SUMMARY.md** - Quick reference card
- **README.md** - Complete overview

### Example Searches by Industry:

**Manufacturing:**
```
"Find AI manufacturing workforce grants in [your state]"
"Search for Industry 4.0 training funding"
"Find automation workforce development opportunities"
```

**Healthcare:**
```
"Find healthcare workforce training grants in [your state]"
"Search for nursing shortage funding"
"Find behavioral health workforce opportunities"
```

**Economic Development:**
```
"Find economic development grants in [your region]"
"Search for entrepreneurship support funding"
"Find small business development opportunities"
```

**Nonprofit/Workforce:**
```
"Find workforce development grants for veterans in [your state]"
"Search for reentry program funding"
"Find youth career pathway opportunities"
```

---

## ✅ Setup Checklist

Before you're done, confirm:

- [ ] Downloaded all skill files
- [ ] Opened CONFIG-COMMUNITY-PRESET.md
- [ ] Replaced [YOUR_ORGANIZATION_NAME]
- [ ] Added YOUR states/regions
- [ ] Added YOUR industry keywords (5-10)
- [ ] Set YOUR funding minimum and sweet spot
- [ ] Adjusted scoring weights if needed (totals 100)
- [ ] Set YOUR organizational capacity
- [ ] Saved as CONFIG.md
- [ ] Created ZIP file with correct structure
- [ ] Uploaded to Claude
- [ ] Enabled the skill
- [ ] Tested with a search command
- [ ] Skill is working!

---

## 🎉 You're All Set!

**Your Mandate Search Agent is configured and ready to find funding opportunities customized to YOUR business!**

### Next Steps:

1. **Run your first real search** for opportunities in your area
2. **Review the results** and scoring
3. **Generate an intelligence brief** for a high-scoring opportunity
4. **Fine-tune your configuration** based on results
5. **Share with your team** or community members!

---

## 💬 Need Help?

**In Claude, try:**
- "Help me use my Mandate Search Agent"
- "Explain how scoring works"
- "What can I customize in my configuration?"
- "Show me example searches for [your industry]"

**Review Documentation:**
- `README.md` - Complete overview
- `SKILLS-SUMMARY.md` - Quick reference
- `CONFIG-TEMPLATE.md` - All configuration options

---

**Happy Funding Hunting! 🎯**

---

**Version:** 2.0.0
**Last Updated:** 2025-10-25
