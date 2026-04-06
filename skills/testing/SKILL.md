---
name: testing
description: pytest and coverage for contentstack-utils-python.
---

# Testing — `contentstack_utils`

## Commands

| Goal | Command |
|------|---------|
| Full suite | `pytest` |
| HTML report | `pytest --html=tests/test-report/test-report.html --self-contained-html` |
| Coverage (example) | `coverage run -m pytest && coverage report -m` |

## Layout

- **`tests/test_*.py`** — feature-focused modules (**utils**, **GQL**, **metadata**, **editable tags**, etc.).
- **`tests/mocks/`** — shared fixture-style data; extend for new scenarios.

## Setup

- Install **`requirements.txt`** in a venv; **`pip install -e .`** for editable package tests.

## References

- `.cursor/rules/testing.mdc`
