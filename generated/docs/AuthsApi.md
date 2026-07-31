# openwebui_client.AuthsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_api_v1_auths_add_post**](AuthsApi.md#add_user_api_v1_auths_add_post) | **POST** /api/v1/auths/add | Add User
[**delete_api_key_api_v1_auths_api_key_delete**](AuthsApi.md#delete_api_key_api_v1_auths_api_key_delete) | **DELETE** /api/v1/auths/api_key | Delete Api Key
[**delete_oauth_session_by_provider_api_v1_auths_oauth_sessions_provider_delete**](AuthsApi.md#delete_oauth_session_by_provider_api_v1_auths_oauth_sessions_provider_delete) | **DELETE** /api/v1/auths/oauth/sessions/{provider} | Delete Oauth Session By Provider
[**generate_api_key_api_v1_auths_api_key_post**](AuthsApi.md#generate_api_key_api_v1_auths_api_key_post) | **POST** /api/v1/auths/api_key | Generate Api Key
[**get_admin_config_api_v1_auths_admin_config_get**](AuthsApi.md#get_admin_config_api_v1_auths_admin_config_get) | **GET** /api/v1/auths/admin/config | Get Admin Config
[**get_admin_details_api_v1_auths_admin_details_get**](AuthsApi.md#get_admin_details_api_v1_auths_admin_details_get) | **GET** /api/v1/auths/admin/details | Get Admin Details
[**get_api_key_api_v1_auths_api_key_get**](AuthsApi.md#get_api_key_api_v1_auths_api_key_get) | **GET** /api/v1/auths/api_key | Get Api Key
[**get_ldap_config_api_v1_auths_admin_config_ldap_get**](AuthsApi.md#get_ldap_config_api_v1_auths_admin_config_ldap_get) | **GET** /api/v1/auths/admin/config/ldap | Get Ldap Config
[**get_ldap_server_api_v1_auths_admin_config_ldap_server_get**](AuthsApi.md#get_ldap_server_api_v1_auths_admin_config_ldap_server_get) | **GET** /api/v1/auths/admin/config/ldap/server | Get Ldap Server
[**get_oauth_config_api_v1_auths_admin_config_oauth_get**](AuthsApi.md#get_oauth_config_api_v1_auths_admin_config_oauth_get) | **GET** /api/v1/auths/admin/config/oauth | Get Oauth Config
[**get_session_user_api_v1_auths_get**](AuthsApi.md#get_session_user_api_v1_auths_get) | **GET** /api/v1/auths/ | Get Session User
[**ldap_auth_api_v1_auths_ldap_post**](AuthsApi.md#ldap_auth_api_v1_auths_ldap_post) | **POST** /api/v1/auths/ldap | Ldap Auth
[**signin_api_v1_auths_signin_post**](AuthsApi.md#signin_api_v1_auths_signin_post) | **POST** /api/v1/auths/signin | Signin
[**signout_api_v1_auths_signout_post**](AuthsApi.md#signout_api_v1_auths_signout_post) | **POST** /api/v1/auths/signout | Signout
[**signup_api_v1_auths_signup_post**](AuthsApi.md#signup_api_v1_auths_signup_post) | **POST** /api/v1/auths/signup | Signup
[**token_exchange_api_v1_auths_oauth_provider_token_exchange_post**](AuthsApi.md#token_exchange_api_v1_auths_oauth_provider_token_exchange_post) | **POST** /api/v1/auths/oauth/{provider}/token/exchange | Token Exchange
[**update_admin_config_api_v1_auths_admin_config_post**](AuthsApi.md#update_admin_config_api_v1_auths_admin_config_post) | **POST** /api/v1/auths/admin/config | Update Admin Config
[**update_ldap_config_api_v1_auths_admin_config_ldap_post**](AuthsApi.md#update_ldap_config_api_v1_auths_admin_config_ldap_post) | **POST** /api/v1/auths/admin/config/ldap | Update Ldap Config
[**update_ldap_server_api_v1_auths_admin_config_ldap_server_post**](AuthsApi.md#update_ldap_server_api_v1_auths_admin_config_ldap_server_post) | **POST** /api/v1/auths/admin/config/ldap/server | Update Ldap Server
[**update_oauth_config_api_v1_auths_admin_config_oauth_post**](AuthsApi.md#update_oauth_config_api_v1_auths_admin_config_oauth_post) | **POST** /api/v1/auths/admin/config/oauth | Update Oauth Config
[**update_password_api_v1_auths_update_password_post**](AuthsApi.md#update_password_api_v1_auths_update_password_post) | **POST** /api/v1/auths/update/password | Update Password
[**update_profile_api_v1_auths_update_profile_post**](AuthsApi.md#update_profile_api_v1_auths_update_profile_post) | **POST** /api/v1/auths/update/profile | Update Profile
[**update_timezone_api_v1_auths_update_timezone_post**](AuthsApi.md#update_timezone_api_v1_auths_update_timezone_post) | **POST** /api/v1/auths/update/timezone | Update Timezone


# **add_user_api_v1_auths_add_post**
> SigninResponse add_user_api_v1_auths_add_post(add_user_form)

Add User

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.add_user_form import AddUserForm
from openwebui_client.models.signin_response import SigninResponse
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openwebui_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)
    add_user_form = openwebui_client.AddUserForm() # AddUserForm | 

    try:
        # Add User
        api_response = await api_instance.add_user_api_v1_auths_add_post(add_user_form)
        print("The response of AuthsApi->add_user_api_v1_auths_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->add_user_api_v1_auths_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_form** | [**AddUserForm**](AddUserForm.md)|  | 

### Return type

[**SigninResponse**](SigninResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key_api_v1_auths_api_key_delete**
> bool delete_api_key_api_v1_auths_api_key_delete()

Delete Api Key

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openwebui_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)

    try:
        # Delete Api Key
        api_response = await api_instance.delete_api_key_api_v1_auths_api_key_delete()
        print("The response of AuthsApi->delete_api_key_api_v1_auths_api_key_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->delete_api_key_api_v1_auths_api_key_delete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_oauth_session_by_provider_api_v1_auths_oauth_sessions_provider_delete**
> bool delete_oauth_session_by_provider_api_v1_auths_oauth_sessions_provider_delete(provider)

Delete Oauth Session By Provider

Disconnect the current user's OAuth session for a specific provider.
The provider string matches the 'provider' field in the oauth_session table
(e.g. 'mcp:server-id' for MCP connections).

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openwebui_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)
    provider = 'provider_example' # str | 

    try:
        # Delete Oauth Session By Provider
        api_response = await api_instance.delete_oauth_session_by_provider_api_v1_auths_oauth_sessions_provider_delete(provider)
        print("The response of AuthsApi->delete_oauth_session_by_provider_api_v1_auths_oauth_sessions_provider_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->delete_oauth_session_by_provider_api_v1_auths_oauth_sessions_provider_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 

### Return type

**bool**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_api_key_api_v1_auths_api_key_post**
> ApiKey generate_api_key_api_v1_auths_api_key_post()

Generate Api Key

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.api_key import ApiKey
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openwebui_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)

    try:
        # Generate Api Key
        api_response = await api_instance.generate_api_key_api_v1_auths_api_key_post()
        print("The response of AuthsApi->generate_api_key_api_v1_auths_api_key_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->generate_api_key_api_v1_auths_api_key_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_config_api_v1_auths_admin_config_get**
> object get_admin_config_api_v1_auths_admin_config_get()

Get Admin Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openwebui_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)

    try:
        # Get Admin Config
        api_response = await api_instance.get_admin_config_api_v1_auths_admin_config_get()
        print("The response of AuthsApi->get_admin_config_api_v1_auths_admin_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->get_admin_config_api_v1_auths_admin_config_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_details_api_v1_auths_admin_details_get**
> object get_admin_details_api_v1_auths_admin_details_get()

Get Admin Details

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openwebui_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)

    try:
        # Get Admin Details
        api_response = await api_instance.get_admin_details_api_v1_auths_admin_details_get()
        print("The response of AuthsApi->get_admin_details_api_v1_auths_admin_details_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->get_admin_details_api_v1_auths_admin_details_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key_api_v1_auths_api_key_get**
> ApiKey get_api_key_api_v1_auths_api_key_get()

Get Api Key

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.api_key import ApiKey
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openwebui_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)

    try:
        # Get Api Key
        api_response = await api_instance.get_api_key_api_v1_auths_api_key_get()
        print("The response of AuthsApi->get_api_key_api_v1_auths_api_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->get_api_key_api_v1_auths_api_key_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ldap_config_api_v1_auths_admin_config_ldap_get**
> object get_ldap_config_api_v1_auths_admin_config_ldap_get()

Get Ldap Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openwebui_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)

    try:
        # Get Ldap Config
        api_response = await api_instance.get_ldap_config_api_v1_auths_admin_config_ldap_get()
        print("The response of AuthsApi->get_ldap_config_api_v1_auths_admin_config_ldap_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->get_ldap_config_api_v1_auths_admin_config_ldap_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ldap_server_api_v1_auths_admin_config_ldap_server_get**
> LdapServerConfig get_ldap_server_api_v1_auths_admin_config_ldap_server_get()

Get Ldap Server

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.ldap_server_config import LdapServerConfig
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openwebui_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)

    try:
        # Get Ldap Server
        api_response = await api_instance.get_ldap_server_api_v1_auths_admin_config_ldap_server_get()
        print("The response of AuthsApi->get_ldap_server_api_v1_auths_admin_config_ldap_server_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->get_ldap_server_api_v1_auths_admin_config_ldap_server_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LdapServerConfig**](LdapServerConfig.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oauth_config_api_v1_auths_admin_config_oauth_get**
> OAuthConfigForm get_oauth_config_api_v1_auths_admin_config_oauth_get()

Get Oauth Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.o_auth_config_form import OAuthConfigForm
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openwebui_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)

    try:
        # Get Oauth Config
        api_response = await api_instance.get_oauth_config_api_v1_auths_admin_config_oauth_get()
        print("The response of AuthsApi->get_oauth_config_api_v1_auths_admin_config_oauth_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->get_oauth_config_api_v1_auths_admin_config_oauth_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OAuthConfigForm**](OAuthConfigForm.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session_user_api_v1_auths_get**
> SessionUserInfoResponse get_session_user_api_v1_auths_get()

Get Session User

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.session_user_info_response import SessionUserInfoResponse
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openwebui_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)

    try:
        # Get Session User
        api_response = await api_instance.get_session_user_api_v1_auths_get()
        print("The response of AuthsApi->get_session_user_api_v1_auths_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->get_session_user_api_v1_auths_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SessionUserInfoResponse**](SessionUserInfoResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_auth_api_v1_auths_ldap_post**
> SessionUserResponse ldap_auth_api_v1_auths_ldap_post(ldap_form)

Ldap Auth

### Example


```python
import openwebui_client
from openwebui_client.models.ldap_form import LdapForm
from openwebui_client.models.session_user_response import SessionUserResponse
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)
    ldap_form = openwebui_client.LdapForm() # LdapForm | 

    try:
        # Ldap Auth
        api_response = await api_instance.ldap_auth_api_v1_auths_ldap_post(ldap_form)
        print("The response of AuthsApi->ldap_auth_api_v1_auths_ldap_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->ldap_auth_api_v1_auths_ldap_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_form** | [**LdapForm**](LdapForm.md)|  | 

### Return type

[**SessionUserResponse**](SessionUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signin_api_v1_auths_signin_post**
> SessionUserResponse signin_api_v1_auths_signin_post(signin_form)

Signin

### Example


```python
import openwebui_client
from openwebui_client.models.session_user_response import SessionUserResponse
from openwebui_client.models.signin_form import SigninForm
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)
    signin_form = openwebui_client.SigninForm() # SigninForm | 

    try:
        # Signin
        api_response = await api_instance.signin_api_v1_auths_signin_post(signin_form)
        print("The response of AuthsApi->signin_api_v1_auths_signin_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->signin_api_v1_auths_signin_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signin_form** | [**SigninForm**](SigninForm.md)|  | 

### Return type

[**SessionUserResponse**](SessionUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signout_api_v1_auths_signout_post**
> object signout_api_v1_auths_signout_post()

Signout

### Example


```python
import openwebui_client
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)

    try:
        # Signout
        api_response = await api_instance.signout_api_v1_auths_signout_post()
        print("The response of AuthsApi->signout_api_v1_auths_signout_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->signout_api_v1_auths_signout_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signup_api_v1_auths_signup_post**
> SessionUserResponse signup_api_v1_auths_signup_post(signup_form)

Signup

### Example


```python
import openwebui_client
from openwebui_client.models.session_user_response import SessionUserResponse
from openwebui_client.models.signup_form import SignupForm
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)
    signup_form = openwebui_client.SignupForm() # SignupForm | 

    try:
        # Signup
        api_response = await api_instance.signup_api_v1_auths_signup_post(signup_form)
        print("The response of AuthsApi->signup_api_v1_auths_signup_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->signup_api_v1_auths_signup_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signup_form** | [**SignupForm**](SignupForm.md)|  | 

### Return type

[**SessionUserResponse**](SessionUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_exchange_api_v1_auths_oauth_provider_token_exchange_post**
> SessionUserResponse token_exchange_api_v1_auths_oauth_provider_token_exchange_post(provider, token_exchange_form)

Token Exchange

Exchange an external OAuth provider token for an OpenWebUI JWT.
This endpoint is disabled by default. Set ENABLE_OAUTH_TOKEN_EXCHANGE=True to enable.

### Example


```python
import openwebui_client
from openwebui_client.models.session_user_response import SessionUserResponse
from openwebui_client.models.token_exchange_form import TokenExchangeForm
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)
    provider = 'provider_example' # str | 
    token_exchange_form = openwebui_client.TokenExchangeForm() # TokenExchangeForm | 

    try:
        # Token Exchange
        api_response = await api_instance.token_exchange_api_v1_auths_oauth_provider_token_exchange_post(provider, token_exchange_form)
        print("The response of AuthsApi->token_exchange_api_v1_auths_oauth_provider_token_exchange_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->token_exchange_api_v1_auths_oauth_provider_token_exchange_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **token_exchange_form** | [**TokenExchangeForm**](TokenExchangeForm.md)|  | 

### Return type

[**SessionUserResponse**](SessionUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_admin_config_api_v1_auths_admin_config_post**
> object update_admin_config_api_v1_auths_admin_config_post(admin_config)

Update Admin Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.admin_config import AdminConfig
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openwebui_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)
    admin_config = openwebui_client.AdminConfig() # AdminConfig | 

    try:
        # Update Admin Config
        api_response = await api_instance.update_admin_config_api_v1_auths_admin_config_post(admin_config)
        print("The response of AuthsApi->update_admin_config_api_v1_auths_admin_config_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->update_admin_config_api_v1_auths_admin_config_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_config** | [**AdminConfig**](AdminConfig.md)|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ldap_config_api_v1_auths_admin_config_ldap_post**
> object update_ldap_config_api_v1_auths_admin_config_ldap_post(ldap_config_form)

Update Ldap Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.ldap_config_form import LdapConfigForm
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openwebui_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)
    ldap_config_form = openwebui_client.LdapConfigForm() # LdapConfigForm | 

    try:
        # Update Ldap Config
        api_response = await api_instance.update_ldap_config_api_v1_auths_admin_config_ldap_post(ldap_config_form)
        print("The response of AuthsApi->update_ldap_config_api_v1_auths_admin_config_ldap_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->update_ldap_config_api_v1_auths_admin_config_ldap_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_config_form** | [**LdapConfigForm**](LdapConfigForm.md)|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ldap_server_api_v1_auths_admin_config_ldap_server_post**
> object update_ldap_server_api_v1_auths_admin_config_ldap_server_post(ldap_server_config)

Update Ldap Server

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.ldap_server_config import LdapServerConfig
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openwebui_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)
    ldap_server_config = openwebui_client.LdapServerConfig() # LdapServerConfig | 

    try:
        # Update Ldap Server
        api_response = await api_instance.update_ldap_server_api_v1_auths_admin_config_ldap_server_post(ldap_server_config)
        print("The response of AuthsApi->update_ldap_server_api_v1_auths_admin_config_ldap_server_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->update_ldap_server_api_v1_auths_admin_config_ldap_server_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_server_config** | [**LdapServerConfig**](LdapServerConfig.md)|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_oauth_config_api_v1_auths_admin_config_oauth_post**
> OAuthConfigForm update_oauth_config_api_v1_auths_admin_config_oauth_post(o_auth_config_form)

Update Oauth Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.o_auth_config_form import OAuthConfigForm
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openwebui_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)
    o_auth_config_form = openwebui_client.OAuthConfigForm() # OAuthConfigForm | 

    try:
        # Update Oauth Config
        api_response = await api_instance.update_oauth_config_api_v1_auths_admin_config_oauth_post(o_auth_config_form)
        print("The response of AuthsApi->update_oauth_config_api_v1_auths_admin_config_oauth_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->update_oauth_config_api_v1_auths_admin_config_oauth_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_config_form** | [**OAuthConfigForm**](OAuthConfigForm.md)|  | 

### Return type

[**OAuthConfigForm**](OAuthConfigForm.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password_api_v1_auths_update_password_post**
> bool update_password_api_v1_auths_update_password_post(update_password_form)

Update Password

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.update_password_form import UpdatePasswordForm
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openwebui_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)
    update_password_form = openwebui_client.UpdatePasswordForm() # UpdatePasswordForm | 

    try:
        # Update Password
        api_response = await api_instance.update_password_api_v1_auths_update_password_post(update_password_form)
        print("The response of AuthsApi->update_password_api_v1_auths_update_password_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->update_password_api_v1_auths_update_password_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_password_form** | [**UpdatePasswordForm**](UpdatePasswordForm.md)|  | 

### Return type

**bool**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile_api_v1_auths_update_profile_post**
> UserProfileImageResponse update_profile_api_v1_auths_update_profile_post(update_profile_form)

Update Profile

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.update_profile_form import UpdateProfileForm
from openwebui_client.models.user_profile_image_response import UserProfileImageResponse
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openwebui_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)
    update_profile_form = openwebui_client.UpdateProfileForm() # UpdateProfileForm | 

    try:
        # Update Profile
        api_response = await api_instance.update_profile_api_v1_auths_update_profile_post(update_profile_form)
        print("The response of AuthsApi->update_profile_api_v1_auths_update_profile_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->update_profile_api_v1_auths_update_profile_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_profile_form** | [**UpdateProfileForm**](UpdateProfileForm.md)|  | 

### Return type

[**UserProfileImageResponse**](UserProfileImageResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_timezone_api_v1_auths_update_timezone_post**
> object update_timezone_api_v1_auths_update_timezone_post(update_timezone_form)

Update Timezone

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.update_timezone_form import UpdateTimezoneForm
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = openwebui_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.AuthsApi(api_client)
    update_timezone_form = openwebui_client.UpdateTimezoneForm() # UpdateTimezoneForm | 

    try:
        # Update Timezone
        api_response = await api_instance.update_timezone_api_v1_auths_update_timezone_post(update_timezone_form)
        print("The response of AuthsApi->update_timezone_api_v1_auths_update_timezone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthsApi->update_timezone_api_v1_auths_update_timezone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_timezone_form** | [**UpdateTimezoneForm**](UpdateTimezoneForm.md)|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

