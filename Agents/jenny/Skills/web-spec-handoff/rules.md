# Web Spec Handoff -- Rules

- Output is a spec only. Never write HTML, CSS, JavaScript, or push to your site's
  repo
- Reference existing components and tokens from your own codebase, never propose a
  new pattern without flagging it through `Skills/style-guide-proposal/` first
- If a brief conflicts with your own brand rules (a second CTA, an off-brand color),
  flag it and ask before speccing, don't spec around the conflict silently
- Run `Skills/web-consistency-audit/` on the resulting PR before merge, every time
- No em dashes in any output

## What this skill does not do
- Write or push code, that's a separate build step entirely
- Decide a new design pattern belongs in your system, that always routes through
  `Skills/style-guide-proposal/`
- Audit pages that already exist without a pending change, that's
  `Skills/web-consistency-audit/`
