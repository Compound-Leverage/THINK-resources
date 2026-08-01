# Plugins

Bundled multi-role Claude Code plugins. Each plugin is a team of DE personas, each
persona a `skills/<persona>/SKILL.md`, plus a `customization/` folder of bring-your-own
config files.

## Plugins in This Marketplace

| Plugin | Roles |
|---|---|
| `capture-team` | Chet (Cluster Discovery), Kipp (CRM Intake), Ben (Signal Delivery) |
| `proposal-team` | Maya (lead), Chase, Priya, Porter, Quinn, Diego, Blair |
| `content-team` | Rohit, Ann, Joanna, Justin, Amy, Josh, Jay, Cal, Sal |
| `sales-bd-team` | Lori (Prospect Scout), Alex (BD Research), Sarah (BD Execution) |
| `sales-enablement` | Marcus (Proof Points) |
| `fulfillment` | Lincoln (Playbook Builder) |
| `ops-team` | Jenny (Design Lead), Jason (QA Reviewer), Eric (Infra Lead) |
| `lead-discovery` | Single skill, no named persona |
| `proposal-generator` | Single skill, no named persona |

## Install Options

### Claude Code (CLI, Desktop app, or cloud sessions)

Full steps for every Claude Code surface: [`../.claude-plugin/README.md`](../.claude-plugin/README.md).

```
/plugin marketplace add Compound-Leverage/THINK-school
/plugin install <plugin-name>@think-school
```

Then turn off auto-update for this marketplace (`/plugin` → **Marketplaces** →
`think-school` → **Disable auto-update**) — every plugin here is meant to be customized
with your own `customization/*.json`, and an auto-update would overwrite your changes.

### Codex CLI or ChatGPT (the full plugin, all personas at once)

Full steps: [`../.agents/README.md`](../.agents/README.md).

Every plugin also ships a `.codex-plugin/plugin.json` alongside its
`.claude-plugin/plugin.json`, plus a root-level `.agents/plugins/marketplace.json`
listing all 9 plugins. This is OpenAI's own plugin format:

- **Codex CLI**: run `/plugins` to open the plugin browser, or
  `/plugin marketplace add Compound-Leverage/THINK-school` if it's not listed yet, then
  `/plugin install <plugin-name>@think-school`.
- **ChatGPT** (desktop app or web): with Codex selected, open the **Plugins** menu (web:
  switch to **Work** mode first) and install from the directory listing. No manual file
  upload needed — this pulls the full bundle, including every persona's `skills/`, the
  same way Claude Code does.

### Gemini or Perplexity (one persona at a time)

Gemini and Perplexity don't support the plugin/marketplace format above, so you'll
install one persona at a time instead. Every `skills/<persona>/SKILL.md` file is a
self-contained skill, installable the same way the standalone files in
[`Skills/`](../Skills/README.md) are:

- **Gemini**: upload the `SKILL.md` in a new conversation, then say "Run this skill."
  Gemini Advanced required.
- **Perplexity**: paste the full contents of `SKILL.md` directly into the message
  field, then add your own parameters below it. Best for the intelligence/research
  personas (Chet, Rohit) since Perplexity has live web search built in.

You can also install a single ChatGPT persona this same way instead of the full
plugin: upload the persona's `SKILL.md` to a project (Settings > Tasks, or a new
conversation), then say "Run this skill." ChatGPT Plus or higher required.

Installing one persona at a time loses the plugin's shared `customization/*.json`
(each persona reads it as a file, not a chat upload), so paste your own filled-in
config values into the conversation instead, or reference them inline in your prompt.

## Plugin Directory

What each plugin does, what to ask it, the personas inside it, and what external tools
it needs. Where a real, maintained MCP server exists for a connector, the plugin ships
a `.mcp.json` at its root so Claude Code and Codex CLI can connect it directly — marked
**(wired)** below. Connectors without a standard MCP server today are listed for
awareness only; configure those however you already do. None of these ship with live
credentials — API keys are read from an environment variable you set yourself, named in
each server's `env`/`headers` block in the plugin's `.mcp.json`.

### capture-team

Finds organizations and named groups worth pursuing, enriches and classifies inbound
leads against your ideal-customer profile, and turns raw market/funding signals into
client-ready intelligence briefs.

**Try asking...**
- "Load our capability map and check for new signals matching our unmapped capabilities — any hits that resolve to a real, bounded group?"
- "Pull the new leads in our intake queue, enrich each one, classify against our ICP, and create or update the CRM record."
- "Here's a CSV of prospects — run them through ICP classification and link decision-makers to the right pipeline deal."
- "Read the new, unactioned signals in our inbox and draft a client-ready intelligence brief for [client name]."

**Skills**: Chet — Cluster Discovery · Kipp — CRM Intake · Ben — Signal Delivery

**Connectors**: Notion (wired) — clusters, contacts, orgs, deals pipeline, signal inbox
· Hunter.io (wired) — enrichment, needs `HUNTER_API_KEY` · Google Drive (wired) — brief
delivery, via the community-maintained `server-gdrive` package (Anthropic's reference
server, no longer actively maintained — swap in your own if you'd rather not depend on
it)

### proposal-team

Runs a qualified opportunity through a full proposal pipeline — research, deal
assessment, competitive positioning, drafting, and QA — producing a submission-ready
proposal with your approval at each stage. Includes a separate track for grant/funder
proposals.

**Try asking...**
- "Run the full proposal pipeline for [prospect name] end to end and stop for my approval at each gate."
- "Research [prospect company] and give me a Discovery Brief with a Go/No-Go recommendation."
- "Build a conservative ROI model for [prospect] with break-even point and Year 1 ROI."
- "Run a standard QA pass on this proposal draft and give me a PASS/WARNING/FAIL verdict."

**Skills**: Maya — Proposal Engine Lead (orchestrator) · Chase — Proposal Researcher ·
Priya — Proposal Analyst · Porter — Proposal Strategist · Quinn — Proposal Writer ·
Diego — Proposal QA · Blair — Pitch Development (grant/funder track)

**Connectors**: None — runs entirely from your own filled-in configuration files
(company profile, pricing model, case studies, bid-sizing, brand guidelines); no
external accounts required.

### content-team

Scans your content signal sources weekly and turns the strongest findings into
newsletters, blog posts, LinkedIn posts, YouTube scripts, intelligence briefs, monthly
theme proposals, a weekly owner brief, and full courses.

**Try asking...**
- "Scan Reddit, industry news, YouTube, and Google's 'People Also Ask' for the strongest content signals this week and give me the top 5 scored topic cards."
- "Take this week's top-scoring topic and draft a WARM edition for engaged subscribers and a COLD edition for new subscribers."
- "Propose 3 genuinely distinct content themes for next month, each scored against our weighting."
- "Here's my course brief for [topic] — build the complete course, ready to paste into [course platform]."

**Skills**: Rohit — Intel Scanner · Ann — Newsletter Editor · Cal — Weekly Brief · Jay —
Theme Proposer · Joanna — Blog Writer · Josh — Intelligence Brief · Justin — LinkedIn
Content · Amy — YouTube Scripts · Sal — Course Builder

**Connectors**: Notion (wired) — content assets, theme proposals, signal inbox;
optional, falls back to local files · a newsletter platform (e.g. Beehiiv, ConvertKit) ·
Reddit, YouTube, news, and Google PAA as signal sources · GA4 or equivalent analytics —
no standard MCP server for these four yet, configure however you already do

### sales-bd-team

Sources people and organizations actively signaling demand for what you sell, enriches
and scores them against your ideal-customer profile, then drafts and sends outreach and
logs the resulting deal activity.

**Try asking...**
- "Scan our configured signal sources for people showing active demand signals matching our ICP, and give me the qualified leads with an intent score."
- "Here are the raw candidates from this week — enrich each with company and contact data and label them against our ICP profiles."
- "Score these enriched leads and draft an HTML outreach email for the top 5 using our differentiators."
- "Log the outreach activity from this batch into our CRM and apply our standard follow-up cadence."

**Skills**: Lori — Prospect Scout · Alex — BD Research · Sarah — BD Execution

**Connectors**: Notion (wired) — deals pipeline, contacts, orgs · Clay (wired) —
enrichment; requires the separate `clay` CLI installed and logged in (`clay login`)
first, the MCP server just wraps that session. This entry runs whatever `clay`
resolves to on your `PATH` — run `which clay` and confirm it points at your genuine
Clay install (e.g. under your package manager's bin directory) before first use, since
anything else earlier on your `PATH` named `clay` would run instead · an email send
account for outreach · public signal sources (forums, event registrations, newsletter
click data) — no standard MCP server for these two yet

### sales-enablement

Pulls completed client engagements and turns them into 1-page case study narratives
tagged by buyer type, keeping a ready supply of proof points on hand for proposal and
outreach work.

**Try asking...**
- "Pull our completed engagements from last quarter and extract 1-page case study narratives, tagged by buyer type."
- "Check our proof points inventory against our minimum threshold per tag and alert me if any tag is running low."
- "Only use completed, quantified outcomes for this one — label anything qualitative-only as such."

**Skills**: Marcus — Proof Points

**Connectors**: Notion (wired) — proof points database, engagement/fulfillment tracker
source

### fulfillment

Builds customized onboarding, customer-success, and expansion playbooks for a specific
active client, using your own base frameworks and that client's CRM record as inputs.

**Try asking...**
- "Using our onboarding playbook framework and [client]'s CRM record, build a customized onboarding playbook for them."
- "Build an expansion playbook for [client] based on their current engagement data. Mark any missing detail as a gap instead of inventing it."

**Skills**: Lincoln — Playbook Builder

**Connectors**: Notion (wired) — client records · Google Drive (wired) — playbook
delivery, via the community-maintained `server-gdrive` package (see the note under
capture-team above)

### ops-team

Keeps a website running well after every deploy — auditing SEO, copy, and broken links;
producing on-brand design assets and web specs; and managing the build pipeline, DNS,
and CI so you don't have to touch infrastructure directly.

**Try asking...**
- "Audit our latest deploy against our performance thresholds and caching rules, and open a PR to staging for any config-only fixes."
- "Run a post-deploy audit of our site — H1 consistency, SEO, copy terminology, and broken links — then open PRs for anything rule-based."
- "Here's the brief: I need a social graphic for [campaign name], sized for LinkedIn and Instagram, delivered to our Drive folder."
- "Check our GitHub Actions for failures or drift and tell me what needs my sign-off before it touches production."

**Skills**: Jenny — Design Lead · Jason — QA Reviewer · Eric — Infra Lead

**Connectors**: GitHub (wired) — Actions, PRs to staging; runs via Docker, needs
`GITHUB_PERSONAL_ACCESS_TOKEN` · Cloudflare (wired) — hosting/CDN, OAuth on first
connect · Canva (wired) — design assets, OAuth on first connect, per-user account ·
Google Drive (wired) — asset delivery, via the community-maintained `server-gdrive`
package (see the note under capture-team above)

**A note on scope**: this is the one plugin that pairs a write-capable connector
(GitHub, authenticated with your PAT) with three connectors that pull in content you
don't control (Cloudflare, Canva, Drive). Scope the PAT to the narrowest access that
works — a fine-grained token limited to this repo, not a classic PAT with broad org
access — and treat anything retrieved from the other three as untrusted input, not an
instruction. Content from a Drive file, a Canva comment, or Cloudflare-served copy
should never drive a GitHub write action without you reviewing it first.

### proposal-generator

A single all-in-one skill that runs one high-value deal through the full proposal
methodology — intake, research, assessment, positioning, drafting, and QA — end to end,
gated by your approval at each phase.

**Try asking...**
- "run proposal [Client Name] — here's their website, industry, due date, and how this opportunity came to us."
- "We're at the Research phase for [client] — here's what we know so far. Give me the Discovery Brief and your Go/No-Go recommendation."
- "Draft the full proposal for [client] using the commercial-style template, pulling from our pricing model, case studies, and brand guidelines."

**Skills**: Proposal Generator (single skill, no named persona)

**Connectors**: None — runs entirely from your own filled-in configuration files
(company profile, pricing model, case studies, brand guidelines); no external accounts
required.

### lead-discovery

Scans procurement, grant, and funding sources weekly and scores each opportunity across
five dimensions, surfacing a ranked shortlist of the deals worth pursuing and screening
out the rest.

**Try asking...**
- "Score this RFP against our 5-dimension model and tell me whether to pursue, delegate outreach, or monitor: [paste opportunity details]."
- "Here are 10 opportunities we pulled this week — qualify each one, drop anything scoring under 12 or hitting a disqualifier, and give me the ranked shortlist."
- "Evaluate this grant opportunity against our current capabilities and give me the full scoring breakdown plus a recommended next step."

**Skills**: Lead Discovery (single skill, no named persona)

**Connectors**: SAM.gov and state/local procurement portals · grants databases · county
business filings and lis pendens records · optionally Notion, Google Sheets, or an
email digest for delivery (your implementation choice, not built in)

## Where Everything Else Lives

Once you know which persona you want, the rest of that persona's material is indexed by
name, not by plugin, in these folders:

| What you want | Where |
|---|---|
| Example prompts | [`../Prompts/`](../Prompts/README.md) |
| Blank deliverable template | [`../Templates/`](../Templates/README.md) |
| Automation setup (Claude routine or ChatGPT Scheduled Tasks) | [`../Workflows/`](../Workflows/README.md) |
| Full standalone folder (config, hooks, Skills, templates) | [`../Agents/`](../Agents/README.md), for personas that have one |

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit [compoundleverage.com](https://compoundleverage.com).
