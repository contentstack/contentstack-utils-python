---
name: python-style
description: Python layout for contentstack_utils, typing, lxml usage, setup.py, packaging.
---

# Python style and repo layout – Contentstack Utils Python

## When to use

- Editing any Python under **`contentstack_utils/`** or **`setup.py`**.
- Adding modules or changing how **`lxml`** is used.

## Layout

- **`contentstack_utils/utils.py`** — **`Utils`** class (rendering, embedded items); delegates **editable tag** static methods to **`entry_editable`**.
- **`contentstack_utils/render/`** — **`Options`** and render-related code.
- **`contentstack_utils/helper/`** — **Metadata**, **NodeToHtml**, **converter**.
- **`contentstack_utils/embedded/`** — **ItemType**, **StyleType**.
- **`contentstack_utils/gql.py`**, **`automate.py`**, **`entry_editable.py`** — feature modules.

## Style

- Match existing patterns: **typing** hints where already used; **pylint** pragmas only where established.
- Prefer **small, focused** changes; avoid drive-by refactors unrelated to the task.

## Imports

- **`lxml.etree`** — HTML/XML parsing in **`utils`** and helpers; keep usage consistent with existing error handling.

## Packaging

- **`setup.py`** — **`name`**, **`version`**, **`packages=find_packages()`**; keep **`install_requires`** accurate if dependencies change.

## Security

- Do not log **delivery tokens**, **API keys**, or stack secrets.

## References

- **`skills/contentstack-utils/SKILL.md`** — public API and features.
- **`skills/framework/SKILL.md`** — **`lxml`** and SDK integration.
