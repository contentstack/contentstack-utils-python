---
description: "Branches, venv, pytest, and lint for contentstack-utils-python"
globs: ["**/*.py", "requirements.txt", "setup.py"]
alwaysApply: false
---

# Development workflow — `contentstack_utils`

## Before a PR

1. **Install** — `pip install -r requirements.txt` and `pip install -e .` in a virtual environment.
2. **`pytest`** — full suite under **`tests/`** must pass.
3. **Lint / format** — run **ruff**, **black**, **flake8**, **isort** as configured for the repo (see **`requirements.txt`**).
4. **Version** — update **`setup.py` `version`** for releases per semver.

## Branching

- Follow org conventions: **`development`** / **`staging`** / **`master`**; PRs to **`master`** may be restricted (see **`.github/workflows/check-branch.yml`**).

## Links

- [`AGENTS.md`](../../AGENTS.md) · [`skills/contentstack-utils-python/SKILL.md`](../../skills/contentstack-utils-python/SKILL.md)
