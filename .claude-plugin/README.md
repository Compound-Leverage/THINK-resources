# .claude-plugin/

This folder holds `marketplace.json` — the manifest Claude Code reads to list every
plugin in this repo (`Plugins/*`). You won't open this folder directly; you point
Claude Code at the repo and it reads this file for you. This README covers how, on
every surface where Claude Code plugins work.

Full plugin list and personas: [`../Plugins/README.md`](../Plugins/README.md).

## Claude Code (terminal CLI)

```
/plugin marketplace add Compound-Leverage/THINK-school
/plugin install <plugin-name>@think-school
/reload-plugins
```

Then turn off auto-update for this marketplace: run `/plugin`, open **Marketplaces**,
select `think-school`, and choose **Disable auto-update**. Every plugin here is meant
to be customized with your own data (`customization/*.json`), and an auto-update would
overwrite your changes.

## Claude Desktop app (Code tab)

Local and SSH sessions only — not available in cloud sessions or WSL sessions.

1. Open the **Code** tab
2. Click the **+** button next to the prompt box → **Plugins** → **Add plugin**
3. In the plugin browser, add `Compound-Leverage/THINK-school` as a marketplace and
   install the plugin you want

## Claude Code cloud sessions (claude.ai)

Cloud sessions don't have the interactive plugin browser. Declare the marketplace and
plugin directly in the repository's `.claude/settings.json` under
`extraKnownMarketplaces` and `enabledPlugins` — see
[Claude Code plugin settings](https://code.claude.com/docs/en/settings#plugin-settings)
for the exact fields. The plugin installs automatically at session start.

## Not using Claude Code?

This marketplace format only works inside Claude Code (CLI, the Desktop app's Code tab,
or cloud sessions) — not the regular Claude.ai chat. For Codex CLI or ChatGPT, see
[`../.agents/README.md`](../.agents/README.md). For Gemini, Perplexity, or installing
one persona's skill file at a time on any platform, see
[`../Skills/README.md`](../Skills/README.md).

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit
[compoundleverage.com](https://compoundleverage.com).
