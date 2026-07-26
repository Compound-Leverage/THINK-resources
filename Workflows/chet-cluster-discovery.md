# Chet (capture-team-open) -- Automation Setup

How to put Chet on a recurring schedule instead of running him by hand. Two options
depending on your platform: Claude's scheduled routines, or ChatGPT's Scheduled Tasks.
Pick one -- you don't need both.

Install the plugin and fill in `customization/my-capture-config.json` first. Automation
just runs the same prompt from [`Prompts/capture-team-open.md`](../Prompts/capture-team-open.md)
on a timer.

---

## Option A -- Claude scheduled routine

Requires Claude Code with the plugin installed. Use the `/schedule` command (or ask
Claude to "set up a scheduled routine") to create this:

Chet -- Cluster Discovery. Suggested cadence: weekly (once). Trigger prompt: "Load our
capability map and check for new signals matching our unmapped capabilities. Refresh
existing tracked groups: update membership, budget confirmation, and window estimates,
and archive anything whose window has closed without conversion."

Name the routine `chet-cluster-discovery` so `/schedule list` stays readable once you're
running more than one persona.

**Durability note:** scheduled Claude Code routines are session-bound and can lapse when
a session ends or after several days idle. If the routine stops firing, just re-ask Claude
to recreate it with the same name and cadence. For a routine you don't want to babysit,
consider migrating it to a GitHub Actions workflow on a cron trigger instead -- more setup
up front, but it survives independent of any Claude session.

**Preferred pattern -- point the routine at your repo instead of pasting everything in.**
If your `customization/my-capture-config.json` lives in a GitHub repo (this one, your
fork, or your own), set the routine's source to that repo and keep the CCR prompt itself
thin: "Read `Plugins/capture-team-open/skills/chet-cluster-discovery/SKILL.md` and
`customization/my-capture-config.json` in this repo, then run today's scan." Claude Code
CCRs re-clone the source repo fresh on every run, so editing the SKILL.md or your
customization file is enough -- you never have to touch the routine's stored prompt.
Save the full trigger prompt above for a repo-less setup (ChatGPT Scheduled Tasks, or a
Claude routine with no git source configured) -- in that case, the "keep both in sync"
habit below still applies.

This is often run as part of a pipeline with Kipp and Ben -- see
[`Workflows/ben-signal-delivery.md`](ben-signal-delivery.md) for the full sequence.

**Three habits worth keeping once the routine is live:**

- **Short-circuit on empty.** Before Chet runs the full refresh, have it check for new
  signals matching your unmapped capabilities first -- if there's nothing new, post "0 new
  signals" and exit rather than burning a run on nothing.
- **The routine's stored prompt is a frozen copy, not a live link back to your files.**
  If you edit `customization/my-capture-config.json` or change how you're prompting Chet,
  update the scheduled routine's prompt too -- editing the repo alone won't change what
  the next scheduled run actually does. (Skip this if you're using the repo-container
  pattern above -- that's the whole point of it.)
- **End every run with a summary, not a raw dump.** A short notification (groups
  refreshed, anything flagged for manual review) is more useful than the full output --
  save the full record for wherever Chet already writes it.

---

## Option B -- ChatGPT Scheduled Tasks

Requires ChatGPT Plus or higher and the SKILL.md file uploaded to a project (Settings >
Tasks, or "Ask ChatGPT to schedule this").

1. Open a conversation with Chet's `SKILL.md` uploaded (see
   [`Skills/README.md`](../Skills/README.md) for upload steps)
2. Say: "Schedule this to run weekly (once) and use this prompt each time: [trigger
   prompt above]"
3. Confirm the task in Settings > Tasks -- ChatGPT will show you the next run time

ChatGPT Scheduled Tasks can't write directly to your CRM or Drive the way a Claude Code
routine with MCP access can -- Chet's output will need a manual copy/paste step unless
you've connected the equivalent tools.

---

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit [compoundleverage.com](https://compoundleverage.com).
