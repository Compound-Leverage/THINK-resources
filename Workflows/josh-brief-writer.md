# Josh (content-team) -- Automation Setup

How to put Josh on a recurring schedule instead of running him by hand. Two options
depending on your platform: Claude's scheduled routines, or ChatGPT's Scheduled Tasks.
Pick one -- you don't need both.

Install the plugin and fill in `customization/my-content-sources.json` (and
`customization/my-brand-guidelines.md`) first. Automation just runs the same prompt
from [`Prompts/content-team.md`](../Prompts/content-team.md) on a timer.

---

## Option A -- Claude scheduled routine

Requires Claude Code with the plugin installed. Use the `/schedule` command (or ask
Claude to "set up a scheduled routine") to create this:

| Persona | Suggested cadence | Trigger prompt |
|---|---|---|
| Josh -- Intelligence Brief | Weekly, after Intel Scanner | "Filter this week's topic cards to only the ones meeting our proof-gate threshold, then draft a Leader edition and a Strategist edition of our intelligence brief. Flag any org-buyer-relevant topic so our BD team can follow up on it." |

Name the routine after the persona (e.g. `josh-brief-writer`) so `/schedule list`
stays readable once you're running more than one.

**Durability note:** scheduled Claude Code routines are session-bound and can lapse when
a session ends or after several days idle. If a routine stops firing, just re-ask Claude
to recreate it with the same name and cadence. For a routine you don't want to babysit,
consider migrating it to a GitHub Actions workflow on a cron trigger instead -- more setup
up front, but it survives independent of any Claude session.

**Preferred pattern -- point the routine at your repo instead of pasting everything in.**
If your `customization/my-content-sources.json` and `my-brand-guidelines.md` live in a
GitHub repo (this one, your fork, or your own), set the routine's source to that repo and
keep the CCR prompt itself thin: "Read
`Plugins/content-team/skills/josh-brief-writer/SKILL.md` and your
`customization/` files in this repo, then draft this week's intelligence brief." Claude
Code CCRs re-clone the source repo fresh on every run, so editing the SKILL.md or your
customization files is enough -- you never have to touch the routine's stored prompt.
Save the full trigger prompt in the table above for a repo-less setup (ChatGPT Scheduled
Tasks, or a Claude routine with no git source configured) -- in that case, the "keep both
in sync" habit below still applies.

Reads from Rohit's topic cards -- see [`Workflows/rohit-master-intel-scan.md`](rohit-master-intel-scan.md)
for the full weekly sequence.

**Three habits worth keeping once a routine is live:**

- **Short-circuit on empty.** If Rohit's topic cards for the week are stale or empty, or
  nothing meets the proof-gate threshold, have Josh say so and skip drafting rather than
  writing a brief off nothing.
- **The routine's stored prompt is a frozen copy, not a live link back to your files.**
  If you edit `customization/my-content-sources.json` or `my-brand-guidelines.md`, or
  change how you're prompting Josh, update the scheduled routine's prompt too -- editing
  the repo alone won't change what the next scheduled run actually does. (Skip this if
  you're using the repo-container pattern above -- that's the whole point of it.)
- **End every run with a summary, not a raw dump.** A short notification (topics meeting
  the gate, any org-buyer flags raised) is more useful than the full output -- save the
  full record for wherever the skill already writes it (`org-buyer-flags.json`, your
  content DB).

---

## Option B -- ChatGPT Scheduled Tasks

Requires ChatGPT Plus or higher and the SKILL.md file uploaded to a project (Settings >
Tasks, or "Ask ChatGPT to schedule this").

1. Open a conversation with Josh's `SKILL.md` uploaded (see
   [`Skills/README.md`](../Skills/README.md) for upload steps)
2. Say: "Schedule this to run weekly, after Intel Scanner, and use this prompt each
   time: [trigger prompt from the table above]"
3. Confirm the task in Settings > Tasks -- ChatGPT will show you the next run time

ChatGPT Scheduled Tasks can't write directly to your content database the way a Claude
Code routine with MCP access can -- Josh's output will need a manual copy/paste step
unless you've connected the equivalent tools. Since Josh depends on Rohit's topic
cards, that step also has to be run manually first, since ChatGPT Scheduled Tasks don't
gate one task's start on another task's completion.

---

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit [compoundleverage.com](https://compoundleverage.com).
