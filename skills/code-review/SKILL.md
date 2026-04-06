---
name: code-review
description: PR review for contentstack_utils — public API, __all__, lxml/deps, pytest.
---

# Code review — `contentstack_utils`

## Checklist

- [ ] **API:** New or changed **`Utils`** / **`Options`** / tag helpers reflected in **`contentstack_utils/__init__.py`** **`__all__`** and **README** if user-facing.
- [ ] **Version:** **`setup.py` `version`** bumped when releasing behavioral or API changes (semver).
- [ ] **Dependencies:** Any new **`install_requires`** entry documented; **`lxml`** usage stays appropriate for parsing/rendering.
- [ ] **Tests:** **`pytest`** passes; add tests under **`tests/`** for new behavior.
- [ ] **Secrets:** No tokens in repo; examples use placeholders only.

## References

- `.cursor/rules/code-review.mdc`
- `.cursor/rules/dev-workflow.md`
