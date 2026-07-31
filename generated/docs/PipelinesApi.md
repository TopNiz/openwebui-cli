# openwebui_client.PipelinesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_pipeline_api_v1_pipelines_add_post**](PipelinesApi.md#add_pipeline_api_v1_pipelines_add_post) | **POST** /api/v1/pipelines/add | Add Pipeline
[**delete_pipeline_api_v1_pipelines_delete_delete**](PipelinesApi.md#delete_pipeline_api_v1_pipelines_delete_delete) | **DELETE** /api/v1/pipelines/delete | Delete Pipeline
[**get_pipeline_valves_api_v1_pipelines_pipeline_id_valves_get**](PipelinesApi.md#get_pipeline_valves_api_v1_pipelines_pipeline_id_valves_get) | **GET** /api/v1/pipelines/{pipeline_id}/valves | Get Pipeline Valves
[**get_pipeline_valves_spec_api_v1_pipelines_pipeline_id_valves_spec_get**](PipelinesApi.md#get_pipeline_valves_spec_api_v1_pipelines_pipeline_id_valves_spec_get) | **GET** /api/v1/pipelines/{pipeline_id}/valves/spec | Get Pipeline Valves Spec
[**get_pipelines_api_v1_pipelines_get**](PipelinesApi.md#get_pipelines_api_v1_pipelines_get) | **GET** /api/v1/pipelines/ | Get Pipelines
[**get_pipelines_list_api_v1_pipelines_list_get**](PipelinesApi.md#get_pipelines_list_api_v1_pipelines_list_get) | **GET** /api/v1/pipelines/list | Get Pipelines List
[**update_pipeline_valves_api_v1_pipelines_pipeline_id_valves_update_post**](PipelinesApi.md#update_pipeline_valves_api_v1_pipelines_pipeline_id_valves_update_post) | **POST** /api/v1/pipelines/{pipeline_id}/valves/update | Update Pipeline Valves
[**upload_pipeline_api_v1_pipelines_upload_post**](PipelinesApi.md#upload_pipeline_api_v1_pipelines_upload_post) | **POST** /api/v1/pipelines/upload | Upload Pipeline


# **add_pipeline_api_v1_pipelines_add_post**
> object add_pipeline_api_v1_pipelines_add_post(add_pipeline_form)

Add Pipeline

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.add_pipeline_form import AddPipelineForm
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
    api_instance = openwebui_client.PipelinesApi(api_client)
    add_pipeline_form = openwebui_client.AddPipelineForm() # AddPipelineForm | 

    try:
        # Add Pipeline
        api_response = await api_instance.add_pipeline_api_v1_pipelines_add_post(add_pipeline_form)
        print("The response of PipelinesApi->add_pipeline_api_v1_pipelines_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->add_pipeline_api_v1_pipelines_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_pipeline_form** | [**AddPipelineForm**](AddPipelineForm.md)|  | 

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

# **delete_pipeline_api_v1_pipelines_delete_delete**
> object delete_pipeline_api_v1_pipelines_delete_delete(delete_pipeline_form)

Delete Pipeline

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.delete_pipeline_form import DeletePipelineForm
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
    api_instance = openwebui_client.PipelinesApi(api_client)
    delete_pipeline_form = openwebui_client.DeletePipelineForm() # DeletePipelineForm | 

    try:
        # Delete Pipeline
        api_response = await api_instance.delete_pipeline_api_v1_pipelines_delete_delete(delete_pipeline_form)
        print("The response of PipelinesApi->delete_pipeline_api_v1_pipelines_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->delete_pipeline_api_v1_pipelines_delete_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_pipeline_form** | [**DeletePipelineForm**](DeletePipelineForm.md)|  | 

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

# **get_pipeline_valves_api_v1_pipelines_pipeline_id_valves_get**
> object get_pipeline_valves_api_v1_pipelines_pipeline_id_valves_get(pipeline_id, url_idx)

Get Pipeline Valves

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
    api_instance = openwebui_client.PipelinesApi(api_client)
    pipeline_id = 'pipeline_id_example' # str | 
    url_idx = 56 # int | 

    try:
        # Get Pipeline Valves
        api_response = await api_instance.get_pipeline_valves_api_v1_pipelines_pipeline_id_valves_get(pipeline_id, url_idx)
        print("The response of PipelinesApi->get_pipeline_valves_api_v1_pipelines_pipeline_id_valves_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->get_pipeline_valves_api_v1_pipelines_pipeline_id_valves_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**|  | 
 **url_idx** | **int**|  | 

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

# **get_pipeline_valves_spec_api_v1_pipelines_pipeline_id_valves_spec_get**
> object get_pipeline_valves_spec_api_v1_pipelines_pipeline_id_valves_spec_get(pipeline_id, url_idx)

Get Pipeline Valves Spec

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
    api_instance = openwebui_client.PipelinesApi(api_client)
    pipeline_id = 'pipeline_id_example' # str | 
    url_idx = 56 # int | 

    try:
        # Get Pipeline Valves Spec
        api_response = await api_instance.get_pipeline_valves_spec_api_v1_pipelines_pipeline_id_valves_spec_get(pipeline_id, url_idx)
        print("The response of PipelinesApi->get_pipeline_valves_spec_api_v1_pipelines_pipeline_id_valves_spec_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->get_pipeline_valves_spec_api_v1_pipelines_pipeline_id_valves_spec_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**|  | 
 **url_idx** | **int**|  | 

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

# **get_pipelines_api_v1_pipelines_get**
> object get_pipelines_api_v1_pipelines_get(url_idx=url_idx)

Get Pipelines

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
    api_instance = openwebui_client.PipelinesApi(api_client)
    url_idx = 56 # int |  (optional)

    try:
        # Get Pipelines
        api_response = await api_instance.get_pipelines_api_v1_pipelines_get(url_idx=url_idx)
        print("The response of PipelinesApi->get_pipelines_api_v1_pipelines_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->get_pipelines_api_v1_pipelines_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_idx** | **int**|  | [optional] 

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

# **get_pipelines_list_api_v1_pipelines_list_get**
> object get_pipelines_list_api_v1_pipelines_list_get()

Get Pipelines List

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
    api_instance = openwebui_client.PipelinesApi(api_client)

    try:
        # Get Pipelines List
        api_response = await api_instance.get_pipelines_list_api_v1_pipelines_list_get()
        print("The response of PipelinesApi->get_pipelines_list_api_v1_pipelines_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->get_pipelines_list_api_v1_pipelines_list_get: %s\n" % e)
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

# **update_pipeline_valves_api_v1_pipelines_pipeline_id_valves_update_post**
> object update_pipeline_valves_api_v1_pipelines_pipeline_id_valves_update_post(pipeline_id, url_idx, request_body)

Update Pipeline Valves

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
    api_instance = openwebui_client.PipelinesApi(api_client)
    pipeline_id = 'pipeline_id_example' # str | 
    url_idx = 56 # int | 
    request_body = None # Dict[str, object] | 

    try:
        # Update Pipeline Valves
        api_response = await api_instance.update_pipeline_valves_api_v1_pipelines_pipeline_id_valves_update_post(pipeline_id, url_idx, request_body)
        print("The response of PipelinesApi->update_pipeline_valves_api_v1_pipelines_pipeline_id_valves_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->update_pipeline_valves_api_v1_pipelines_pipeline_id_valves_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_id** | **str**|  | 
 **url_idx** | **int**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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

# **upload_pipeline_api_v1_pipelines_upload_post**
> object upload_pipeline_api_v1_pipelines_upload_post(url_idx, file)

Upload Pipeline

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
    api_instance = openwebui_client.PipelinesApi(api_client)
    url_idx = 56 # int | 
    file = 'file_example' # str | 

    try:
        # Upload Pipeline
        api_response = await api_instance.upload_pipeline_api_v1_pipelines_upload_post(url_idx, file)
        print("The response of PipelinesApi->upload_pipeline_api_v1_pipelines_upload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->upload_pipeline_api_v1_pipelines_upload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_idx** | **int**|  | 
 **file** | **str**|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

