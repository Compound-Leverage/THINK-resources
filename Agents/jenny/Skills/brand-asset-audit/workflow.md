# Brand Asset Audit -- Workflow

A recurring pass across your produced visual output, thumbnails, social graphics,
decks, or documents, scoring each against your own brand rules and reporting
violations with corrected versions where producible.

## Scope

Assets to audit, adjust to your own inventory:
1. Assets produced in the last 30 days at your configured delivery destination
2. Social graphics currently live on your own channels, if accessible
3. Any asset in your production folder not previously audited

## Step 1: Pull assets

List recent files at `tools.delivery_destination` from your config. If a live
channel (social, web) is accessible via its own tool, pull current assets from
there too. Otherwise note plainly which surfaces need manual review.

## Step 2: Score each asset

For each asset, score against your own QA checklist (the same one
`Skills/asset-production/` uses before delivery):

| Check | Pass | Fail |
|---|---|---|
| Accent color at or under your configured max-percent, used only where designated | | |
| Body copy and backgrounds match your configured colors | | |
| Correct dimensions for its surface | | |
| One CTA, benefit-led copy | | |
| Logo sized and placed per your config | | |
| Imagery matches your imagery policy | | |
| Typography uses only your configured fonts | | |
| File named per your naming convention | | |
| Copy follows every `voice_rules` entry, including no em dashes | | |

## Step 3: Report

```
BRAND AUDIT -- [date]

PASS: [list asset names]

VIOLATIONS:
- [asset name] -- [check that failed] -- [corrected version, or a note on what's needed]

PATTERN GAPS (the same violation recurring across multiple assets):
- [description] -- route to Skills/style-guide-proposal/
```

## Step 4: Route

- **Correctable violations** (a wrong file name, a small copy fix): fix and
  re-deliver directly, no approval needed for a mechanical correction
- **Pattern gaps** (the same deviation showing up across multiple assets): route
  through `Skills/style-guide-proposal/` for approval before anything changes in your
  actual guide
- **Structural violations** (wrong dimensions, wrong color ratio): flag to your
  notification destination with a corrected version attached if you can produce one

**Notification rule**: post to your notification destination only if there's
something to report. A clean audit with zero violations logs quietly and posts
nothing, don't manufacture a report to justify the run.

## Output

A scored pass/fail report, corrected assets where mechanically fixable, and pattern
gaps routed onward. Silent on a clean run.
