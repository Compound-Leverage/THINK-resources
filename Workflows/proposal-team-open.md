# Proposal Team (proposal-team-open) - Automation Setup

How to put Maya, Chase, Priya, Porter, Quinn, Diego, and Blair on a recurring schedule
instead of running the pipeline by hand. Two options depending on your platform: Claude's
scheduled routines, or ChatGPT's Scheduled Tasks. Pick one - you don't need both.

Install the plugin and fill in `customization/my-pricing-model.json`,
`customization/my-company-profile.json`, `customization/my-case-studies.json`,
`customization/my-brand-guidelines.md`, and (if you handle grant/funder deals)
`customization/my-bid-sizing.json` first. Automation just runs the same prompts from
[`Prompts/proposal-team-open.md`](../Prompts/proposal-team-open.md) on a timer or a
trigger.

---

## Option A - Claude scheduled routine

Requires Claude Code with the plugin installed. Use the `/schedule` command (or ask
Claude to "set up a scheduled routine") to create each of these.

This is a gated pipeline tied to specific deals, not a pure time-based scan - only Maya's
role genuinely fits a recurring clock. Chase, Priya, Porter, Quinn, and Diego each only
make sense once the prior phase's package has been approved at its gate, and Blair only
makes sense once a deal reaches Proposal Stage for a grant/funder category. Set those five
up as on-demand prompts you (or Maya) fire at the right moment, not fixed cadences.

| Persona | Suggested cadence | Trigger prompt |
|---|---|---|
| Maya - Proposal Engine Lead | Daily (pipeline scan) | "Check our deal pipeline for opportunities marked qualified but not yet started in the proposal workflow, and any phase that's been sitting at my approval gate for more than [N] days. Report status only - don't advance anything without my gate approval." |
| Chase - Proposal Researcher | On new qualified opportunity (not a fixed clock) | "A new opportunity just cleared qualification: [prospect name]. Research it and give me a Discovery Brief with a Go/No-Go recommendation before we spend anything further on this deal." |
| Priya - Proposal Analyst | On Discovery Brief approval (not a fixed clock) | "Here's the approved Discovery Brief for [prospect name]. Classify the deal, score our capability fit, build a conservative ROI model, and configure pricing from our pricing model." |
| Porter - Proposal Strategist | On Assessment Package approval (not a fixed clock) | "Using the Discovery Brief and Assessment Package for [prospect name], develop our competitive positioning, 3-5 win themes, and pick our top 3 matching case studies." |
| Quinn - Proposal Writer | On Strategy Package approval (not a fixed clock) | "Draft the full proposal for [prospect name] from the Discovery Brief, Assessment Package, and Strategy Package. Use the [Government / Commercial / Simple / SOW] template and mark any gap as a placeholder instead of assuming an answer." |
| Diego - Proposal QA | On draft completion (not a fixed clock) | "Run a Standard QA pass on the [prospect name] proposal draft - requirements, consistency, compliance, and methodology - and give me a PASS/WARNING/FAIL verdict with exact section citations." |
| Blair - Pitch Development | On deal reaching Proposal Stage for a grant/funder category (not a fixed clock) | "[Prospect name]'s deal just moved to Proposal Stage and it's a [funder category] opportunity. Convert it into a customized funder proposal using our bid-sizing rules and real case studies, and hold it for my approval before any outreach." |

Name each routine after the persona (e.g. `maya-proposal-engine-lead`,
`chase-proposal-researcher`) so `/schedule list` stays readable once you're running more
than one.

**Durability note:** scheduled Claude Code routines are session-bound and can lapse when
a session ends or after several days idle. If a routine stops firing, just re-ask Claude
to recreate it with the same name and cadence. For a routine you don't want to babysit,
consider migrating it to a GitHub Actions workflow on a cron trigger instead - more setup
up front, but it survives independent of any Claude session.

**Preferred pattern - point the routine at your repo instead of pasting everything in.**
If your `customization/` files live in a GitHub repo (this one, your fork, or your own),
set Maya's routine source to that repo and keep the CCR prompt itself thin: "Read
`Plugins/proposal-team-open/skills/maya-proposal-engine-lead/SKILL.md` and your
`customization/` files in this repo, then run today's pipeline scan." Claude Code CCRs
re-clone the source repo fresh on every run, so editing the SKILL.md or your
customization files is enough - you never have to touch the routine's stored prompt.
Save the full trigger prompts in the table above for a repo-less setup (ChatGPT Scheduled
Tasks, or a Claude routine with no git source configured) - in that case, the "keep both
in sync" habit below still applies.

**Optional - run as a pipeline:** Maya's own job is to sequence Chase, Priya, Porter,
Quinn, and Diego in dependency order - research feeds assessment, assessment feeds
strategy, strategy feeds the draft, the draft feeds QA - gating at your approval between
each phase, the same way you'd gate any multi-step pipeline. If you want the whole
sequence to run as one routine instead of five separate ones, schedule Maya alone and let
her dispatch the rest; each phase should confirm the prior phase's package landed and got
your gate approval before continuing. Blair runs on a separate track for grant/funder
deals only - it does not feed into or depend on Maya's chain, and Maya's chain does not
feed into it.

**Three habits worth keeping once a routine is live:**

- **Short-circuit on empty.** Before Maya runs a full pipeline scan, have it check for
  qualified-but-unstarted opportunities and stalled gates first - if there's nothing
  waiting, post "nothing new" and exit rather than burning a run on nothing.
- **The routine's stored prompt is a frozen copy, not a live link back to your files.**
  If you edit `customization/my-pricing-model.json`, `my-company-profile.json`, or any
  other customization file, update the scheduled routine's prompt too - editing the repo
  alone won't change what the next scheduled run actually does. (Skip this if you're
  using the repo-container pattern above - that's the whole point of it.)
- **End every run with a summary, not a raw dump.** A short notification (which deals
  moved phase, which gates are awaiting your approval, anything flagged for manual
  review) is more useful than the full Discovery Brief or proposal draft - save the full
  document for wherever Quinn's drafts already live (your CRM, your Drive folder).

---

## Option B - ChatGPT Scheduled Tasks

Requires ChatGPT Plus or higher and the SKILL.md files uploaded to a project (Settings >
Tasks, or "Ask ChatGPT to schedule this").

1. Open a conversation with the persona's `SKILL.md` uploaded (see
   [`Skills/README.md`](../Skills/README.md) for upload steps)
2. Say: "Schedule this to run [cadence from the table above, or 'when I tell you to' for
   the gate-triggered roles] and use this prompt each time: [trigger prompt from the
   table above]"
3. Confirm the task in Settings > Tasks - ChatGPT will show you the next run time

ChatGPT Scheduled Tasks can't write directly to your CRM or Drive the way a Claude Code
routine with MCP access can - Priya's pricing lookups, Porter's case study matching, and
Quinn and Diego's document outputs will need a manual copy/paste step unless you've
connected the equivalent tools.

---

## Questions

Contact [marvin@compoundleverage.co](mailto:marvin@compoundleverage.co) or visit [compoundleverage.com](https://compoundleverage.com).
