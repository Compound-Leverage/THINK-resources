# GitHub Actions Audit -- Workflow

Reviews CI/CD workflows across the repos listed in `repos` in your config. Catches
deprecated action versions, security gaps, and missing checks before they cause build
failures or expose secrets.

## Step 1: Enumerate workflows

```bash
find .github/workflows -name "*.yml" -o -name "*.yaml" | sort
```

For each workflow, read the full file and note:
- Trigger (push, PR, schedule, manual)
- Jobs and steps
- Action versions used (`uses: actions/checkout@v3` etc.)

## Step 2: Deprecated versions

Check against `ci_cd.minimum_action_versions` in your config. Flag any action pinned
below the minimum your config specifies -- older pins are deprecated and may stop
working without notice.

## Step 3: Security checks

- Are secrets referenced correctly (`${{ secrets.NAME }}`), never hardcoded?
- Are third-party action versions pinned to a SHA for critical steps? (Recommended, not
  required)
- Does any workflow set `permissions: write-all`? Flag for review.
- Any `pull_request_target` triggers? These can be exploited by a malicious PR -- flag if
  present.

## Step 4: Missing checks

Verify, per repo:
- A build validation check runs on every PR before merge
- A staging deploy triggers on merge to your staging branch
- A production deploy triggers on merge to your production branch

If any of these are missing, notify with a proposed workflow.

## Step 5: Route findings

| Finding | Action |
|---|---|
| Deprecated action version | PR to staging with the updated version |
| Hardcoded secret | Notify immediately -- this is a live exposure risk |
| Missing build check on PRs | Notify with a workflow proposal |
| `permissions: write-all` | Notify -- scope review needed |

## Output
See `Templates/eric-infrastructure.md`'s Infra/Deploy Audit Report for the combined
output format this and the other audit skills share.
