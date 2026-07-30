# .agents/

This folder holds `plugins/marketplace.json` — OpenAI's plugin marketplace manifest,
the Codex/ChatGPT equivalent of the root [`.claude-plugin/`](../.claude-plugin/) folder.
It lists the same 9 plugins as the Claude Code marketplace, each pointing at its
`.codex-plugin/plugin.json` inside `Plugins/<name>/`.

Full plugin list and personas: [`../Plugins/README.md`](../Plugins/README.md).

## Codex CLI

```
codex
/plugins
```

This opens the plugin browser (marketplace tabs, plugin details, one-key install). If
`Compound-Leverage/THINK-school` isn't already listed as a marketplace source, add it
first:

```
/plugin marketplace add Compound-Leverage/THINK-school
/plugin install <plugin-name>@think-school
```

Start a new Codex session after installing to pick up the plugin's skills.

## ChatGPT (desktop app or web)

- **Desktop app**: with **Codex** selected, open the **Plugins** menu, click the **+**
  button, and install from the directory listing.
- **Web app**: switch to **Work** mode, open **Plugins**, and install the same way.

Some plugins prompt you to authenticate during install; others wait until first use.
No manual file upload needed — this pulls the full bundle, including every persona's
`skills/`, the same way Claude Code does.

## Not using Codex or ChatGPT?

For Claude Code (CLI, Desktop app, or cloud sessions), see
[`../.claude-plugin/README.md`](../.claude-plugin/README.md). For Gemini, Perplexity,
or installing one persona's skill file at a time on any platform, see
[`../Skills/README.md`](../Skills/README.md).

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit
[compoundleverage.com](https://compoundleverage.com).
