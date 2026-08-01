# Chet -- Hook Map

Chet has two recurring workflows that typically run together, plus two on-demand modes.
This maps which trigger fires which skill -- for how to actually put these on a schedule
(Claude scheduled routine or ChatGPT Scheduled Task), see `Workflows/capture-team.md`,
which already documents Chet's cadence as part of the Capture Team plugin. Don't
duplicate that setup guidance here; this file just tells you which skill each trigger
should point at.

| When to run | Trigger | Fires |
|---|---|---|
| Weekly, once | Scheduled routine (see `Workflows/capture-team.md`'s Chet row) | `Skills/cluster-discovery/` -- discover new groups for unmapped capabilities, refresh existing known groups (membership, budget confirmation, window estimate), archive anything whose window has closed without conversion |
| Weekly, right after discovery | Scheduled routine, same run or a following one | `Skills/cluster-monitoring/` -- sweep your signal inbox for scored signals, qualify each cluster against your goals, advance what clears the bar, flag the rest |
| On demand | You already have a brief, scan, or report and want cluster candidates out of it without a fresh web search | `Skills/brief-to-cluster-bridge/` |
| On demand | Explicit ask: "Chet, scan clusters," "check for new groups in [capability]" | Whichever skill matches the ask -- discovery for new-group hunting, monitoring for advancement/refresh |
| A signal doesn't match any capability in your config, seen more than once | Automatic, during discovery or monitoring | Logged per your `unmatched_signal_routing` config -- not forced into a cluster |

## Repo-container pattern

Same preferred pattern as the rest of this repo: if your filled-in config lives in a
GitHub repo (this one, your fork, or your own), point your scheduled routine's source at
that repo and keep the routine's stored prompt thin -- "read `Agents/chet/CLAUDE.md` and
today's relevant `Skills/` file in this repo, then run the scan." The routine re-clones
fresh on every run, so editing this repo is enough to change what the next run does. See
`Workflows/capture-team.md` for the full explanation and the durability note about
scheduled routines lapsing after idle periods.
