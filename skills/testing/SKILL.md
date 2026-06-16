---
name: testing
description: Use for pytest layout, coverage, tests/mocks fixtures, and hygiene in contentstack-utils-python.
---

# Testing – Contentstack Utils Python

## When to use

- Adding or changing tests under `tests/`.
- Debugging flaky tests; improving mocks or fixtures.

## Instructions

### Commands

| Goal | Command |
|------|---------|
| Full suite | `pytest` |
| HTML report | `pytest --html=tests/test-report/test-report.html --self-contained-html` |
| Coverage | `coverage run -m pytest && coverage report -m` |

### Layout

- `tests/test_*.py` — feature-focused modules (utils, GQL, metadata, editable tags, etc.).
- `tests/mocks/` — shared fixture-style data; extend for new scenarios instead of duplicating large JSON.

### Setup

- Install `requirements.txt` in a venv; `pip install -e .` for editable package tests.

### Hygiene

- No committed `pytest.mark.skip` or `xfail` without justification; no `breakpoint()` left in CI paths.
- No API keys or real tokens in tests.
