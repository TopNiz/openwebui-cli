# OpenAPI source

`openapi.json` is the pinned API description used to generate the low-level Python client.

## Provenance

- upstream application: Open WebUI;
- upstream runtime version: `0.11.0`;
- OpenAPI version: `3.1.0`;
- acquisition method: authenticated project instance exposed `/openapi.json` temporarily through Open WebUI development mode;
- deployment-specific hostnames and credentials: not present in the committed specification.

See `source.json` for machine-readable provenance.

## Updating

1. Use an isolated or approved Open WebUI instance running the target version.
2. Temporarily set `ENV=dev` if Swagger/OpenAPI routes are unavailable.
3. Download `/openapi.json`.
4. Validate the document and scan it for deployment-specific information and credentials.
5. Update `source.json` and regenerate the client.
6. Review the diff and compatibility impact in a pull request.
7. Restore `ENV=prod` before production deployment.
