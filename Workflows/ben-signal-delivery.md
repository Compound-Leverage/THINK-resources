# Ben (capture-team-open) -- Automation Setup

How to put Ben on a recurring schedule instead of running him by hand. Two options
depending on your platform: Claude's scheduled routines, or ChatGPT's Scheduled Tasks.
Pick one -- you don't need both.

Install the plugin and fill in `customization/my-capture-config.json` first. Automation
just runs the same prompt from [`Prompts/capture-team-open.md`](../Prompts/capture-team-open.md)
on a timer.

---

## Option A -- Claude scheduled routine

Requires Claude Code with the plugin installed. Use the `/schedule` command (or ask
Claude to "set up a scheduled routine") to create this:

Ben -- Signal Delivery. Suggested cadence: daily or on new signal. Trigger prompt: "Read
the new, unactioned signals in our signal inbox and draft a client-ready intelligence
brief for any client with a new signal, using our brief section structure. Flag
exceptions instead of guessing."

Name the routine `ben-signal-delivery` so `/schedule list` stays readable once you're
running more than one persona.

**Durability note:** scheduled Claude Code routines are session-bound and can lapse when
a session ends or after several days idle. If the routine stops firing, just re-ask Claude
to recreate it with the same name and cadence. For a routine you don't want to babysit,
consider migrating it to a GitHub Actions workflow on a cron trigger instead -- more setup
up front, but it survives independent of any Claude session.

**Preferred pattern -- point the routine at your repo instead of pasting everything in.**
If your `customization/my-capture-config.json` lives in a GitHub repo (this one, your
fork, or your own), set the routine's source to that repo and keep the CCR prompt itself
thin: "Read `Plugins/capture-team-open/skills/ben-signal-delivery/SKILL.md` and
`customization/my-capture-config.json` in this repo, then run today's scan." Claude Code
CCRs re-clone the source repo fresh on every run, so editing the SKILL.md or your
customization file is enough -- you never have to touch the routine's stored prompt.
Save the full trigger prompt above for a repo-less setup (ChatGPT Scheduled Tasks, or a
Claude routine with no git source configured) -- in that case, the "keep both in sync"
habit below still applies.

**Optional -- run all three as a pipeline instead of independently:** Ben's brief is the
last step in the sequence, so it's the one that benefits most from freshness upstream. If
you want Ben's brief to always reflect the freshest clusters and contacts, chain all
three personas in one routine instead of three separate ones: Chet refreshes clusters
first, Kipp intakes and classifies next, Ben drafts briefs last. Each step should
validate the previous one's output landed before continuing, the same way you'd gate any
multi-step pipeline. See `Workflows/chet-cluster-discovery.md` and
`Workflows/kipp-crm-intake.md` for those two personas' individual setup.

**Three habits worth keeping once the routine is live:**

- **Short-circuit on empty.** Before Ben drafts anything, have it check the signal inbox
  first -- if there are no new, unactioned signals, post "0 briefs" and exit rather than
  burning a run on nothing.
- **The routine's stored prompt is a frozen copy, not a live link back to your files.**
  If you edit `customization/my-capture-config.json` or change how you're prompting Ben,
  update the scheduled routine's prompt too -- editing the repo alone won't change what
  the next scheduled run actually does. (Skip this if you're using the repo-container
  pattern above -- that's the whole point of it.)
- **End every run with a summary, not a raw dump.** A short notification (briefs
  drafted, anything flagged for manual review) is more useful than the full output --
  save the full record for wherever Ben already writes it (your Drive folder).

---

## Option B -- ChatGPT Scheduled Tasks

Requires ChatGPT Plus or higher and the SKILL.md file uploaded to a project (Settings >
Tasks, or "Ask ChatGPT to schedule this").

1. Open a conversation with Ben's `SKILL.md` uploaded (see
   [`Skills/README.md`](../Skills/README.md) for upload steps)
2. Say: "Schedule this to run daily or on new signal and use this prompt each time:
   [trigger prompt above]"
3. Confirm the task in Settings > Tasks -- ChatGPT will show you the next run time

ChatGPT Scheduled Tasks can't write directly to your Drive the way a Claude Code routine
with MCP access can -- Ben's output will need a manual copy/paste step unless you've
connected the equivalent tools.

---

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit [compoundleverage.com](https://compoundleverage.com).
