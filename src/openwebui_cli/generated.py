"""Bridge to the complete OpenAPI-generated asynchronous client."""

from openwebui_client import ApiClient, Configuration

from openwebui_cli.config import ResolvedConnection


def create_generated_client(connection: ResolvedConnection) -> ApiClient:
    """Create the low-level generated client for advanced API operations.

    The caller should use the returned asynchronous client as documented in
    ``generated/docs`` and close it after use.
    """

    configuration = Configuration(host=connection.base_url, access_token=connection.api_key)
    configuration.verify_ssl = connection.verify_ssl
    return ApiClient(configuration)
