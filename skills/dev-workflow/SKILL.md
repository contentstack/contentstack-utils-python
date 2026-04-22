---
name: dev-workflow
description: Branches, CI, venv, pytest, lint—standard workflow for Contentstack Utils Python.
---

# Development workflow – Contentstack Utils Python

## When to use

- Setting up locally, opening a PR, or aligning with CI.
- Answering “how do we run tests?” or “which branch targets `master`?”

## Before a PR

1. **Install** — `pip install -r requirements.txt` and `pip install -e .` in a virtual environment.
2. **`pytest`** — full suite under **`tests/`** must pass.
3. **Lint / format** — run **ruff**, **black**, **flake8**, **isort** as configured for the repo (see **`requirements.txt`**).
4. **Version** — update **`setup.py` `version`** for releases per semver.

## Branching

- Follow org conventions: **`development`** / **`staging`** / **`master`**; PRs to **`master`** may be restricted (see **`.github/workflows/check-branch.yml`**). Confirm with your team before opening PRs to **`master`**.

## Links

- **`AGENTS.md`** — commands and layout overview.
- **`skills/code-review/SKILL.md`** — pre-merge checklist.
