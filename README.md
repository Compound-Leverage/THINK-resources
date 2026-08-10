# THINK School

Compound Leverage's training and educational resource hub, every training we produce is
THINK School, whether or not the person using it is a formal (paid) member. Free,
source-available, community-shareable skills and plugins.

New here and wondering what THINK School is? Learn more at
[skool.com/thinkschool/about](https://www.skool.com/thinkschool/about).

## Structure

This repo is an installable marketplace: add it directly in Claude Code, Codex CLI, or
ChatGPT to install any plugin as a full bundle, no manual file upload needed. See
[`Plugins/README.md`](Plugins/README.md) for install steps.

- `Skills/` — Reusable skills (THINK School modules, community tooling, open-source contributions)
- `Plugins/` : Bundled multi-role Claude Code plugins, each with its own `skills/` and `customization/*.json`
- `Agents/` : Standalone THINK Framework methodology agents, plus full downloadable persona folders (config, hooks, Skills, templates) for personas that also ship inside a `Plugins/` team
- `Prompts/` : One example-prompt file per plugin
- `Templates/` : One blank-deliverable file per DE persona
- `Workflows/` : One automation-setup file per DE persona (Claude scheduled routines and ChatGPT Scheduled Tasks)
- `Docs/` : Reference material about how this repo fits together (see `Docs/repo-map.md`)

## Skills Catalog

Persona skills are named `[role]-[persona]` (e.g. `proposal-writer-quinn.zip`) so you can tell what a DE does at a glance. Upload the `.zip` from `Skills/` in Claude.ai (Settings > Feature preview > Add skills) or Claude Desktop (Settings > Extensions > Add).

### Foundations

| Skill | Description | Install |
|-------|-------------|---------|
| THINK Foundations | 7-module curriculum — Thinking Crisis through your first DE | `Skills/think-foundations/SKILL.md` |

### Sales & BD

| Skill | DE | Description | Install |
|-------|----|-------------|---------|
| BD Execution | Sarah Grant | Lead scoring, HTML outreach, deal admin, OKR tracking | `Skills/bd-execution-sarah.zip` |
| BD Research | Alex Schultz | Signal detection, lead enrichment, ICP scoring | `Skills/bd-research-alex.zip` |
| Proposal Engine | Blair Enns | Capital and grant proposals for institutional funders | `Skills/pitch-development-blair.zip` |
| Contact Enrichment | Kipp | Hunter.io enrichment, CRM intake and classification | `Skills/crm-intake-kipp.zip` |
| Mandate Search Agent | — | Monitors and scores funding opportunities; surfaces pre-RFP signals | `Skills/mandate-mapping/SKILL.md` |
| Community Grant Radar | — | Scans for grant opportunities in your community and sector | `Skills/community-grant-radar/` |

### Intelligence & Research

| Skill | DE | Description | Install |
|-------|----|-------------|---------|
| Opportunity Mapper | Chet Holmes | Capital event scanning and funder intel | `Skills/cluster-discovery-chet.zip` |
| CE Brief Writer | Ben | Stratechery-style client intelligence briefs | `Skills/signal-delivery-ben.zip` |
| Proposal Researcher | Chase Holloway | Client and industry intelligence for proposals | `Skills/proposal-researcher-chase.zip` |
| Evidence Builder | Marcus Sheridan | Proof points, case studies, testimonial intake | `Skills/proof-points-marcus.zip` |
| Signal Finder Toolkit | — | 4-phase guided session to map active capital events in your sector | `Skills/Signal Finder Toolkit/SKILL.md` |

### Proposals

| Skill | DE | Description | Install |
|-------|----|-------------|---------|
| Proposal Engine Lead | Maya Ross | Orchestrates the full 6-DE proposal pipeline | `Skills/proposal-engine-lead-maya.zip` |
| Proposal Strategist | Porter Nash | Competitive positioning and win themes | `Skills/proposal-strategist-porter.zip` |
| Proposal Analyst | Priya Mehta | ROI models, deal classification, pricing | `Skills/proposal-analyst-priya.zip` |
| Proposal Writer | Quinn Mercer | Full proposal drafting across all sections | `Skills/proposal-writer-quinn.zip` |
| Proposal Reviewer | Diego Reyes | QA and compliance gate before delivery | `Skills/proposal-qa-diego.zip` |

### Content

| Skill | DE | Description | Install |
|-------|----|-------------|---------|
| LinkedIn Content | Justin | LinkedIn posts across personal, company, and product pages | `Skills/linkedin-content-justin.zip` |

### Operations

| Skill | DE | Description | Install |
|-------|----|-------------|---------|
| Playbook Agent | Lincoln | Customer success playbooks and onboarding frameworks | `Skills/playbooks-lincoln.zip` |

## DE Persona Roster

Every named persona across every `Plugins/` team, and where to find their prompt, blank
deliverable template, and automation setup. Personas with a standalone `Skills/` zip or a
full `Agents/` folder are noted -- everyone else is only available bundled inside their
plugin.

### Capture Team (`capture-team`)

| Persona | Role | Prompt | Template | Workflow | Also available as |
|---|---|---|---|---|---|
| Chet | Cluster Discovery | `Prompts/capture-team.md` | `Templates/cluster-discovery-chet.md` | `Workflows/cluster-discovery-chet.md` | `Skills/cluster-discovery-chet.zip`, `Agents/chet/` |
| Kipp | CRM Intake | `Prompts/capture-team.md` | `Templates/crm-intake-kipp.md` | `Workflows/crm-intake-kipp.md` | `Skills/crm-intake-kipp.zip` |
| Ben | Signal Delivery | `Prompts/capture-team.md` | `Templates/signal-delivery-ben.md` | `Workflows/signal-delivery-ben.md` | `Skills/signal-delivery-ben.zip` |

### Proposal Team (`proposal-team`)

| Persona | Role | Prompt | Template | Workflow | Also available as |
|---|---|---|---|---|---|
| Maya | Proposal Engine Lead (orchestrator) | `Prompts/proposal-team.md` | `Templates/proposal-engine-lead-maya.md` | `Workflows/proposal-engine-lead-maya.md` | `Skills/proposal-engine-lead-maya.zip` |
| Chase | Proposal Researcher | `Prompts/proposal-team.md` | `Templates/proposal-researcher-chase.md` | `Workflows/proposal-researcher-chase.md` | `Skills/proposal-researcher-chase.zip` |
| Priya | Proposal Analyst | `Prompts/proposal-team.md` | `Templates/proposal-analyst-priya.md` | `Workflows/proposal-analyst-priya.md` | `Skills/proposal-analyst-priya.zip` |
| Porter | Proposal Strategist | `Prompts/proposal-team.md` | `Templates/proposal-strategist-porter.md` | `Workflows/proposal-strategist-porter.md` | `Skills/proposal-strategist-porter.zip` |
| Quinn | Proposal Writer | `Prompts/proposal-team.md` | `Templates/proposal-writer-quinn.md` | `Workflows/proposal-writer-quinn.md` | `Skills/proposal-writer-quinn.zip` |
| Diego | Proposal QA | `Prompts/proposal-team.md` | `Templates/proposal-qa-diego.md` | `Workflows/proposal-qa-diego.md` | `Skills/proposal-qa-diego.zip` |
| Blair | Pitch Development (grant/funder track) | `Prompts/proposal-team.md` | `Templates/pitch-development-blair.md` | `Workflows/pitch-development-blair.md` | `Skills/pitch-development-blair.zip` |

### Content Team (`content-team`)

| Persona | Role | Prompt | Template | Workflow | Also available as |
|---|---|---|---|---|---|
| Rohit | Master Intel Scan | `Prompts/content-team.md` | `Templates/master-intel-scan-rohit.md` | `Workflows/master-intel-scan-rohit.md` | -- |
| Ann | Newsletter Editor | `Prompts/content-team.md` | `Templates/newsletter-editor-ann.md` | `Workflows/newsletter-editor-ann.md` | -- |
| Joanna | Blog Writer | `Prompts/content-team.md` | `Templates/blog-writer-joanna.md` | `Workflows/blog-writer-joanna.md` | -- |
| Justin | LinkedIn Content | `Prompts/content-team.md` | `Templates/linkedin-content-justin.md` | `Workflows/linkedin-content-justin.md` | `Skills/linkedin-content-justin.zip` |
| Amy | YouTube Scripts | `Prompts/content-team.md` | `Templates/youtube-scripts-amy.md` | `Workflows/youtube-scripts-amy.md` | -- |
| Josh | Intelligence Brief | `Prompts/content-team.md` | `Templates/brief-writer-josh.md` | `Workflows/brief-writer-josh.md` | -- |
| Jay | Theme Proposer | `Prompts/content-team.md` | `Templates/theme-proposer-jay.md` | `Workflows/theme-proposer-jay.md` | -- |
| Cal | Weekly Brief | `Prompts/content-team.md` | `Templates/weekly-brief-cal.md` | `Workflows/weekly-brief-cal.md` | -- |
| Sal | Course Builder | `Prompts/content-team.md` | `Templates/course-builder-sal.md` | `Workflows/course-builder-sal.md` | -- |

### Sales BD Team (`sales-bd-team`)

| Persona | Role | Prompt | Template | Workflow | Also available as |
|---|---|---|---|---|---|
| Lori | Prospect Scout | `Prompts/sales-bd-team.md` | `Templates/prospect-scout-lori.md` | `Workflows/prospect-scout-lori.md` | -- |
| Alex | BD Research | `Prompts/sales-bd-team.md` | `Templates/bd-research-alex.md` | `Workflows/bd-research-alex.md` | `Skills/bd-research-alex.zip` |
| Sarah | BD Execution | `Prompts/sales-bd-team.md` | `Templates/bd-execution-sarah.md` | `Workflows/bd-execution-sarah.md` | `Skills/bd-execution-sarah.zip` |

### Sales Enablement (`sales-enablement`)

| Persona | Role | Prompt | Template | Workflow | Also available as |
|---|---|---|---|---|---|
| Marcus | Proof Points | `Prompts/sales-enablement.md` | `Templates/proof-points-marcus.md` | `Workflows/proof-points-marcus.md` | `Skills/proof-points-marcus.zip` |

### Fulfillment (`fulfillment`)

| Persona | Role | Prompt | Template | Workflow | Also available as |
|---|---|---|---|---|---|
| Lincoln | Playbook Builder | `Prompts/fulfillment.md` | `Templates/playbooks-lincoln.md` | `Workflows/playbooks-lincoln.md` | `Skills/playbooks-lincoln.zip` |

### Ops Team (`ops-team`)

| Persona | Role | Prompt | Template | Workflow | Also available as |
|---|---|---|---|---|---|
| Jenny | Design Lead | `Prompts/ops-team.md` | `Templates/head-of-design-jenny.md` | `Workflows/head-of-design-jenny.md` | -- |
| Jason | QA Reviewer | `Prompts/ops-team.md` | `Templates/qa-reviewer-jason.md` | `Workflows/qa-reviewer-jason.md` | -- |
| Eric | Infra Lead | `Prompts/ops-team.md` | `Templates/infrastructure-eric.md` | `Workflows/infrastructure-eric.md` | -- |

### Standalone (no named persona)

| Plugin | Prompt | Template | Workflow |
|---|---|---|---|
| `lead-discovery` | `Prompts/lead-discovery.md` | `Templates/lead-discovery.md` | `Workflows/lead-discovery.md` |
| `proposal-generator` | `Prompts/proposal-generator.md` | `Templates/proposal-generator.md` | `Workflows/proposal-generator.md` |

## About Compound Leverage

**Compound Leverage** builds deployment infrastructure for institutional workforce funding. We specialize in:

- **THINK Intelligence Methodology** — Strategic assessment framework for identifying high-ROI business opportunities
- **Digital Employee (DE) Training** — Certifying strategic practitioners to deploy THINK methodology at scale
- **Institutional Funding Capture** — Enabling government agencies, state workforce boards, and foundations to deploy THINK across their networks

### Community Commitment

This repository contains community-shareable components that help organizations:
- Learn and apply THINK methodology
- Generate high-quality institutional proposals
- Identify and map funding opportunities
- Build strategic capability across teams

### License & Usage

All skills and plugins in this repository are free to use and modify for your own
organization's purposes under the [PolyForm Shield License 1.0.0](LICENSE) -- the one
restriction is that you can't use them to build or offer a competing product or service.
Everything else (internal use, client work, modification, redistribution within your own
org) is permitted. Attribution appreciated, not required.

Built or modified something useful with this? Share it in Wins in the [THINK School community](https://www.skool.com/thinkschool/about).

### Questions?

For skill documentation, usage examples, or contribution guidelines, see individual skill directories.

Already a THINK School member? Post any question in the [community](https://www.skool.com/thinkschool/about), or drop a win in Wins about how you're using these resources to get work done that wasn't getting done before.

For collaboration, partnerships, or institutional licensing, visit our [Partner page](https://www.compoundleverage.com/contact-sales/) (referral or infrastructure partner) or contact [partners@compoundleverage.com](mailto:partners@compoundleverage.com).