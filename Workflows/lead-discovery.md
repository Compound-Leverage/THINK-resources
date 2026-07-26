# Lead Discovery (lead-discovery): Automation Setup

How to put lead-discovery on a recurring schedule instead of running it by hand. Two
options depending on your platform: Claude's scheduled routines, or ChatGPT's Scheduled
Tasks. Pick one, you don't need both.

Install the plugin first. Unlike some other THINK School plugins, lead-discovery doesn't
ship a `customization/*.json` file: there are no DB IDs or provider keys to fill in. The
full methodology (scoring dimensions, disqualifiers, source hierarchy, decision rules)
lives in the skill itself. What you do need to decide before automating it is a delivery
mechanism: the skill's Implementation Notes call out Notion database, email digest, JSON
API endpoint, or Google Sheets as options, and don't prescribe one. Pick where the weekly
shortlist should land before you schedule the routine. Automation just runs the same
prompt from [`Prompts/lead-discovery.md`](../Prompts/lead-discovery.md) on a timer.

---

## Option A: Claude scheduled routine

Requires Claude Code with the plugin installed. Use the `/schedule` command (or ask
Claude to "set up a scheduled routine") to create this:

| Persona | Suggested cadence | Trigger prompt |
|---|---|---|
| Lead Discovery | Weekly | "Scan SAM.gov, our state/local procurement portals, and grants databases for opportunities that surfaced since last run. Score each against our 5-dimension model (fit, win probability, economic value, timeline realism, strategic leverage), apply the disqualifiers, and give me the ranked shortlist of Include-decision leads plus anything that lands as Monitor. Target 5-10 qualified leads." |

Name the routine after the skill (e.g. `lead-discovery-weekly`) so `/schedule list` stays
readable once you're running more than one plugin's routines.

**Durability note:** scheduled Claude Code routines are session-bound and can lapse when a
session ends or after several days idle. If the routine stops firing, just re-ask Claude
to recreate it with the same name and cadence. For a routine you don't want to babysit,
consider migrating it to a GitHub Actions workflow on a cron trigger instead: more setup
up front, but it survives independent of any Claude session.

**Preferred pattern -- point the routine at your repo instead of pasting everything in.**
If your fork of this repo is what you're actually using, set the routine's source to
that repo and keep the CCR prompt itself thin: "Read
`Plugins/lead-discovery/skills/lead-discovery/SKILL.md` in this repo, then run this
week's scoring sweep." Claude Code CCRs re-clone the source repo fresh on every run, so
editing the SKILL.md is enough -- you never have to touch the routine's stored prompt.
Save the full trigger prompt above for a repo-less setup (ChatGPT Scheduled Tasks, or a
Claude routine with no git source configured) -- in that case, the "keep both in sync"
habit below still applies.

lead-discovery is a single standalone skill, not a multi-persona team, so there's no
second persona downstream to chain it into and no pipeline ordering to set up here.

**Three habits worth keeping once the routine is live:**

- **Short-circuit on empty.** Before running the full scoring pass, have the routine check
  whether anything new has actually surfaced across the source list since the last run.
  If the procurement portals and grants databases have nothing new, report "0 new
  opportunities" and exit rather than re-scoring last week's already-processed leads.
- **The routine's stored prompt is a frozen copy, not a live link back to your files.** If
  you edit the scoring dimensions, disqualifiers, or decision rules in
  `Skills/lead-discovery/SKILL.md`, update the scheduled routine's prompt too. Editing
  the repo alone won't change what the next scheduled run actually does. (Skip this if
  you're using the repo-container pattern above -- that's the whole point of it.)
- **End every run with a summary, not a raw dump.** A short notification (Include /
  Monitor / Exclude counts, anything flagged for manual review) is more useful than the
  full shortlist. Save the full output for wherever you've wired delivery to (Notion,
  email digest, spreadsheet, whatever you chose above).

---

## Option B: ChatGPT Scheduled Tasks

Requires ChatGPT Plus or higher and the skill's `SKILL.md` uploaded to a project
(Settings > Tasks, or "Ask ChatGPT to schedule this").

1. Open a conversation with `Skills/lead-discovery/SKILL.md` uploaded (see
   [`Skills/README.md`](../Skills/README.md) for upload steps)
2. Say: "Schedule this to run weekly and use this prompt each time: [trigger prompt from
   the table above]"
3. Confirm the task in Settings > Tasks. ChatGPT will show you the next run time

ChatGPT Scheduled Tasks can't write directly to a CRM, Drive, or database the way a Claude
Code routine with MCP access can. Whatever delivery mechanism you chose (Notion, a
spreadsheet, an email digest) will need a manual copy/paste step from the chat output
unless you've connected the equivalent tool.

---

## Questions

Contact [marvin@compoundleverage.co](mailto:marvin@compoundleverage.co) or visit [compoundleverage.com](https://compoundleverage.com).
