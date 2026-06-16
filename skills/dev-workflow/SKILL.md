---
name: dev-workflow
description: Use for install, pytest, lint, versioning, and PR baseline in contentstack-utils-python.
---

# Development workflow – Contentstack Utils Python

## When to use

- Setting up locally, opening a PR, or matching CI expectations.
- Answering "how do we run tests?" or "what lint tooling is required?"

## Instructions

### Branches & releases

- Follow org conventions: `development` / `staging` / `master`; PRs to `master` may be restricted (see `.github/workflows/check-branch.yml`).
- Bump `setup.py` `version` for releases per semver.

### Before a PR

1. **Install** — `pip install -r requirements.txt` and `pip install -e .` in a virtual environment.
2. **Test** — full suite under `tests/` must pass: `pytest`.
3. **Lint / format** — run `ruff`, `black`, `flake8`, `isort` as configured (see `requirements.txt`).

### Pre-merge checklist

- Follow `skills/code-review/SKILL.md` before merge.
- Prefer backward-compatible public API; call out breaking changes and semver.
