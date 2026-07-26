# Priya (proposal-team-open) -- Automation Setup

How to put Priya, the Proposal Analyst, on a recurring schedule instead of running her by
hand. Two options depending on your platform: Claude's scheduled routines, or ChatGPT's
Scheduled Tasks. Pick one - you don't need both.

Install the plugin and fill in `customization/my-pricing-model.json` and
`customization/my-company-profile.json` first. Automation just runs the same prompt from
[`Prompts/proposal-team-open.md`](../Prompts/proposal-team-open.md) on a trigger.

This role runs as part of Maya's gated pipeline - see
[`Workflows/maya-proposal-engine-lead.md`](./maya-proposal-engine-lead.md) for the full
sequence.

---

## Option A - Claude scheduled routine

Requires Claude Code with the plugin installed. Use the `/schedule` command (or ask
Claude to "set up a scheduled routine") to create this.

Priya only makes sense triggered on Discovery Brief approval, not a fixed clock - set
this up as an on-demand prompt you (or Maya) fire at the right moment.

| Persona | Suggested cadence | Trigger prompt |
|---|---|---|
| Priya - Proposal Analyst | On Discovery Brief approval (not a fixed clock) | "Here's the approved Discovery Brief for [prospect name]. Classify the deal, score our capability fit, build a conservative ROI model, and configure pricing from our pricing model." |

Name the routine `priya-proposal-analyst` so `/schedule list` stays readable once you're
running more than one.

**Durability note:** scheduled Claude Code routines are session-bound and can lapse when
a session ends or after several days idle. If a routine stops firing, just re-ask Claude
to recreate it with the same name and cadence. For a routine you don't want to babysit,
consider migrating it to a GitHub Actions workflow on a cron trigger instead - more setup
up front, but it survives independent of any Claude session.

**Preferred pattern - point the routine at your repo instead of pasting everything in.**
If your `customization/` files live in a GitHub repo (this one, your fork, or your own),
set Priya's routine source to that repo and keep the CCR prompt itself thin: "Read
`Plugins/proposal-team-open/skills/priya-proposal-analyst/SKILL.md` and your
`customization/` files in this repo, then run the assessment for today's approved
Discovery Brief." Claude Code CCRs re-clone the source repo fresh on every run, so
editing the SKILL.md or your customization files is enough - you never have to touch the
routine's stored prompt. Save the full trigger prompt above for a repo-less setup
(ChatGPT Scheduled Tasks, or a Claude routine with no git source configured) - in that
case, the "keep both in sync" habit below still applies.

**Three habits worth keeping once a routine is live:**

- **Short-circuit on empty.** Before Priya runs, have it check whether a Discovery Brief
  has actually been approved first - if there's nothing waiting, post "nothing new" and
  exit rather than burning a run on nothing.
- **The routine's stored prompt is a frozen copy, not a live link back to your files.**
  If you edit `customization/my-pricing-model.json`, `my-company-profile.json`, or any
  other customization file, update the scheduled routine's prompt too - editing the repo
  alone won't change what the next scheduled run actually does. (Skip this if you're
  using the repo-container pattern above - that's the whole point of it.)
- **End every run with a summary, not a raw dump.** A short notification (overall fit
  score, ROI headline numbers, pricing configuration chosen) is more useful than the full
  Assessment Package dropped into chat - save the full document for wherever your CRM or
  Drive folder already keeps deal records.

---

## Option B - ChatGPT Scheduled Tasks

Requires ChatGPT Plus or higher and the SKILL.md file uploaded to a project (Settings >
Tasks, or "Ask ChatGPT to schedule this").

1. Open a conversation with Priya's `SKILL.md` uploaded (see
   [`Skills/README.md`](../Skills/README.md) for upload steps)
2. Say: "Schedule this to run when I tell you to and use this prompt each time: Here's
   the approved Discovery Brief for [prospect name]. Classify the deal, score our
   capability fit, build a conservative ROI model, and configure pricing from our
   pricing model."
3. Confirm the task in Settings > Tasks - ChatGPT will show you the next run time

ChatGPT Scheduled Tasks can't write directly to your CRM or Drive the way a Claude Code
routine with MCP access can - Priya's pricing lookups will need a manual copy/paste step
unless you've connected the equivalent tools.

---

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit [compoundleverage.com](https://compoundleverage.com).
