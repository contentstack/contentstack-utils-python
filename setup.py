"""Minimal setup.py for custom build hooks.

Project metadata lives in pyproject.toml (PEP 621). This file only registers
BuildPyWithRegions so sdist/wheel builds refresh regions.json from the CDN.
"""

import os
import sys

from setuptools import setup
from setuptools.command.build_py import build_py


class BuildPyWithRegions(build_py):
    """Fetch latest regions.json from Contentstack CDN before packaging."""

    def run(self):
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        try:
            from contentstack_utils.region_refresh import refresh_regions

            refresh_regions()
        except Exception as exc:
            # Never block a build over a network failure — warn and continue.
            print(f"WARNING: Could not refresh regions.json: {exc}", file=sys.stderr)
        super().run()


setup(cmdclass={"build_py": BuildPyWithRegions})
