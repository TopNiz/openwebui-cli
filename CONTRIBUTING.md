# Contributing

## Workflow

1. Open or select a GitHub issue.
2. Create a focused branch from `main`.
3. Add implementation, tests, embedded CLI help, and documentation together.
4. Open a pull request linking the issue.
5. Merge only after automated checks pass and review feedback is resolved.

## Local development

The project uses Python 3.11+ and `uv`.

```bash
uv sync --all-extras --dev
uv run pytest
uv run ruff check .
uv run mypy src
```

## Generated client

Do not hand-edit generated files. Update the pinned OpenAPI specification or generator templates/configuration and run the documented regeneration command. Commit the specification, generated code, and generated documentation in the same pull request.

## Security

Never include real API keys, JWTs, passwords, cookies, private server URLs, or personal data in code, fixtures, issues, or pull requests.
