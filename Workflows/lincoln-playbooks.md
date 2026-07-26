# Lincoln (fulfillment-open) -- Automation Setup

How to put Lincoln on a schedule, or hook him to the event that actually triggers his
work. One option depending on your platform: Claude's scheduled routines, or ChatGPT's
Scheduled Tasks. Pick one -- you don't need both.

Install the plugin and fill in `customization/my-fulfillment-config.json` first (your
client records DB ID, and a base template populated for each playbook type you support).
Automation just runs the same prompts from
[`Prompts/fulfillment-open.md`](../Prompts/fulfillment-open.md) on a timer or in response
to an event.

Lincoln's work is triggered by something happening to a client, not by the clock, most of
the time. A new client gets onboarded. An existing client hits a success or expansion
milestone. There isn't a natural daily or weekly cadence for "build a playbook" the way
there is for a CRM intake sweep. Below, most rows are event-triggered. There's also a
recurring-check option if you want a standing sweep that catches milestones your event
trigger might miss.

---

## Option A -- Claude scheduled routine

Requires Claude Code with the plugin installed. Use the `/schedule` command (or ask
Claude to "set up a scheduled routine") to create each of these:

| Persona / trigger | Suggested cadence | Trigger prompt |
|---|---|---|
| Lincoln -- New client onboarding | Event-triggered (run when a new client is signed) | "Using our onboarding playbook framework and [client]'s record in our client records database, build a customized onboarding playbook for them. If a detail isn't in their record, mark it as a gap rather than inventing it." |
| Lincoln -- Success or expansion milestone | Event-triggered (run when a client hits a renewal, health-score change, or usage milestone) | "[Client] just hit [milestone]. Using our [customer success / expansion] playbook framework and their record in our client records database, build a [customer success / expansion] playbook for them. If a detail isn't in their record, mark it as a gap rather than inventing it." |
| Lincoln -- Recurring milestone scan (optional) | Weekly | "Scan our client records database for any active client due for a success or expansion playbook this week -- renewal coming up, usage milestone hit, or engagement stage changed. For each one, build the appropriate playbook using our base framework. If nothing is due, say so and stop." |

Name each routine after the persona and trigger (e.g. `lincoln-onboarding-playbook`,
`lincoln-milestone-scan`) so `/schedule list` stays readable once you're running more than
one.

**Durability note:** scheduled Claude Code routines are session-bound and can lapse when
a session ends or after several days idle. If a routine stops firing, just re-ask Claude
to recreate it with the same name and cadence. For a routine you don't want to babysit,
consider migrating it to a GitHub Actions workflow on a cron trigger instead -- more setup
up front, but it survives independent of any Claude session.

**Preferred pattern -- point the routine at your repo instead of pasting everything in.**
If your `customization/my-fulfillment-config.json` lives in a GitHub repo (this one, your
fork, or your own), set the routine's source to that repo and keep the CCR prompt itself
thin: "Read `Plugins/fulfillment-open/skills/lincoln-playbooks/SKILL.md` and
`customization/my-fulfillment-config.json` in this repo, then run this week's scan."
Claude Code CCRs re-clone the source repo fresh on every run, so editing the SKILL.md or
your customization file is enough -- you never have to touch the routine's stored prompt.
Save the full trigger prompts in the table above for a repo-less setup (ChatGPT Scheduled
Tasks, or a Claude routine with no git source configured) -- in that case, the "keep both
in sync" habit below still applies.

Note that a true event
trigger (new client signed, milestone hit) needs something to notify the routine when
that event happens -- a scheduled recurring scan is the more durable stand-in if you don't
have that wired up yet.

**Three habits worth keeping once a routine is live:**

- **Short-circuit on empty.** Before the recurring scan builds anything, have it check
  whether any client is actually due first -- if nothing is due, post "nothing due" and
  exit rather than burning a run on nothing.
- **The routine's stored prompt is a frozen copy, not a live link back to your files.**
  If you edit `customization/my-fulfillment-config.json` or update a base playbook
  template, update the scheduled routine's prompt too -- editing the repo alone won't
  change what the next scheduled run actually does. (Skip this if you're using the
  repo-container pattern above -- that's the whole point of it.)
- **End every run with a summary, not a raw dump.** A short notification (which client,
  which playbook type, what was flagged as a gap) is more useful than the full playbook
  text -- save the full document for wherever Lincoln already writes it (your Notion or
  Drive destination), and remember the owner still reviews every playbook before it goes
  to the client.

---

## Option B -- ChatGPT Scheduled Tasks

Requires ChatGPT Plus or higher and the SKILL.md file uploaded to a project (Settings >
Tasks, or "Ask ChatGPT to schedule this").

1. Open a conversation with Lincoln's `SKILL.md` uploaded (see
   [`Skills/README.md`](../Skills/README.md) for upload steps)
2. Say: "Schedule this to run [cadence from the table above] and use this prompt each
   time: [trigger prompt from the table above]"
3. Confirm the task in Settings > Tasks -- ChatGPT will show you the next run time

ChatGPT Scheduled Tasks can't read your client records database or write directly to
Notion or Drive the way a Claude Code routine with MCP access can, and it has no way to
detect a real-world event like a new client signing or a milestone being hit. The
event-triggered rows above become "check in and tell me if anything changed" prompts you
run manually, and Lincoln's output will need a manual copy/paste into your client records
system unless you've connected the equivalent tools.

---

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit [compoundleverage.com](https://compoundleverage.com).
