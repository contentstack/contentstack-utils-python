---
name: code-review
description: PR checklist—public API, __all__, semver, lxml/deps, pytest, secrets; aligns with JS utils where applicable.
---

# Code review – Contentstack Utils Python

## When to use

- Reviewing a PR, self-review before submit, or automated review prompts.

## Instructions

Work through the checklist below. Optionally tag findings: **Blocker**, **Major**, **Minor**.

### Public API

- [ ] **`contentstack_utils/__init__.py`** **`__all__`** and exports match **README** examples and intended surface (**`Utils`**, **`Options`**, **`GQL`**, **`Automate`**, embed types, **`addEditableTags`** / **`addTags`** / **`getTag`**).
- [ ] **JS parity** — where methods mirror the JS utils SDK, **parameter names** and behavior stay consistent unless a documented breaking change.

### Compatibility

- [ ] No breaking **`Utils`** / **`Options`** / tag helpers without a **semver** plan; **`setup.py` `version`** bumped for user-visible changes.

### Dependencies

- [ ] **`lxml`** usage stays bounded to parsing/rendering paths; new **`install_requires`** documented in **README** / changelog.

### Tests

- [ ] **`pytest`** passes; tests added or extended under **`tests/`** for new behavior and edge cases.

### Security

- [ ] No hardcoded tokens; no logging of secrets in new code.

### Severity (optional)

| Level | Examples |
|-------|----------|
| **Blocker** | Breaking public API without approval; security issue; no tests where practical |
| **Major** | Inconsistent behavior vs documented API; README examples wrong |
| **Minor** | Style; minor docs |

## References

- **`skills/testing/SKILL.md`**
- **`skills/contentstack-utils/SKILL.md`**
