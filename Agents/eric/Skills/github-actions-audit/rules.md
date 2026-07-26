# GitHub Actions Audit -- Rules

- A hardcoded secret is a notify-immediately finding, never a silent fix -- rotating or
  removing a live credential is a human decision
- Deprecated action version bumps go out as a PR to staging, never committed directly
- Never widen or narrow a workflow's `permissions` block yourself -- flag it, a human
  decides the correct scope
- No em dashes in any output
