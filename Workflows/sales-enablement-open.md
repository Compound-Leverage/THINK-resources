# Sales Enablement (sales-enablement-open): Automation Setup

How to put Marcus on a recurring schedule instead of running him by hand. Two options
depending on your platform: Claude's scheduled routines, or ChatGPT's Scheduled Tasks.
Pick one, you don't need both.

Install the plugin and fill in `customization/my-proof-points-config.json` first.
Automation just runs the same prompts from
[`Prompts/sales-enablement-open.md`](../Prompts/sales-enablement-open.md) on a timer.

---

## Option A: Claude scheduled routine

Requires Claude Code with the plugin installed. Use the `/schedule` command (or ask
Claude to "set up a scheduled routine") to create each of these:

| Persona | Suggested cadence | Trigger prompt |
|---|---|---|
| Marcus, Proof Points harvest | Weekly | "Pull our completed engagements from the last quarter and extract 1-page case study narratives, tagged by buyer type, for our proof points library." |
| Marcus, Inventory check | Weekly, after the harvest run | "Check our proof points inventory against our minimum threshold per buyer tag and alert me if any tag is running low." |

Name the routine after the persona (e.g. `marcus-proof-points`) so `/schedule list` stays
readable once you're running more than one.

**Durability note:** scheduled Claude Code routines are session-bound and can lapse when a
session ends or after several days idle. If a routine stops firing, just re-ask Claude to
recreate it with the same name and cadence. For a routine you don't want to babysit,
consider migrating it to a GitHub Actions workflow on a cron trigger instead: more setup
up front, but it survives independent of any Claude session.

**Preferred pattern: point the routine at your repo instead of pasting everything in.**
If your `customization/my-proof-points-config.json` lives in a GitHub repo (this one,
your fork, or your own), set the routine's source to that repo and keep the CCR prompt
itself thin: "Read `Plugins/sales-enablement-open/skills/marcus-proof-points/SKILL.md`
and `customization/my-proof-points-config.json` in this repo, then run this week's
harvest." Claude Code CCRs re-clone the source repo fresh on every run, so editing the
SKILL.md or your customization file is enough: you never have to touch the routine's
stored prompt. Save the full trigger prompt above for a repo-less setup (ChatGPT
Scheduled Tasks, or a Claude routine with no git source configured): in that case, the
"keep both in sync" habit below still applies.

**Three habits worth keeping once a routine is live:**

- **Short-circuit on empty.** Before Marcus runs the full extraction/tagging steps, have
  it check for new completed engagements first: if there's nothing new to harvest, post
  "0 records" and exit rather than burning a run on nothing.
- **The routine's stored prompt is a frozen copy, not a live link back to your files.** If
  you edit `customization/my-proof-points-config.json` or change how you're prompting
  Marcus, update the scheduled routine's prompt too: editing the repo alone won't change
  what the next scheduled run actually does. (Skip this if you're using the
  repo-container pattern above: that's the whole point of it.)
- **End every run with a short summary, not a raw dump.** A short notification (count
  harvested this run, current inventory level per buyer tag vs. minimum threshold) is more
  useful than the full output: save the full record for wherever Marcus already writes it
  (your Proof Points database).

---

## Option B: ChatGPT Scheduled Tasks

Requires ChatGPT Plus or higher and the SKILL.md file uploaded to a project (Settings >
Tasks, or "Ask ChatGPT to schedule this").

1. Open a conversation with Marcus's `SKILL.md` uploaded (see
   [`Skills/README.md`](../Skills/README.md) for upload steps)
2. Say: "Schedule this to run [cadence from the table above] and use this prompt each
   time: [trigger prompt from the table above]"
3. Confirm the task in Settings > Tasks: ChatGPT will show you the next run time

ChatGPT Scheduled Tasks can't write directly to your Notion database the way a Claude Code
routine with MCP access can: Marcus's output will need a manual copy/paste step unless
you've connected the equivalent tools.

---

## Questions

Contact [marvin@compoundleverage.co](mailto:marvin@compoundleverage.co) or visit [compoundleverage.com](https://compoundleverage.com).
