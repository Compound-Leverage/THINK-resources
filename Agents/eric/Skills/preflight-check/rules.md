# Preflight Check -- Rules

- YAML syntax fixes and deprecated-action-version updates go out as a PR to staging --
  never committed directly, even though these are the most mechanical fixes Eric makes.
  A blocking failure the night before a run is still not a reason to push straight to
  production or bypass review
- Missing secrets are a flag-only finding -- Eric cannot create or set a secret himself
- An invalid or low-credit API key is a flag-only finding -- Eric cannot fix billing or
  rotate a key himself
- Always send a sweep summary, even when everything passes -- silence the night before a
  scheduled run is worse than a one-line "all clear"
- No em dashes in any output
