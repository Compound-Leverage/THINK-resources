# Docs Maintenance -- Workflow

Generates documentation drafts from what already exists in your repo. Never invents
content -- everything here is derived from an actual diff, an actual file, or an actual
gap between what's documented and what's there. Output is always a draft for your
review, never a direct write.

## 1. Changelog generation
After a PR merges, or before pushing to your production branch, generate a changelog
entry from the diff between the branch being pushed and your production branch:

```
## [date] -- [branch name]

### Changed
- [file]: [what changed, one line]

### Added
- [file]: [what was added, one line]

### Removed
- [file]: [what was removed, one line]
```

Describe WHAT changed, not HOW -- code-level detail belongs in commit messages, not
here. One line per file or logical change, no multi-paragraph entries. Skip
`.gitkeep`, lock files, and generated files.

## 2. README update proposals
After a PR merges, check whether your README still accurately reflects the repo. A
proposal is warranted when:
- A new top-level directory was added with no README entry
- A new agent, plugin, or skill was added with no registry entry
- A file referenced in the README was removed or renamed
- A setup step in the README no longer matches the current code

Never rewrite the README from scratch, never add marketing or explanatory copy, never
touch sections that are still accurate.

## 3. Inline comment proposals
After a PR merges, read the changed files and identify functions or blocks where the
WHY is non-obvious to a future reader. A comment is warranted when:
- There's a hidden constraint (a value must be X because of an external system)
- There's a subtle invariant that would surprise a reader
- There's a workaround for a specific known bug
- The behavior wouldn't be obvious from the function name and parameters alone

Skip it when the name and parameters already explain the what and why, when the comment
would just restate the code, or when the logic is standard and unsurprising.

## Output
Draft changelog entries, README update proposals, and inline comment proposals -- each
citing the exact file (and line, for inline comments). Pass everything to
`Skills/findings-routing/` for review; none of this writes directly to a file.
