# Eric, Infrastructure Lead (ops-team) -- Automation Setup

How to put Eric on a recurring schedule instead of running him by hand. Two options
depending on your platform: Claude's scheduled routines, or ChatGPT's Scheduled Tasks.
Pick one, you don't need both.

Install the plugin and fill in `customization/my-infra-config.json` first. Automation
just runs the same prompts below on a timer.

---

## Option A: Claude scheduled routine

Requires Claude Code with the plugin installed. Use the `/schedule` command (or ask
Claude to "set up a scheduled routine") to create each of these:

| Trigger | Suggested cadence | Trigger prompt |
|---|---|---|
| Deploy check | After each deploy | "Check our latest deploy against our performance thresholds and caching rules, and open a PR to staging for any config-only fixes you find. Flag anything that needs a DNS change or a production promotion instead of acting on it." |
| Recurring audit | Weekly | "Audit our GitHub Actions for failures or drift, check our caching rules and DNS state against our config, and tell me what needs my sign-off before it touches production." |

Eric's role is independent rather than part of a strict pipeline with Jason or Jenny, so
there's no required run order between them, set this up on its own cadence.

Name each routine after the persona and function (e.g. `eric-deploy-check`,
`eric-infra-audit`) so `/schedule list` stays readable once you're running more than one.

**Durability note:** scheduled Claude Code routines are session-bound and can lapse when
a session ends or after several days idle. If a routine stops firing, just re-ask Claude
to recreate it with the same name and cadence. For a routine you don't want to babysit,
consider migrating it to a GitHub Actions workflow on a cron trigger instead, more setup
up front, but it survives independent of any Claude session.

**Preferred pattern, point the routine at your repo instead of pasting everything in.**
If your `customization/my-infra-config.json` lives in a GitHub repo (this one, your fork,
or your own), set the routine's source to that repo and keep the CCR prompt itself thin:
"Read `Plugins/ops-team/skills/eric-infrastructure/SKILL.md` and your
`customization/` files in this repo, then run today's check." Claude Code CCRs re-clone
the source repo fresh on every run, so editing the SKILL.md or your customization file is
enough, you never have to touch the routine's stored prompt. Save the full trigger
prompts in the table above for a repo-less setup (ChatGPT Scheduled Tasks, or a Claude
routine with no git source configured), in that case, the "keep both in sync" habit below
still applies.

This is especially relevant for Eric: GitHub Actions is already one of Infra Lead's own
tools, so a cron-triggered workflow fits naturally alongside the deploy and drift checks
it's already auditing.

**Three habits worth keeping once a routine is live:**

- **Short-circuit on empty.** Before this runs the full audit, have it check whether
  there's anything new to review first, if there's nothing since the last run, post
  "nothing to flag" and exit rather than burning a run on nothing.
- **The routine's stored prompt is a frozen copy, not a live link back to your files.**
  If you edit `customization/my-infra-config.json`, or change how you're prompting Eric,
  update the scheduled routine's prompt too, editing the repo alone won't change what the
  next scheduled run actually does. (Skip this if you're using the repo-container
  pattern above, that's the whole point of it.)
- **End every run with a summary, not a raw dump.** A short notification (what was
  checked, what was fixed, what's flagged) is more useful than the full output, save the
  full record for wherever the PR or changelog already lives.

**Nothing here should auto-apply a fix to production.** Eric opens config-fix PRs to
staging but routes DNS changes and production promotions to you. Findings get surfaced
for review, a human approves before anything ships. Keep that gate in place if you
customize any of these prompts.

---

## Option B: ChatGPT Scheduled Tasks

Requires ChatGPT Plus or higher and the SKILL.md file uploaded to a project (Settings >
Tasks, or "Ask ChatGPT to schedule this").

1. Open a conversation with Eric's `SKILL.md` uploaded (see
   [`Skills/README.md`](../Skills/README.md) for upload steps)
2. Say: "Schedule this to run [cadence from the table above] and use this prompt each
   time: [trigger prompt from the table above]"
3. Confirm the task in Settings > Tasks, ChatGPT will show you the next run time

ChatGPT Scheduled Tasks can't open PRs, query GitHub Actions, or write directly to your
repo the way a Claude Code routine with MCP access can, Eric's outputs will need a
manual copy/paste step unless you've connected the equivalent tools. This is a
particularly weak fit for Eric specifically: GitHub Actions, DNS, and CDN work assume a
connected dev environment that ChatGPT Scheduled Tasks doesn't have, so treat its output
as a written recommendation for you to act on by hand rather than an audit that can open
a PR or touch config on its own.

---

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit [compoundleverage.com](https://compoundleverage.com).
