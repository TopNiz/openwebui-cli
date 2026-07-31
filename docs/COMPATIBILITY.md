# Compatibility

## Supported baseline

| Component | Version |
|---|---|
| Open WebUI | 0.11.0 |
| OpenAPI | 3.1.0 |
| OpenAPI Generator | 7.21.0 |
| Python | 3.11–3.14 |

The high-level client and CLI are tested against the API shape captured in `openapi/openapi.json`. The low-level generated client exposes all operations in that exact description.

## Upstream API stability

Open WebUI describes its programmatic API as experimental. Administrative routes, request schemas, and response schemas can change between Open WebUI releases. Before upgrading a managed instance:

1. capture the new OpenAPI description from an isolated or approved instance;
2. review raw and normalized diffs;
3. regenerate the low-level client;
4. run unit, CLI, and compatibility tests;
5. test read-only operations against the target version;
6. test mutations in a disposable environment;
7. publish a compatibility release before production rollout.

## Development mode

Open WebUI normally exposes `/docs` and `/openapi.json` only when `ENV=dev`. Development mode is acceptable for an explicitly approved proof of concept. Before production, restore `ENV=prod`, confirm the documentation routes are unavailable, restrict API-key endpoints where appropriate, and complete a security review.

The CLI does not require Swagger routes after installation; it calls ordinary authenticated API endpoints.

## Known limitations

- One API key is supported per Open WebUI account by upstream 0.11.0.
- Profiles select one API key through environment or keyring lookup.
- Arbitrary group, knowledge, model, and tool administration is available only through the generated client until stable high-level commands are added.
- The CLI does not provide a mobile authentication proxy; do not embed service keys in mobile or browser applications.
- No claim of compatibility is made for older or newer Open WebUI versions until tested.
