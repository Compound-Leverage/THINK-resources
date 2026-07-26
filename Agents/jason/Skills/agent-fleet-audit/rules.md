# Agent Fleet Audit -- Rules

- Structure only -- never judge whether a skill's content, rules, or judgment calls are
  actually good; that's a human review task
- Flag a skill defined in a `CLAUDE.md` or hook map with no matching file on disk --
  don't assume it exists elsewhere
- Flag a skill that exists on disk but never appears in its own agent's hook map -- a
  skill nobody triggers is dead weight
- Flag any absolute local file path found in an agent's files -- it's a portability
  violation, the same file should work in anyone else's clone of the same setup
- Flag scope creep: a skill writing to a database, repo, or destination outside its own
  agent's declared scope
- This skill is only relevant if you're actually running a multi-agent setup on this
  repo's `Agents/[name]/` pattern -- skip it entirely if you're just running Jason
  standalone
- No em dashes in any output

## What this skill does not do
- Execute any agent's skill to see if it actually works -- this is a static, read-only
  structural check
- Judge whether an agent's role or scope makes business sense -- only whether the
  pieces that exist are wired together correctly
