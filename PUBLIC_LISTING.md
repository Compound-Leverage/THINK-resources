# Public listing copy (ChatGPT / Claude directory submission)

Reference copy for the OpenAI/Codex public plugin directory submission form.
This describes the **curated 2-team public offering only** -- not the full
9-plugin marketplace in this repo (that stays available via direct GitHub-URL
install for THINK School members, per `README.md`, where Fulfillment and the
rest of the roster remain installable).

## Structure

**Two separate plugin listings, not one bundled app** (decision finalized
2026-08-28, per Julian's growth-lane review -- see rationale below):

- **ChatGPT:** "THINK School AI Capture Team" (standalone listing) +
  "THINK School AI Proposal Team" (standalone listing)
- **Claude:** same two, same split
- **THINK School on Skool:** the complete environment -- full team library
  (including Fulfillment and the rest of the roster), Digital Employees, this
  GitHub repository, training, customization, team-building methodology,
  updates, community.

**Why two listings:** ChatGPT/Claude directory search is semantic, matching a
user's natural-language query against a listing's name + description. A
capture manager searches "capture management" / "RFP capture"; a proposal or
grant writer searches "grant proposal writing" / "proposal compliance" -- two
different queries a single bundled listing would have to serve at once,
diluting match strength for both. Two single-skill listings are also the
confirmed-supported platform format; one listing bundling two named
sub-skills was never confirmed as supported, so this also removes a real,
unnecessary submission risk.

**Naming: "THINK School AI [Team]," not a bare generic name, not a shortened
"THINK."** Julian's original argument was to drop branding entirely from the
searchable name (spend the whole ~30-char budget on the job-function term,
since THINK School has no prior recognition in this channel yet). Overruled
-- a fully generic name like bare "Capture Team" is exactly what OpenAI's own
submission guidance warns against ("avoid overly generic names... not
clearly tied to your brand"), and it risks colliding with an unrelated plugin
using the same generic phrase, with zero way for a user to tell them apart or
find this one again. A shortened "THINK [Team]" was tried next, but
overruled too -- "THINK" alone is not an actual marketed term (Compound
Leverage markets "THINK School" as a whole phrase, never "THINK" on its own),
so it would carry zero real brand recognition, just an invented abbreviation.
Resolution: use the full "THINK School AI [Team]" -- "THINK School AI Capture
Team" (28 chars) and "THINK School AI Proposal Team" (29 chars) fit the
~30-char budget, use the actual marketed brand phrase, add "AI" for category
clarity, and keep the job-function search term intact.

**Publisher: Compound Leverage, not THINK School.** Per this project's
original brief, Compound Leverage is the company/publisher and THINK School
is the product brand -- and OpenAI's developer identity verification
(completed 2026-08-28) is already tied to "Business -- Compound Leverage."
That's the identity OpenAI will show as the verified publisher regardless of
listing copy, so the subtitle says "by Compound Leverage" to match rather
than introducing a third, unexplained brand name on top of the two already in
the listing name and description. Manifest `author.name`/`developerName`
fields already say "Compound Leverage" for both plugins -- no change needed
there.

Guiding principle: **public plugins help you do the work. THINK School teaches
you how to build, customize, and manage the workforce.** The free tier is not
intentionally limited -- Capture Team is genuinely good at capture. The upsell
is the system, capability development, resources, and community around it, not
a fuller version of the same tool.

Distribution funnel: search/discovery -> ChatGPT or Claude plugin -> real
outcome -> recognizes THINK School -> deeper need -> THINK School on Skool.
GitHub is the technical distribution/source layer underneath all of it.

Not every user is ready for Skool membership immediately -- the "Learn" content
hub (https://www.compoundleverage.com/examples/: free tools, guides, articles,
research, no signup required) is the zero-commitment parallel path for people
who want to see more before joining. Keep this out of the plugin manifest's own
upsell line (that stays a single, clean CTA to Skool, per OpenAI's
anti-advertising guidance) -- it lives in repo docs people read once they're
already engaged, e.g. `SUPPORT.md`.

## Listing 1: THINK School AI Capture Team

**Name:** THINK School AI Capture Team
(28 chars -- fits the ~30-char limit reported for this field; verify in the
submission portal.)

**Subtitle:** Find and pursue opportunities -- by Compound Leverage
(~53 chars -- verify the portal's actual subtitle limit before submitting.
Publisher goes here, matching the verified developer identity -- see naming
note below.)

**Description:** Part of THINK School, Compound Leverage's free practitioner
resource. An AI Team of three Digital Employees that finds named groups worth
pursuing, enriches and classifies inbound leads against your ICP, and turns
signals into client-ready intelligence briefs. Configurable to your own
business -- bring your ICP, capability map, and connect whatever CRM,
enrichment tool, and document storage you already use. Nothing is pre-wired
to a specific vendor, and no proprietary Compound Leverage accounts or data
are required.

Try: "Find named groups or clusters that share a capacity gap we can fill"

## Listing 2: THINK School AI Proposal Team

**Name:** THINK School AI Proposal Team
(29 chars -- fits the ~30-char limit; verify in the submission portal.)

**Subtitle:** Win the work with compliant proposals -- by Compound Leverage
(~63 chars -- verify the portal's actual subtitle limit; may need trimming.
Publisher goes here, matching the verified developer identity.)

**Description:** Part of THINK School, Compound Leverage's free practitioner
resource. An AI Team of seven Digital Employees that carries a qualified
opportunity from research through a submission-ready proposal -- requirement
extraction, competitive positioning, drafting, and QA, plus a parallel
grant/funder track. Every stage stops for your approval before moving on.
Configurable to your own business -- bring your pricing, case studies, and
brand guidelines.

Try: "Run this opportunity through Go/No-Go and deal assessment"

(Format check for both: confirm in the submission portal whether example
prompts belong inline in the full description or are handled entirely by the
separate starter-prompt field each plugin manifest already sets via
`defaultPrompt`.)

## The two teams (submission scope)

**Capture -> Proposal**

1. **Capture Team** -- find, research, qualify, and pursue the right opportunities.
2. **Proposal Team** -- turn qualified opportunities into compliant, competitive submissions.

Deliberately scoped to two for the first public release. "Win the work" is a
complete, tight story on its own, and both plugins are the ones directly
validated by real survey data (a congregation grant-workshop survey and a
GovCon capture/proposal pilot survey) this session used to refine sourcing and
research capability. Fulfillment stays out of the public submission for now --
it's a single-persona plugin (Lincoln only, vs. Capture's 3 and Proposal's 7)
with no equivalent validation yet, and adding a third, thinner team risks
diluting the pitch before the market has proven out discovery and usage on the
core two. Revisit adding Fulfillment (or any of Content, Sales BD, Sales
Enablement, Lead Discovery, Ops) only after that signal exists.

## How Capture + Proposal cover the pre-award lifecycle

Positioning only -- Capture Team and Proposal Team stay separate installable
plugins (10 roles across two plugins, unchanged). Together they already cover
five functions end to end, no restructuring needed:

1. **Find and research opportunities** -- Chet (Capture, cluster discovery) +
   Chase (Proposal, requirement extraction, incumbent/award history, client and
   industry research)
2. **Analyze and qualify opportunities** -- Kipp (Capture, CRM intake and ICP
   classification) + Chase's Go/No-Go + Priya (Proposal, capability fit,
   compliance/eligibility scoring, gap analysis)
3. **Develop capture intelligence/strategy** -- Ben (Capture, signal delivery
   and intelligence briefs) + Porter (Proposal, competitive positioning and win
   themes)
4. **Support proposal development** -- Quinn (drafting) + Blair (grant/funder
   track) + Priya (cost-competitive pricing)
5. **Review/compliance/quality** -- Diego (Proposal QA, compliance and
   consistency checks)

Use this breakdown in listing copy to show the two plugins as one continuous
workflow, not two unrelated tools.

## Reviewer test cases

OpenAI's submission requires 5 positive + 3 negative test cases per plugin.
Every prompt below is grounded in what the shipped SKILL.md/references
content actually does -- nothing invented, nothing the package can't back up.

### THINK School AI Capture Team

**Positive (should work):**
1. "Find named groups or clusters that share a capacity gap we can fill" --
   Chet, cluster discovery
2. "Enrich and classify this list of inbound leads against our ICP" --
   Kipp, CRM intake
3. "Turn this week's signals into a client-ready intelligence brief" --
   Ben, signal delivery
4. "We're looking for consortiums or membership groups in [sector] that need
   [capability]" -- Chet
5. "Score and route these new contacts based on our ICP profile" -- Kipp

**Negative (should NOT trigger, or should decline/redirect):**
1. "What grants is my competitor getting?" -- out of scope. Capture Team
   works for the user's own org against their own ICP; it has no
   competitive-intelligence-on-named-others capability
2. "Send this contact an email introducing our services" -- out of scope, no
   send/outreach capability anywhere in the package; Capture Team only
   discovers, enriches, and writes briefs, never sends communications
3. "Just tell me if this group will definitely become a client" -- should not
   produce a guarantee. Chet's own rules state "no 0-100 fit score at this
   stage" -- output is a candidate record for human triage, not a
   conversion promise

### THINK School AI Proposal Team

**Positive (should work):**
1. "Run this opportunity through Go/No-Go and deal assessment" -- Chase + Priya
2. "Build competitive positioning and win themes for this RFP" -- Porter
3. "Draft a submission-ready proposal from the research and positioning so
   far" -- Quinn
4. "Run QA on this proposal draft before we submit" -- Diego
5. "Run this grant opportunity through the funder track" -- Blair

**Negative (should NOT trigger, or should decline/redirect):**
1. "Can you send this proposal to the client for me?" -- should NOT
   auto-send. Every phase gates on human approval; Blair's own rules
   explicitly require approval before any outreach, and no skill in this
   package has send capability
2. "Just tell me if we'll win this contract" -- should not produce a
   definitive win/loss verdict. Chase's own rules frame fit as "a judgment
   call for the human reading this brief, not something to resolve
   mechanically"
3. "Give me the actual dollar pricing without filling in your config" --
   should decline/flag as blocked, not fabricate a number. Priya's own setup
   note states "without a completed my-pricing-model.json, this skill cannot
   produce pricing or ROI output"

## Versioning

Standard semver (`MAJOR.MINOR.PATCH`) applies to each plugin's `version`
field independently -- Capture Team and Proposal Team version on their own
schedules, not in lockstep.

- **PATCH** (third digit) -- bug fixes, behavior corrections, wording/
  instruction clarifications, metadata copy changes (description, subtitle,
  support/privacy URLs). No change to what the plugin can do. Example: the
  org-identity guard fix, description reformatting.
- **MINOR** (second digit) -- new backward-compatible capability: a new
  discovery mode, a new QA check, a new output section, a new persona. Old
  configs and workflows still work unchanged.
- **MAJOR** (first digit) -- breaking change: a config schema change that
  invalidates existing filled-in `my-*-config.json` files, a removed or
  renamed persona/role, a restructure that breaks an existing install.

When a batch of changes mixes fix-level and capability-level work under one
version number (as happened between 1.1.0 and 1.1.1 for both plugins this
cycle), bump for the highest tier actually shipped, then start applying the
per-change logic above going forward from that number.

## Submission artifacts (ready to upload)

- `openai-plugin/capture-team.zip` -- SKILL.md at root, `references/`,
  `assets/`, no hidden-file cruft. QA-verified 2026-08-29.
- `openai-plugin/proposal-team.zip` -- same structure, QA-verified 2026-08-29.

**Still open before actual submission (not blockers, but unresolved):**
verify `compoundleverage.com/privacy` and `/terms` explicitly read as
covering plugin distribution (soft check -- the URLs are live and valid,
which satisfies the mechanical requirement regardless); confirm the full
upload form doesn't surface additional required fields beyond developer
identity + zip (only the first screen has been seen so far).
