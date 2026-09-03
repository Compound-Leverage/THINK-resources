---
name: plugin-release
description: Prepares a THINK School plugin (capture-team, proposal-team, or any future public plugin) for release across both distribution surfaces -- Claude Code (Plugins/<team>) and OpenAI (openai-plugin/<team>). Use when content, instructions, or copy changed in a plugin and it needs to go out as a versioned update, or before resubmitting/reuploading either surface.
---

## Purpose

THINK School plugins ship on two structurally different surfaces from one
source of truth:

- **`Plugins/<team>/`** -- canonical, Claude Code-native. Multi-persona
  `skills/<persona>/SKILL.md` files, `.claude-plugin/plugin.json` +
  `.codex-plugin/plugin.json`, `customization/` config path, em dash (`—`)
  convention.
- **`openai-plugin/<team>/`** -- derived, OpenAI Skills-only packaging.
  One consolidated `skills/<team>/SKILL.md` + `references/*.md`,
  `.codex-plugin/plugin.json` only, `assets/` config path, double-hyphen
  (`--`) convention (no em dashes anywhere -- OpenAI copy rule).

Content drifts between these two trees when a fix lands in one and doesn't
get carried to the other -- this happened twice in one session (a missing
save-or-discard confirmation on canonical Chet, a stale `.claude-plugin`
description on both teams). This skill is the checklist that prevents that.

## When to use

- After editing any `SKILL.md`, `references/*.md`, or config file in either
  `Plugins/<team>/` or `openai-plugin/<team>/`
- Before resubmitting to the Claude Code community marketplace
- Before telling the user a new zip is ready to reupload to OpenAI

## Process

1. **Identify what changed and where.** Diff the edited file(s) against
   their counterpart in the other tree. Canonical persona files map to
   `openai-plugin/<team>/skills/<team>/references/<persona>.md`; the
   canonical router/orchestrator persona (`proposal-engine-lead-maya`,
   or the standalone `cluster-discovery-chet` for capture-team) maps to
   the openai-plugin root `SKILL.md`.

2. **Sync in both directions.** Apply the same logical change to both
   trees, translating conventions as you go:
   - em dash `—` (canonical) <-> double hyphen `--` (openai-plugin)
   - `customization/` (canonical) <-> `assets/` (openai-plugin)
   - multi-file persona structure (canonical) <-> single consolidated
     file with `## Persona Name` sections (openai-plugin)
   Do not skip this step because "it's just a copy change" -- the
   `.claude-plugin/plugin.json` `description` field and the
   `.codex-plugin/plugin.json` `interface.longDescription` field should
   show the same text on both surfaces unless there's a stated reason
   for them to differ.

3. **Sweep for leaked identity/company references** if the change touches
   org-identification logic, discovery prompts, or any place a "whose
   organization" question gets asked. Run:
   ```
   grep -rliE "compound.?leverage|compoundleverage\.com" Plugins/<team> openai-plugin/<team>
   ```
   Only the two manifest files' `author`/`developerName`/URL fields should
   match -- required publisher attribution, not skill content. Anything
   else is a regression of the org-identity guard fix.

4. **Apply the version bump**, per the policy in `PUBLIC_LISTING.md` ->
   Versioning:
   - **Patch** -- bug fix, wording/instruction clarification, metadata
     copy change. No capability change.
   - **Minor** -- new backward-compatible capability (new discovery mode,
     new QA check, new persona). Old configs still work.
   - **Major** -- breaking change (config schema change that invalidates
     existing configs, removed/renamed persona).
   Each plugin (capture-team, proposal-team, future additions) versions
   independently -- they don't need to move together. Update the version
   in all three manifest locations for the affected plugin:
   `Plugins/<team>/.claude-plugin/plugin.json`,
   `Plugins/<team>/.codex-plugin/plugin.json`,
   `openai-plugin/<team>/.codex-plugin/plugin.json`.

5. **Validate.**
   ```
   claude plugin validate ./Plugins/<team> --strict
   python3 -c "import json; json.load(open('<path>'))"  # every touched .json
   ```

6. **Rebuild the OpenAI zip from a clean state** -- never trust an
   existing zip after a content change:
   ```
   cd openai-plugin
   rm -f <team>.zip
   cd <team> && zip -r -X ../<team>.zip . -x "*.DS_Store" -x "__MACOSX*" && cd ..
   ```

7. **Diff-verify the zip against source** -- this is non-negotiable, it's
   what catches a stale rebuild before the user reuploads it:
   ```
   rm -rf /tmp/verify-<team> && mkdir -p /tmp/verify-<team>
   unzip -q <team>.zip -d /tmp/verify-<team>
   diff -rq <team> /tmp/verify-<team>   # must be silent, exit 0
   ```

8. **Commit** with a message that states what changed and the version
   bump, e.g. "Fix X in Chase; patch bump proposal-team 1.1.2 -> 1.1.3."

9. **Report back**, explicitly stating:
   - Which plugin(s) changed and their new version numbers
   - Whether the zip needs reuploading to OpenAI (always, if
     `openai-plugin/<team>/` changed)
   - Whether `main` needs a push for the Claude Code submission to see
     the update -- the review pipeline reads from the repo's default
     branch, not `Staging`. If a submission is pending or already live,
     changes sitting only on `Staging` are invisible to review until
     merged and pushed to `main`.

## Rules

- Never rebuild a zip without doing the diff-verify step -- a silent stale
  zip is worse than no zip, because it looks done
- Never bump only one manifest location's version and leave the others
  behind -- all three locations for a given plugin must agree
- Never skip the identity-leak sweep when the change touches org-detection
  logic -- this is the one category of bug that shipped twice already
  because it wasn't checked mechanically
- If canonical and openai-plugin diverge in ways that aren't just the
  stated conventions (em dash, path names, file structure), stop and
  flag it rather than silently picking one side
