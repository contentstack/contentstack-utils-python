================
**CHANGELOG**
================

*v1.5.0*
============

NEW FEATURE: Variants utility (CDA entry variant aliases).

- Added ``Utils.get_variant_aliases`` to read variant alias strings from ``publish_details.variants`` on a CDA entry (single dict or list of entries). Supports optional ``content_type_uid`` when ``_content_type_uid`` is absent on the entry.
- Added ``Utils.get_variant_metadata_tags`` to build a ``data-csvariants`` HTML data-attribute value (JSON string of the multi-entry alias results).

NEW FEATURE: Live Preview editable tags (CSLP).

- Added JS-parity editable tagging helpers in ``contentstack_utils/entry_editable.py``.
- Added ``addEditableTags`` / ``addTags`` to mutate an entry with a ``$`` map of CSLP tags (supports nested objects, arrays, references, and applied variants; normalizes case for ``contentTypeUid`` and locale similar to JS).
- Added ``getTag`` helper for building tag maps recursively.
- Exported ``addEditableTags``, ``addTags``, and ``getTag`` at package level, and delegated via ``Utils`` for backward compatibility.

BUG FIX: Test compatibility.

- Fixed deprecated unittest assertion usage in ``tests/convert_style.py`` for newer Python versions.

*v1.4.0*
============

NEW FEATURE: Variants utility (CDA entry variant aliases).

- Added ``Utils.get_variant_aliases`` to read variant alias strings from ``publish_details.variants`` on a CDA entry (single dict or list of entries). Supports optional ``content_type_uid`` when ``_content_type_uid`` is absent on the entry.
- Added ``Utils.get_variant_metadata_tags`` to build a ``data-csvariants`` HTML data-attribute value (JSON string of the multi-entry alias results).

*v1.3.3*
============

Bug Fix: Fixed security issues.

*v1.3.2*
============

Bug Fix: Fixed security issues.

- setuptools package version bump.

*v1.3.1*
============

Bug Fix: Fixed Link type attributes.

- Fixed link type attribute issue

*v1.3.0*
============

NEW FEATURE: Added Reference attribute.

- added node attribute Reference

*v1.2.3*
============

NEW FEATURE: Added Fragment attribute.

- added new style attribute fragment

*v1.2.2*
============

NEW FEATURE: Minor bug fixes and code improvements.

- package release support added

*v1.2.1*
============

NEW FEATURE: GraphQL SRTE  

- GraphQL SRTE support added


*v1.2.0*
============

NEW FEATURE: GraphQl supercharged RTE

- GQL.jsonToHtml function support added


*v1.1.0*
============

NEW FEATURE: Supercharged RTE

- Utils.jsonToHtml function support added

*v0.2.0*
============

**Date: 02-Sept-2021**

 - Initial release of contentstack utility package


ENHANCEMENT, NEW FEATURE, BUG RESOLVE

*v0.1.0*
============

**Date: 02-Sept-2021**

 - Initial release of contentstack utility package
