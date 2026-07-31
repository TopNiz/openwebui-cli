from openwebui_client import ApiClient, Configuration
from openwebui_client.api.auths_api import AuthsApi
from openwebui_client.api.users_api import UsersApi


def test_generated_client_is_importable() -> None:
    configuration = Configuration(host="https://example.test", access_token="not-a-real-credential")
    client = ApiClient(configuration)

    assert isinstance(AuthsApi(client), AuthsApi)
    assert isinstance(UsersApi(client), UsersApi)
