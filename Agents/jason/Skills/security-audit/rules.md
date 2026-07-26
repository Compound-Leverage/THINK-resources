# Security Audit -- Rules

- Pattern-match only -- never execute code, never make a live network request as part of
  this check
- A committed `.env` variant is a flag regardless of whether it currently holds a real
  value -- the exposure risk is in the commit, not the current content
- Findings from this skill route to your configured destination immediately, not batched
  into the next scheduled report -- credential exposure is time-sensitive
- Don't attempt to validate whether a flagged credential is still live -- that
  determination (and any rotation) is yours to make, not this skill's
- Keep dependency vulnerability checks to your own maintained pattern list -- this is not
  a live feed, and claiming otherwise would overstate what the check actually does
- No em dashes in any output

## What this skill does not do
- Confirm or rotate a credential once flagged
- Patch a vulnerable dependency -- flag it, don't touch `package.json` or equivalent
- Replace a real secrets scanner if you already run one -- this is a lightweight,
  portable pattern-match layer, not a substitute for dedicated tooling
