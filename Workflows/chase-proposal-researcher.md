# Chase (proposal-team-open) -- Automation Setup

How to put Chase, the Proposal Researcher, on a recurring schedule instead of running him
by hand. Two options depending on your platform: Claude's scheduled routines, or ChatGPT's
Scheduled Tasks. Pick one - you don't need both.

Install the plugin first. Chase's Discovery Brief doesn't require a customization file to
be filled in. Automation just runs the same prompt from
[`Prompts/proposal-team-open.md`](../Prompts/proposal-team-open.md) on a trigger.

This role runs as part of Maya's gated pipeline - see
[`Workflows/maya-proposal-engine-lead.md`](./maya-proposal-engine-lead.md) for the full
sequence.

---

## Option A - Claude scheduled routine

Requires Claude Code with the plugin installed. Use the `/schedule` command (or ask
Claude to "set up a scheduled routine") to create this.

Chase only makes sense triggered on a new qualified opportunity, not a fixed clock - set
this up as an on-demand prompt you (or Maya) fire at the right moment.

| Persona | Suggested cadence | Trigger prompt |
|---|---|---|
| Chase - Proposal Researcher | On new qualified opportunity (not a fixed clock) | "A new opportunity just cleared qualification: [prospect name]. Research it and give me a Discovery Brief with a Go/No-Go recommendation before we spend anything further on this deal." |

Name the routine `chase-proposal-researcher` so `/schedule list` stays readable once
you're running more than one.

**Durability note:** scheduled Claude Code routines are session-bound and can lapse when
a session ends or after several days idle. If a routine stops firing, just re-ask Claude
to recreate it with the same name and cadence. For a routine you don't want to babysit,
consider migrating it to a GitHub Actions workflow on a cron trigger instead - more setup
up front, but it survives independent of any Claude session.

**Preferred pattern - point the routine at your repo instead of pasting everything in.**
If your `customization/` files live in a GitHub repo (this one, your fork, or your own),
set Chase's routine source to that repo and keep the CCR prompt itself thin: "Read
`Plugins/proposal-team-open/skills/chase-proposal-researcher/SKILL.md` and your
`customization/` files in this repo, then research today's qualified opportunity." Claude
Code CCRs re-clone the source repo fresh on every run, so editing the SKILL.md or your
customization files is enough - you never have to touch the routine's stored prompt.
Save the full trigger prompt above for a repo-less setup (ChatGPT Scheduled Tasks, or a
Claude routine with no git source configured) - in that case, the "keep both in sync"
habit below still applies.

**Three habits worth keeping once a routine is live:**

- **Short-circuit on empty.** Before Chase runs, have it check whether a new opportunity
  has actually cleared qualification first - if there's nothing waiting, post "nothing
  new" and exit rather than burning a run on nothing.
- **The routine's stored prompt is a frozen copy, not a live link back to your files.**
  If you edit any customization file, update the scheduled routine's prompt too -
  editing the repo alone won't change what the next scheduled run actually does. (Skip
  this if you're using the repo-container pattern above - that's the whole point of it.)
- **End every run with a summary, not a raw dump.** A short notification (Go/No-Go
  recommendation, fit score, any red flags) is more useful than the full Discovery Brief
  dropped into chat - save the full document for wherever your CRM or Drive folder
  already keeps deal records.

---

## Option B - ChatGPT Scheduled Tasks

Requires ChatGPT Plus or higher and the SKILL.md file uploaded to a project (Settings >
Tasks, or "Ask ChatGPT to schedule this").

1. Open a conversation with Chase's `SKILL.md` uploaded (see
   [`Skills/README.md`](../Skills/README.md) for upload steps)
2. Say: "Schedule this to run when I tell you to and use this prompt each time: A new
   opportunity just cleared qualification: [prospect name]. Research it and give me a
   Discovery Brief with a Go/No-Go recommendation before we spend anything further on
   this deal."
3. Confirm the task in Settings > Tasks - ChatGPT will show you the next run time

ChatGPT Scheduled Tasks can't write directly to your CRM or Drive the way a Claude Code
routine with MCP access can - Chase's research output will need a manual copy/paste step
unless you've connected the equivalent tools.

---

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit [compoundleverage.com](https://compoundleverage.com).
