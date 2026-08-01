# Blair (proposal-team) -- Automation Setup

How to put Blair, Pitch Development, on a recurring schedule instead of running him by
hand. Two options depending on your platform: Claude's scheduled routines, or ChatGPT's
Scheduled Tasks. Pick one - you don't need both.

Install the plugin and fill in `customization/my-bid-sizing.json` and
`customization/my-case-studies.json` first. Automation just runs the same prompt from
[`Prompts/proposal-team.md`](../Prompts/proposal-team.md) on a trigger.

Blair runs on a separate track from Maya's gated pipeline, not part of the Chase-Priya-
Porter-Quinn-Diego chain - see
[`Workflows/maya-proposal-engine-lead.md`](./maya-proposal-engine-lead.md) for how the
two tracks relate.

---

## Option A - Claude scheduled routine

Requires Claude Code with the plugin installed. Use the `/schedule` command (or ask
Claude to "set up a scheduled routine") to create this.

Blair only makes sense triggered on a deal reaching Proposal Stage for a grant/funder
category, not a fixed clock - set this up as an on-demand prompt you fire at the right
moment.

| Persona | Suggested cadence | Trigger prompt |
|---|---|---|
| Blair - Pitch Development | On deal reaching Proposal Stage for a grant/funder category (not a fixed clock) | "[Prospect name]'s deal just moved to Proposal Stage and it's a [funder category] opportunity. Convert it into a customized funder proposal using our bid-sizing rules and real case studies, and hold it for my approval before any outreach." |

Name the routine `blair-pitch-development` so `/schedule list` stays readable once you're
running more than one.

**Durability note:** scheduled Claude Code routines are session-bound and can lapse when
a session ends or after several days idle. If a routine stops firing, just re-ask Claude
to recreate it with the same name and cadence. For a routine you don't want to babysit,
consider migrating it to a GitHub Actions workflow on a cron trigger instead - more setup
up front, but it survives independent of any Claude session.

**Preferred pattern - point the routine at your repo instead of pasting everything in.**
If your `customization/` files live in a GitHub repo (this one, your fork, or your own),
set Blair's routine source to that repo and keep the CCR prompt itself thin: "Read
`Plugins/proposal-team/skills/blair-pitch-development/SKILL.md` and your
`customization/` files in this repo, then convert today's Proposal-Stage grant/funder
deal into a funder proposal." Claude Code CCRs re-clone the source repo fresh on every
run, so editing the SKILL.md or your customization files is enough - you never have to
touch the routine's stored prompt. Save the full trigger prompt above for a repo-less
setup (ChatGPT Scheduled Tasks, or a Claude routine with no git source configured) - in
that case, the "keep both in sync" habit below still applies.

**Three habits worth keeping once a routine is live:**

- **Short-circuit on empty.** Before Blair runs, have it check whether a deal has
  actually reached Proposal Stage for a grant/funder category first - if there's nothing
  waiting, post "nothing new" and exit rather than burning a run on nothing.
- **The routine's stored prompt is a frozen copy, not a live link back to your files.**
  If you edit `customization/my-bid-sizing.json`, `my-case-studies.json`, or any other
  customization file, update the scheduled routine's prompt too - editing the repo alone
  won't change what the next scheduled run actually does. (Skip this if you're using the
  repo-container pattern above - that's the whole point of it.)
- **End every run with a summary, not a raw dump.** A short notification (bid amount,
  decision timeline, approval status) is more useful than the full funder proposal
  dropped into chat - save the full document for wherever your CRM or Drive folder
  already keeps deal records. Your approval is required before any outreach.

---

## Option B - ChatGPT Scheduled Tasks

Requires ChatGPT Plus or higher and the SKILL.md file uploaded to a project (Settings >
Tasks, or "Ask ChatGPT to schedule this").

1. Open a conversation with Blair's `SKILL.md` uploaded (see
   [`Skills/README.md`](../Skills/README.md) for upload steps)
2. Say: "Schedule this to run when I tell you to and use this prompt each time:
   [Prospect name]'s deal just moved to Proposal Stage and it's a [funder category]
   opportunity. Convert it into a customized funder proposal using our bid-sizing rules
   and real case studies, and hold it for my approval before any outreach."
3. Confirm the task in Settings > Tasks - ChatGPT will show you the next run time

ChatGPT Scheduled Tasks can't write directly to your CRM or Drive the way a Claude Code
routine with MCP access can - Blair's document output will need a manual copy/paste step
unless you've connected the equivalent tools.

---

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit [compoundleverage.com](https://compoundleverage.com).
