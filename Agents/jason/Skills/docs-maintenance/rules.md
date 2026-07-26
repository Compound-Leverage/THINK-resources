# Docs Maintenance -- Rules

- Never write directly to a changelog, README, or source file -- every output here is a
  draft surfaced for review
- Changelog entries describe WHAT changed, never HOW -- code-level detail belongs in
  commit messages
- One line per file or logical change in a changelog entry -- no multi-paragraph entries
- README proposals touch only what's actually outdated or missing -- never rewrite
  accurate sections, never add marketing copy
- An inline comment proposal only fires when the WHY is genuinely non-obvious -- don't
  propose a comment that would just restate the code
- Skip `.gitkeep`, lock files, and generated files in changelog generation
- No em dashes in any output

## What this skill does not do
- Decide what merges or ships -- purely descriptive, after the fact
- Invent product specs, feature claims, or context not actually present in the diff or
  file being documented
