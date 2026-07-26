# Agent Fleet Audit -- Workflow

Structural review only -- if you're running a multi-agent setup built on this repo's
`Agents/[name]/` pattern (a `CLAUDE.md`, a `core/` config, `hooks/`, a `Skills/` folder),
this checks that the pieces are actually wired together. It does not read for content
quality and does not execute anything.

## What it checks

**Skill completeness.** Every skill referenced in an agent's `CLAUDE.md` or hook map
exists as a file (or folder) under that agent's `Skills/`. Every skill folder has a
workflow, a rule set, and a clear output/findings-routing destination.

**Hook map coverage.** Every skill an agent defines appears at least once in that
agent's `hooks/hook-map.md`. Flag any skill that's defined but never triggered by
anything.

**Scope creep.** No skill writes outside its own agent's declared scope. No skill
references an absolute local path (a portability violation -- anything hardcoding a
path specific to one machine won't run anywhere else).

**Registry accuracy.** Every agent folder has a `CLAUDE.md`. If you keep a top-level
registry of your agents (a table in a root `CLAUDE.md` or README), every entry in that
registry has a corresponding folder, and every folder has a registry entry.

**Output format consistency.** If your agents share a common verdict format (PASS / FLAG
/ RECOMMEND, or your own equivalent), flag any skill whose output doesn't follow it.

## Output format
```
AGENT: [name]
SKILL: [skill-name] -- complete, PASS
SKILL: [skill-name] -- missing rules.md, FLAG
HOOK: [skill-name] defined but not in hook-map, RECOMMEND
REGISTRY: [agent] listed in your registry but folder missing, RECOMMEND
```

## Findings routing
All FLAGs and RECOMMENDs pass to `Skills/findings-routing/`.

## Portability note
Reads only markdown and config files across your agent folders. No external calls, no
execution. Token-efficient by design: this checks structure and presence, not content
quality -- whether a skill's judgment calls are actually good is a human review task,
not something this skill claims to assess.
