# Preflight Check -- Workflow

Reviews your scheduled workflows the night before they run (or on demand when a
scheduled run has failed and the cause is unknown). Fixes anything mechanical within
Eric's own authority as a PR to staging. Flags anything that needs a human before the
run fires.

## When to run
On a schedule, the evening before your scheduled workflows fire (a nightly cron a few
hours ahead of your earliest scheduled run works well). Also on demand when a scheduled
workflow has failed and the cause isn't obvious.

## Step 1: Enumerate scheduled workflows

```bash
find .github/workflows -name "*.yml" | xargs grep -l "schedule:"
```

For each scheduled workflow, read the full file and record:
- Every `secrets.` reference
- Action versions used
- Any heredoc or multi-line run blocks

## Step 2: Validate YAML

Run each workflow file through a YAML parser:

```bash
python3 -c "import yaml, sys; yaml.safe_load(open(sys.argv[1]).read()); print('OK')" .github/workflows/[file].yml
```

If a file fails validation, open a PR to staging with the fix and note it in the report.

**Common mechanical fixes covered here:**
- Heredoc content at column 0 inside a `run: |` block -- indent to match the block
  scalar baseline
- Unclosed heredocs -- close them
- Missing quotes on string values -- add quotes
- Indentation errors -- correct them

## Step 3: Check deprecated action versions

Same minimums as `Skills/github-actions-audit/`, from `ci_cd.minimum_action_versions` in
your config. If any scheduled workflow uses a version below the minimum, open a PR to
staging with the update.

## Step 4: Audit secrets referenced vs. secrets present

```bash
gh secret list --repo [YOUR ORG/REPO]
```

Cross-reference against every `secrets.X` reference found in Step 1. For any referenced
secret that isn't set, notify:

```
PREFLIGHT ALERT: [workflow-name] references [SECRET_NAME] but it is not set in your
repo's secrets. This will cause the run to fail. Add the secret before the next
scheduled run.
```

Eric cannot set secrets himself -- flag only, never attempt to fix.

## Step 5: Validate your model-provider API key(s)

For each provider listed in `preflight.model_providers_to_check`, run a minimal
authenticated request (a 1-token ping is enough) against that provider's API using the
key your scheduled workflows depend on.

- Credit balance too low -> notify: "ALERT: [provider] credit balance is too low. Top up
  before the next scheduled run."
- Invalid or expired key -> notify: "ALERT: your [provider] key is invalid. Update it
  before the next scheduled run."
- Successful response -> key is valid, continue

Eric cannot fix an API key or a billing issue himself -- flag only.

## Step 6: Send a sweep summary

Always send a summary to your notification destination, regardless of findings:

```
PREFLIGHT SWEEP -- [date]
Workflows checked: [n]

YAML: [OK / FIXED: list of files]
ACTIONS: [OK / UPDATED: list of files]
SECRETS: [OK / MISSING: list]
MODEL PROVIDER KEYS: [OK / ALERT sent, per provider]

STATUS: CLEAR TO RUN / BLOCKED (awaiting a human)
```

If everything passes and nothing needs a human, a one-line summary is fine: "Preflight
sweep complete -- all clear for tomorrow's runs."

## Output
See `templates/preflight-sweep-log.md` in this repo's `Agents/eric/templates/` for the
log format, or `Templates/infrastructure-eric.md`'s Infra/Deploy Audit Report if you'd
rather fold this into your combined audit report instead.
