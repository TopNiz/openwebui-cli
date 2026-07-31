# openwebui_client.ConfigsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_config_api_v1_configs_export_get**](ConfigsApi.md#export_config_api_v1_configs_export_get) | **GET** /api/v1/configs/export | Export Config
[**get_banners_api_v1_configs_banners_get**](ConfigsApi.md#get_banners_api_v1_configs_banners_get) | **GET** /api/v1/configs/banners | Get Banners
[**get_code_execution_config_api_v1_configs_code_execution_get**](ConfigsApi.md#get_code_execution_config_api_v1_configs_code_execution_get) | **GET** /api/v1/configs/code_execution | Get Code Execution Config
[**get_config_namespace_api_v1_configs_namespace_namespace_get**](ConfigsApi.md#get_config_namespace_api_v1_configs_namespace_namespace_get) | **GET** /api/v1/configs/namespace/{namespace} | Get Config Namespace
[**get_connections_config_api_v1_configs_connections_get**](ConfigsApi.md#get_connections_config_api_v1_configs_connections_get) | **GET** /api/v1/configs/connections | Get Connections Config
[**get_models_config_api_v1_configs_models_get**](ConfigsApi.md#get_models_config_api_v1_configs_models_get) | **GET** /api/v1/configs/models | Get Models Config
[**get_models_defaults_api_v1_configs_models_defaults_get**](ConfigsApi.md#get_models_defaults_api_v1_configs_models_defaults_get) | **GET** /api/v1/configs/models/defaults | Get Models Defaults
[**get_subagents_config_api_v1_configs_subagents_get**](ConfigsApi.md#get_subagents_config_api_v1_configs_subagents_get) | **GET** /api/v1/configs/subagents | Get Subagents Config
[**get_terminal_servers_config_api_v1_configs_terminal_servers_get**](ConfigsApi.md#get_terminal_servers_config_api_v1_configs_terminal_servers_get) | **GET** /api/v1/configs/terminal_servers | Get Terminal Servers Config
[**get_tool_servers_config_api_v1_configs_tool_servers_get**](ConfigsApi.md#get_tool_servers_config_api_v1_configs_tool_servers_get) | **GET** /api/v1/configs/tool_servers | Get Tool Servers Config
[**import_config_api_v1_configs_import_post**](ConfigsApi.md#import_config_api_v1_configs_import_post) | **POST** /api/v1/configs/import | Import Config
[**put_terminal_server_lifecycle_api_v1_configs_terminal_servers_lifecycle_post**](ConfigsApi.md#put_terminal_server_lifecycle_api_v1_configs_terminal_servers_lifecycle_post) | **POST** /api/v1/configs/terminal_servers/lifecycle | Put Terminal Server Lifecycle
[**put_terminal_server_policy_api_v1_configs_terminal_servers_policy_post**](ConfigsApi.md#put_terminal_server_policy_api_v1_configs_terminal_servers_policy_post) | **POST** /api/v1/configs/terminal_servers/policy | Put Terminal Server Policy
[**refresh_terminal_server_terminals_api_v1_configs_terminal_servers_refresh_post**](ConfigsApi.md#refresh_terminal_server_terminals_api_v1_configs_terminal_servers_refresh_post) | **POST** /api/v1/configs/terminal_servers/refresh | Refresh Terminal Server Terminals
[**register_oauth_client_api_v1_configs_oauth_clients_register_post**](ConfigsApi.md#register_oauth_client_api_v1_configs_oauth_clients_register_post) | **POST** /api/v1/configs/oauth/clients/register | Register Oauth Client
[**set_banners_api_v1_configs_banners_post**](ConfigsApi.md#set_banners_api_v1_configs_banners_post) | **POST** /api/v1/configs/banners | Set Banners
[**set_code_execution_config_api_v1_configs_code_execution_post**](ConfigsApi.md#set_code_execution_config_api_v1_configs_code_execution_post) | **POST** /api/v1/configs/code_execution | Set Code Execution Config
[**set_connections_config_api_v1_configs_connections_post**](ConfigsApi.md#set_connections_config_api_v1_configs_connections_post) | **POST** /api/v1/configs/connections | Set Connections Config
[**set_default_suggestions_api_v1_configs_suggestions_post**](ConfigsApi.md#set_default_suggestions_api_v1_configs_suggestions_post) | **POST** /api/v1/configs/suggestions | Set Default Suggestions
[**set_models_config_api_v1_configs_models_post**](ConfigsApi.md#set_models_config_api_v1_configs_models_post) | **POST** /api/v1/configs/models | Set Models Config
[**set_subagents_config_api_v1_configs_subagents_post**](ConfigsApi.md#set_subagents_config_api_v1_configs_subagents_post) | **POST** /api/v1/configs/subagents | Set Subagents Config
[**set_terminal_servers_config_api_v1_configs_terminal_servers_post**](ConfigsApi.md#set_terminal_servers_config_api_v1_configs_terminal_servers_post) | **POST** /api/v1/configs/terminal_servers | Set Terminal Servers Config
[**set_tool_servers_config_api_v1_configs_tool_servers_post**](ConfigsApi.md#set_tool_servers_config_api_v1_configs_tool_servers_post) | **POST** /api/v1/configs/tool_servers | Set Tool Servers Config
[**verify_terminal_server_connection_api_v1_configs_terminal_servers_verify_post**](ConfigsApi.md#verify_terminal_server_connection_api_v1_configs_terminal_servers_verify_post) | **POST** /api/v1/configs/terminal_servers/verify | Verify Terminal Server Connection
[**verify_tool_servers_config_api_v1_configs_tool_servers_verify_post**](ConfigsApi.md#verify_tool_servers_config_api_v1_configs_tool_servers_verify_post) | **POST** /api/v1/configs/tool_servers/verify | Verify Tool Servers Config


# **export_config_api_v1_configs_export_get**
> Dict[str, object] export_config_api_v1_configs_export_get()

Export Config

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
    api_instance = openwebui_client.ConfigsApi(api_client)

    try:
        # Export Config
        api_response = await api_instance.export_config_api_v1_configs_export_get()
        print("The response of ConfigsApi->export_config_api_v1_configs_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->export_config_api_v1_configs_export_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

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

# **get_banners_api_v1_configs_banners_get**
> List[BannerModel] get_banners_api_v1_configs_banners_get()

Get Banners

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.banner_model import BannerModel
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
    api_instance = openwebui_client.ConfigsApi(api_client)

    try:
        # Get Banners
        api_response = await api_instance.get_banners_api_v1_configs_banners_get()
        print("The response of ConfigsApi->get_banners_api_v1_configs_banners_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->get_banners_api_v1_configs_banners_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BannerModel]**](BannerModel.md)

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

# **get_code_execution_config_api_v1_configs_code_execution_get**
> CodeInterpreterConfigForm get_code_execution_config_api_v1_configs_code_execution_get()

Get Code Execution Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.code_interpreter_config_form import CodeInterpreterConfigForm
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
    api_instance = openwebui_client.ConfigsApi(api_client)

    try:
        # Get Code Execution Config
        api_response = await api_instance.get_code_execution_config_api_v1_configs_code_execution_get()
        print("The response of ConfigsApi->get_code_execution_config_api_v1_configs_code_execution_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->get_code_execution_config_api_v1_configs_code_execution_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CodeInterpreterConfigForm**](CodeInterpreterConfigForm.md)

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

# **get_config_namespace_api_v1_configs_namespace_namespace_get**
> Dict[str, object] get_config_namespace_api_v1_configs_namespace_namespace_get(namespace)

Get Config Namespace

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
    api_instance = openwebui_client.ConfigsApi(api_client)
    namespace = 'namespace_example' # str | 

    try:
        # Get Config Namespace
        api_response = await api_instance.get_config_namespace_api_v1_configs_namespace_namespace_get(namespace)
        print("The response of ConfigsApi->get_config_namespace_api_v1_configs_namespace_namespace_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->get_config_namespace_api_v1_configs_namespace_namespace_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**|  | 

### Return type

**Dict[str, object]**

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

# **get_connections_config_api_v1_configs_connections_get**
> ConnectionsConfigForm get_connections_config_api_v1_configs_connections_get()

Get Connections Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.connections_config_form import ConnectionsConfigForm
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
    api_instance = openwebui_client.ConfigsApi(api_client)

    try:
        # Get Connections Config
        api_response = await api_instance.get_connections_config_api_v1_configs_connections_get()
        print("The response of ConfigsApi->get_connections_config_api_v1_configs_connections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->get_connections_config_api_v1_configs_connections_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ConnectionsConfigForm**](ConnectionsConfigForm.md)

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

# **get_models_config_api_v1_configs_models_get**
> ModelsConfigForm get_models_config_api_v1_configs_models_get()

Get Models Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.models_config_form import ModelsConfigForm
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
    api_instance = openwebui_client.ConfigsApi(api_client)

    try:
        # Get Models Config
        api_response = await api_instance.get_models_config_api_v1_configs_models_get()
        print("The response of ConfigsApi->get_models_config_api_v1_configs_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->get_models_config_api_v1_configs_models_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ModelsConfigForm**](ModelsConfigForm.md)

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

# **get_models_defaults_api_v1_configs_models_defaults_get**
> object get_models_defaults_api_v1_configs_models_defaults_get()

Get Models Defaults

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
    api_instance = openwebui_client.ConfigsApi(api_client)

    try:
        # Get Models Defaults
        api_response = await api_instance.get_models_defaults_api_v1_configs_models_defaults_get()
        print("The response of ConfigsApi->get_models_defaults_api_v1_configs_models_defaults_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->get_models_defaults_api_v1_configs_models_defaults_get: %s\n" % e)
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

# **get_subagents_config_api_v1_configs_subagents_get**
> SubagentsConfigForm get_subagents_config_api_v1_configs_subagents_get()

Get Subagents Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.subagents_config_form import SubagentsConfigForm
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
    api_instance = openwebui_client.ConfigsApi(api_client)

    try:
        # Get Subagents Config
        api_response = await api_instance.get_subagents_config_api_v1_configs_subagents_get()
        print("The response of ConfigsApi->get_subagents_config_api_v1_configs_subagents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->get_subagents_config_api_v1_configs_subagents_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SubagentsConfigForm**](SubagentsConfigForm.md)

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

# **get_terminal_servers_config_api_v1_configs_terminal_servers_get**
> object get_terminal_servers_config_api_v1_configs_terminal_servers_get()

Get Terminal Servers Config

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
    api_instance = openwebui_client.ConfigsApi(api_client)

    try:
        # Get Terminal Servers Config
        api_response = await api_instance.get_terminal_servers_config_api_v1_configs_terminal_servers_get()
        print("The response of ConfigsApi->get_terminal_servers_config_api_v1_configs_terminal_servers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->get_terminal_servers_config_api_v1_configs_terminal_servers_get: %s\n" % e)
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

# **get_tool_servers_config_api_v1_configs_tool_servers_get**
> ToolServersConfigForm get_tool_servers_config_api_v1_configs_tool_servers_get()

Get Tool Servers Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.tool_servers_config_form import ToolServersConfigForm
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
    api_instance = openwebui_client.ConfigsApi(api_client)

    try:
        # Get Tool Servers Config
        api_response = await api_instance.get_tool_servers_config_api_v1_configs_tool_servers_get()
        print("The response of ConfigsApi->get_tool_servers_config_api_v1_configs_tool_servers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->get_tool_servers_config_api_v1_configs_tool_servers_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ToolServersConfigForm**](ToolServersConfigForm.md)

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

# **import_config_api_v1_configs_import_post**
> Dict[str, object] import_config_api_v1_configs_import_post(import_config_form)

Import Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.import_config_form import ImportConfigForm
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
    api_instance = openwebui_client.ConfigsApi(api_client)
    import_config_form = openwebui_client.ImportConfigForm() # ImportConfigForm | 

    try:
        # Import Config
        api_response = await api_instance.import_config_api_v1_configs_import_post(import_config_form)
        print("The response of ConfigsApi->import_config_api_v1_configs_import_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->import_config_api_v1_configs_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_config_form** | [**ImportConfigForm**](ImportConfigForm.md)|  | 

### Return type

**Dict[str, object]**

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

# **put_terminal_server_lifecycle_api_v1_configs_terminal_servers_lifecycle_post**
> object put_terminal_server_lifecycle_api_v1_configs_terminal_servers_lifecycle_post(terminal_server_lifecycle_form)

Put Terminal Server Lifecycle

Proxy a lifecycle read or update to an orchestrator terminal server.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.terminal_server_lifecycle_form import TerminalServerLifecycleForm
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
    api_instance = openwebui_client.ConfigsApi(api_client)
    terminal_server_lifecycle_form = openwebui_client.TerminalServerLifecycleForm() # TerminalServerLifecycleForm | 

    try:
        # Put Terminal Server Lifecycle
        api_response = await api_instance.put_terminal_server_lifecycle_api_v1_configs_terminal_servers_lifecycle_post(terminal_server_lifecycle_form)
        print("The response of ConfigsApi->put_terminal_server_lifecycle_api_v1_configs_terminal_servers_lifecycle_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->put_terminal_server_lifecycle_api_v1_configs_terminal_servers_lifecycle_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal_server_lifecycle_form** | [**TerminalServerLifecycleForm**](TerminalServerLifecycleForm.md)|  | 

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

# **put_terminal_server_policy_api_v1_configs_terminal_servers_policy_post**
> object put_terminal_server_policy_api_v1_configs_terminal_servers_policy_post(terminal_server_policy_form)

Put Terminal Server Policy

Proxy a policy read or update to an orchestrator terminal server.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.terminal_server_policy_form import TerminalServerPolicyForm
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
    api_instance = openwebui_client.ConfigsApi(api_client)
    terminal_server_policy_form = openwebui_client.TerminalServerPolicyForm() # TerminalServerPolicyForm | 

    try:
        # Put Terminal Server Policy
        api_response = await api_instance.put_terminal_server_policy_api_v1_configs_terminal_servers_policy_post(terminal_server_policy_form)
        print("The response of ConfigsApi->put_terminal_server_policy_api_v1_configs_terminal_servers_policy_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->put_terminal_server_policy_api_v1_configs_terminal_servers_policy_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal_server_policy_form** | [**TerminalServerPolicyForm**](TerminalServerPolicyForm.md)|  | 

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

# **refresh_terminal_server_terminals_api_v1_configs_terminal_servers_refresh_post**
> object refresh_terminal_server_terminals_api_v1_configs_terminal_servers_refresh_post(terminal_server_refresh_form)

Refresh Terminal Server Terminals

Proxy a terminal refresh request to an orchestrator terminal server.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.terminal_server_refresh_form import TerminalServerRefreshForm
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
    api_instance = openwebui_client.ConfigsApi(api_client)
    terminal_server_refresh_form = openwebui_client.TerminalServerRefreshForm() # TerminalServerRefreshForm | 

    try:
        # Refresh Terminal Server Terminals
        api_response = await api_instance.refresh_terminal_server_terminals_api_v1_configs_terminal_servers_refresh_post(terminal_server_refresh_form)
        print("The response of ConfigsApi->refresh_terminal_server_terminals_api_v1_configs_terminal_servers_refresh_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->refresh_terminal_server_terminals_api_v1_configs_terminal_servers_refresh_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal_server_refresh_form** | [**TerminalServerRefreshForm**](TerminalServerRefreshForm.md)|  | 

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

# **register_oauth_client_api_v1_configs_oauth_clients_register_post**
> object register_oauth_client_api_v1_configs_oauth_clients_register_post(o_auth_client_registration_form, type=type)

Register Oauth Client

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.o_auth_client_registration_form import OAuthClientRegistrationForm
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
    api_instance = openwebui_client.ConfigsApi(api_client)
    o_auth_client_registration_form = openwebui_client.OAuthClientRegistrationForm() # OAuthClientRegistrationForm | 
    type = 'type_example' # str |  (optional)

    try:
        # Register Oauth Client
        api_response = await api_instance.register_oauth_client_api_v1_configs_oauth_clients_register_post(o_auth_client_registration_form, type=type)
        print("The response of ConfigsApi->register_oauth_client_api_v1_configs_oauth_clients_register_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->register_oauth_client_api_v1_configs_oauth_clients_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_client_registration_form** | [**OAuthClientRegistrationForm**](OAuthClientRegistrationForm.md)|  | 
 **type** | **str**|  | [optional] 

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

# **set_banners_api_v1_configs_banners_post**
> List[BannerModel] set_banners_api_v1_configs_banners_post(set_banners_form)

Set Banners

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.banner_model import BannerModel
from openwebui_client.models.set_banners_form import SetBannersForm
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
    api_instance = openwebui_client.ConfigsApi(api_client)
    set_banners_form = openwebui_client.SetBannersForm() # SetBannersForm | 

    try:
        # Set Banners
        api_response = await api_instance.set_banners_api_v1_configs_banners_post(set_banners_form)
        print("The response of ConfigsApi->set_banners_api_v1_configs_banners_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->set_banners_api_v1_configs_banners_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_banners_form** | [**SetBannersForm**](SetBannersForm.md)|  | 

### Return type

[**List[BannerModel]**](BannerModel.md)

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

# **set_code_execution_config_api_v1_configs_code_execution_post**
> CodeInterpreterConfigForm set_code_execution_config_api_v1_configs_code_execution_post(code_interpreter_config_form)

Set Code Execution Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.code_interpreter_config_form import CodeInterpreterConfigForm
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
    api_instance = openwebui_client.ConfigsApi(api_client)
    code_interpreter_config_form = openwebui_client.CodeInterpreterConfigForm() # CodeInterpreterConfigForm | 

    try:
        # Set Code Execution Config
        api_response = await api_instance.set_code_execution_config_api_v1_configs_code_execution_post(code_interpreter_config_form)
        print("The response of ConfigsApi->set_code_execution_config_api_v1_configs_code_execution_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->set_code_execution_config_api_v1_configs_code_execution_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_interpreter_config_form** | [**CodeInterpreterConfigForm**](CodeInterpreterConfigForm.md)|  | 

### Return type

[**CodeInterpreterConfigForm**](CodeInterpreterConfigForm.md)

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

# **set_connections_config_api_v1_configs_connections_post**
> ConnectionsConfigForm set_connections_config_api_v1_configs_connections_post(connections_config_form)

Set Connections Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.connections_config_form import ConnectionsConfigForm
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
    api_instance = openwebui_client.ConfigsApi(api_client)
    connections_config_form = openwebui_client.ConnectionsConfigForm() # ConnectionsConfigForm | 

    try:
        # Set Connections Config
        api_response = await api_instance.set_connections_config_api_v1_configs_connections_post(connections_config_form)
        print("The response of ConfigsApi->set_connections_config_api_v1_configs_connections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->set_connections_config_api_v1_configs_connections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connections_config_form** | [**ConnectionsConfigForm**](ConnectionsConfigForm.md)|  | 

### Return type

[**ConnectionsConfigForm**](ConnectionsConfigForm.md)

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

# **set_default_suggestions_api_v1_configs_suggestions_post**
> List[PromptSuggestion] set_default_suggestions_api_v1_configs_suggestions_post(set_default_suggestions_form)

Set Default Suggestions

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.prompt_suggestion import PromptSuggestion
from openwebui_client.models.set_default_suggestions_form import SetDefaultSuggestionsForm
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
    api_instance = openwebui_client.ConfigsApi(api_client)
    set_default_suggestions_form = openwebui_client.SetDefaultSuggestionsForm() # SetDefaultSuggestionsForm | 

    try:
        # Set Default Suggestions
        api_response = await api_instance.set_default_suggestions_api_v1_configs_suggestions_post(set_default_suggestions_form)
        print("The response of ConfigsApi->set_default_suggestions_api_v1_configs_suggestions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->set_default_suggestions_api_v1_configs_suggestions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_default_suggestions_form** | [**SetDefaultSuggestionsForm**](SetDefaultSuggestionsForm.md)|  | 

### Return type

[**List[PromptSuggestion]**](PromptSuggestion.md)

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

# **set_models_config_api_v1_configs_models_post**
> ModelsConfigForm set_models_config_api_v1_configs_models_post(models_config_form)

Set Models Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.models_config_form import ModelsConfigForm
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
    api_instance = openwebui_client.ConfigsApi(api_client)
    models_config_form = openwebui_client.ModelsConfigForm() # ModelsConfigForm | 

    try:
        # Set Models Config
        api_response = await api_instance.set_models_config_api_v1_configs_models_post(models_config_form)
        print("The response of ConfigsApi->set_models_config_api_v1_configs_models_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->set_models_config_api_v1_configs_models_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **models_config_form** | [**ModelsConfigForm**](ModelsConfigForm.md)|  | 

### Return type

[**ModelsConfigForm**](ModelsConfigForm.md)

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

# **set_subagents_config_api_v1_configs_subagents_post**
> SubagentsConfigForm set_subagents_config_api_v1_configs_subagents_post(subagents_config_form)

Set Subagents Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.subagents_config_form import SubagentsConfigForm
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
    api_instance = openwebui_client.ConfigsApi(api_client)
    subagents_config_form = openwebui_client.SubagentsConfigForm() # SubagentsConfigForm | 

    try:
        # Set Subagents Config
        api_response = await api_instance.set_subagents_config_api_v1_configs_subagents_post(subagents_config_form)
        print("The response of ConfigsApi->set_subagents_config_api_v1_configs_subagents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->set_subagents_config_api_v1_configs_subagents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subagents_config_form** | [**SubagentsConfigForm**](SubagentsConfigForm.md)|  | 

### Return type

[**SubagentsConfigForm**](SubagentsConfigForm.md)

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

# **set_terminal_servers_config_api_v1_configs_terminal_servers_post**
> object set_terminal_servers_config_api_v1_configs_terminal_servers_post(terminal_servers_config_form)

Set Terminal Servers Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.terminal_servers_config_form import TerminalServersConfigForm
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
    api_instance = openwebui_client.ConfigsApi(api_client)
    terminal_servers_config_form = openwebui_client.TerminalServersConfigForm() # TerminalServersConfigForm | 

    try:
        # Set Terminal Servers Config
        api_response = await api_instance.set_terminal_servers_config_api_v1_configs_terminal_servers_post(terminal_servers_config_form)
        print("The response of ConfigsApi->set_terminal_servers_config_api_v1_configs_terminal_servers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->set_terminal_servers_config_api_v1_configs_terminal_servers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal_servers_config_form** | [**TerminalServersConfigForm**](TerminalServersConfigForm.md)|  | 

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

# **set_tool_servers_config_api_v1_configs_tool_servers_post**
> ToolServersConfigForm set_tool_servers_config_api_v1_configs_tool_servers_post(tool_servers_config_form)

Set Tool Servers Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.tool_servers_config_form import ToolServersConfigForm
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
    api_instance = openwebui_client.ConfigsApi(api_client)
    tool_servers_config_form = openwebui_client.ToolServersConfigForm() # ToolServersConfigForm | 

    try:
        # Set Tool Servers Config
        api_response = await api_instance.set_tool_servers_config_api_v1_configs_tool_servers_post(tool_servers_config_form)
        print("The response of ConfigsApi->set_tool_servers_config_api_v1_configs_tool_servers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->set_tool_servers_config_api_v1_configs_tool_servers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_servers_config_form** | [**ToolServersConfigForm**](ToolServersConfigForm.md)|  | 

### Return type

[**ToolServersConfigForm**](ToolServersConfigForm.md)

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

# **verify_terminal_server_connection_api_v1_configs_terminal_servers_verify_post**
> object verify_terminal_server_connection_api_v1_configs_terminal_servers_verify_post(terminal_server_connection)

Verify Terminal Server Connection

Verify the connection to a terminal server by detecting its type.

Tries GET {url}/api/v1/policies (orchestrator) then GET {url}/api/config
(plain terminal).  Returns ``{status: true, type: "orchestrator"|"terminal"}``.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.terminal_server_connection import TerminalServerConnection
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
    api_instance = openwebui_client.ConfigsApi(api_client)
    terminal_server_connection = openwebui_client.TerminalServerConnection() # TerminalServerConnection | 

    try:
        # Verify Terminal Server Connection
        api_response = await api_instance.verify_terminal_server_connection_api_v1_configs_terminal_servers_verify_post(terminal_server_connection)
        print("The response of ConfigsApi->verify_terminal_server_connection_api_v1_configs_terminal_servers_verify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->verify_terminal_server_connection_api_v1_configs_terminal_servers_verify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal_server_connection** | [**TerminalServerConnection**](TerminalServerConnection.md)|  | 

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

# **verify_tool_servers_config_api_v1_configs_tool_servers_verify_post**
> object verify_tool_servers_config_api_v1_configs_tool_servers_verify_post(tool_server_connection)

Verify Tool Servers Config

Verify the connection to the tool server.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.tool_server_connection import ToolServerConnection
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
    api_instance = openwebui_client.ConfigsApi(api_client)
    tool_server_connection = openwebui_client.ToolServerConnection() # ToolServerConnection | 

    try:
        # Verify Tool Servers Config
        api_response = await api_instance.verify_tool_servers_config_api_v1_configs_tool_servers_verify_post(tool_server_connection)
        print("The response of ConfigsApi->verify_tool_servers_config_api_v1_configs_tool_servers_verify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigsApi->verify_tool_servers_config_api_v1_configs_tool_servers_verify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_server_connection** | [**ToolServerConnection**](ToolServerConnection.md)|  | 

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

