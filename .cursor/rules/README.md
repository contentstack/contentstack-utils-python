# Cursor Rules — `contentstack_utils`

Rules for **contentstack-utils-python**: Python **utils** package for **RTE / embedded** rendering, **GQL**, and **editable tags** (companion to the Contentstack Python SDK).

## Rules overview

| Rule | Role |
|------|------|
| [`dev-workflow.md`](dev-workflow.md) | Branch/PR, venv, **pytest**, lint (**ruff** / **black** / **flake8**) |
| [`python.mdc`](python.mdc) | Python layout, `contentstack_utils/`, `setup.py` |
| [`contentstack-utils-python.mdc`](contentstack-utils-python.mdc) | **Utils**, **Options**, RTE/embedded, **GQL**, **entry_editable** |
| [`testing.mdc`](testing.mdc) | **pytest** under **`tests/`** |
| [`code-review.mdc`](code-review.mdc) | PR checklist (**always applied**) |

## Rule application

| Context | Typical rules |
|---------|----------------|
| **Every session** | `code-review.mdc` |
| **Most files** | `dev-workflow.md` |
| **`contentstack_utils/`** | `python.mdc` + `contentstack-utils-python.mdc` |
| **`tests/**`** | `testing.mdc` |
| **`setup.py` / packaging** | `python.mdc` |

## Quick reference

| File | `alwaysApply` | Globs (summary) |
|------|---------------|-----------------|
| `dev-workflow.md` | no | `**/*.py`, `requirements.txt`, `setup.py` |
| `python.mdc` | no | `contentstack_utils/**/*.py`, `setup.py` |
| `contentstack-utils-python.mdc` | no | `contentstack_utils/**/*.py` |
| `testing.mdc` | no | `tests/**/*.py` |
| `code-review.mdc` | **yes** | — |

## Skills

- [`skills/README.md`](../../skills/README.md) · [`AGENTS.md`](../../AGENTS.md)
