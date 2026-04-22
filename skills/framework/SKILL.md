---
name: framework
description: lxml parsing layers, setup.py install_requires, companion Contentstack Python SDK handoff.
---

# Framework / integration – Contentstack Utils Python

## When to use

- Changing HTML/XML parsing behavior or **`lxml`** touchpoints.
- Adding runtime dependencies or documenting **`install_requires`**.

## Integration points

- **`lxml.etree`** — parsing and tree operations in **`utils.py`** and related helpers; errors should remain predictable for malformed HTML/XML inputs.
- **Contentstack delivery SDK** — consumers fetch **`entry`** data with **`contentstack.Stack`**, then pass fields into **`Utils.render`** / **`Utils.render_content`** with **`Options`**.

## When to change

- **Parsing behavior** — verify impact on **RTE** output and existing **`tests/`** fixtures.
- **New dependencies** — add to **`setup.py` `install_requires`** and document; prefer stdlib or existing stack (**`lxml`** already required).

## Testing

- **Unit** — **`tests/test_*.py`** with mocks under **`tests/mocks/`** where applicable.

## References

- **`skills/python-style/SKILL.md`**
- **`skills/dev-workflow/SKILL.md`**
