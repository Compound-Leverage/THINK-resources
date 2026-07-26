# Repo Map: What's Where

This repo has grown past "Skills and Plugins." Here's what each top-level folder is for
and when to reach for it.

| Folder | What it is | Start here when... |
|---|---|---|
| `Skills/` | Single `SKILL.md` modules, install one at a time in Claude, ChatGPT, Gemini, or Perplexity | You want one specific capability (a scanner, a scorer, a toolkit) without a full plugin |
| `Plugins/` | Bundled multi-role Claude Code plugins, each with its own `skills/`, `customization/*.json` | You want a full team of personas (Capture Team, Proposal Team, etc.) working together |
| `Agents/` | Standalone THINK Framework agents (think-execution, think-intelligence, think-signal, think-score) with their own `Skills/` (`workflow.md`, `rules.md`, `schema.md`) | You want the methodology layer itself, not a named persona team |
| `Prompts/` | One example-prompt file per plugin | You've installed a plugin and want a starting prompt for each persona in it |
| `Templates/` | One blank-deliverable file per plugin | You want the output format a persona produces, without running the plugin at all |
| `Workflows/` | One automation-setup file per plugin | You want to put a plugin's personas on a schedule (Claude scheduled routine or ChatGPT Scheduled Tasks) instead of running them by hand |
| `Docs/` | Reference material about the repo itself | You want to understand how the pieces fit together (this file) or the full private architecture |

**Agents/ has two shapes.** Most of the folder is the standalone THINK Framework layer
described above (methodology, not a named persona). A persona folder like `Agents/chet/`
is a different shape: a fuller, downloadable version of a persona that also ships as
part of a `Plugins/` team (see `Plugins/capture-team-open`). Same rules and boundaries as
the plugin version -- just with the full `core/`, `hooks/`, `Skills/`, and `templates/`
structure so it can run standalone, be modified for your own use, or be pointed at
directly by a scheduled routine.

## The pattern across Prompts / Templates / Workflows

These three folders are all indexed the same way: one file per plugin, named after the
plugin (e.g. `capture-team-open.md` appears in all three). Once you've installed a
plugin:

1. Read its `Prompts/<plugin>.md` for example prompts per persona
2. Read its `Templates/<plugin>.md` for the blank output format per persona
3. Read its `Workflows/<plugin>.md` if you want it running on a schedule instead of by hand

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit [compoundleverage.com](https://compoundleverage.com).
