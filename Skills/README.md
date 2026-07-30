# Compound Leverage — DE Skills Library

Skills built internally to run specific Digital Employee functions. Free to use.

Each skill is a SKILL.md file you install in your AI platform of choice. Under 10 minutes to deploy.

---

## Platform Guide

Different platforms have different strengths. Match the skill type to the platform.

| Skill Type | Best Platform | Why |
|------------|---------------|-----|
| Signal scanning, research, radar | Perplexity | Live web search built in. Returns current data without extra prompting. |
| Outreach, writing, BD | Claude or ChatGPT | Strong instruction-following and tone consistency for high-stakes copy. |
| Workflow, structured output | Claude or Gemini | Handles multi-step logic and long context well. |
| General / all-purpose | Any of the four | All platforms can run any skill. Platform guidance above is for best results. |

---

## Install in Claude

1. Open [Claude.ai](https://claude.ai) and start a new conversation
2. Click the paperclip icon and upload `SKILL.md` from the skill folder
3. Type: `Run this skill` and press send
4. Follow the prompts

**Claude Pro or higher required** for file uploads and extended context.

---

## Install in ChatGPT

1. Open [ChatGPT](https://chatgpt.com) and start a new conversation
2. Click the paperclip icon and upload `SKILL.md`
3. If the skill includes scripts (e.g. `scripts/score_event.py`), upload those as well
4. Type: `Run this skill` and press send

**ChatGPT Plus or higher required** for file uploads.

---

## Install in Gemini

1. Open [Gemini](https://gemini.google.com) and start a new conversation
2. Click the file upload icon and upload `SKILL.md`
3. Type: `Run this skill` and press send

**Gemini Advanced required** for file uploads and extended context.

---

## Install in Perplexity

Best for skills that involve scanning, research, or signal detection. Perplexity has live web search built in, so research skills return current data automatically.

1. Open [Perplexity](https://perplexity.ai) and start a new thread
2. Paste the full contents of `SKILL.md` directly into the message field
3. Add your parameters below the pasted content (sector, region, goal, etc.)
4. Press send

**Perplexity Pro recommended** for longer skill files and file upload support.

---

## Skills in This Library

### Tool Skills

| Skill | Function | Best Platform |
|-------|----------|---------------|
| Signal Finder Toolkit | Scans active grants, contracts, and pre-RFP signals in your sector | Perplexity, Claude |
| Community Grant Radar | Surfaces community-level funding open in your region | Perplexity |
| Mandate Mapping | Maps funding sources to your organization's eligibility | Claude, ChatGPT |

### Persona Skills (Digital Employees)

Named `[role]-[persona]` so you can tell what the DE does at a glance. Each one is also
listed with its full team in the root [README.md](../README.md) DE Persona Roster.

| DE (role) | Persona | What it does | File |
|-----------|---------|---------------|------|
| BD Execution | Sarah | Lead scoring, HTML outreach, deal admin, OKR tracking | `bd-execution-sarah.zip` |
| BD Research | Alex | Signal detection, lead enrichment, ICP scoring | `bd-research-alex.zip` |
| Pitch Development | Blair | Capital and grant proposals for institutional funders | `pitch-development-blair.zip` |
| CRM Intake | Kipp | Hunter.io enrichment, CRM intake and classification | `crm-intake-kipp.zip` |
| Cluster Discovery | Chet | Capital event scanning and funder intel | `cluster-discovery-chet.zip` |
| Signal Delivery | Ben | Stratechery-style client intelligence briefs | `signal-delivery-ben.zip` |
| Proposal Researcher | Chase | Client and industry intelligence for proposals | `proposal-researcher-chase.zip` |
| Proof Points | Marcus | Proof points, case studies, testimonial intake | `proof-points-marcus.zip` |
| Proposal Engine Lead | Maya | Orchestrates the full 6-DE proposal pipeline | `proposal-engine-lead-maya.zip` |
| Proposal Strategist | Porter | Competitive positioning and win themes | `proposal-strategist-porter.zip` |
| Proposal Analyst | Priya | ROI models, deal classification, pricing | `proposal-analyst-priya.zip` |
| Proposal Writer | Quinn | Full proposal drafting across all sections | `proposal-writer-quinn.zip` |
| Proposal QA | Diego | QA and compliance gate before delivery | `proposal-qa-diego.zip` |
| LinkedIn Content | Justin | LinkedIn posts from your real stories | `linkedin-content-justin.zip` |
| Playbook Builder | Lincoln | Customer success playbooks and onboarding frameworks | `playbooks-lincoln.zip` |

More skills added as Compound Leverage builds and deploys new Digital Employee functions internally.

---

## Questions

Contact [marvin@compoundleverage.co](mailto:marvin@compoundleverage.co) or visit [compoundleverage.com](https://compoundleverage.com).
