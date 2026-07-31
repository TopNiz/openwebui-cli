# openwebui_client.FunctionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_function_api_v1_functions_create_post**](FunctionsApi.md#create_new_function_api_v1_functions_create_post) | **POST** /api/v1/functions/create | Create New Function
[**delete_function_by_id_api_v1_functions_id_id_delete_delete**](FunctionsApi.md#delete_function_by_id_api_v1_functions_id_id_delete_delete) | **DELETE** /api/v1/functions/id/{id}/delete | Delete Function By Id
[**get_function_by_id_api_v1_functions_id_id_get**](FunctionsApi.md#get_function_by_id_api_v1_functions_id_id_get) | **GET** /api/v1/functions/id/{id} | Get Function By Id
[**get_function_list_api_v1_functions_list_get**](FunctionsApi.md#get_function_list_api_v1_functions_list_get) | **GET** /api/v1/functions/list | Get Function List
[**get_function_user_valves_by_id_api_v1_functions_id_id_valves_user_get**](FunctionsApi.md#get_function_user_valves_by_id_api_v1_functions_id_id_valves_user_get) | **GET** /api/v1/functions/id/{id}/valves/user | Get Function User Valves By Id
[**get_function_user_valves_spec_by_id_api_v1_functions_id_id_valves_user_spec_get**](FunctionsApi.md#get_function_user_valves_spec_by_id_api_v1_functions_id_id_valves_user_spec_get) | **GET** /api/v1/functions/id/{id}/valves/user/spec | Get Function User Valves Spec By Id
[**get_function_valves_by_id_api_v1_functions_id_id_valves_get**](FunctionsApi.md#get_function_valves_by_id_api_v1_functions_id_id_valves_get) | **GET** /api/v1/functions/id/{id}/valves | Get Function Valves By Id
[**get_function_valves_spec_by_id_api_v1_functions_id_id_valves_spec_get**](FunctionsApi.md#get_function_valves_spec_by_id_api_v1_functions_id_id_valves_spec_get) | **GET** /api/v1/functions/id/{id}/valves/spec | Get Function Valves Spec By Id
[**get_functions_api_v1_functions_export_get**](FunctionsApi.md#get_functions_api_v1_functions_export_get) | **GET** /api/v1/functions/export | Get Functions
[**get_functions_api_v1_functions_get**](FunctionsApi.md#get_functions_api_v1_functions_get) | **GET** /api/v1/functions/ | Get Functions
[**load_function_from_url_api_v1_functions_load_url_post**](FunctionsApi.md#load_function_from_url_api_v1_functions_load_url_post) | **POST** /api/v1/functions/load/url | Load Function From Url
[**sync_functions_api_v1_functions_sync_post**](FunctionsApi.md#sync_functions_api_v1_functions_sync_post) | **POST** /api/v1/functions/sync | Sync Functions
[**toggle_function_by_id_api_v1_functions_id_id_toggle_post**](FunctionsApi.md#toggle_function_by_id_api_v1_functions_id_id_toggle_post) | **POST** /api/v1/functions/id/{id}/toggle | Toggle Function By Id
[**toggle_global_by_id_api_v1_functions_id_id_toggle_global_post**](FunctionsApi.md#toggle_global_by_id_api_v1_functions_id_id_toggle_global_post) | **POST** /api/v1/functions/id/{id}/toggle/global | Toggle Global By Id
[**update_function_by_id_api_v1_functions_id_id_update_post**](FunctionsApi.md#update_function_by_id_api_v1_functions_id_id_update_post) | **POST** /api/v1/functions/id/{id}/update | Update Function By Id
[**update_function_user_valves_by_id_api_v1_functions_id_id_valves_user_update_post**](FunctionsApi.md#update_function_user_valves_by_id_api_v1_functions_id_id_valves_user_update_post) | **POST** /api/v1/functions/id/{id}/valves/user/update | Update Function User Valves By Id
[**update_function_valves_by_id_api_v1_functions_id_id_valves_update_post**](FunctionsApi.md#update_function_valves_by_id_api_v1_functions_id_id_valves_update_post) | **POST** /api/v1/functions/id/{id}/valves/update | Update Function Valves By Id


# **create_new_function_api_v1_functions_create_post**
> FunctionResponse create_new_function_api_v1_functions_create_post(function_form)

Create New Function

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.function_form import FunctionForm
from openwebui_client.models.function_response import FunctionResponse
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
    api_instance = openwebui_client.FunctionsApi(api_client)
    function_form = openwebui_client.FunctionForm() # FunctionForm | 

    try:
        # Create New Function
        api_response = await api_instance.create_new_function_api_v1_functions_create_post(function_form)
        print("The response of FunctionsApi->create_new_function_api_v1_functions_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->create_new_function_api_v1_functions_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_form** | [**FunctionForm**](FunctionForm.md)|  | 

### Return type

[**FunctionResponse**](FunctionResponse.md)

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

# **delete_function_by_id_api_v1_functions_id_id_delete_delete**
> bool delete_function_by_id_api_v1_functions_id_id_delete_delete(id)

Delete Function By Id

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
    api_instance = openwebui_client.FunctionsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Function By Id
        api_response = await api_instance.delete_function_by_id_api_v1_functions_id_id_delete_delete(id)
        print("The response of FunctionsApi->delete_function_by_id_api_v1_functions_id_id_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->delete_function_by_id_api_v1_functions_id_id_delete_delete: %s\n" % e)
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

# **get_function_by_id_api_v1_functions_id_id_get**
> FunctionModel get_function_by_id_api_v1_functions_id_id_get(id)

Get Function By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.function_model import FunctionModel
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
    api_instance = openwebui_client.FunctionsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Function By Id
        api_response = await api_instance.get_function_by_id_api_v1_functions_id_id_get(id)
        print("The response of FunctionsApi->get_function_by_id_api_v1_functions_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->get_function_by_id_api_v1_functions_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FunctionModel**](FunctionModel.md)

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

# **get_function_list_api_v1_functions_list_get**
> List[FunctionUserResponse] get_function_list_api_v1_functions_list_get()

Get Function List

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.function_user_response import FunctionUserResponse
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
    api_instance = openwebui_client.FunctionsApi(api_client)

    try:
        # Get Function List
        api_response = await api_instance.get_function_list_api_v1_functions_list_get()
        print("The response of FunctionsApi->get_function_list_api_v1_functions_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->get_function_list_api_v1_functions_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FunctionUserResponse]**](FunctionUserResponse.md)

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

# **get_function_user_valves_by_id_api_v1_functions_id_id_valves_user_get**
> Dict[str, object] get_function_user_valves_by_id_api_v1_functions_id_id_valves_user_get(id)

Get Function User Valves By Id

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
    api_instance = openwebui_client.FunctionsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Function User Valves By Id
        api_response = await api_instance.get_function_user_valves_by_id_api_v1_functions_id_id_valves_user_get(id)
        print("The response of FunctionsApi->get_function_user_valves_by_id_api_v1_functions_id_id_valves_user_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->get_function_user_valves_by_id_api_v1_functions_id_id_valves_user_get: %s\n" % e)
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

# **get_function_user_valves_spec_by_id_api_v1_functions_id_id_valves_user_spec_get**
> Dict[str, object] get_function_user_valves_spec_by_id_api_v1_functions_id_id_valves_user_spec_get(id)

Get Function User Valves Spec By Id

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
    api_instance = openwebui_client.FunctionsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Function User Valves Spec By Id
        api_response = await api_instance.get_function_user_valves_spec_by_id_api_v1_functions_id_id_valves_user_spec_get(id)
        print("The response of FunctionsApi->get_function_user_valves_spec_by_id_api_v1_functions_id_id_valves_user_spec_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->get_function_user_valves_spec_by_id_api_v1_functions_id_id_valves_user_spec_get: %s\n" % e)
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

# **get_function_valves_by_id_api_v1_functions_id_id_valves_get**
> Dict[str, object] get_function_valves_by_id_api_v1_functions_id_id_valves_get(id)

Get Function Valves By Id

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
    api_instance = openwebui_client.FunctionsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Function Valves By Id
        api_response = await api_instance.get_function_valves_by_id_api_v1_functions_id_id_valves_get(id)
        print("The response of FunctionsApi->get_function_valves_by_id_api_v1_functions_id_id_valves_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->get_function_valves_by_id_api_v1_functions_id_id_valves_get: %s\n" % e)
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

# **get_function_valves_spec_by_id_api_v1_functions_id_id_valves_spec_get**
> Dict[str, object] get_function_valves_spec_by_id_api_v1_functions_id_id_valves_spec_get(id)

Get Function Valves Spec By Id

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
    api_instance = openwebui_client.FunctionsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Function Valves Spec By Id
        api_response = await api_instance.get_function_valves_spec_by_id_api_v1_functions_id_id_valves_spec_get(id)
        print("The response of FunctionsApi->get_function_valves_spec_by_id_api_v1_functions_id_id_valves_spec_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->get_function_valves_spec_by_id_api_v1_functions_id_id_valves_spec_get: %s\n" % e)
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

# **get_functions_api_v1_functions_export_get**
> List[ResponseGetFunctionsApiV1FunctionsExportGetInner] get_functions_api_v1_functions_export_get(include_valves=include_valves)

Get Functions

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.response_get_functions_api_v1_functions_export_get_inner import ResponseGetFunctionsApiV1FunctionsExportGetInner
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
    api_instance = openwebui_client.FunctionsApi(api_client)
    include_valves = False # bool |  (optional) (default to False)

    try:
        # Get Functions
        api_response = await api_instance.get_functions_api_v1_functions_export_get(include_valves=include_valves)
        print("The response of FunctionsApi->get_functions_api_v1_functions_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->get_functions_api_v1_functions_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_valves** | **bool**|  | [optional] [default to False]

### Return type

[**List[ResponseGetFunctionsApiV1FunctionsExportGetInner]**](ResponseGetFunctionsApiV1FunctionsExportGetInner.md)

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

# **get_functions_api_v1_functions_get**
> List[FunctionResponse] get_functions_api_v1_functions_get()

Get Functions

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.function_response import FunctionResponse
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
    api_instance = openwebui_client.FunctionsApi(api_client)

    try:
        # Get Functions
        api_response = await api_instance.get_functions_api_v1_functions_get()
        print("The response of FunctionsApi->get_functions_api_v1_functions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->get_functions_api_v1_functions_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FunctionResponse]**](FunctionResponse.md)

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

# **load_function_from_url_api_v1_functions_load_url_post**
> Dict[str, object] load_function_from_url_api_v1_functions_load_url_post(load_url_form)

Load Function From Url

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
    api_instance = openwebui_client.FunctionsApi(api_client)
    load_url_form = openwebui_client.LoadUrlForm() # LoadUrlForm | 

    try:
        # Load Function From Url
        api_response = await api_instance.load_function_from_url_api_v1_functions_load_url_post(load_url_form)
        print("The response of FunctionsApi->load_function_from_url_api_v1_functions_load_url_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->load_function_from_url_api_v1_functions_load_url_post: %s\n" % e)
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

# **sync_functions_api_v1_functions_sync_post**
> List[FunctionWithValvesModel] sync_functions_api_v1_functions_sync_post(sync_functions_form)

Sync Functions

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.function_with_valves_model import FunctionWithValvesModel
from openwebui_client.models.sync_functions_form import SyncFunctionsForm
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
    api_instance = openwebui_client.FunctionsApi(api_client)
    sync_functions_form = openwebui_client.SyncFunctionsForm() # SyncFunctionsForm | 

    try:
        # Sync Functions
        api_response = await api_instance.sync_functions_api_v1_functions_sync_post(sync_functions_form)
        print("The response of FunctionsApi->sync_functions_api_v1_functions_sync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->sync_functions_api_v1_functions_sync_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_functions_form** | [**SyncFunctionsForm**](SyncFunctionsForm.md)|  | 

### Return type

[**List[FunctionWithValvesModel]**](FunctionWithValvesModel.md)

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

# **toggle_function_by_id_api_v1_functions_id_id_toggle_post**
> FunctionModel toggle_function_by_id_api_v1_functions_id_id_toggle_post(id)

Toggle Function By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.function_model import FunctionModel
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
    api_instance = openwebui_client.FunctionsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Toggle Function By Id
        api_response = await api_instance.toggle_function_by_id_api_v1_functions_id_id_toggle_post(id)
        print("The response of FunctionsApi->toggle_function_by_id_api_v1_functions_id_id_toggle_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->toggle_function_by_id_api_v1_functions_id_id_toggle_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FunctionModel**](FunctionModel.md)

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

# **toggle_global_by_id_api_v1_functions_id_id_toggle_global_post**
> FunctionModel toggle_global_by_id_api_v1_functions_id_id_toggle_global_post(id)

Toggle Global By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.function_model import FunctionModel
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
    api_instance = openwebui_client.FunctionsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Toggle Global By Id
        api_response = await api_instance.toggle_global_by_id_api_v1_functions_id_id_toggle_global_post(id)
        print("The response of FunctionsApi->toggle_global_by_id_api_v1_functions_id_id_toggle_global_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->toggle_global_by_id_api_v1_functions_id_id_toggle_global_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FunctionModel**](FunctionModel.md)

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

# **update_function_by_id_api_v1_functions_id_id_update_post**
> FunctionModel update_function_by_id_api_v1_functions_id_id_update_post(id, function_form)

Update Function By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.function_form import FunctionForm
from openwebui_client.models.function_model import FunctionModel
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
    api_instance = openwebui_client.FunctionsApi(api_client)
    id = 'id_example' # str | 
    function_form = openwebui_client.FunctionForm() # FunctionForm | 

    try:
        # Update Function By Id
        api_response = await api_instance.update_function_by_id_api_v1_functions_id_id_update_post(id, function_form)
        print("The response of FunctionsApi->update_function_by_id_api_v1_functions_id_id_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->update_function_by_id_api_v1_functions_id_id_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **function_form** | [**FunctionForm**](FunctionForm.md)|  | 

### Return type

[**FunctionModel**](FunctionModel.md)

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

# **update_function_user_valves_by_id_api_v1_functions_id_id_valves_user_update_post**
> Dict[str, object] update_function_user_valves_by_id_api_v1_functions_id_id_valves_user_update_post(id, request_body)

Update Function User Valves By Id

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
    api_instance = openwebui_client.FunctionsApi(api_client)
    id = 'id_example' # str | 
    request_body = None # Dict[str, object] | 

    try:
        # Update Function User Valves By Id
        api_response = await api_instance.update_function_user_valves_by_id_api_v1_functions_id_id_valves_user_update_post(id, request_body)
        print("The response of FunctionsApi->update_function_user_valves_by_id_api_v1_functions_id_id_valves_user_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->update_function_user_valves_by_id_api_v1_functions_id_id_valves_user_update_post: %s\n" % e)
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

# **update_function_valves_by_id_api_v1_functions_id_id_valves_update_post**
> Dict[str, object] update_function_valves_by_id_api_v1_functions_id_id_valves_update_post(id, request_body)

Update Function Valves By Id

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
    api_instance = openwebui_client.FunctionsApi(api_client)
    id = 'id_example' # str | 
    request_body = None # Dict[str, object] | 

    try:
        # Update Function Valves By Id
        api_response = await api_instance.update_function_valves_by_id_api_v1_functions_id_id_valves_update_post(id, request_body)
        print("The response of FunctionsApi->update_function_valves_by_id_api_v1_functions_id_id_valves_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->update_function_valves_by_id_api_v1_functions_id_id_valves_update_post: %s\n" % e)
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

