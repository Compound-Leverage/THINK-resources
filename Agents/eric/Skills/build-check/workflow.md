# Build Check -- Workflow

Validates your build config (`build.build_tool` in `core/config.template.json`, e.g.
Astro, Next.js, Hugo). Catches dead imports, dependency drift, config inconsistencies,
and build-time regressions before they cause a deploy failure.

## Step 1: Dependency audit

Read your package manifest and check:
- Any packages listed under production dependencies that should be dev-only (adds
  unnecessary weight to the deployed bundle)
- Any packages listed but not imported anywhere (grep your source directory for usage)
- Runtime version compatibility with your current hosting provider's supported versions

## Step 2: Build tool config check

Read your build tool's config file. Verify:
- Output mode matches what a static-site deploy expects (most static-site setups should
  not be in a server-rendering mode unless you've deliberately chosen one)
- Integrations/plugins: flag any unused or duplicated
- Base URL and trailing-slash config match your hosting provider's settings
- Image handling is correctly configured if your build tool has an image pipeline

## Step 3: Build time check

If build logs are available, check the build-time trend. Flag anything exceeding
`build.max_build_time_seconds` on a clean build -- usually a sign of bundle growth or
unoptimized imports.

## Step 4: Dead import check

```bash
# Check for files not referenced anywhere, adjust the path to your own source layout
find src/pages -type f | xargs grep -l "import" | head -20
```

Flag any component imported but not used, or any page importing a component that no
longer exists.

## Step 5: Route findings

| Finding | Action |
|---|---|
| Wrong dependency scope | Open a PR to staging moving it to dev dependencies |
| Unused dependency | Notify for manual removal review -- don't remove it unilaterally |
| Wrong build-tool output mode | Open a PR to staging with the corrected config |
| Build time over threshold with no new pages added | Notify with analysis |
| All clear | No action needed |

## Output
See `Templates/infrastructure-eric.md`'s Infra/Deploy Audit Report for the combined
output format this and the other audit skills share.
