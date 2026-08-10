# Kipp -- Hook Map

Kipp has one recurring workflow with three trigger sources feeding it, plus an
on-demand mode. This maps which trigger fires which skill -- for how to actually put
this on a schedule (Claude scheduled routine or ChatGPT Scheduled Task), see
`Workflows/crm-intake-kipp.md`, which already documents Kipp's cadence as part of
the Capture Team plugin. Don't duplicate that setup guidance here; this file just
tells you which skill each trigger should point at.

| When to run | Trigger | Fires |
|---|---|---|
| Daily, once | Scheduled routine (see `Workflows/crm-intake-kipp.md`) | `Skills/crm-intake/` -- sweep every configured intake source (signal inbox, scored prospect list, warm inbound), enrich, classify, write to CRM |
| Weekly, same run or a following one | Scheduled routine | `Skills/crm-intake/`'s audit step -- flag any pipeline record still missing a decision-maker contact or ICP tag past your `audit.stalled_after_days` |
| On demand | You have a single lead or a short list and don't want to wait for the next sweep | `Skills/crm-intake/`, scoped to just that record or list |
| On demand | Explicit ask: "Kipp, run intake," "process this lead," "sweep the queue" | `Skills/crm-intake/` |

## Repo-container pattern

Same preferred pattern as the rest of this repo: if your filled-in config lives in a
GitHub repo (this one, your fork, or your own), point your scheduled routine's source
at that repo and keep the routine's stored prompt thin -- "read `Agents/kipp/CLAUDE.md`
and `Skills/crm-intake/` in this repo, then run today's sweep." The routine re-clones
fresh on every run, so editing this repo is enough to change what the next run does.
See `Workflows/crm-intake-kipp.md` for the full explanation and the durability note
about scheduled routines lapsing after idle periods.
