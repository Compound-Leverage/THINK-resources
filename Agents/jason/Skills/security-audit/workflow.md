# Security Audit -- Workflow

Pattern-match only, no execution, no live traffic generated. Runs on file content alone,
so it's portable across whatever tool you run Jason in.

## What it checks

**Hardcoded credentials.** Grep for common credential patterns (API key prefixes, bare
`token=`, `password=`, `api_key=` assignments) in non-config source files.

**Committed secret files.** Check git-tracked files for `.env` and its common variants
(`.env.local`, `.env.production`, `.env.backup`). A committed variant is a flag
regardless of whether it currently holds a live value.

**Config files with live values outside their intended path.** If your repo has a
convention for where config/credential values are allowed to live (e.g. only inside a
specific `config.json` that's itself gitignored, or only in environment variables),
flag any credential-shaped value found outside that convention.

**Logging that leaks sensitive data.** Grep for logging calls (`console.log` or your
language's equivalent) whose arguments contain `key`, `token`, `secret`, or `password`.

**Known-vulnerable or deprecated dependencies.** Check your dependency manifest against
a pattern list of packages you know are deprecated or carry known vulnerabilities. This
is not a live CVE feed -- keep your own pattern list current if you want this check to
stay useful.

**Agent/skill scope creep.** If you're running a multi-agent setup, review each agent's
hook map for any skill that writes outside its own declared scope.

## What it does not check
- Runtime security -- nothing here executes code or makes live requests
- Network-level vulnerabilities
- Authentication flow correctness

## Output
Findings citing the exact file and line (or file, for a committed-secret-file flag).
Pass everything to `Skills/findings-routing/`, flagged as high priority -- surface
immediately rather than batching into a routine weekly report.
