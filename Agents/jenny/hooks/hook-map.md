# Jenny -- Hook Map

Jenny has three on-demand modes (asset, web spec, deck spec) plus recurring audit
modes. This maps which trigger fires which skill -- for how to actually put the
recurring ones on a schedule (Claude scheduled routine or ChatGPT Scheduled Task),
see `Workflows/jenny-head-of-design.md`, which already documents Jenny's cadence as
part of the ops-team-open plugin. Don't duplicate that setup guidance here, this
file just tells you which skill each trigger should point at.

| When to run | Trigger | Fires |
|---|---|---|
| On demand | An asset brief comes in (type, context, dimensions, deadline) | `Skills/asset-production/` |
| On demand | A web page or component brief comes in | `Skills/web-spec-handoff/` -- output is a spec only, handed to whatever builds your site |
| On demand | A deck or presentation brief comes in | `Skills/deck-spec/` -- output is a slide-by-slide brief, handed to whatever builds the deck |
| Recurring, weekly or monthly, your choice | Scheduled routine | `Skills/brand-asset-audit/` -- sweep recently produced assets against your brand guidelines |
| Recurring, or triggered by a pending change to your site | Scheduled routine, or run against a pull request diff | `Skills/web-consistency-audit/` -- audit live pages or a diff against your style guide |
| On demand | A surface is being produced for the second time with no template yet, or you explicitly ask for one | `Skills/template-library/` |
| On demand | An audit or brief surfaces a gap in your design system itself | `Skills/style-guide-proposal/` -- always routes to you before anything commits |
| A finding doesn't fit any existing skill above | Automatic, during any audit | Flagged to you directly rather than forced into one of the above |

## Repo-container pattern

Same preferred pattern as the rest of this repo: if your filled-in config and brand
guidelines live in a GitHub repo (this one, your fork, or your own), point your
scheduled routine's source at that repo and keep the routine's stored prompt thin,
"read `Agents/jenny/CLAUDE.md` and today's relevant `Skills/` file in this repo, then
run the check." The routine re-clones fresh on every run, so editing this repo is
enough to change what the next run does. See `Workflows/jenny-head-of-design.md` for
the full explanation and the durability note about scheduled routines lapsing after
idle periods.
