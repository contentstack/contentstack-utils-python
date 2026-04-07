# Contentstack Utils Python – Agent guide

**Universal entry point** for anyone automating or assisting work in this repo—AI agents (Cursor, Copilot, CLI tools), reviewers, and contributors. Conventions and detailed guidance live in **`skills/*/SKILL.md`**, not in editor-specific config, so the same instructions apply whether or not you use Cursor.

## What this repo is

- **Name:** [contentstack-utils-python](https://github.com/contentstack/contentstack-utils-python) — **`contentstack_utils`** on PyPI (**Contentstack Python Utils SDK**).
- **Purpose:** Utilities for **Contentstack** headless CMS: **RTE / embedded** rendering (`Utils`, `Options`), **GQL** helpers, **editable tags** on entries, HTML/metadata helpers. Often used alongside the **Contentstack** Python delivery package.
- **Out of scope:** This package does **not** ship HTTP clients or stack credentials. Apps fetch content with the [Content Delivery API](https://www.contentstack.com/docs/developers/apis/content-delivery-api/) / Python SDK, then pass field data into **`Utils`**.

## Tech stack (at a glance)

| Area | Details |
|------|---------|
| **Language** | **Python** (`python_requires` in `setup.py`; classifiers list 3.6–3.9; dev tooling in `requirements.txt` may need a newer interpreter) |
| **Package** | **`setuptools`** — `find_packages()`, `contentstack_utils/` |
| **Runtime deps** | **`lxml`** (XML/HTML parsing in `utils.py` and helpers) |
| **Tests** | **pytest** + **pytest-cov**, **pytest-html** (optional HTML report) |
| **Lint / format** | **ruff**, **black**, **flake8**, **isort** (see `requirements.txt`) |

## Source layout

| Path | Role |
|------|------|
| `contentstack_utils/utils.py` | **`Utils`** — `render_content`, embedded/RTE flows; extends **`Automate`** |
| `contentstack_utils/render/options.py` | **`Options`** for rendering |
| `contentstack_utils/helper/` | **Metadata**, **NodeToHtml**, **converter** (e.g. `convert_style`) |
| `contentstack_utils/embedded/` | **ItemType**, **StyleType** |
| `contentstack_utils/gql.py` | **GQL** helpers |
| `contentstack_utils/automate.py` | **`Automate`** base for automation-style rendering |
| `contentstack_utils/entry_editable.py` | **`addEditableTags`**, **`addTags`**, **`getTag`**; re-exported via **`Utils`** static methods and package **`__init__`** |
| `contentstack_utils/__init__.py` | Public exports — keep **`__all__`** aligned with documented API |
| `tests/` | pytest modules (`test_*.py`), mocks under `tests/mocks/` |

## Commands (quick reference)

```bash
python -m venv .venv && source .venv/bin/activate  # or equivalent on Windows
pip install -r requirements.txt
pip install -e .
pytest
pytest --html=tests/test-report/test-report.html --self-contained-html
coverage run -m pytest && coverage report -m
```

## Security

- Do not commit **API keys**, **delivery tokens**, or other secrets. Examples in **`README.md`** use placeholders only.

## Where the real documentation lives: skills

Read these **`SKILL.md` files** for full conventions—**this is the source of truth** for implementation and review:

| Skill | Path | What it covers |
|-------|------|----------------|
| **Development workflow** | [`skills/dev-workflow/SKILL.md`](skills/dev-workflow/SKILL.md) | Branches, CI, venv, **pytest**, ruff/black/flake8, PR expectations |
| **Contentstack Utils (SDK)** | [`skills/contentstack-utils/SKILL.md`](skills/contentstack-utils/SKILL.md) | **`Utils`**, **`Options`**, RTE/embedded, **GQL**, editable tags, JS parity, semver |
| **Python style & layout** | [`skills/python-style/SKILL.md`](skills/python-style/SKILL.md) | Package layout, typing, imports, **`lxml`**, **`setup.py`**, security |
| **Testing** | [`skills/testing/SKILL.md`](skills/testing/SKILL.md) | **pytest** layout, coverage, **`tests/mocks/`**, hygiene |
| **Code review** | [`skills/code-review/SKILL.md`](skills/code-review/SKILL.md) | PR checklist (API, **`__all__`**, deps, tests, secrets) |
| **Framework / integration** | [`skills/framework/SKILL.md`](skills/framework/SKILL.md) | **`lxml`**, companion **Contentstack** Python SDK, dependency boundaries |

An index with short “when to use” hints is in [`skills/README.md`](skills/README.md).

## Using Cursor

If you use **Cursor**, [`.cursor/rules/README.md`](.cursor/rules/README.md) only points to **`AGENTS.md`**—same source of truth as everyone else; no separate `.mdc` rule files.
