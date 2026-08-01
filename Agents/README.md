# Agents

This folder has two different shapes. Both are genericized, bring-your-own-data: no
proprietary Compound Leverage logic, no real database IDs or live infrastructure.

## 1. THINK Framework methodology agents

Standalone agents for the THINK Framework itself, not tied to a named persona or a
`Plugins/` team. Each is a `CLAUDE.md` (role, when to run, tools required, output) plus a
`Skills/` folder (`workflow.md`, `rules.md`, `schema.md`, `templates/`).

| Agent | What it does |
|---|---|
| [`think-execution/`](./think-execution/) | Converts a scored opportunity into a go-to-market plan and implementation roadmap |
| [`think-intelligence/`](./think-intelligence/) | Writes dated intelligence briefs and tracks capital event window timelines |
| [`think-signal/`](./think-signal/) | Client-facing signal feed tied to active clusters and funding windows |
| [`think-score/`](./think-score/) | Scores an org's readiness against a specific capital event, with gap analysis |

## 2. Full persona folders

A fuller, standalone, downloadable version of a persona that also ships bundled inside a
`Plugins/` team. Same rules and boundaries as the plugin version, just with the complete
`core/`, `hooks/`, `Skills/`, and `templates/` structure so it can run on its own, be
modified for your own use, or be pointed at directly by a scheduled routine (see the
"preferred pattern" note in any `Workflows/` file for what that means in practice).

| Persona | Also ships in | Folder |
|---|---|---|
| Chet | `Plugins/capture-team` | [`chet/`](./chet/) |
| Eric | `Plugins/ops-team` | [`eric/`](./eric/) |
| Jason | `Plugins/ops-team` | [`jason/`](./jason/) |
| Jenny | `Plugins/ops-team` | [`jenny/`](./jenny/) |
| Kipp | `Plugins/capture-team` | [`kipp/`](./kipp/) |

More persona folders get added here over time. If a persona you want isn't here yet, the
condensed version in their `Plugins/<team>/skills/<persona>/SKILL.md` still works on its
own.

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit [compoundleverage.com](https://compoundleverage.com).
