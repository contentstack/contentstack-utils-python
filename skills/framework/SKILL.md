---
name: framework
description: lxml and companion Contentstack Python SDK — how utils fits in the stack.
---

# Framework skill — `lxml` + Contentstack Python ecosystem

## Integration points

- **`lxml.etree`** — parsing and tree operations in **`utils.py`** and related helpers; errors should remain predictable for malformed HTML/XML inputs.
- **Contentstack delivery SDK** — consumers fetch **`entry`** data with **`contentstack.Stack`**, then pass fields into **`Utils.render`** / **`Utils.render_content`** with **`Options`**.

## When to change

- **Parsing behavior** — verify impact on **RTE** output and existing **`tests/`** fixtures.
- **New dependencies** — add to **`setup.py` `install_requires`** and document; prefer stdlib or existing stack (**`lxml`** already required).

## Testing

- **Unit** — **`tests/test_*.py`** with mocks under **`tests/mocks/`** where applicable.

## Rule shortcut

- `.cursor/rules/contentstack-utils-python.mdc`
- `.cursor/rules/python.mdc`
