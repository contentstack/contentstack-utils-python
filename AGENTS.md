# Contentstack Utils Python – Agent guide

**Universal entry point** for contributors and AI agents. Detailed conventions live in **`skills/*/SKILL.md`**.

## What this repo is

| Field | Detail |
|--------|--------|
| **Name:** | [contentstack-utils-python](https://github.com/contentstack/contentstack-utils-python) — **`contentstack_utils`** on PyPI |
| **Purpose:** | Utilities for Contentstack headless CMS: RTE / embedded rendering (`Utils`, `Options`), GQL helpers, editable tags on entries, HTML/metadata helpers. Used alongside the Contentstack Python delivery package. |
| **Out of scope:** | This package does not ship HTTP clients or stack credentials. Apps fetch content with the CDA / Python SDK, then pass field data into `Utils`. |

## Tech stack (at a glance)

| Area | Details |
|------|---------|
| Language | Python (`python_requires` in `setup.py`; classifiers list 3.6–3.9) |
| Build | `setuptools` — `find_packages()`, package `contentstack_utils` |
| Runtime deps | `lxml` (XML/HTML parsing in `utils.py` and helpers) |
| Tests | `pytest`, `pytest-cov`, `pytest-html` (optional HTML report) |
| Lint / format | `ruff`, `black`, `flake8`, `isort` (see `requirements.txt`) |

## Commands (quick reference)

| Command Type | Command |
|--------------|---------|
| Install | `pip install -r requirements.txt && pip install -e .` |
| Test | `pytest` |
| Test (HTML report) | `pytest --html=tests/test-report/test-report.html --self-contained-html` |
| Coverage | `coverage run -m pytest && coverage report -m` |

## Where the documentation lives: skills

| Skill | Path | What it covers |
|-------|------|----------------|
| **Development workflow** | [`skills/dev-workflow/SKILL.md`](skills/dev-workflow/SKILL.md) | Branches, CI, venv, pytest, ruff/black/flake8, PR expectations |
| **Contentstack Utils (SDK)** | [`skills/contentstack-utils/SKILL.md`](skills/contentstack-utils/SKILL.md) | `Utils`, `Options`, RTE/embedded, GQL, editable tags, JS parity, semver |
| **Python style & layout** | [`skills/python-style/SKILL.md`](skills/python-style/SKILL.md) | Package layout, typing, imports, `lxml`, `setup.py`, security |
| **Testing** | [`skills/testing/SKILL.md`](skills/testing/SKILL.md) | pytest layout, coverage, `tests/mocks/`, hygiene |
| **Code review** | [`skills/code-review/SKILL.md`](skills/code-review/SKILL.md) | PR checklist (API, `__all__`, deps, tests, secrets) |
| **Framework / integration** | [`skills/framework/SKILL.md`](skills/framework/SKILL.md) | `lxml`, companion Contentstack Python SDK, dependency boundaries |

An index with "when to use" hints is in [`skills/README.md`](skills/README.md).

## Using Cursor (optional)

If you use **Cursor**, [`.cursor/rules/README.md`](.cursor/rules/README.md) only points to **`AGENTS.md`**—same docs as everyone else.
