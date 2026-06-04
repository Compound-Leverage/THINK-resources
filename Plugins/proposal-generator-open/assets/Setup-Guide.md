# Proposal Generator Skill - Setup Guide

## Welcome

This guide walks you through setting up the Proposal Generator skill on your preferred AI platform. The skill works with Claude Desktop, ChatGPT Projects, Google Gemini Gems, and Microsoft Copilot.

**Time to Setup:** 15-30 minutes
**Prerequisites:** Active subscription to your chosen AI platform

---

## Quick Start Checklist

Before you begin, gather this information about YOUR company:

- [ ] Company name, website, and elevator pitch
- [ ] Team members who will appear in proposals (names, titles, bios)
- [ ] Your pricing structure (hourly rates, packages, or project ranges)
- [ ] 2-3 case studies or past performance examples
- [ ] Brand voice guidelines (tone, terminology preferences)
- [ ] Any certifications or awards to highlight

---

## Step 1: Complete Your Customization Files

The skill includes four customization files in the `/customization` folder. **You MUST complete these before the skill will generate personalized proposals.**

### 1.1 my-company-profile.json

Open this file and replace all `[PLACEHOLDER]` values with your company information:

| Section | What to Add |
|---------|-------------|
| `company_info` | Name, website, tagline, founding year |
| `positioning` | How you describe what you do |
| `team` | Key team members with bios |
| `certifications` | Relevant certifications and credentials |
| `service_areas` | Industries and problem types you serve |

**Tip:** Be specific. Generic descriptions generate generic proposals.

### 1.2 my-pricing-model.json

Configure your pricing structure:

| Section | What to Add |
|---------|-------------|
| `rate_card` | Hourly/daily rates by role |
| `packages` | Pre-defined offering packages |
| `pricing_rules` | Discounts, minimums, success fees |

**Tip:** Include ranges if your pricing varies by client size or complexity.

### 1.3 my-case-studies.json

Add your past performance:

| Section | What to Add |
|---------|-------------|
| `case_studies` | Project name, client, challenge, solution, outcomes |
| `reference_contacts` | Clients who can serve as references |
| `awards_recognition` | Relevant awards and recognition |

**Tip:** Quantify outcomes wherever possible (%, $, time saved).

### 1.4 my-brand-guidelines.md

Define your brand voice:

| Section | What to Add |
|---------|-------------|
| Voice characteristics | Professional? Casual? Authoritative? |
| Terminology | Words to use and avoid |
| Visual standards | Colors, fonts for digital proposals |
| Legal disclaimers | Required compliance language |

---

## Step 2: Platform-Specific Setup

Choose your platform and follow the instructions below.

---

### Option A: Claude Desktop (Recommended)

Claude Desktop provides the best experience with full file access and tool use.

**Setup Steps:**

1. **Open Claude Desktop** and go to Settings → Features

2. **Enable Projects** if not already enabled

3. **Create a New Project:**
   - Click "New Project"
   - Name it "Proposal Generator"
   - Add a description: "Generate winning proposals using structured methodology"

4. **Add Project Knowledge:**
   - Click "Add Content" → "Files"
   - Upload the entire `proposal-generator-skill` folder
   - Or upload these files individually:
     - `SKILL.md`
     - All files from `references/` folder
     - All files from `customization/` folder (your completed versions)

5. **Set Project Instructions:**
   - In Project Settings, add custom instructions:
   ```
   You are a proposal generation assistant. Follow the methodology in SKILL.md exactly.
   Always complete each phase before proceeding. Use my company data from the
   customization files for all proposals.
   ```

6. **Test the Setup:**
   - Type: `run proposal Test Company`
   - Verify it asks the 8 discovery questions from SKILL.md

**File Access:** Claude Desktop can read/write files directly, enabling automated document generation.

---

### Option B: ChatGPT Projects (GPT-4)

ChatGPT Projects work well for conversation-based proposal development.

**Setup Steps:**

1. **Open ChatGPT** and click "Explore GPTs" → "Create"

2. **Configure Your GPT:**

   **Name:** Proposal Generator

   **Description:** Generate winning proposals using structured 7-phase methodology

   **Instructions:** Copy the entire contents of `SKILL.md` into the Instructions field

3. **Upload Knowledge Files:**
   - Click "Upload files"
   - Upload all files from:
     - `references/frameworks/` (3 files)
     - `references/templates/` (4 files)
     - `references/prompts/` (4 files)
     - `customization/` (4 files - your completed versions)

4. **Configure Capabilities:**
   - Enable: Web Browsing (for research phase)
   - Enable: Code Interpreter (for ROI calculations)
   - Enable: DALL-E (optional, for proposal graphics)

5. **Save and Test:**
   - Click "Save" → "Only me" or "Anyone with link"
   - Test: `run proposal Test Company`

**Limitations:** ChatGPT cannot directly create .docx files. It will generate markdown that you copy to Word.

---

### Option C: Google Gemini Gems

Gemini Gems provide good integration with Google Workspace.

**Setup Steps:**

1. **Open Google AI Studio** (aistudio.google.com) or Gemini Advanced

2. **Create a New Gem:**
   - Click "Create Gem"
   - Name: "Proposal Generator"

3. **Add System Instructions:**
   - Copy the entire contents of `SKILL.md` into the system instructions

4. **Upload Context Files:**
   - Add all reference files as context documents
   - Add your completed customization files

   **Note:** Gemini has context limits. Prioritize:
   1. SKILL.md (required)
   2. Your 4 customization files (required)
   3. Templates matching your most common deal types
   4. Framework files

5. **Configure Settings:**
   - Temperature: 0.7 (balanced creativity/consistency)
   - Enable Google Search for research phase

6. **Test the Setup:**
   - Open your Gem
   - Type: `run proposal Test Company`

**Integration Tip:** Gemini works well with Google Docs for collaborative proposal editing.

---

### Option D: Microsoft Copilot

Copilot integrates with Microsoft 365 for direct document creation.

**Setup Steps:**

1. **Open Microsoft Copilot** (copilot.microsoft.com) or Copilot in Edge

2. **Create a Custom Copilot (Business/Enterprise):**
   - Go to Copilot Studio
   - Create new Copilot
   - Name: "Proposal Generator"

3. **Add Knowledge Sources:**
   - Upload reference files to SharePoint
   - Connect SharePoint folder as knowledge source
   - Upload your customization files

4. **Configure System Prompt:**
   - Add SKILL.md content as system message
   - Set conversation style to "More Precise"

5. **Enable Plugins:**
   - Web Search (for research)
   - Microsoft 365 (for document creation)

6. **For Personal Use (Copilot Free/Pro):**
   - Use Copilot in Edge with Notebook mode
   - Paste SKILL.md as initial context
   - Reference your customization data in conversations

**Integration Tip:** Copilot can create Word/PowerPoint files directly when connected to Microsoft 365.

---

## Step 3: Verify Your Setup

Run this test on any platform to verify correct setup:

### Test Prompt:
```
run proposal Acme Corporation

Here's what I know:
- Website: acme.com
- Industry: Manufacturing
- Due date: 2 weeks from today
- Source: Referral from existing client
- Focus: Process automation
- Budget signals: $50K-$75K range
```

### Expected Behavior:

1. **System asks any missing discovery questions** from the 8 required
2. **System acknowledges intake** and creates intake summary
3. **System asks for Go/No-Go confirmation** before proceeding
4. **Research phase produces Discovery Brief** with findings

If this happens, your setup is working correctly.

### Troubleshooting:

| Issue | Solution |
|-------|----------|
| System doesn't follow phases | Re-check that SKILL.md is loaded as primary instruction |
| Generic company info in output | Verify customization files are uploaded and completed |
| Missing methodology references | Ensure framework files are uploaded |
| Skips discovery questions | Add instruction: "Always complete intake before proceeding" |

---

## Step 4: Your First Real Proposal

Once verified, you're ready to generate proposals:

1. **Gather opportunity information** - client name, website, how you heard about them, budget signals

2. **Start the intake:** `run proposal [Client Name]`

3. **Answer all discovery questions** - the more detail, the better the output

4. **Progress through phases** - use `approved` or `proceed` to advance

5. **Review at each gate** - the methodology enforces human checkpoints

6. **Export final document** - copy to Word/Docs or use platform export

---

## Tips for Best Results

### Give Rich Inputs
- Include meeting notes, email threads, RFP documents
- The more context, the more tailored the proposal

### Use the Gates
- Don't skip phases - they exist to prevent wasted effort
- The Go/No-Go decision saves time on bad-fit opportunities

### Customize Templates
- Edit templates in `references/templates/` for your specific needs
- Add industry-specific sections as needed

### Keep Customization Current
- Update case studies after each win
- Refresh pricing quarterly
- Review brand guidelines annually

---

## Support and Updates

### Getting Help
- Review SKILL.md for workflow questions
- Check `/references/prompts/` for phase-specific guidance
- Methodology questions → refer to `/references/frameworks/methodology.md`

### Updating the Skill
- Replace reference files to update templates
- Add new case studies to expand past performance
- Adjust pricing model as your business evolves

---

## Platform Comparison

| Feature | Claude Desktop | ChatGPT | Gemini | Copilot |
|---------|---------------|---------|--------|---------|
| File creation | ✅ Direct | ❌ Copy/paste | ⚠️ Limited | ✅ With M365 |
| Web research | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| Context window | ✅ Large | ✅ Large | ⚠️ Moderate | ⚠️ Moderate |
| Conversation memory | ✅ Projects | ✅ Projects | ⚠️ Session | ⚠️ Session |
| Best for | Full workflow | Collaborative | Google users | M365 users |

---

**You're Ready!**

Your Proposal Generator skill is now configured. Start winning more deals with consistent, methodology-driven proposals.

*Built on the THINK methodology*
