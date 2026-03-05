# Skill: Push Workflow Guard

## Goal
Enforce safe and consistent push behavior across dual remotes.

## Trigger
Use this skill before any `git push` command.

## Required checks
Run and review:

```bash
git status --short --branch
git diff --name-only
git ls-files
git remote -v
```

## Remote policy
- `private` receives full repository content.
- `public` receives minimal publishable content only.

## Content policy

### Private push (full)
Allowed: full repo, including `SPECS/`.

### Public push (minimal)
Allowed paths:
- `scripts/`
- `notebooks/`
- `requirements.txt`
- `README.md`
- `.gitignore`
- `LICENSE` (if present)

Blocked from public:
- `SPECS/`
- private planning notes
- raw source extraction folders unless explicitly intended

## Branch policy
- Development branch (`master`/`main`) -> push to `private`.
- `public-minimal` branch -> push to `public`.

## Mandatory reference
Read `PUSH_WORKFLOW.md` before push. If conflict exists, `PUSH_WORKFLOW.md` is the source of truth.
