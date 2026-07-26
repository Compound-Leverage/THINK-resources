# Maya (proposal-team-open) -- Automation Setup

How to put Maya, the Proposal Engine Lead, on a recurring schedule instead of running her
by hand. Two options depending on your platform: Claude's scheduled routines, or ChatGPT's
Scheduled Tasks. Pick one - you don't need both.

Install the plugin first. Maya's own pipeline scan doesn't require a customization file,
but the phases she sequences do - `customization/my-pricing-model.json`,
`customization/my-company-profile.json`, `customization/my-case-studies.json`,
`customization/my-brand-guidelines.md`, and (if you handle grant/funder deals)
`customization/my-bid-sizing.json` - so fill those in too before running a full pipeline.
Automation just runs the same prompt from
[`Prompts/proposal-team-open.md`](../Prompts/proposal-team-open.md) on a timer.

---

## Option A - Claude scheduled routine

Requires Claude Code with the plugin installed. Use the `/schedule` command (or ask
Claude to "set up a scheduled routine") to create this.

Maya's role genuinely fits a recurring clock - she's the one checking the pipeline for
what needs attention, not waiting on a single gate.

| Persona | Suggested cadence | Trigger prompt |
|---|---|---|
| Maya - Proposal Engine Lead | Daily (pipeline scan) | "Check our deal pipeline for opportunities marked qualified but not yet started in the proposal workflow, and any phase that's been sitting at my approval gate for more than [N] days. Report status only - don't advance anything without my gate approval." |

Name the routine `maya-proposal-engine-lead` so `/schedule list` stays readable once
you're running more than one.

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
Save the full trigger prompt above for a repo-less setup (ChatGPT Scheduled Tasks, or a
Claude routine with no git source configured) - in that case, the "keep both in sync"
habit below still applies.

**How the pipeline is sequenced - Maya's whole job.** Maya's role is to sequence Chase,
Priya, Porter, Quinn, and Diego in dependency order - research feeds assessment,
assessment feeds strategy, strategy feeds the draft, the draft feeds QA - gating at your
approval between each phase, the same way you'd gate any multi-step pipeline:

- **Chase (Proposal Researcher)** runs first, on a new qualified opportunity (not a fixed
  clock). His Discovery Brief, with its Go/No-Go recommendation, is the input every later
  phase depends on - nothing advances past a NO-GO.
- **Priya (Proposal Analyst)** runs next, on Discovery Brief approval (not a fixed clock).
  She classifies the deal, scores capability fit, builds the ROI model, and configures
  pricing - feeding Porter and Quinn.
- **Porter (Proposal Strategist)** runs next, on Assessment Package approval (not a fixed
  clock). He develops competitive positioning, win themes, and case study selection -
  feeding Quinn.
- **Quinn (Proposal Writer)** runs next, on Strategy Package approval (not a fixed clock).
  She drafts the full proposal from everything upstream.
- **Diego (Proposal QA)** runs last in the chain, on draft completion (not a fixed clock).
  He returns a PASS/WARNING/FAIL verdict with exact section citations - never rewriting
  content himself.

If you want the whole sequence to run as one routine instead of five separate ones,
schedule Maya alone and let her dispatch the rest; each phase should confirm the prior
phase's package landed and got your gate approval before continuing. Chase, Priya,
Porter, Quinn, and Diego each only make sense once the prior phase's package has been
approved at its gate - set those up as on-demand prompts you (or Maya) fire at the right
moment, not fixed cadences.

**Blair runs on a separate track.** Blair (Pitch Development) only makes sense once a
deal reaches Proposal Stage for a grant/funder category - it does not feed into or depend
on Maya's chain, and Maya's chain does not feed into it. See
[`Workflows/blair-pitch-development.md`](./blair-pitch-development.md) for that track.

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

Requires ChatGPT Plus or higher and the SKILL.md file uploaded to a project (Settings >
Tasks, or "Ask ChatGPT to schedule this").

1. Open a conversation with Maya's `SKILL.md` uploaded (see
   [`Skills/README.md`](../Skills/README.md) for upload steps)
2. Say: "Schedule this to run daily and use this prompt each time: Check our deal
   pipeline for opportunities marked qualified but not yet started in the proposal
   workflow, and any phase that's been sitting at my approval gate for more than [N]
   days. Report status only - don't advance anything without my gate approval."
3. Confirm the task in Settings > Tasks - ChatGPT will show you the next run time

ChatGPT Scheduled Tasks can't write directly to your CRM the way a Claude Code routine
with MCP access can - Maya's pipeline scan will need a manual copy/paste step against
your CRM unless you've connected the equivalent tools.

---

## Questions

Post in the [THINK School community](https://www.skool.com/thinkschool/about) or visit [compoundleverage.com](https://compoundleverage.com).
