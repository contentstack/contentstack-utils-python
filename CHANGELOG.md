# Changelog

## v1.5.0

### New feature: Variants utility (CDA entry variant aliases)

- Added `Utils.get_variant_aliases` to read variant alias strings from `publish_details.variants` on a CDA entry (single dict or list of entries).
- Added support for optional `content_type_uid` when `_content_type_uid` is absent on the entry.
- Added `Utils.get_variant_metadata_tags` to build a `data-csvariants` HTML data-attribute value (JSON string of multi-entry alias results).

### New feature: Live Preview editable tags (CSLP)

- Added JS-parity editable tagging helpers in `contentstack_utils/entry_editable.py`.
- Added `addEditableTags` and `addTags` to mutate an entry with a `$` map of CSLP tags.
- Added support for nested objects, arrays, references, and applied variants.
- Added locale and `contentTypeUid` case normalization behavior aligned with JS.
- Added `getTag` helper for recursive tag map construction.
- Exported `addEditableTags`, `addTags`, and `getTag` at package level.
- Added delegation via `Utils` for backward compatibility.

### Bug fix: Test compatibility

- Fixed deprecated unittest assertion usage in `tests/convert_style.py` for newer Python versions.

## v1.4.0

### New feature: Variants utility (CDA entry variant aliases)

- Added `Utils.get_variant_aliases` to read variant alias strings from `publish_details.variants` on a CDA entry (single dict or list of entries).
- Added support for optional `content_type_uid` when `_content_type_uid` is absent on the entry.
- Added `Utils.get_variant_metadata_tags` to build a `data-csvariants` HTML data-attribute value (JSON string of multi-entry alias results).

## v1.3.3

### Bug fix

- Fixed security issues.

## v1.3.2

### Bug fix

- Fixed security issues.
- Bumped `setuptools` package version.

## v1.3.1

### Bug fix

- Fixed link type attributes issue.

## v1.3.0

### New feature

- Added `Reference` attribute node support.

## v1.2.3

### New feature

- Added `fragment` style attribute support.

## v1.2.2

### Improvements

- Minor bug fixes and code improvements.
- Added package release support.

## v1.2.1

### New feature: GraphQL SRTE

- Added GraphQL SRTE support.

## v1.2.0

### New feature: GraphQL supercharged RTE

- Added `GQL.jsonToHtml` support.

## v1.1.0

### New feature: Supercharged RTE

- Added `Utils.jsonToHtml` support.

## v0.2.0 (02-Sept-2021)

- Initial release of `contentstack_utils`.

## v0.1.0 (02-Sept-2021)

- Initial release of `contentstack_utils`.
