# Skills – Contentstack Utils Python

**This directory is the source of truth** for conventions (workflow, SDK API, style, tests, review, framework). Read **`AGENTS.md`** at the repo root for the index and quick commands; each skill is a folder with **`SKILL.md`** (YAML frontmatter: `name`, `description`).

## When to use which skill

| Skill folder | Use when |
|--------------|----------|
| **dev-workflow** | Branches, CI, venv, **`pip install -e .`**, **pytest**, ruff/black/flake8, PRs |
| **contentstack-utils** | **`Utils`**, **`Options`**, RTE/embedded, **GQL**, editable tags, semver, README |
| **python-style** | `contentstack_utils/` layout, typing, **`lxml`** usage, **`setup.py`** |
| **testing** | **pytest**, coverage, **`tests/mocks/`**, HTML reports |
| **code-review** | PR checklist, public API / **`__all__`**, dependencies, security |
| **framework** | **`lxml`** integration, delivery SDK handoff, parsing impact |

## How to use these docs

- **Humans / any AI tool:** Start at **`AGENTS.md`**, then open the relevant **`skills/<name>/SKILL.md`**.
- **Cursor users:** **`.cursor/rules/README.md`** only points to **`AGENTS.md`** so guidance stays universal—no duplicate `.mdc` rule sets.
