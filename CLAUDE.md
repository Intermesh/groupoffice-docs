# GroupOffice documentation

Sphinx (reStructuredText) source for the GroupOffice manual.

## Building

The docs are built with Docker. Don't use a locally installed `sphinx-build`.

- `docker compose up -d` starts the `sphinx-autobuild` container (see `compose.yaml` and
  `docker-sphinx-autobuild/Dockerfile`). It rebuilds when files change and serves the
  docs at http://localhost:8004/.
- To see build errors and warnings, do a clean one-off build in the container:

  ```
  docker compose run --rm sphinx-autobuild sphinx-build -E -q -b html /docs /tmp/html
  ```

  The build should finish with no output (no errors or warnings).

## Conventions

- Refer to the three-dot menu as the "more options menu (⋮)".
