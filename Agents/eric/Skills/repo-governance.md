# Repo Governance -- Decision Rubric

A quick rubric for deciding whether a new piece of work needs its own repo, or belongs
inside one you already have. Not a workflow with sequential steps -- ask the questions
below when the question comes up.

## When to create a new repo
- The work has a distinct deployment target (a separate edge function/Worker, a separate
  hosting project, a separate GitHub Action)
- It has a different runtime or auth context than your existing repos
- It would need its own separate CI/CD pipeline
- It's owned by an external collaborator who shouldn't have access to your other repos
- Its scope is large enough that PRs would routinely conflict with unrelated work already
  happening in an existing repo

## When to add to an existing repo
- It shares the same runtime, deployment, and auth as an existing repo
- A new automation follows the same hook/plugin/skill pattern already established there
- The addition is a new profile, config, or skill file, not a new system
- It's invoked by, or feeds, an automation already living in that repo

## Consolidation rule
A new automation with no deployment of its own is a folder or config addition inside an
existing repo, not a new repo. This applies whether it's a new persona, a new scheduled
check, or a new skill file -- the deployment question is what matters, not how novel the
capability feels.

## Profile/config files
Profiles (client ICP configs, output templates, threshold configs) are never a reason to
create a new repo on their own. They're config files added to the relevant existing
repo's own customization or config directory.

## When in doubt
Ask: does this need its own deployment, its own CI, or its own access control? If the
answer is no to all three, it belongs in an existing repo.
