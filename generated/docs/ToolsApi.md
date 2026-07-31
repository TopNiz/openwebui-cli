# openwebui_client.ToolsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_tools_api_v1_tools_create_post**](ToolsApi.md#create_new_tools_api_v1_tools_create_post) | **POST** /api/v1/tools/create | Create New Tools
[**delete_tools_by_id_api_v1_tools_id_id_delete_delete**](ToolsApi.md#delete_tools_by_id_api_v1_tools_id_id_delete_delete) | **DELETE** /api/v1/tools/id/{id}/delete | Delete Tools By Id
[**export_tools_api_v1_tools_export_get**](ToolsApi.md#export_tools_api_v1_tools_export_get) | **GET** /api/v1/tools/export | Export Tools
[**get_tool_list_api_v1_tools_list_get**](ToolsApi.md#get_tool_list_api_v1_tools_list_get) | **GET** /api/v1/tools/list | Get Tool List
[**get_tools_api_v1_tools_get**](ToolsApi.md#get_tools_api_v1_tools_get) | **GET** /api/v1/tools/ | Get Tools
[**get_tools_by_id_api_v1_tools_id_id_get**](ToolsApi.md#get_tools_by_id_api_v1_tools_id_id_get) | **GET** /api/v1/tools/id/{id} | Get Tools By Id
[**get_tools_user_valves_by_id_api_v1_tools_id_id_valves_user_get**](ToolsApi.md#get_tools_user_valves_by_id_api_v1_tools_id_id_valves_user_get) | **GET** /api/v1/tools/id/{id}/valves/user | Get Tools User Valves By Id
[**get_tools_user_valves_spec_by_id_api_v1_tools_id_id_valves_user_spec_get**](ToolsApi.md#get_tools_user_valves_spec_by_id_api_v1_tools_id_id_valves_user_spec_get) | **GET** /api/v1/tools/id/{id}/valves/user/spec | Get Tools User Valves Spec By Id
[**get_tools_valves_by_id_api_v1_tools_id_id_valves_get**](ToolsApi.md#get_tools_valves_by_id_api_v1_tools_id_id_valves_get) | **GET** /api/v1/tools/id/{id}/valves | Get Tools Valves By Id
[**get_tools_valves_spec_by_id_api_v1_tools_id_id_valves_spec_get**](ToolsApi.md#get_tools_valves_spec_by_id_api_v1_tools_id_id_valves_spec_get) | **GET** /api/v1/tools/id/{id}/valves/spec | Get Tools Valves Spec By Id
[**load_tool_from_url_api_v1_tools_load_url_post**](ToolsApi.md#load_tool_from_url_api_v1_tools_load_url_post) | **POST** /api/v1/tools/load/url | Load Tool From Url
[**update_tool_access_by_id_api_v1_tools_id_id_access_update_post**](ToolsApi.md#update_tool_access_by_id_api_v1_tools_id_id_access_update_post) | **POST** /api/v1/tools/id/{id}/access/update | Update Tool Access By Id
[**update_tools_by_id_api_v1_tools_id_id_update_post**](ToolsApi.md#update_tools_by_id_api_v1_tools_id_id_update_post) | **POST** /api/v1/tools/id/{id}/update | Update Tools By Id
[**update_tools_user_valves_by_id_api_v1_tools_id_id_valves_user_update_post**](ToolsApi.md#update_tools_user_valves_by_id_api_v1_tools_id_id_valves_user_update_post) | **POST** /api/v1/tools/id/{id}/valves/user/update | Update Tools User Valves By Id
[**update_tools_valves_by_id_api_v1_tools_id_id_valves_update_post**](ToolsApi.md#update_tools_valves_by_id_api_v1_tools_id_id_valves_update_post) | **POST** /api/v1/tools/id/{id}/valves/update | Update Tools Valves By Id


# **create_new_tools_api_v1_tools_create_post**
> ToolResponse create_new_tools_api_v1_tools_create_post(tool_form)

Create New Tools

Create a new tool from user-supplied Python source code.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.tool_form import ToolForm
from openwebui_client.models.tool_response import ToolResponse
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
    api_instance = openwebui_client.ToolsApi(api_client)
    tool_form = openwebui_client.ToolForm() # ToolForm | 

    try:
        # Create New Tools
        api_response = await api_instance.create_new_tools_api_v1_tools_create_post(tool_form)
        print("The response of ToolsApi->create_new_tools_api_v1_tools_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->create_new_tools_api_v1_tools_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_form** | [**ToolForm**](ToolForm.md)|  | 

### Return type

[**ToolResponse**](ToolResponse.md)

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

# **delete_tools_by_id_api_v1_tools_id_id_delete_delete**
> bool delete_tools_by_id_api_v1_tools_id_id_delete_delete(id)

Delete Tools By Id

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
    api_instance = openwebui_client.ToolsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Tools By Id
        api_response = await api_instance.delete_tools_by_id_api_v1_tools_id_id_delete_delete(id)
        print("The response of ToolsApi->delete_tools_by_id_api_v1_tools_id_id_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->delete_tools_by_id_api_v1_tools_id_id_delete_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **export_tools_api_v1_tools_export_get**
> List[ToolModel] export_tools_api_v1_tools_export_get()

Export Tools

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.tool_model import ToolModel
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
    api_instance = openwebui_client.ToolsApi(api_client)

    try:
        # Export Tools
        api_response = await api_instance.export_tools_api_v1_tools_export_get()
        print("The response of ToolsApi->export_tools_api_v1_tools_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->export_tools_api_v1_tools_export_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ToolModel]**](ToolModel.md)

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

# **get_tool_list_api_v1_tools_list_get**
> List[ToolAccessResponse] get_tool_list_api_v1_tools_list_get()

Get Tool List

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.tool_access_response import ToolAccessResponse
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
    api_instance = openwebui_client.ToolsApi(api_client)

    try:
        # Get Tool List
        api_response = await api_instance.get_tool_list_api_v1_tools_list_get()
        print("The response of ToolsApi->get_tool_list_api_v1_tools_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->get_tool_list_api_v1_tools_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ToolAccessResponse]**](ToolAccessResponse.md)

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

# **get_tools_api_v1_tools_get**
> List[ToolUserResponse] get_tools_api_v1_tools_get()

Get Tools

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.tool_user_response import ToolUserResponse
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
    api_instance = openwebui_client.ToolsApi(api_client)

    try:
        # Get Tools
        api_response = await api_instance.get_tools_api_v1_tools_get()
        print("The response of ToolsApi->get_tools_api_v1_tools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->get_tools_api_v1_tools_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ToolUserResponse]**](ToolUserResponse.md)

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

# **get_tools_by_id_api_v1_tools_id_id_get**
> ToolAccessResponse get_tools_by_id_api_v1_tools_id_id_get(id)

Get Tools By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.tool_access_response import ToolAccessResponse
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
    api_instance = openwebui_client.ToolsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Tools By Id
        api_response = await api_instance.get_tools_by_id_api_v1_tools_id_id_get(id)
        print("The response of ToolsApi->get_tools_by_id_api_v1_tools_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->get_tools_by_id_api_v1_tools_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ToolAccessResponse**](ToolAccessResponse.md)

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

# **get_tools_user_valves_by_id_api_v1_tools_id_id_valves_user_get**
> Dict[str, object] get_tools_user_valves_by_id_api_v1_tools_id_id_valves_user_get(id)

Get Tools User Valves By Id

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
    api_instance = openwebui_client.ToolsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Tools User Valves By Id
        api_response = await api_instance.get_tools_user_valves_by_id_api_v1_tools_id_id_valves_user_get(id)
        print("The response of ToolsApi->get_tools_user_valves_by_id_api_v1_tools_id_id_valves_user_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->get_tools_user_valves_by_id_api_v1_tools_id_id_valves_user_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **get_tools_user_valves_spec_by_id_api_v1_tools_id_id_valves_user_spec_get**
> Dict[str, object] get_tools_user_valves_spec_by_id_api_v1_tools_id_id_valves_user_spec_get(id)

Get Tools User Valves Spec By Id

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
    api_instance = openwebui_client.ToolsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Tools User Valves Spec By Id
        api_response = await api_instance.get_tools_user_valves_spec_by_id_api_v1_tools_id_id_valves_user_spec_get(id)
        print("The response of ToolsApi->get_tools_user_valves_spec_by_id_api_v1_tools_id_id_valves_user_spec_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->get_tools_user_valves_spec_by_id_api_v1_tools_id_id_valves_user_spec_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **get_tools_valves_by_id_api_v1_tools_id_id_valves_get**
> Dict[str, object] get_tools_valves_by_id_api_v1_tools_id_id_valves_get(id)

Get Tools Valves By Id

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
    api_instance = openwebui_client.ToolsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Tools Valves By Id
        api_response = await api_instance.get_tools_valves_by_id_api_v1_tools_id_id_valves_get(id)
        print("The response of ToolsApi->get_tools_valves_by_id_api_v1_tools_id_id_valves_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->get_tools_valves_by_id_api_v1_tools_id_id_valves_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **get_tools_valves_spec_by_id_api_v1_tools_id_id_valves_spec_get**
> Dict[str, object] get_tools_valves_spec_by_id_api_v1_tools_id_id_valves_spec_get(id)

Get Tools Valves Spec By Id

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
    api_instance = openwebui_client.ToolsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Tools Valves Spec By Id
        api_response = await api_instance.get_tools_valves_spec_by_id_api_v1_tools_id_id_valves_spec_get(id)
        print("The response of ToolsApi->get_tools_valves_spec_by_id_api_v1_tools_id_id_valves_spec_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->get_tools_valves_spec_by_id_api_v1_tools_id_id_valves_spec_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **load_tool_from_url_api_v1_tools_load_url_post**
> Dict[str, object] load_tool_from_url_api_v1_tools_load_url_post(load_url_form)

Load Tool From Url

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.load_url_form import LoadUrlForm
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
    api_instance = openwebui_client.ToolsApi(api_client)
    load_url_form = openwebui_client.LoadUrlForm() # LoadUrlForm | 

    try:
        # Load Tool From Url
        api_response = await api_instance.load_tool_from_url_api_v1_tools_load_url_post(load_url_form)
        print("The response of ToolsApi->load_tool_from_url_api_v1_tools_load_url_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->load_tool_from_url_api_v1_tools_load_url_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **load_url_form** | [**LoadUrlForm**](LoadUrlForm.md)|  | 

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

# **update_tool_access_by_id_api_v1_tools_id_id_access_update_post**
> ToolModel update_tool_access_by_id_api_v1_tools_id_id_access_update_post(id, tool_access_grants_form)

Update Tool Access By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.tool_access_grants_form import ToolAccessGrantsForm
from openwebui_client.models.tool_model import ToolModel
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
    api_instance = openwebui_client.ToolsApi(api_client)
    id = 'id_example' # str | 
    tool_access_grants_form = openwebui_client.ToolAccessGrantsForm() # ToolAccessGrantsForm | 

    try:
        # Update Tool Access By Id
        api_response = await api_instance.update_tool_access_by_id_api_v1_tools_id_id_access_update_post(id, tool_access_grants_form)
        print("The response of ToolsApi->update_tool_access_by_id_api_v1_tools_id_id_access_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->update_tool_access_by_id_api_v1_tools_id_id_access_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tool_access_grants_form** | [**ToolAccessGrantsForm**](ToolAccessGrantsForm.md)|  | 

### Return type

[**ToolModel**](ToolModel.md)

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

# **update_tools_by_id_api_v1_tools_id_id_update_post**
> ToolModel update_tools_by_id_api_v1_tools_id_id_update_post(id, tool_form)

Update Tools By Id

Update an existing tool's source code and metadata.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.tool_form import ToolForm
from openwebui_client.models.tool_model import ToolModel
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
    api_instance = openwebui_client.ToolsApi(api_client)
    id = 'id_example' # str | 
    tool_form = openwebui_client.ToolForm() # ToolForm | 

    try:
        # Update Tools By Id
        api_response = await api_instance.update_tools_by_id_api_v1_tools_id_id_update_post(id, tool_form)
        print("The response of ToolsApi->update_tools_by_id_api_v1_tools_id_id_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->update_tools_by_id_api_v1_tools_id_id_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tool_form** | [**ToolForm**](ToolForm.md)|  | 

### Return type

[**ToolModel**](ToolModel.md)

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

# **update_tools_user_valves_by_id_api_v1_tools_id_id_valves_user_update_post**
> Dict[str, object] update_tools_user_valves_by_id_api_v1_tools_id_id_valves_user_update_post(id, request_body)

Update Tools User Valves By Id

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
    api_instance = openwebui_client.ToolsApi(api_client)
    id = 'id_example' # str | 
    request_body = None # Dict[str, object] | 

    try:
        # Update Tools User Valves By Id
        api_response = await api_instance.update_tools_user_valves_by_id_api_v1_tools_id_id_valves_user_update_post(id, request_body)
        print("The response of ToolsApi->update_tools_user_valves_by_id_api_v1_tools_id_id_valves_user_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->update_tools_user_valves_by_id_api_v1_tools_id_id_valves_user_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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

# **update_tools_valves_by_id_api_v1_tools_id_id_valves_update_post**
> Dict[str, object] update_tools_valves_by_id_api_v1_tools_id_id_valves_update_post(id, request_body)

Update Tools Valves By Id

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
    api_instance = openwebui_client.ToolsApi(api_client)
    id = 'id_example' # str | 
    request_body = None # Dict[str, object] | 

    try:
        # Update Tools Valves By Id
        api_response = await api_instance.update_tools_valves_by_id_api_v1_tools_id_id_valves_update_post(id, request_body)
        print("The response of ToolsApi->update_tools_valves_by_id_api_v1_tools_id_id_valves_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->update_tools_valves_by_id_api_v1_tools_id_id_valves_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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

