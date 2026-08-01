# Cal (content-team) -- Automation Setup

How to put Cal on a recurring schedule instead of running her by hand. Two options
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
| Cal -- Weekly Brief | Weekly, last | "Pull together everything the content skills produced this week and give me one page: what happened, what's pending, and what needs my decision. Overwrite last week's brief, don't append to it." |

Name the routine after the persona (e.g. `cal-weekly-brief`) so `/schedule list`
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
`Plugins/content-team/skills/cal-weekly-brief/SKILL.md` and your `customization/`
files in this repo, then pull together this week's brief." Claude Code CCRs re-clone the
source repo fresh on every run, so editing the SKILL.md or your customization files is
enough -- you never have to touch the routine's stored prompt. Save the full trigger
prompt in the table above for a repo-less setup (ChatGPT Scheduled Tasks, or a Claude
routine with no git source configured) -- in that case, the "keep both in sync" habit
below still applies.

**Pipeline note -- Cal runs last.** The 9 roles in this plugin don't all sit at the same
dependency level, so if you're running more than one, don't just chain them in list
order. Based on what each SKILL.md actually reads and writes:

1. **Rohit (Intel Scanner) runs first.** Every other skill in this plugin reads its topic
   input from `topic-cards.json`, so nothing downstream -- including Cal -- should start
   before this run lands.
2. **Parallel gate once Rohit's output exists:** Ann (Newsletter Editor), Joanna (Blog
   Writer), Justin (LinkedIn Content), and Josh (Intelligence Brief) all read from the
   same topic cards independently -- they can run at the same time instead of one after
   another.
3. **Amy (YouTube Scripts) reads a research file plus "the current weekly brief."**
   Sequence her after Josh's Intelligence Brief lands so there's real brief content to
   parse, or point her at the raw topic cards directly if you'd rather fold her into the
   same parallel gate as step 2.
4. **Cal (Weekly Brief) runs last.** She reads everything the other content skills (and,
   if installed, the BD Team and Fulfillment plugins) produced that week and synthesizes
   it into the one owner-facing page -- gate her run behind every other step in the
   cycle finishing. If she runs before the others land, her page will be missing
   whatever hasn't finished yet.

Two roles sit outside this weekly chain entirely: **Jay (Theme Proposer)** runs on its
own month-end cadence off accumulated topic cards and engagement signals, not gated into
the weekly cycle. **Sal (Course Builder)** is fully standalone -- triggered by dropping a
new course brief, with no dependency on any other skill's output. Cal doesn't need to
wait on either of them.

**Three habits worth keeping once a routine is live:**

- **Short-circuit on empty.** If nothing meaningful happened this week (no topic cards
  cleared the scoring threshold, no downstream drafts written), have Cal say so plainly
  in the brief rather than padding out a page to look busy.
- **The routine's stored prompt is a frozen copy, not a live link back to your files.**
  If you edit `customization/my-content-sources.json` or `my-brand-guidelines.md`, or
  change how you're prompting Cal, update the scheduled routine's prompt too -- editing
  the repo alone won't change what the next scheduled run actually does. (Skip this if
  you're using the repo-container pattern above -- that's the whole point of it.)
- **End every run with a summary, not a raw dump.** A short notification that the brief
  is ready (and where) is more useful than pasting the full page into the notification
  itself -- save the full page for wherever it's meant to live (Notion page, or your
  local file path).

---

## Option B -- ChatGPT Scheduled Tasks

Requires ChatGPT Plus or higher and the SKILL.md file uploaded to a project (Settings >
Tasks, or "Ask ChatGPT to schedule this").

1. Open a conversation with Cal's `SKILL.md` uploaded (see
   [`Skills/README.md`](../Skills/README.md) for upload steps)
2. Say: "Schedule this to run weekly, last, and use this prompt each time: [trigger
   prompt from the table above]"
3. Confirm the task in Settings > Tasks -- ChatGPT will show you the next run time

ChatGPT Scheduled Tasks can't write directly to a Notion page the way a Claude Code
routine with MCP access can -- Cal's brief will need a manual copy/paste step unless
you've connected the equivalent tools. The pipeline gating above (Rohit before the
parallel writers, Cal last) also has to be run manually in that order, since ChatGPT
Scheduled Tasks don't gate one task's start on another task's completion -- there's no
automatic way to hold Cal's task until the others are done.

---

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit [compoundleverage.com](https://compoundleverage.com).
