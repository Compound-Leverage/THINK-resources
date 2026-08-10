# Deploy Check -- Workflow

Validates your build and deploy state after every merge. Catches failed builds, broken
previews, and config drift before they become production incidents.

Load your filled-in `core/config.template.json` copy before running any step below.

## Step 1: Check recent deployments

Use your CDN/hosting provider's CLI, MCP, or dashboard to check:
- The last several deployments on your `hosting.provider` project: status
  (success/failed/building)
- Most recent production deployment: URL, timestamp, commit SHA
- Most recent staging deployment: URL, timestamp, commit SHA
- Any failed builds: error messages from the build log

## Step 2: Validate build config

Check your provider's build config file (`wrangler.toml`, `vercel.json`, a Pages/Netlify
config, or equivalent). Verify against `build` in your config:
- Build command matches `build.build_command`
- Output directory matches `build.output_directory`
- Runtime version (Node or otherwise) matches your `package.json` engines field or
  equivalent
- Environment variables are correctly scoped (preview vs. production)

## Step 3: Check preview URLs

If a PR is open, verify the preview URL resolves. A broken preview usually means the
build failed silently or the PR's config is wrong.

## Step 4: Classify failures as active or resolved

Before routing any finding, determine whether it is active or resolved:
- A failure is **active** if the most recent run on that branch failed
- A failure is **resolved** if a subsequent run on the same branch succeeded after the
  failure

**Never escalate a resolved failure.** If the run that triggered this deploy check is
itself a success, any failures earlier in the history are already resolved -- report
them as context, not as an open issue. This matters because a deploy check is often
itself triggered by a push that fixed the very failure you'd otherwise flag.

## Step 5: Route findings

| Finding | Action |
|---|---|
| Failed build (active) | Post the error and last working commit to your notification destination immediately |
| Failed build (resolved) | Note in the summary only, no escalation |
| Build config drift (wrong output dir, wrong command) | Open a PR to staging with the corrected config |
| Preview URL not resolving | Notify -- may need a hosting-project config fix only a human can apply |
| All clear | Post a brief status summary, or stay silent per `notifications.silent_on_zero_findings` |

## Output
See `Templates/infrastructure-eric.md`'s Infra/Deploy Audit Report for the combined
output format this and the other audit skills share.
