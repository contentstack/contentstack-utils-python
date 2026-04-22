---
name: contentstack-utils
description: Public API—Utils, Options, RTE/embedded, GQL, editable tags; JS parity; no bundled HTTP client.
---

# Contentstack Utils – SDK skill

## When to use

- Implementing or changing RTE/HTML rendering, embedded resolution, **GQL**, or editable-tag behavior.
- Updating **`README.md`** / **`changelog.rst`** / **`setup.py`** for user-visible behavior.
- Assessing semver impact of **`__init__.py`** exports and public classes.

## Core entry points

- **`Utils`** — **`contentstack_utils.utils`**: **`render_content`**, **`render`**, embedded/RTE resolution; subclasses **`Automate`**.
- **`Options`** — **`contentstack_utils.render.options`**: rendering configuration passed into **`Utils`** methods.
- **Editable tags** — **`entry_editable`**: **`addEditableTags`**, **`addTags`**, **`getTag`**; also exposed as **`Utils.addEditableTags`** / **`Utils.addTags`** / **`Utils.getTag`** for parity.

## Features

- **Embedded / RTE** — JSON and HTML paths through **`Utils`** and **`Automate`**; **metadata** via **`Metadata`**.
- **Styles** — **`convert_style`** and **embedded** **StyleType** / **ItemType** where applicable.
- **GQL** — **`GQL`** in **`gql.py`** for GraphQL-oriented HTML/helpers.

## Public API and docs

- **`contentstack_utils/__init__.py`** **`__all__`** and exports must match **README** examples and intended surface (**`Utils`**, **`Options`**, **`GQL`**, **`Automate`**, embed types, tag helpers).
- **JS parity** — where methods mirror the JS utils SDK, keep **parameter names** and behavior consistent unless a documented breaking change.

## Compatibility

- Avoid breaking **`Utils`** / **`Options`** / tag helpers without a **semver** plan; bump **`setup.py` `version`** for user-visible changes.

## Dependencies

- **`lxml`** usage stays bounded to parsing/rendering paths; note any new **`install_requires`** in **README** / changelog if added to **`setup.py`**.

## No network layer

- This package does **not** ship HTTP clients or tokens.
- Consumers often use **`contentstack.Stack`** (**Contentstack** package) to fetch entries, then **`Utils.render`** / **`Utils.render_content`** — keep **README** examples accurate.

## References

- [Content Delivery API](https://www.contentstack.com/docs/developers/apis/content-delivery-api/)
- **`skills/python-style/SKILL.md`**, **`skills/framework/SKILL.md`**
