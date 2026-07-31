# OpenAPI client generation

## Inputs and outputs

- Raw upstream document: `openapi/openapi.json`
- Deterministic normalized document: `openapi/openapi.normalized.json`
- Repair report: `openapi/NORMALIZATION.md`
- Generator configuration: `openapi-generator.yaml`
- Generated Python package: `generated/openwebui_client`
- Generated endpoint/model reference: `generated/docs`

The raw document is never edited. Open WebUI 0.11.0 emits duplicate operation IDs on wildcard proxy routes and omits one path-parameter declaration. `scripts/normalize-openapi.py` repairs only structural generator blockers and records every change.

## Requirements

- Python 3.11 or newer;
- OpenAPI Generator version recorded in `.openapi-generator-version`;
- Java required by OpenAPI Generator.

## Regenerate

```bash
./scripts/generate-client.sh
```

The script validates the normalized document before generating. Generated sources are intentionally excluded from linting because they follow upstream templates; import and package smoke tests still cover them.

## Check drift

After generated files are tracked:

```bash
./scripts/check-generated.sh
```

A specification or generator update must include raw provenance, normalization output, generated code, generated documentation, compatibility notes, and tests in the same pull request.

## Low-level client example

The generated HTTPX client is asynchronous:

```python
from openwebui_cli import ConfigStore, resolve_connection
from openwebui_cli.generated import create_generated_client
from openwebui_client.api.auths_api import AuthsApi

connection = resolve_connection(ConfigStore())
api_client = create_generated_client(connection)
auths = AuthsApi(api_client)

# Await generated operations inside an async function, then close the client.
```

Operation names and schemas are version-specific. Prefer the stable high-level `OpenWebUIClient` facade when it supports the required workflow.
