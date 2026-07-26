# Automation Ops Audit -- Rules

- This skill never changes anything itself -- it's advisory only, every recommendation
  waits for your approval before implementation
- Never recommend removing an approval gate around an external send or an irreversible
  action, regardless of how routine it looks
- Base every recommendation on what an automation's own instructions actually say --
  don't guess at its notification behavior from its name or general purpose
- If an automation has no documented schedule or notification rules, flag that as a
  finding in its own right rather than skipping it silently
- No em dashes in any output
