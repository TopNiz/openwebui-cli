# openwebui_client.TerminalsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_terminal_servers_api_v1_terminals_get**](TerminalsApi.md#list_terminal_servers_api_v1_terminals_get) | **GET** /api/v1/terminals/ | List Terminal Servers
[**proxy_terminal_api_v1_terminals_server_id_path_head**](TerminalsApi.md#proxy_terminal_api_v1_terminals_server_id_path_head) | **GET** /api/v1/terminals/{server_id}/{path} | Proxy Terminal
[**proxy_terminal_api_v1_terminals_server_id_path_head_delete7e13da56da**](TerminalsApi.md#proxy_terminal_api_v1_terminals_server_id_path_head_delete7e13da56da) | **DELETE** /api/v1/terminals/{server_id}/{path} | Proxy Terminal
[**proxy_terminal_api_v1_terminals_server_id_path_head_head1bff31aa5f**](TerminalsApi.md#proxy_terminal_api_v1_terminals_server_id_path_head_head1bff31aa5f) | **HEAD** /api/v1/terminals/{server_id}/{path} | Proxy Terminal
[**proxy_terminal_api_v1_terminals_server_id_path_head_options309800e44a**](TerminalsApi.md#proxy_terminal_api_v1_terminals_server_id_path_head_options309800e44a) | **OPTIONS** /api/v1/terminals/{server_id}/{path} | Proxy Terminal
[**proxy_terminal_api_v1_terminals_server_id_path_head_patch51a79d73f9**](TerminalsApi.md#proxy_terminal_api_v1_terminals_server_id_path_head_patch51a79d73f9) | **PATCH** /api/v1/terminals/{server_id}/{path} | Proxy Terminal
[**proxy_terminal_api_v1_terminals_server_id_path_head_post9b7b34e967**](TerminalsApi.md#proxy_terminal_api_v1_terminals_server_id_path_head_post9b7b34e967) | **POST** /api/v1/terminals/{server_id}/{path} | Proxy Terminal
[**proxy_terminal_api_v1_terminals_server_id_path_head_put51587aa4cd**](TerminalsApi.md#proxy_terminal_api_v1_terminals_server_id_path_head_put51587aa4cd) | **PUT** /api/v1/terminals/{server_id}/{path} | Proxy Terminal


# **list_terminal_servers_api_v1_terminals_get**
> object list_terminal_servers_api_v1_terminals_get()

List Terminal Servers

Return terminal servers the authenticated user has access to.

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
    api_instance = openwebui_client.TerminalsApi(api_client)

    try:
        # List Terminal Servers
        api_response = await api_instance.list_terminal_servers_api_v1_terminals_get()
        print("The response of TerminalsApi->list_terminal_servers_api_v1_terminals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalsApi->list_terminal_servers_api_v1_terminals_get: %s\n" % e)
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

# **proxy_terminal_api_v1_terminals_server_id_path_head**
> object proxy_terminal_api_v1_terminals_server_id_path_head(server_id, path)

Proxy Terminal

Proxy a request to the admin terminal server identified by *server_id*.

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
    api_instance = openwebui_client.TerminalsApi(api_client)
    server_id = 'server_id_example' # str | 
    path = 'path_example' # str | 

    try:
        # Proxy Terminal
        api_response = await api_instance.proxy_terminal_api_v1_terminals_server_id_path_head(server_id, path)
        print("The response of TerminalsApi->proxy_terminal_api_v1_terminals_server_id_path_head:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalsApi->proxy_terminal_api_v1_terminals_server_id_path_head: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **path** | **str**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_terminal_api_v1_terminals_server_id_path_head_delete7e13da56da**
> object proxy_terminal_api_v1_terminals_server_id_path_head_delete7e13da56da(server_id, path)

Proxy Terminal

Proxy a request to the admin terminal server identified by *server_id*.

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
    api_instance = openwebui_client.TerminalsApi(api_client)
    server_id = 'server_id_example' # str | 
    path = 'path_example' # str | 

    try:
        # Proxy Terminal
        api_response = await api_instance.proxy_terminal_api_v1_terminals_server_id_path_head_delete7e13da56da(server_id, path)
        print("The response of TerminalsApi->proxy_terminal_api_v1_terminals_server_id_path_head_delete7e13da56da:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalsApi->proxy_terminal_api_v1_terminals_server_id_path_head_delete7e13da56da: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **path** | **str**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_terminal_api_v1_terminals_server_id_path_head_head1bff31aa5f**
> object proxy_terminal_api_v1_terminals_server_id_path_head_head1bff31aa5f(server_id, path)

Proxy Terminal

Proxy a request to the admin terminal server identified by *server_id*.

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
    api_instance = openwebui_client.TerminalsApi(api_client)
    server_id = 'server_id_example' # str | 
    path = 'path_example' # str | 

    try:
        # Proxy Terminal
        api_response = await api_instance.proxy_terminal_api_v1_terminals_server_id_path_head_head1bff31aa5f(server_id, path)
        print("The response of TerminalsApi->proxy_terminal_api_v1_terminals_server_id_path_head_head1bff31aa5f:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalsApi->proxy_terminal_api_v1_terminals_server_id_path_head_head1bff31aa5f: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **path** | **str**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_terminal_api_v1_terminals_server_id_path_head_options309800e44a**
> object proxy_terminal_api_v1_terminals_server_id_path_head_options309800e44a(server_id, path)

Proxy Terminal

Proxy a request to the admin terminal server identified by *server_id*.

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
    api_instance = openwebui_client.TerminalsApi(api_client)
    server_id = 'server_id_example' # str | 
    path = 'path_example' # str | 

    try:
        # Proxy Terminal
        api_response = await api_instance.proxy_terminal_api_v1_terminals_server_id_path_head_options309800e44a(server_id, path)
        print("The response of TerminalsApi->proxy_terminal_api_v1_terminals_server_id_path_head_options309800e44a:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalsApi->proxy_terminal_api_v1_terminals_server_id_path_head_options309800e44a: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **path** | **str**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_terminal_api_v1_terminals_server_id_path_head_patch51a79d73f9**
> object proxy_terminal_api_v1_terminals_server_id_path_head_patch51a79d73f9(server_id, path)

Proxy Terminal

Proxy a request to the admin terminal server identified by *server_id*.

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
    api_instance = openwebui_client.TerminalsApi(api_client)
    server_id = 'server_id_example' # str | 
    path = 'path_example' # str | 

    try:
        # Proxy Terminal
        api_response = await api_instance.proxy_terminal_api_v1_terminals_server_id_path_head_patch51a79d73f9(server_id, path)
        print("The response of TerminalsApi->proxy_terminal_api_v1_terminals_server_id_path_head_patch51a79d73f9:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalsApi->proxy_terminal_api_v1_terminals_server_id_path_head_patch51a79d73f9: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **path** | **str**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_terminal_api_v1_terminals_server_id_path_head_post9b7b34e967**
> object proxy_terminal_api_v1_terminals_server_id_path_head_post9b7b34e967(server_id, path)

Proxy Terminal

Proxy a request to the admin terminal server identified by *server_id*.

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
    api_instance = openwebui_client.TerminalsApi(api_client)
    server_id = 'server_id_example' # str | 
    path = 'path_example' # str | 

    try:
        # Proxy Terminal
        api_response = await api_instance.proxy_terminal_api_v1_terminals_server_id_path_head_post9b7b34e967(server_id, path)
        print("The response of TerminalsApi->proxy_terminal_api_v1_terminals_server_id_path_head_post9b7b34e967:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalsApi->proxy_terminal_api_v1_terminals_server_id_path_head_post9b7b34e967: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **path** | **str**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy_terminal_api_v1_terminals_server_id_path_head_put51587aa4cd**
> object proxy_terminal_api_v1_terminals_server_id_path_head_put51587aa4cd(server_id, path)

Proxy Terminal

Proxy a request to the admin terminal server identified by *server_id*.

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
    api_instance = openwebui_client.TerminalsApi(api_client)
    server_id = 'server_id_example' # str | 
    path = 'path_example' # str | 

    try:
        # Proxy Terminal
        api_response = await api_instance.proxy_terminal_api_v1_terminals_server_id_path_head_put51587aa4cd(server_id, path)
        print("The response of TerminalsApi->proxy_terminal_api_v1_terminals_server_id_path_head_put51587aa4cd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalsApi->proxy_terminal_api_v1_terminals_server_id_path_head_put51587aa4cd: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 
 **path** | **str**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

