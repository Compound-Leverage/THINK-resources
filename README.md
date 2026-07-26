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

Skills are organized by workstream. Upload the `.zip` from `Skills/[workstream]/` in Claude.ai (Settings > Feature preview > Add skills) or Claude Desktop (Settings > Extensions > Add).

### Foundations

| Skill | Description | Install |
|-------|-------------|---------|
| THINK Foundations | 7-module curriculum — Thinking Crisis through your first DE | `Skills/think-foundations/SKILL.md` |

### Sales & BD

| Skill | DE | Description | Install |
|-------|----|-------------|---------|
| BD Execution | Sarah Grant | Lead scoring, HTML outreach, deal admin, OKR tracking | `Skills/sales-bd/sarah-bd-execution.zip` |
| BD Research | Alex Schultz | Signal detection, lead enrichment, ICP scoring | `Skills/sales-bd/alex-bd-research.zip` |
| Proposal Engine | Blair Enns | Capital and grant proposals for institutional funders | `Skills/sales-bd/blair-pitch-development.zip` |
| Contact Enrichment | Kipp | Hunter.io enrichment, CRM intake and classification | `Skills/sales-bd/kipp-crm-intake.zip` |
| Mandate Search Agent | — | Monitors and scores funding opportunities; surfaces pre-RFP signals | `Skills/mandate-mapping/SKILL.md` |
| Community Grant Radar | — | Scans for grant opportunities in your community and sector | `Skills/community-grant-radar/` |

### Intelligence & Research

| Skill | DE | Description | Install |
|-------|----|-------------|---------|
| Opportunity Mapper | Chet Holmes | Capital event scanning and funder intel | `Skills/intelligence/chet-cluster-discovery.zip` |
| CE Brief Writer | Ben | Stratechery-style client intelligence briefs | `Skills/intelligence/ben-signal-delivery.zip` |
| Proposal Researcher | Chase Holloway | Client and industry intelligence for proposals | `Skills/intelligence/chase-proposal-researcher.zip` |
| Evidence Builder | Marcus Sheridan | Proof points, case studies, testimonial intake | `Skills/intelligence/marcus-proof-points.zip` |
| Signal Finder Toolkit | — | 4-phase guided session to map active capital events in your sector | `Skills/Signal Finder Toolkit/SKILL.md` |

### Proposals

| Skill | DE | Description | Install |
|-------|----|-------------|---------|
| Proposal Engine Lead | Maya Ross | Orchestrates the full 6-DE proposal pipeline | `Skills/proposals/maya-proposal-engine-lead.zip` |
| Proposal Strategist | Porter Nash | Competitive positioning and win themes | `Skills/proposals/porter-proposal-strategist.zip` |
| Proposal Analyst | Priya Mehta | ROI models, deal classification, pricing | `Skills/proposals/priya-proposal-analyst.zip` |
| Proposal Writer | Quinn Mercer | Full proposal drafting across all sections | `Skills/proposals/quinn-proposal-writer.zip` |
| Proposal Reviewer | Diego Reyes | QA and compliance gate before delivery | `Skills/proposals/diego-proposal-qa.zip` |

### Content

| Skill | DE | Description | Install |
|-------|----|-------------|---------|
| LinkedIn Content | Justin | LinkedIn posts across personal, company, and product pages | `Skills/content/justin-linkedin-content.zip` |

### Operations

| Skill | DE | Description | Install |
|-------|----|-------------|---------|
| Playbook Agent | Lincoln | Customer success playbooks and onboarding frameworks | `Skills/operations/lincoln-playbooks.zip` |

## DE Persona Roster

Every named persona across every `Plugins/` team, and where to find their prompt, blank
deliverable template, and automation setup. Personas with a standalone `Skills/` zip or a
full `Agents/` folder are noted -- everyone else is only available bundled inside their
plugin.

### Capture Team (`capture-team-open`)

| Persona | Role | Prompt | Template | Workflow | Also available as |
|---|---|---|---|---|---|
| Chet | Cluster Discovery | `Prompts/capture-team-open.md` | `Templates/chet-cluster-discovery.md` | `Workflows/chet-cluster-discovery.md` | `Skills/intelligence/chet-cluster-discovery.zip`, `Agents/chet/` |
| Kipp | CRM Intake | `Prompts/capture-team-open.md` | `Templates/kipp-crm-intake.md` | `Workflows/kipp-crm-intake.md` | `Skills/sales-bd/kipp-crm-intake.zip` |
| Ben | Signal Delivery | `Prompts/capture-team-open.md` | `Templates/ben-signal-delivery.md` | `Workflows/ben-signal-delivery.md` | `Skills/intelligence/ben-signal-delivery.zip` |

### Proposal Team (`proposal-team-open`)

| Persona | Role | Prompt | Template | Workflow | Also available as |
|---|---|---|---|---|---|
| Maya | Proposal Engine Lead (orchestrator) | `Prompts/proposal-team-open.md` | `Templates/maya-proposal-engine-lead.md` | `Workflows/maya-proposal-engine-lead.md` | `Skills/proposals/maya-proposal-engine-lead.zip` |
| Chase | Proposal Researcher | `Prompts/proposal-team-open.md` | `Templates/chase-proposal-researcher.md` | `Workflows/chase-proposal-researcher.md` | `Skills/intelligence/chase-proposal-researcher.zip` |
| Priya | Proposal Analyst | `Prompts/proposal-team-open.md` | `Templates/priya-proposal-analyst.md` | `Workflows/priya-proposal-analyst.md` | `Skills/proposals/priya-proposal-analyst.zip` |
| Porter | Proposal Strategist | `Prompts/proposal-team-open.md` | `Templates/porter-proposal-strategist.md` | `Workflows/porter-proposal-strategist.md` | `Skills/proposals/porter-proposal-strategist.zip` |
| Quinn | Proposal Writer | `Prompts/proposal-team-open.md` | `Templates/quinn-proposal-writer.md` | `Workflows/quinn-proposal-writer.md` | `Skills/proposals/quinn-proposal-writer.zip` |
| Diego | Proposal QA | `Prompts/proposal-team-open.md` | `Templates/diego-proposal-qa.md` | `Workflows/diego-proposal-qa.md` | `Skills/proposals/diego-proposal-qa.zip` |
| Blair | Pitch Development (grant/funder track) | `Prompts/proposal-team-open.md` | `Templates/blair-pitch-development.md` | `Workflows/blair-pitch-development.md` | `Skills/sales-bd/blair-pitch-development.zip` |

### Content Team (`content-team-open`)

| Persona | Role | Prompt | Template | Workflow | Also available as |
|---|---|---|---|---|---|
| Rohit | Master Intel Scan | `Prompts/content-team-open.md` | `Templates/rohit-master-intel-scan.md` | `Workflows/rohit-master-intel-scan.md` | -- |
| Ann | Newsletter Editor | `Prompts/content-team-open.md` | `Templates/ann-newsletter-editor.md` | `Workflows/ann-newsletter-editor.md` | -- |
| Joanna | Blog Writer | `Prompts/content-team-open.md` | `Templates/joanna-blog-writer.md` | `Workflows/joanna-blog-writer.md` | -- |
| Justin | LinkedIn Content | `Prompts/content-team-open.md` | `Templates/justin-linkedin-content.md` | `Workflows/justin-linkedin-content.md` | `Skills/content/justin-linkedin-content.zip` |
| Amy | YouTube Scripts | `Prompts/content-team-open.md` | `Templates/amy-youtube-scripts.md` | `Workflows/amy-youtube-scripts.md` | -- |
| Josh | Intelligence Brief | `Prompts/content-team-open.md` | `Templates/josh-brief-writer.md` | `Workflows/josh-brief-writer.md` | -- |
| Jay | Theme Proposer | `Prompts/content-team-open.md` | `Templates/jay-theme-proposer.md` | `Workflows/jay-theme-proposer.md` | -- |
| Cal | Weekly Brief | `Prompts/content-team-open.md` | `Templates/cal-weekly-brief.md` | `Workflows/cal-weekly-brief.md` | -- |
| Sal | Course Builder | `Prompts/content-team-open.md` | `Templates/sal-course-builder.md` | `Workflows/sal-course-builder.md` | -- |

### Sales BD Team (`sales-bd-team-open`)

| Persona | Role | Prompt | Template | Workflow | Also available as |
|---|---|---|---|---|---|
| Lori | Prospect Scout | `Prompts/sales-bd-team-open.md` | `Templates/lori-prospect-scout.md` | `Workflows/lori-prospect-scout.md` | -- |
| Alex | BD Research | `Prompts/sales-bd-team-open.md` | `Templates/alex-bd-research.md` | `Workflows/alex-bd-research.md` | `Skills/sales-bd/alex-bd-research.zip` |
| Sarah | BD Execution | `Prompts/sales-bd-team-open.md` | `Templates/sarah-bd-execution.md` | `Workflows/sarah-bd-execution.md` | `Skills/sales-bd/sarah-bd-execution.zip` |

### Sales Enablement (`sales-enablement-open`)

| Persona | Role | Prompt | Template | Workflow | Also available as |
|---|---|---|---|---|---|
| Marcus | Proof Points | `Prompts/sales-enablement-open.md` | `Templates/marcus-proof-points.md` | `Workflows/marcus-proof-points.md` | `Skills/intelligence/marcus-proof-points.zip` |

### Fulfillment (`fulfillment-open`)

| Persona | Role | Prompt | Template | Workflow | Also available as |
|---|---|---|---|---|---|
| Lincoln | Playbook Builder | `Prompts/fulfillment-open.md` | `Templates/lincoln-playbooks.md` | `Workflows/lincoln-playbooks.md` | `Skills/operations/lincoln-playbooks.zip` |

### Ops Team (`ops-team-open`)

| Persona | Role | Prompt | Template | Workflow | Also available as |
|---|---|---|---|---|---|
| Jenny | Design Lead | `Prompts/ops-team-open.md` | `Templates/jenny-head-of-design.md` | `Workflows/jenny-head-of-design.md` | -- |
| Jason | QA Reviewer | `Prompts/ops-team-open.md` | `Templates/jason-qa-reviewer.md` | `Workflows/jason-qa-reviewer.md` | -- |
| Eric | Infra Lead | `Prompts/ops-team-open.md` | `Templates/eric-infrastructure.md` | `Workflows/eric-infrastructure.md` | -- |

### Standalone (no named persona)

| Plugin | Prompt | Template | Workflow |
|---|---|---|---|
| `lead-discovery` | `Prompts/lead-discovery.md` | `Templates/lead-discovery.md` | `Workflows/lead-discovery.md` |
| `proposal-generator-open` | `Prompts/proposal-generator-open.md` | `Templates/proposal-generator-open.md` | `Workflows/proposal-generator-open.md` |

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