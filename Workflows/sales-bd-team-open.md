# Sales BD Team (sales-bd-team-open) - Automation Setup

How to put Lori, Alex, and Sarah on a recurring schedule instead of running them by hand.
Two options depending on your platform: Claude's scheduled routines, or ChatGPT's
Scheduled Tasks. Pick one - you don't need both.

Install the plugin and fill in `customization/my-icp-profile.json`,
`customization/my-outreach-config.json`, and `customization/my-company-profile.json`
first. Automation just runs the same prompts from
[`Prompts/sales-bd-team-open.md`](../Prompts/sales-bd-team-open.md) on a timer.

---

## Option A - Claude scheduled routine

Requires Claude Code with the plugin installed. Use the `/schedule` command (or ask
Claude to "set up a scheduled routine") to create each of these:

| Persona | Suggested cadence | Trigger prompt |
|---|---|---|
| Lori - Lead Scout | Daily, weekdays | "Scan our configured signal sources for candidates showing an active intent signal against our ICP profile(s). Apply our auto-exclude disqualifiers to what comes back, score what survives, and write today's qualified leads to CSV with a routing flag, the way we configured it." |
| Alex - BD Research | Daily, weekdays | "Take the leads Lori sourced today, enrich each one with our connected enrichment tool, and label them against our ICP profile. Flag anything missing a required field instead of guessing it, and write the completed records to our pipeline and contacts databases." |
| Sarah - BD Execution | Several times a day for inbound response; once daily for scheduled outreach | "Score today's enriched records against our scoring dimensions and draft outreach for anything above threshold. Hold drafts for my approval if this is a new segment, per our approval gate. For already-approved segments, send from our configured address, log the activity, and apply our follow-up cadence." |

Name each routine after the persona (e.g. `lori-lead-scout`) so `/schedule list` stays
readable once you're running more than one.

**Durability note:** scheduled Claude Code routines are session-bound and can lapse when
a session ends or after several days idle. If a routine stops firing, just re-ask Claude
to recreate it with the same name and cadence. For a routine you don't want to babysit,
consider migrating it to a GitHub Actions workflow on a cron trigger instead - more setup
up front, but it survives independent of any Claude session.

**Preferred pattern - point the routine at your repo instead of pasting everything in.**
If your `customization/my-icp-profile.json` and `my-outreach-config.json` live in a
GitHub repo (this one, your fork, or your own), set the routine's source to that repo and
keep the CCR prompt itself thin: "Read
`Plugins/sales-bd-team-open/skills/lori-prospect-scout/SKILL.md` and your
`customization/` files in this repo, then run today's sourcing pass." Claude Code CCRs
re-clone the source repo fresh on every run, so editing the SKILL.md or your
customization files is enough - you never have to touch the routine's stored prompt. Save
the full trigger prompts in the table above for a repo-less setup (ChatGPT Scheduled
Tasks, or a Claude routine with no git source configured) - in that case, the "keep both
in sync" habit below still applies.

**Optional - run all three as a pipeline instead of independently:** Lori sources leads
first, Alex enriches and labels them next, Sarah scores and executes outreach last. Chain
them in one routine if you want Sarah always working off the freshest enriched records
instead of whatever happens to be sitting in your CRM. Each step should validate the
previous one's output landed before continuing, the same way you'd gate any multi-step
pipeline.

**Three habits worth keeping once a routine is live:**

- **Short-circuit on empty.** Before Alex runs full enrichment, have it check whether
  Lori actually produced any new leads today - if there's nothing new, post "0 leads" and
  exit rather than burning a run on nothing.
- **The routine's stored prompt is a frozen copy, not a live link back to your files.**
  If you edit `customization/my-icp-profile.json` or `customization/my-outreach-config.json`,
  or change how you're prompting a persona, update the scheduled routine's prompt too -
  editing the repo alone won't change what the next scheduled run actually does. (Skip
  this if you're using the repo-container pattern above - that's the whole point of it.)
- **End every run with a summary, not a raw dump.** A short notification (leads sourced,
  records enriched, sends held vs. sent, anything escalated) is more useful than the full
  output - save the full record for wherever Alex/Sarah already write it (your CRM).

---

## Option B - ChatGPT Scheduled Tasks

Requires ChatGPT Plus or higher and the SKILL.md files uploaded to a project (Settings >
Tasks, or "Ask ChatGPT to schedule this").

1. Open a conversation with the persona's `SKILL.md` uploaded (see
   [`Skills/README.md`](../Skills/README.md) for upload steps)
2. Say: "Schedule this to run [cadence from the table above] and use this prompt each
   time: [trigger prompt from the table above]"
3. Confirm the task in Settings > Tasks - ChatGPT will show you the next run time

ChatGPT Scheduled Tasks can't write directly to your enrichment tool or CRM the way a
Claude Code routine with MCP access can - Alex and Sarah's outputs will need a manual
copy/paste step unless you've connected the equivalent tools.

**Keep the approval step manual either way.** Sarah's approval gate in
`customization/my-outreach-config.json` is a plugin default, not a platform feature.
Whether you're running her via a Claude scheduled routine or a ChatGPT Scheduled Task,
keep a human reviewing the draft before any real outreach email goes out - never let a
scheduled run auto-send external outreach without your review, new segment or not.

---

## Questions

Contact [marvin@compoundleverage.co](mailto:marvin@compoundleverage.co) or visit [compoundleverage.com](https://compoundleverage.com).
