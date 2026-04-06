# AGENTS.md — AI / automation context

## Project

| | |
|---|---|
| **Name** | **`contentstack_utils`** (PyPI) — **Contentstack Python Utils SDK** |
| **Purpose** | Utilities for **Contentstack** headless CMS: **RTE / embedded** rendering (`Utils`, `Options`), **GQL** helpers, **editable tags** on entries, HTML/metadata helpers. Often used alongside the **`Contentstack`** Python delivery package. |
| **Repository** | [contentstack/contentstack-utils-python](https://github.com/contentstack/contentstack-utils-python.git) |

## Tech stack

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

## Common commands

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

## Further guidance

- **Cursor rules:** [`.cursor/rules/README.md`](.cursor/rules/README.md)
- **Skills:** [`skills/README.md`](skills/README.md)

Product docs: [Content Delivery API](https://www.contentstack.com/docs/developers/apis/content-delivery-api/).
