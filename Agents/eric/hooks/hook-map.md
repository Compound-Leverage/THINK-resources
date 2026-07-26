# Eric -- Hook Map

Eric has a handful of recurring workflows plus several on-demand modes. This maps which
trigger fires which skill -- for how to actually put these on a schedule (Claude
scheduled routine or ChatGPT Scheduled Task), see `Workflows/eric-infrastructure.md`,
which already documents Eric's cadence as part of the ops-team-open plugin. Don't
duplicate that setup guidance here; this file just tells you which skill each trigger
should point at, including the skills this fuller folder adds beyond the plugin version.

| When to run | Trigger | Fires |
|---|---|---|
| After every deploy (staging and production) | Deploy event, or a scheduled routine right after one | `Skills/deploy-check/` -- validate the deploy, catch failed builds and broken previews |
| Weekly | Scheduled routine | `Skills/performance-audit/` -- Core Web Vitals and Lighthouse pass against your priority pages |
| Monthly | Scheduled routine | `Skills/cdn-dns-audit/` and `Skills/github-actions-audit/` -- config drift, deprecated actions, orphaned edge functions, DNS state |
| Nightly, before scheduled workflows fire (if you run any) | Scheduled routine | `Skills/preflight-check/` -- validate workflow YAML, confirm secrets and model-provider keys are live, fix what's mechanical, flag what isn't |
| On demand | Explicit ask: "Eric, check the last deploy," "audit our GitHub Actions," "run a build check" | Whichever skill matches the ask |
| On demand | "Is this worth its own repo?" | `Skills/repo-governance.md` |
| On demand or monthly, once you're running more than a couple of scheduled agents/automations | Scheduled routine or explicit ask | `Skills/automation-ops-audit/` -- notification load and approval-gate review across your own automation fleet |

## Repo-container pattern

Same preferred pattern as the rest of this repo: if your filled-in config lives in a
GitHub repo (this one, your fork, or your own), point your scheduled routine's source at
that repo and keep the routine's stored prompt thin -- "read `Agents/eric/CLAUDE.md` and
today's relevant `Skills/` file in this repo, then run the check." The routine re-clones
fresh on every run, so editing this repo is enough to change what the next run does. See
`Workflows/eric-infrastructure.md` for the full explanation and the durability note about
scheduled routines lapsing after idle periods.

GitHub Actions on a cron trigger is a particularly natural fit for Eric specifically --
GitHub Actions is already one of his own audit targets, so a workflow he audits can also
be the thing running his own scheduled checks.

## Authority reminder

Every trigger above resolves through the same authority split, no exceptions:
config-only fixes go out as a PR to your staging branch; DNS, edge function/Worker, and
environment variable changes always stop and go to a human first; production promotion
is never Eric's call. See `core/capabilities.md` for the full breakdown.
