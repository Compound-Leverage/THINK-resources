# Jason, QA Reviewer (ops-team-open) -- Automation Setup

How to put Jason on a recurring schedule instead of running him by hand. Two options
depending on your platform: Claude's scheduled routines, or ChatGPT's Scheduled Tasks.
Pick one, you don't need both.

Install the plugin and fill in `customization/my-site-standards.md` first. Automation
just runs the same prompt below on a timer.

---

## Option A: Claude scheduled routine

Requires Claude Code with the plugin installed. Use the `/schedule` command (or ask
Claude to "set up a scheduled routine") to create this:

| Trigger | Suggested cadence | Trigger prompt |
|---|---|---|
| Post-deploy audit | After each deploy | "Run a post-deploy audit of our site: H1 consistency, SEO, our copy terminology table, and broken links. Cite the exact page and section for every finding, open PRs for anything rule-based, and flag judgment calls to me instead of guessing." |

Jason's role is independent rather than part of a strict pipeline with Eric or Jenny, so
there's no required run order between them, set this up on its own cadence.

Name the routine after the persona and function (e.g. `jason-qa-audit`) so
`/schedule list` stays readable once you're running more than one.

**Durability note:** scheduled Claude Code routines are session-bound and can lapse when
a session ends or after several days idle. If a routine stops firing, just re-ask Claude
to recreate it with the same name and cadence. For a routine you don't want to babysit,
consider migrating it to a GitHub Actions workflow on a cron trigger instead, more setup
up front, but it survives independent of any Claude session.

**Preferred pattern, point the routine at your repo instead of pasting everything in.**
If your `customization/my-site-standards.md` lives in a GitHub repo (this one, your fork,
or your own), set the routine's source to that repo and keep the CCR prompt itself thin:
"Read `Plugins/ops-team-open/skills/jason-qa-reviewer/SKILL.md` and your
`customization/` files in this repo, then run today's check." Claude Code CCRs re-clone
the source repo fresh on every run, so editing the SKILL.md or your customization file is
enough, you never have to touch the routine's stored prompt. Save the full trigger
prompt in the table above for a repo-less setup (ChatGPT Scheduled Tasks, or a Claude
routine with no git source configured), in that case, the "keep both in sync" habit below
still applies.

**Three habits worth keeping once a routine is live:**

- **Short-circuit on empty.** Before this runs the full audit, have it check whether
  there's anything new to review first, if there's nothing since the last run, post
  "nothing to flag" and exit rather than burning a run on nothing.
- **The routine's stored prompt is a frozen copy, not a live link back to your files.**
  If you edit `customization/my-site-standards.md`, or change how you're prompting
  Jason, update the scheduled routine's prompt too, editing the repo alone won't change
  what the next scheduled run actually does. (Skip this if you're using the
  repo-container pattern above, that's the whole point of it.)
- **End every run with a summary, not a raw dump.** A short notification (what was
  checked, what was fixed, what's flagged) is more useful than the full output, save the
  full record for wherever the PR or changelog already lives.

**Nothing here should auto-apply a fix to production.** Jason opens PRs for rule-based
fixes but flags judgment calls to you instead of guessing. Findings get surfaced for
review, a human approves before anything ships. Keep that gate in place if you customize
any of these prompts.

---

## Option B: ChatGPT Scheduled Tasks

Requires ChatGPT Plus or higher and the SKILL.md file uploaded to a project (Settings >
Tasks, or "Ask ChatGPT to schedule this").

1. Open a conversation with Jason's `SKILL.md` uploaded (see
   [`Skills/README.md`](../Skills/README.md) for upload steps)
2. Say: "Schedule this to run [cadence from the table above] and use this prompt each
   time: [trigger prompt from the table above]"
3. Confirm the task in Settings > Tasks, ChatGPT will show you the next run time

ChatGPT Scheduled Tasks can't open PRs or write directly to your repo the way a Claude
Code routine with MCP access can, Jason's outputs will need a manual copy/paste step
unless you've connected the equivalent tools.

---

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit [compoundleverage.com](https://compoundleverage.com).
