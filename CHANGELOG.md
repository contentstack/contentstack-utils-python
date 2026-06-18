# Changelog

## v1.6.0 (2026-06-22)

### New feature: Multi-region endpoint resolution

- Added `Endpoint.get_contentstack_endpoint()` for dynamic region-aware URL resolution across all Contentstack regions and services.
- Added `Utils.get_contentstack_endpoint()` proxy for backward-compatible access via the existing `Utils` import path.
- Added `getContentstackEndpoint` camelCase alias on both `Endpoint` and `Utils` for cross-SDK parity.
- Bundled `contentstack_utils/assets/regions.json` — the authoritative registry of 7 regions (AWS NA/EU/AU, Azure NA/EU, GCP NA/EU) and 18 service endpoint keys.
- Added runtime fallback in `Endpoint._load_regions()` — downloads `regions.json` from `artifacts.contentstack.com` on first use when the file is absent.
- Added `scripts/refresh_regions.py` to manually pull the latest regions from Contentstack.
- Exported `Endpoint` at package level in `__all__`.
- Added `refresh_regions()` utility to programmatically download the latest regions manifest from the Contentstack CDN and overwrite the bundled `assets/regions.json`.
- Exposed `refresh_regions` at the package level (`from contentstack_utils import refresh_regions`) for use in CI pipelines and tooling.
- `setup.py` now auto-refreshes `regions.json` at build time via a custom `BuildPyWithRegions` command; network failures warn but never block the build.
- Added `assets/regions.json` to `package_data` so the bundled file is correctly shipped in the sdist/wheel.

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
