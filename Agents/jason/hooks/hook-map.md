# Jason -- Hook Map

Jason has a PR-triggered lane, a pre-push lane, a post-deploy lane, and a scheduled lane
for the slower checks. This maps which trigger fires which skill -- for how to actually
put the scheduled checks on a timer (Claude scheduled routine or ChatGPT Scheduled Task),
see `Workflows/qa-reviewer-jason.md`, which already documents this as part of the Ops
Team plugin. Don't duplicate that setup guidance here; this file just tells you which
skill each trigger should point at.

| When to run | Trigger | Fires |
|---|---|---|
| A PR opens against your staging branch | PR opened | `Skills/content-qa/` (page classification, H1 audit, rewrite proposals, copy consistency) then `Skills/site-audit/`'s redirect check -> `Skills/findings-routing/` |
| Before pushing to your staging branch | Manual, or a pre-push step in your own tooling | `Skills/content-qa/` + `Skills/site-audit/`'s redirect check -> `Skills/findings-routing/` |
| Before pushing to your production branch | Manual, gated by your own approval step | `Skills/content-qa/` + `Skills/site-audit/`'s redirect check + `Skills/docs-maintenance/`'s changelog generation -> `Skills/findings-routing/` |
| After your build/deploy completes | Deploy webhook, or manual | `Skills/site-audit/`'s broken-links and uptime checks -> `Skills/findings-routing/` |
| After a PR merges | PR merged | `Skills/docs-maintenance/` (inline comment and README update proposals) -> `Skills/findings-routing/` |
| Weekly (pick a fixed day) | Scheduled routine | `Skills/site-audit/`'s SEO, LLM/AI discoverability, performance, and secondary-property checks -> `Skills/findings-routing/` |
| Monthly | Scheduled routine | `Skills/security-audit/` and `Skills/agent-fleet-audit/` -> `Skills/findings-routing/` |
| A search console notification arrives | Email, or your platform's own alerting | `Skills/site-audit/`'s search console monitor step, routing to its redirect or coverage checks -> `Skills/findings-routing/` |
| On demand | Explicit ask: "Jason, audit the site," "check for broken links" | Whichever skill matches the ask |

## Repo-container pattern

Same preferred pattern as the rest of this repo: if your filled-in site standards and
config live in a GitHub repo (this one, your fork, or your own), point your scheduled
routine's source at that repo and keep the routine's stored prompt thin -- "read
`Agents/jason/CLAUDE.md` and today's relevant `Skills/` file in this repo, then run the
check." The routine re-clones fresh on every run, so editing this repo is enough to
change what the next run does. See `Workflows/qa-reviewer-jason.md` for the full
explanation and the durability note about scheduled routines lapsing after idle periods.
