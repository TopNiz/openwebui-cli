# Release procedure

## Preconditions

- milestone scope reviewed;
- all included issues linked to merged pull requests;
- CI green on `main`;
- package version and changelog updated;
- pinned Open WebUI compatibility verified;
- generated-client drift check passes;
- repository and artifacts checked for credentials and private deployment data.

## Local verification

```bash
uv sync --extra dev --locked
uv run ruff check .
uv run ruff format --check src tests scripts
uv run mypy src/openwebui_cli
uv run pytest
./scripts/check-generated.sh
uv build
uvx twine check dist/*
```

Use only read-only live smoke tests unless a disposable environment and explicit mutation approval are available.

## Tag and GitHub pre-release

The release workflow builds from tags matching `v*` and publishes wheel/source artifacts to a GitHub pre-release.

```bash
git tag -s v0.1.0a1 -m "Open WebUI CLI 0.1.0a1"
git push origin v0.1.0a1
```

If signed tags are unavailable, document the reason and use an annotated tag. Do not publish to PyPI until trusted publishing and package ownership are configured explicitly.

## Post-release

- verify artifact checks and installation in a clean environment;
- verify `owui --version` and all help groups;
- update the milestone and compatibility documentation;
- announce known limitations and the exact supported Open WebUI version.
