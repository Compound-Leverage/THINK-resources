# Amy (content-team-open) -- Automation Setup

How to put Amy on a recurring schedule instead of running her by hand. Two options
depending on your platform: Claude's scheduled routines, or ChatGPT's Scheduled Tasks.
Pick one -- you don't need both.

Install the plugin and fill in `customization/my-content-sources.json` (and
`customization/my-brand-guidelines.md`) first. Automation just runs the same prompt
from [`Prompts/content-team-open.md`](../Prompts/content-team-open.md) on a timer.

---

## Option A -- Claude scheduled routine

Requires Claude Code with the plugin installed. Use the `/schedule` command (or ask
Claude to "set up a scheduled routine") to create this:

| Persona | Suggested cadence | Trigger prompt |
|---|---|---|
| Amy -- YouTube Scripts | Weekly, after Intelligence Brief | "Here's our research file and this week's brief, write a 4-5 minute YouTube script with 2-3 title options, 2-3 hook variants, a signal walkthrough, and a CTA close. Check that the script actually runs 4-5 minutes read aloud before you finish." |

Name the routine after the persona (e.g. `amy-youtube-scripts`) so `/schedule list`
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
`Plugins/content-team-open/skills/amy-youtube-scripts/SKILL.md` and your
`customization/` files in this repo, then write this week's YouTube script." Claude Code
CCRs re-clone the source repo fresh on every run, so editing the SKILL.md or your
customization files is enough -- you never have to touch the routine's stored prompt.
Save the full trigger prompt in the table above for a repo-less setup (ChatGPT Scheduled
Tasks, or a Claude routine with no git source configured) -- in that case, the "keep both
in sync" habit below still applies.

Reads from Rohit's topic cards (via Josh's brief) -- see
[`Workflows/rohit-master-intel-scan.md`](rohit-master-intel-scan.md) for the full weekly
sequence.

**Three habits worth keeping once a routine is live:**

- **Short-circuit on empty.** If there's no fresh Intelligence Brief (or topic cards) to
  work from this week, have Amy say so and skip drafting rather than writing a script
  off nothing.
- **The routine's stored prompt is a frozen copy, not a live link back to your files.**
  If you edit `customization/my-content-sources.json` or `my-brand-guidelines.md`, or
  change how you're prompting Amy, update the scheduled routine's prompt too -- editing
  the repo alone won't change what the next scheduled run actually does. (Skip this if
  you're using the repo-container pattern above -- that's the whole point of it.)
- **End every run with a summary, not a raw dump.** A short notification (title options,
  estimated runtime) is more useful than the full script in the notification itself --
  save the full record for wherever the skill already writes it
  (`output/{week}/YouTube_Script_{week}.md`).

---

## Option B -- ChatGPT Scheduled Tasks

Requires ChatGPT Plus or higher and the SKILL.md file uploaded to a project (Settings >
Tasks, or "Ask ChatGPT to schedule this").

1. Open a conversation with Amy's `SKILL.md` uploaded (see
   [`Skills/README.md`](../Skills/README.md) for upload steps)
2. Say: "Schedule this to run weekly, after the Intelligence Brief, and use this prompt
   each time: [trigger prompt from the table above]"
3. Confirm the task in Settings > Tasks -- ChatGPT will show you the next run time

ChatGPT Scheduled Tasks work fine for Amy since her output is a script file rather than
a database write, but since she depends on Josh's brief (or Rohit's topic cards
directly), that upstream step still has to be run manually first, since ChatGPT
Scheduled Tasks don't gate one task's start on another task's completion.

---

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit [compoundleverage.com](https://compoundleverage.com).
