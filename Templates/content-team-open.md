# Content Team (content-team-open) -- Deliverable Templates

Blank versions of the documents Rohit, Ann, Joanna, Justin, Amy, Josh, Jay, Cal, and Sal
produce. Use these directly (fill in your own data by hand) or as the reference format
the plugin's outputs should match. Every `[bracket]` is a placeholder.

---

### Rohit -- Intel Scanner

Writes `topic-cards.json` at the plugin working directory, plus Draft records to your
content database, ranked by composite score. Every other skill in this plugin reads its
topic input from here.

```
Topic Cards -- Week of [date]

| Rank | Title | Source | Summary | Composite score | Confidence flag |
|---|---|---|---|---|---|
| [1] | [Topic title] | [Reddit / News / YouTube / Google PAA / Platform performance] | [1-2 sentence summary] | [score] | [High / Low -- flag reason] |

Draft records written: [count] to [content DB name, or "local only"]
```

---

### Ann -- Newsletter Editor

Section headers below match the WARM/COLD structure this skill always produces.

```
Newsletter -- Week of [date]
Source topic card: [topic card title or link]

## WARM Edition (engaged subscribers)
Subject: [subject line]
[Body -- deeper insight, direct CTA]
CTA: [CTA text / link]

## COLD Edition (new / unengaged subscribers)
Subject: [subject line]
[Body -- more framing, lighter CTA]
CTA: [subscription hook or lighter CTA]

Posted as drafts to: [newsletter platform name]
Local backup: output/[week]/
```

---

### Joanna -- Blog Writer

One block per ICP voice, matching `icp_voice_profiles` in
`customization/my-content-sources.json`.

```
Blog Posts -- Week of [date]
Source signal/topic: [topic title or input]

## Practitioner ICP Post
Title: [title]
[Body]
CTA: [practitioner CTA style]

## Org-Buyer ICP Post
Title: [title]
[Body]
CTA: [org-buyer CTA style]

Draft records written: [count] to [content DB name]
```

---

### Justin -- LinkedIn Content

One block per configured persona, grouped by posting day, matching `linkedin_personas`
in `customization/my-content-sources.json`.

```
LinkedIn Queue -- Week of [date]

## [Persona name] -- [Posting day]
[Post text]

## [Persona name] -- [Posting day]
[Post text]

## [Persona name] -- [Posting day]
[Post text]

Saved to: output/[week]/LI_Queue_[week].md
```

---

### Amy -- YouTube Scripts

```
YouTube Script -- Week of [date]
Source: [research file path] + [this week's brief]

Title options:
1. [Title option]
2. [Title option]
3. [Title option]

Hook variants (first 15 seconds):
1. [Hook variant]
2. [Hook variant]
3. [Hook variant]

## Signal Walkthrough
[Body]

## Practitioner Takeaway
[What the viewer does with this]

## CTA Close
[CTA]

Estimated read-aloud runtime: [X:XX] (target 4-5 min)
Saved to: output/[week]/YouTube_Script_[week].md
```

---

### Josh -- Intelligence Brief

Section headers below match the Leader/Strategist structure this skill always produces.

```
Intelligence Brief -- Week of [date]
Topics meeting proof gate ([threshold]): [count]

## Leader Edition (org-buyer audience)
[Body -- framing and depth for the org-buyer reader]

## Strategist Edition (practitioner audience)
[Body -- framing and depth for the practitioner reader]

Org-buyer flags written: [count] to org-buyer-flags.json
Draft records written: [count] to [content DB name]
```

---

### Jay -- Theme Proposer

Always exactly 3 options, written as Pending records for owner approval.

```
Theme Proposals -- [Target month]

## Option A
Theme: [theme name]
Signal cluster(s): [cluster(s) this proposal is anchored to]
Score: [composite score]
Rationale: [why this theme, tied to offer alignment]

## Option B
Theme: [theme name]
Signal cluster(s): [cluster(s) this proposal is anchored to]
Score: [composite score]
Rationale: [why this theme, tied to offer alignment]

## Option C
Theme: [theme name]
Signal cluster(s): [cluster(s) this proposal is anchored to]
Score: [composite score]
Rationale: [why this theme, tied to offer alignment]

Status: Pending owner approval
Written to: [theme proposals DB name]
```

---

### Cal -- Weekly Brief

One page, overwritten each week, never appended.

```
Weekly Brief -- [date]

## What Happened
[Synthesis of this week's content output, plus BD/fulfillment activity if those plugins are installed]

## What's Pending
[In-flight items awaiting completion]

## Needs Your Decision
[Ranked by priority -- what genuinely needs owner attention this week]

---
One-line summary: [summary]
Page overwritten: [Notion page name or local file path]
```

---

### Sal -- Course Builder

One complete course directory per brief. No partial output -- every listed file ships
together.

```
Course: [COURSE_SLUG]
Source brief: inputs/[filename].md

## Outline
[Module list]

## Start-Here Module
[Content]

## Lessons
[Lesson 1 title] -- [content]
[Lesson 2 title] -- [content]
[one entry per module]

## Exercises
[Exercise per module]

## Capstone Project
[Description]

## Course Index
[Index / table of contents]

Consistency pass: [Passed / Issues flagged -- list]
Saved to: outputs/[COURSE_SLUG]/
```

---

## Questions

Contact [marvin@compoundleverage.co](mailto:marvin@compoundleverage.co) or visit [compoundleverage.com](https://compoundleverage.com).
