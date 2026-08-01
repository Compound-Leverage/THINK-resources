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

Full descriptions live in [`.claude-plugin/marketplace.json`](../.claude-plugin/marketplace.json) at the repo root.

## Install Options

### Claude Code (the full plugin, all personas at once)

Add this repo as a marketplace with **"Sync automatically" turned OFF** (plugins here
are meant to be customized with your own `customization/*.json`, and sync would
overwrite your changes), then install the plugin you want.

### Codex CLI or ChatGPT (the full plugin, all personas at once)

Every plugin also ships a `.codex-plugin/plugin.json` alongside its `.claude-plugin/plugin.json`,
plus a root-level `.agents/plugins/marketplace.json` listing all 9 plugins. This is
OpenAI's own plugin format, and it installs the same way in both places:

- **Codex CLI**: run `/plugins` to open the plugin browser, find this marketplace, and
  install the plugin you want.
- **ChatGPT** (desktop app or web): open the plugin browser the same way, find this
  marketplace, and install the plugin you want. No manual file upload needed, this
  pulls the full bundle, including every persona's `skills/`, the same way Claude Code
  does.

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
