---
name: contentstack-utils-python
description: contentstack_utils — Python RTE/embedded rendering, Options, GQL, editable tags.
---

# Contentstack Python Utils skill

## Entry

- **`Utils`** — **`contentstack_utils.utils`**: **`render_content`**, **`render`**, embedded item automation via **`Automate`**.
- **`Options`** — configure rendering behavior for **`Utils`** calls.

## Structure

- **`Automate`** — **`automate.py`**: shared automation/rendering flow used by **`Utils`**.
- **Helpers** — **`helper/metadata.py`**, **`helper/node_to_html.py`**, **`helper/converter.py`**.
- **Embedded** — **`embedded/item_type.py`**, **`embedded/styletype.py`**.
- **GQL** — **`gql.py`**.
- **Live preview / tags** — **`entry_editable.py`**; static wrappers on **`Utils`** keep JS-style parameter names where needed.

## Extending

- Prefer matching **JS contentstack-utils** behavior when the feature exists there; document intentional divergences.
- Keep **`lxml`** usage in parsing/rendering layers; avoid broad new runtime deps without packaging updates.

## Companion package

- **`Contentstack`** (delivery SDK) fetches entries; this package renders RTE/embedded fields — see **README** examples.

## Docs

- [Content Delivery API](https://www.contentstack.com/docs/developers/apis/content-delivery-api/)

## Rule shortcut

- `.cursor/rules/contentstack-utils-python.mdc`
