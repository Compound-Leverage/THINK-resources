# Deploy Check -- Rules

- Never escalate a resolved failure -- check whether a later run on the same branch
  already succeeded before reporting anything as active
- Config-only fixes (build command, output directory, env var scoping mismatches within
  your own already-approved variable set) go out as a PR to your staging branch, never
  committed directly
- A broken preview URL or hosting-project-level config issue is a notify, not a fix --
  Eric doesn't have standing access to change your hosting dashboard settings himself
- Never push directly to your production branch, even for a fix you're fully confident
  in
- No em dashes in any output
