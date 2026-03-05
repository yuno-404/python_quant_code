# Push Workflow (Private + Public)

Use this document before every push.

## Purpose
- Keep `private` as the full working repository.
- Keep `public` as a minimal teaching repository.
- Prevent accidental leak of internal planning files (for example `SPECS/`) to `public`.

## Remotes
```bash
git remote -v
```

Expected remotes:
- `private` -> `https://github.com/yuno-404/quantforme.git`
- `public` -> `https://github.com/yuno-404/python_quant_code.git`

If missing:
```bash
git remote add private https://github.com/yuno-404/quantforme.git
git remote add public https://github.com/yuno-404/python_quant_code.git
```

## Pre-push Checklist (Mandatory)
Run these checks every time before push:

```bash
git status --short --branch
git diff --name-only
git ls-files
```

Confirm:
- You are on the correct branch.
- Staged/unstaged changes are expected.
- No sensitive files are included (`.env`, keys, tokens, credentials).
- Push target (`private` or `public`) matches intent.

## Branch Strategy
- `master` (or main development branch): full content for `private`.
- `public-minimal`: only public-safe teaching deliverables.

## What Goes to Each Remote

### Private (`private` remote)
Push full repository, including:
- `scripts/`
- `notebooks/`
- `SPECS/`
- `AGENTS.md`
- other development/support files

### Public (`public` remote)
Push only minimal set:
- `scripts/`
- `notebooks/`
- `requirements.txt`
- `README.md`
- `.gitignore`
- `LICENSE` (if present)

Do not include in `public`:
- `SPECS/`
- private planning notes
- raw extraction/source material folders unless explicitly intended

## Push Full Content to Private
```bash
git checkout master
git add -A
git commit -m "chore: sync full repository content"
git push -u private master
```

If there is nothing to commit, run only:
```bash
git push -u private master
```

## Create/Refresh Public Minimal Branch

### First time setup
```bash
git checkout --orphan public-minimal
git rm -rf .
git checkout master -- scripts notebooks requirements.txt README.md .gitignore LICENSE
git add scripts notebooks requirements.txt README.md .gitignore LICENSE
git commit -m "chore: publish minimal teaching materials"
git push -u public public-minimal
git checkout master
```

### Regular updates
```bash
git checkout public-minimal
git rm -rf .
git checkout master -- scripts notebooks requirements.txt README.md .gitignore LICENSE
git add scripts notebooks requirements.txt README.md .gitignore LICENSE
git commit -m "chore: refresh public minimal content"
git push public public-minimal
git checkout master
```

## Safety Notes
- `.gitignore` does not remove already tracked files.
- Prefer explicit file allow-list for `public` (commands above).
- Never force-push unless absolutely necessary and explicitly decided.
- Before pushing to `public`, always run:

```bash
git checkout public-minimal
git ls-files
```

Only expected minimal files should appear.
