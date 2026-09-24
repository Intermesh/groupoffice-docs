#!/usr/bin/env python3
"""Rebuild only the currently checked-out branch's docs.

sphinx-multiversion always rebuilds every whitelisted branch, which is slow
for a watch loop. This reuses the version metadata from the last full
"sphinx-multiversion --dump-metadata" run (see entrypoint.sh) and invokes
sphinx-build directly for just the current branch, reading its .rst sources
live from the working tree so uncommitted edits show up immediately. Other
branches' pages (and the cross-version links to them) are left untouched
until the next full rebuild.
"""
import json
import os
import subprocess
import sys

SOURCEDIR = "/docs"
BUILDDIR = "/docs/_build/html"
ORIG_METADATA_PATH = "/docs/_build/smv_metadata.orig.json"
LIVE_METADATA_PATH = "/docs/_build/smv_metadata.live.json"


def full_rebuild():
    return subprocess.call(["sphinx-multiversion", SOURCEDIR, BUILDDIR])


def main():
    branch = subprocess.check_output(
        ["git", "branch", "--show-current"], cwd=SOURCEDIR, text=True
    ).strip()

    try:
        with open(ORIG_METADATA_PATH) as f:
            metadata = json.load(f)
    except (OSError, json.JSONDecodeError):
        print("No cached version metadata, doing a full rebuild", file=sys.stderr)
        return full_rebuild()

    if branch not in metadata:
        print(
            "'{}' is not a whitelisted version, doing a full rebuild".format(branch),
            file=sys.stderr,
        )
        return full_rebuild()

    data = dict(metadata[branch])
    data["confdir"] = SOURCEDIR
    data["sourcedir"] = SOURCEDIR
    metadata[branch] = data

    with open(LIVE_METADATA_PATH, "w") as f:
        json.dump(metadata, f)

    outputdir = data["outputdir"]
    os.makedirs(outputdir, exist_ok=True)

    cmd = [
        "sphinx-build",
        "-D", "smv_metadata_path={}".format(LIVE_METADATA_PATH),
        "-D", "smv_current_version={}".format(branch),
        "-c", SOURCEDIR,
        SOURCEDIR,
        outputdir,
    ]
    return subprocess.call(cmd)


if __name__ == "__main__":
    sys.exit(main())
