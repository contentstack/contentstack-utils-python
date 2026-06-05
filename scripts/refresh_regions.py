#!/usr/bin/env python3
"""
Pull the latest regions.json from the Contentstack CDN and overwrite the
bundled copy at contentstack_utils/assets/regions.json.

Usage:
    python3 scripts/refresh_regions.py

Mirrors the ``composer refresh-regions`` command in the PHP SDK.
Run this whenever Contentstack adds a new region or service, then commit the
updated file so all consumers get the change on their next install.
"""

import json
import os
import sys
import urllib.request

REGIONS_URL = "https://artifacts.contentstack.com/regions.json"
DEST = os.path.join(
    os.path.dirname(__file__),
    "..",
    "contentstack_utils",
    "assets",
    "regions.json",
)


def main() -> int:
    dest = os.path.normpath(DEST)
    print(f"Fetching {REGIONS_URL} ...")

    try:
        with urllib.request.urlopen(REGIONS_URL, timeout=30) as resp:
            data = resp.read().decode("utf-8")
    except Exception as exc:
        print(f"ERROR: Could not download regions.json: {exc}", file=sys.stderr)
        return 1

    try:
        decoded = json.loads(data)
    except json.JSONDecodeError as exc:
        print(f"ERROR: Downloaded content is not valid JSON: {exc}", file=sys.stderr)
        return 1

    if not isinstance(decoded, dict) or "regions" not in decoded:
        print("ERROR: Downloaded JSON does not contain a 'regions' key.", file=sys.stderr)
        return 1

    region_count = len(decoded["regions"])
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(decoded, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print(f"OK: Wrote {region_count} regions to {dest}")
    print("Next steps:")
    print("  git add contentstack_utils/assets/regions.json")
    print('  git commit -m "chore: refresh regions.json"')
    return 0


if __name__ == "__main__":
    sys.exit(main())
