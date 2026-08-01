# Proposal Generator (proposal-generator) -- Automation Setup

How to put the Proposal Generator to work, and where recurring automation actually fits
a plugin that's built to run per-deal, not on a timer.

Install the plugin and fill in the `customization/` files first:
`my-company-profile.json`, `my-pricing-model.json`, `my-case-studies.json`, and
`my-brand-guidelines.md`. The skill will not produce a personalized proposal without them.

This is a single-persona, single-workflow plugin: one skill runs 7 gated phases (Intake,
Research, Assessment, Strategy, Draft, QA, Output) end to end for one deal at a time, with
a human approval gate between every phase. **It is fundamentally an on-demand tool, not a
recurring one** - you don't schedule "run the proposal generator" the way you'd schedule a
daily intake sweep, because it needs a specific client and a specific opportunity to run
against, and a human decision at every gate. Don't force a fake cadence onto it.

The one piece of this that *is* worth automating on a schedule is the scan that feeds it:
checking whether any deal has reached the point where a proposal should be started. That's
a real recurring check even though the proposal work itself stays on-demand.

---

## Option A - Claude scheduled routine

Requires Claude Code with the plugin installed. Use the `/schedule` command (or ask
Claude to "set up a scheduled routine") to create the recurring piece; run the on-demand
piece by hand whenever a deal needs a proposal.

| Task | Suggested cadence | Trigger prompt |
|---|---|---|
| Proposal Generator - run for a deal | On-demand (per deal, not scheduled) | "run proposal [Client Name] - here's their website, industry, due date, and how this opportunity came to us." |
| Proposal-ready scan | Weekly | "Check our deal pipeline for any opportunities that have reached proposal stage but don't have a proposal started yet. List each one with client name, due date, and how it came to us, so I can kick off `run proposal` for it." |

Phase-gate commands you'll use while a run is in progress, straight from the skill's
command reference: `status` (show current phase), `go` (approve the Go/No-Go decision),
`approved` (approve the current phase), `proceed` (move to the next phase), and
`revise [feedback]` (send a phase back for changes).

Name the scan routine something like `proposal-generator-scan` so `/schedule list` stays
readable if you add other scheduled routines later. Don't name a schedule after the
generator itself - there's nothing to schedule there, only the scan.

**Durability note:** scheduled Claude Code routines are session-bound and can lapse when
a session ends or after several days idle. If the scan stops firing, just re-ask Claude
to recreate it with the same name and cadence. For a routine you don't want to babysit,
consider migrating it to a GitHub Actions workflow on a cron trigger instead - more setup
up front, but it survives independent of any Claude session.

**Preferred pattern - point the routine at your repo instead of pasting everything in.**
If your `customization/` files live in a GitHub repo (this one, your fork, or your own),
set the routine's source to that repo and keep the CCR prompt itself thin: "Read
`Plugins/proposal-generator/skills/proposal-generator/SKILL.md` and your
`customization/` files in this repo, then scan for deals ready for a proposal." Claude
Code CCRs re-clone the source repo fresh on every run, so editing the SKILL.md or your
customization files is enough - you never have to touch the routine's stored prompt.
Save the full trigger prompt above for a repo-less setup (ChatGPT Scheduled Tasks, or a
Claude routine with no git source configured) - in that case, the "keep both in sync"
habit below still applies.

**Three habits worth keeping once the scan is live:**

- **Short-circuit on empty.** If the scan finds no deals newly at proposal stage, have it
  post "0 deals ready" and exit rather than running deeper analysis on nothing.
- **The routine's stored prompt is a frozen copy, not a live link back to your files.**
  If you change how you're prompting the scan, or update `customization/` in a way that
  changes what "ready for proposal" means, update the scheduled routine's prompt too:
  editing the repo alone won't change what the next scheduled run actually does. (Skip
  this if you're using the repo-container pattern above: that's the whole point of it.)
- **End every run with a summary, not a raw dump.** A short notification (how many deals
  found, which ones, due dates) is more useful than pasting the full pipeline query - keep
  the full detail wherever your deal tracker already lives.

---

## Option B - ChatGPT Scheduled Tasks

Requires ChatGPT Plus or higher and the `SKILL.md` uploaded to a project (Settings >
Tasks, or "Ask ChatGPT to schedule this").

1. Open a conversation with the skill's `SKILL.md` uploaded (see
   [`Skills/README.md`](../Skills/README.md) for upload steps)
2. Say: "Schedule this to run weekly and use this prompt each time: Check our deal
   pipeline for any opportunities that have reached proposal stage but don't have a
   proposal started yet. List each one with client name, due date, and how it came to us."
3. Confirm the task in Settings > Tasks - ChatGPT will show you the next run time

ChatGPT Scheduled Tasks can't read your deal tracker or CRM directly the way a Claude Code
routine with MCP access can - the scan will need you to paste in the current pipeline list
(or a CSV export) each time, unless you've connected the equivalent tool. Once the scan
flags a deal, run the actual proposal generation (`run proposal [Client Name]...`) by hand
in a normal conversation - that part stays manual and gated in both platforms.

---

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit [compoundleverage.com](https://compoundleverage.com).
