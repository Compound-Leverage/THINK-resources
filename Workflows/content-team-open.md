# Content Team (content-team-open) -- Automation Setup

How to put Rohit, Ann, Joanna, Justin, Amy, Josh, Jay, Cal, and Sal on a recurring
schedule instead of running them by hand. Two options depending on your platform:
Claude's scheduled routines, or ChatGPT's Scheduled Tasks. Pick one -- you don't need
both.

Install the plugin and fill in `customization/my-content-sources.json` (and
`customization/my-brand-guidelines.md`) first. Automation just runs the same prompts
from [`Prompts/content-team-open.md`](../Prompts/content-team-open.md) on a timer.

---

## Option A -- Claude scheduled routine

Requires Claude Code with the plugin installed. Use the `/schedule` command (or ask
Claude to "set up a scheduled routine") to create each of these:

| Persona | Suggested cadence | Trigger prompt |
|---|---|---|
| Rohit -- Intel Scanner | Weekly | "Scan Reddit, industry news, YouTube, and Google's People Also Ask for the strongest content signals in our space this week, plus our own platform performance data, and write the top scored topic cards to our content database. Flag any signal you're not confident about instead of inflating its score." |
| Ann -- Newsletter Editor | Weekly, after Intel Scanner | "Take this week's top-scoring topic card and draft a WARM edition of our newsletter for engaged subscribers and a COLD edition for new subscribers, translated through our methodology framework. Post both as drafts to our newsletter platform, don't send them live." |
| Cal -- Weekly Brief | Weekly, last | "Pull together everything the content skills produced this week and give me one page: what happened, what's pending, and what needs my decision. Overwrite last week's brief, don't append to it." |
| Jay -- Theme Proposer | Monthly, at month-end | "Based on our strongest signal clusters and current offer this month, propose 3 genuinely distinct content themes for next month, each scored against our weighting, and write them as Pending records in our theme proposals database for me to approve." |
| Joanna -- Blog Writer | Weekly, after Intel Scanner | "Take this week's top signal and write two long-form blog posts from it, one in our practitioner ICP voice and one in our org-buyer ICP voice, so neither reads generic. End each post with the CTA style we've configured for that ICP." |
| Josh -- Intelligence Brief | Weekly, after Intel Scanner | "Filter this week's topic cards to only the ones meeting our proof-gate threshold, then draft a Leader edition and a Strategist edition of our intelligence brief. Flag any org-buyer-relevant topic so our BD team can follow up on it." |
| Justin -- LinkedIn Content | Weekly, after Intel Scanner | "Generate a full week of LinkedIn posts for our personal brand page, company page, and product page from this week's signal stack, matching each persona's configured posting cadence. Combine this week's posts into one queue file, grouped by persona and posting day." |
| Amy -- YouTube Scripts | Weekly, after Intelligence Brief | "Here's our research file and this week's brief, write a 4-5 minute YouTube script with 2-3 title options, 2-3 hook variants, a signal walkthrough, and a CTA close. Check that the script actually runs 4-5 minutes read aloud before you finish." |
| Sal -- Course Builder | On-demand, per course brief | "Here's my course brief for [topic], build the complete course: outline, start-here module, lessons, exercises, capstone, and index, ready to paste into [our course platform]. Run your final consistency pass across all modules and flag anything missing from my brief instead of inventing content to fill the gap." |

Name each routine after the persona (e.g. `rohit-intel-scanner`) so `/schedule list`
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
`Plugins/content-team-open/skills/rohit-master-intel-scan/SKILL.md` and your
`customization/` files in this repo, then run this week's scan." Claude Code CCRs
re-clone the source repo fresh on every run, so editing the SKILL.md or your
customization files is enough -- you never have to touch the routine's stored prompt.
Save the full trigger prompts in the table above for a repo-less setup (ChatGPT Scheduled
Tasks, or a Claude routine with no git source configured) -- in that case, the "keep both
in sync" habit below still applies.

**Optional -- run as a pipeline:** the 9 roles don't all sit at the same dependency
level, so don't just chain them in list order. Based on what each SKILL.md actually reads
and writes:

1. **Rohit (Intel Scanner) runs first.** Every other skill in this plugin reads its topic
   input from `topic-cards.json`, so nothing downstream should start before this run
   lands.
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
   cycle finishing.

Two roles sit outside this weekly chain entirely: **Jay (Theme Proposer)** runs on its
own month-end cadence off accumulated topic cards and engagement signals, not gated into
the weekly cycle. **Sal (Course Builder)** is fully standalone -- triggered by dropping a
new course brief, with no dependency on any other skill's output.

**Three habits worth keeping once a routine is live:**

- **Short-circuit on empty.** Before Rohit writes topic cards downstream skills will
  read, have it check whether anything actually cleared the scoring threshold this week --
  if not, post "no new signals" and exit rather than sending five other skills to work
  off a stale or empty topic card set.
- **The routine's stored prompt is a frozen copy, not a live link back to your files.**
  If you edit `customization/my-content-sources.json` or `my-brand-guidelines.md`, or
  change how you're prompting a persona, update the scheduled routine's prompt too --
  editing the repo alone won't change what the next scheduled run actually does. (Skip
  this if you're using the repo-container pattern above -- that's the whole point of it.)
- **End every run with a summary, not a raw dump.** A short notification (topics scored,
  drafts written, anything flagged for review) is more useful than the full output --
  save the full record for wherever each skill already writes it (your content DB, your
  local `output/{week}/` folder).

---

## Option B -- ChatGPT Scheduled Tasks

Requires ChatGPT Plus or higher and the SKILL.md files uploaded to a project (Settings >
Tasks, or "Ask ChatGPT to schedule this").

1. Open a conversation with the persona's `SKILL.md` uploaded (see
   [`Skills/README.md`](../Skills/README.md) for upload steps)
2. Say: "Schedule this to run [cadence from the table above] and use this prompt each
   time: [trigger prompt from the table above]"
3. Confirm the task in Settings > Tasks -- ChatGPT will show you the next run time

ChatGPT Scheduled Tasks can't write directly to your content database, newsletter
platform, or theme proposals database the way a Claude Code routine with MCP access can
-- Rohit, Ann, Joanna, Justin, Josh, and Jay's outputs will need a manual copy/paste step
unless you've connected the equivalent tools. The pipeline gating in Option A (Rohit
before the parallel writers, Cal last) also has to be run manually in that order, since
ChatGPT Scheduled Tasks don't gate one task's start on another task's completion.

---

## Questions

Contact [marvin@compoundleverage.co](mailto:marvin@compoundleverage.co) or visit [compoundleverage.com](https://compoundleverage.com).
