---
name: dev-workflow
description: Branches, CI, venv, pytest, lint—standard workflow for Contentstack Utils Python.
---

# Development workflow – Contentstack Utils Python

## When to use

- Setting up locally, opening a PR, or aligning with CI.
- Answering “how do we run tests?” or “which branch targets `development` or `master`?”

## Before a PR

1. **Install** — `pip install -r requirements.txt` and `pip install -e .` in a virtual environment.
2. **`pytest`** — full suite under **`tests/`** must pass.
3. **Lint / format** — run **ruff**, **black**, **flake8**, **isort** as configured for the repo (see **`requirements.txt`**).
4. **Version** — update **`setup.py` `version`** for releases per semver.

## Branching

- Follow direct-flow conventions: feature/fix PRs target **`development`**, and release PRs are raised from **`development`** to **`master`**.

## Links

- **`AGENTS.md`** — commands and layout overview.
- **`skills/code-review/SKILL.md`** — pre-merge checklist.
