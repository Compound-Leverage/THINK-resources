# Agent Fleet Audit Report -- Template

Produced by `Skills/agent-fleet-audit/`. Only relevant if you're running a multi-agent
setup on this repo's `Agents/[name]/` pattern. One block per agent checked.

```
Agent Fleet Audit -- [date]
Agents checked: [count / list]

AGENT: [name]
SKILL: [skill-name] -- [complete, PASS / missing [what], FLAG]
HOOK: [skill-name] defined but not in hook-map -- RECOMMEND
REGISTRY: [agent] listed in your registry but folder missing -- RECOMMEND

[repeat per agent]

Checks passed: [count]
Flagged for review: [list, or "none"]
Recommendations: [list, or "none"]
```
