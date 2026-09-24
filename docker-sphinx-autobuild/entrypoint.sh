#!/bin/sh
set -e

SOURCEDIR=/docs
BUILDDIR=/docs/_build/html
METADATA=/docs/_build/smv_metadata.orig.json

# Start clean: a stale non-multiversion build (files written directly into
# $BUILDDIR) would otherwise shadow the per-version directories below it,
# and would be served at "/" instead of the redirect below.
rm -rf "$BUILDDIR"

sphinx-multiversion "$SOURCEDIR" "$BUILDDIR"

# Keep a copy of the version metadata sphinx-multiversion generates
# internally (it normally throws it away) so rebuild_current.py can rebuild
# just the current branch on file changes, instead of every branch.
sphinx-multiversion --dump-metadata "$SOURCEDIR" "$BUILDDIR" > "$METADATA"

cat > "$BUILDDIR/index.html" <<'HTML'
<!DOCTYPE html>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=./latest/">
<a href="./latest/">Redirecting to the latest docs&hellip;</a>
HTML

python3 -m http.server 8000 --directory "$BUILDDIR" --bind 0.0.0.0 &

exec watchmedo shell-command \
    --patterns="*.rst;*.py;*.html;*.css;*.js;*.png;*.jpg;*.svg;*.gif" \
    --ignore-patterns="*/_build/*;*/.git/*" \
    --ignore-directories \
    --recursive \
    --drop \
    --command="python3 $SOURCEDIR/docker-sphinx-autobuild/rebuild_current.py" \
    "$SOURCEDIR"
