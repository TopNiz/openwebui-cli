# openwebui_client.PromptsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_prompt_api_v1_prompts_create_post**](PromptsApi.md#create_new_prompt_api_v1_prompts_create_post) | **POST** /api/v1/prompts/create | Create New Prompt
[**delete_prompt_by_id_api_v1_prompts_id_prompt_id_delete_delete**](PromptsApi.md#delete_prompt_by_id_api_v1_prompts_id_prompt_id_delete_delete) | **DELETE** /api/v1/prompts/id/{prompt_id}/delete | Delete Prompt By Id
[**delete_prompt_history_entry_api_v1_prompts_id_prompt_id_history_history_id_delete**](PromptsApi.md#delete_prompt_history_entry_api_v1_prompts_id_prompt_id_history_history_id_delete) | **DELETE** /api/v1/prompts/id/{prompt_id}/history/{history_id} | Delete Prompt History Entry
[**get_prompt_by_id_api_v1_prompts_id_prompt_id_get**](PromptsApi.md#get_prompt_by_id_api_v1_prompts_id_prompt_id_get) | **GET** /api/v1/prompts/id/{prompt_id} | Get Prompt By Id
[**get_prompt_diff_api_v1_prompts_id_prompt_id_history_diff_get**](PromptsApi.md#get_prompt_diff_api_v1_prompts_id_prompt_id_history_diff_get) | **GET** /api/v1/prompts/id/{prompt_id}/history/diff | Get Prompt Diff
[**get_prompt_history_api_v1_prompts_id_prompt_id_history_get**](PromptsApi.md#get_prompt_history_api_v1_prompts_id_prompt_id_history_get) | **GET** /api/v1/prompts/id/{prompt_id}/history | Get Prompt History
[**get_prompt_history_entry_api_v1_prompts_id_prompt_id_history_history_id_get**](PromptsApi.md#get_prompt_history_entry_api_v1_prompts_id_prompt_id_history_history_id_get) | **GET** /api/v1/prompts/id/{prompt_id}/history/{history_id} | Get Prompt History Entry
[**get_prompt_list_api_v1_prompts_list_get**](PromptsApi.md#get_prompt_list_api_v1_prompts_list_get) | **GET** /api/v1/prompts/list | Get Prompt List
[**get_prompt_tags_api_v1_prompts_tags_get**](PromptsApi.md#get_prompt_tags_api_v1_prompts_tags_get) | **GET** /api/v1/prompts/tags | Get Prompt Tags
[**get_prompts_api_v1_prompts_get**](PromptsApi.md#get_prompts_api_v1_prompts_get) | **GET** /api/v1/prompts/ | Get Prompts
[**set_prompt_version_api_v1_prompts_id_prompt_id_update_version_post**](PromptsApi.md#set_prompt_version_api_v1_prompts_id_prompt_id_update_version_post) | **POST** /api/v1/prompts/id/{prompt_id}/update/version | Set Prompt Version
[**toggle_prompt_active_api_v1_prompts_id_prompt_id_toggle_post**](PromptsApi.md#toggle_prompt_active_api_v1_prompts_id_prompt_id_toggle_post) | **POST** /api/v1/prompts/id/{prompt_id}/toggle | Toggle Prompt Active
[**update_prompt_access_by_id_api_v1_prompts_id_prompt_id_access_update_post**](PromptsApi.md#update_prompt_access_by_id_api_v1_prompts_id_prompt_id_access_update_post) | **POST** /api/v1/prompts/id/{prompt_id}/access/update | Update Prompt Access By Id
[**update_prompt_by_id_api_v1_prompts_id_prompt_id_update_post**](PromptsApi.md#update_prompt_by_id_api_v1_prompts_id_prompt_id_update_post) | **POST** /api/v1/prompts/id/{prompt_id}/update | Update Prompt By Id
[**update_prompt_metadata_api_v1_prompts_id_prompt_id_update_meta_post**](PromptsApi.md#update_prompt_metadata_api_v1_prompts_id_prompt_id_update_meta_post) | **POST** /api/v1/prompts/id/{prompt_id}/update/meta | Update Prompt Metadata


# **create_new_prompt_api_v1_prompts_create_post**
> PromptModel create_new_prompt_api_v1_prompts_create_post(prompt_form)

Create New Prompt

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.prompt_form import PromptForm
from openwebui_client.models.prompt_model import PromptModel
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
    api_instance = openwebui_client.PromptsApi(api_client)
    prompt_form = openwebui_client.PromptForm() # PromptForm | 

    try:
        # Create New Prompt
        api_response = await api_instance.create_new_prompt_api_v1_prompts_create_post(prompt_form)
        print("The response of PromptsApi->create_new_prompt_api_v1_prompts_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->create_new_prompt_api_v1_prompts_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_form** | [**PromptForm**](PromptForm.md)|  | 

### Return type

[**PromptModel**](PromptModel.md)

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

# **delete_prompt_by_id_api_v1_prompts_id_prompt_id_delete_delete**
> bool delete_prompt_by_id_api_v1_prompts_id_prompt_id_delete_delete(prompt_id)

Delete Prompt By Id

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
    api_instance = openwebui_client.PromptsApi(api_client)
    prompt_id = 'prompt_id_example' # str | 

    try:
        # Delete Prompt By Id
        api_response = await api_instance.delete_prompt_by_id_api_v1_prompts_id_prompt_id_delete_delete(prompt_id)
        print("The response of PromptsApi->delete_prompt_by_id_api_v1_prompts_id_prompt_id_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->delete_prompt_by_id_api_v1_prompts_id_prompt_id_delete_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_id** | **str**|  | 

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

# **delete_prompt_history_entry_api_v1_prompts_id_prompt_id_history_history_id_delete**
> bool delete_prompt_history_entry_api_v1_prompts_id_prompt_id_history_history_id_delete(prompt_id, history_id)

Delete Prompt History Entry

Delete a history entry. Cannot delete the active production version.

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
    api_instance = openwebui_client.PromptsApi(api_client)
    prompt_id = 'prompt_id_example' # str | 
    history_id = 'history_id_example' # str | 

    try:
        # Delete Prompt History Entry
        api_response = await api_instance.delete_prompt_history_entry_api_v1_prompts_id_prompt_id_history_history_id_delete(prompt_id, history_id)
        print("The response of PromptsApi->delete_prompt_history_entry_api_v1_prompts_id_prompt_id_history_history_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->delete_prompt_history_entry_api_v1_prompts_id_prompt_id_history_history_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_id** | **str**|  | 
 **history_id** | **str**|  | 

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

# **get_prompt_by_id_api_v1_prompts_id_prompt_id_get**
> PromptAccessResponse get_prompt_by_id_api_v1_prompts_id_prompt_id_get(prompt_id)

Get Prompt By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.prompt_access_response import PromptAccessResponse
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
    api_instance = openwebui_client.PromptsApi(api_client)
    prompt_id = 'prompt_id_example' # str | 

    try:
        # Get Prompt By Id
        api_response = await api_instance.get_prompt_by_id_api_v1_prompts_id_prompt_id_get(prompt_id)
        print("The response of PromptsApi->get_prompt_by_id_api_v1_prompts_id_prompt_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->get_prompt_by_id_api_v1_prompts_id_prompt_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_id** | **str**|  | 

### Return type

[**PromptAccessResponse**](PromptAccessResponse.md)

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

# **get_prompt_diff_api_v1_prompts_id_prompt_id_history_diff_get**
> object get_prompt_diff_api_v1_prompts_id_prompt_id_history_diff_get(prompt_id, from_id, to_id)

Get Prompt Diff

Get diff between two versions.

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
    api_instance = openwebui_client.PromptsApi(api_client)
    prompt_id = 'prompt_id_example' # str | 
    from_id = 'from_id_example' # str | 
    to_id = 'to_id_example' # str | 

    try:
        # Get Prompt Diff
        api_response = await api_instance.get_prompt_diff_api_v1_prompts_id_prompt_id_history_diff_get(prompt_id, from_id, to_id)
        print("The response of PromptsApi->get_prompt_diff_api_v1_prompts_id_prompt_id_history_diff_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->get_prompt_diff_api_v1_prompts_id_prompt_id_history_diff_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_id** | **str**|  | 
 **from_id** | **str**|  | 
 **to_id** | **str**|  | 

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

# **get_prompt_history_api_v1_prompts_id_prompt_id_history_get**
> List[PromptHistoryResponse] get_prompt_history_api_v1_prompts_id_prompt_id_history_get(prompt_id, page=page)

Get Prompt History

Get version history for a prompt.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.prompt_history_response import PromptHistoryResponse
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
    api_instance = openwebui_client.PromptsApi(api_client)
    prompt_id = 'prompt_id_example' # str | 
    page = 0 # int |  (optional) (default to 0)

    try:
        # Get Prompt History
        api_response = await api_instance.get_prompt_history_api_v1_prompts_id_prompt_id_history_get(prompt_id, page=page)
        print("The response of PromptsApi->get_prompt_history_api_v1_prompts_id_prompt_id_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->get_prompt_history_api_v1_prompts_id_prompt_id_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 0]

### Return type

[**List[PromptHistoryResponse]**](PromptHistoryResponse.md)

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

# **get_prompt_history_entry_api_v1_prompts_id_prompt_id_history_history_id_get**
> PromptHistoryModel get_prompt_history_entry_api_v1_prompts_id_prompt_id_history_history_id_get(prompt_id, history_id)

Get Prompt History Entry

Get a specific version from history.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.prompt_history_model import PromptHistoryModel
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
    api_instance = openwebui_client.PromptsApi(api_client)
    prompt_id = 'prompt_id_example' # str | 
    history_id = 'history_id_example' # str | 

    try:
        # Get Prompt History Entry
        api_response = await api_instance.get_prompt_history_entry_api_v1_prompts_id_prompt_id_history_history_id_get(prompt_id, history_id)
        print("The response of PromptsApi->get_prompt_history_entry_api_v1_prompts_id_prompt_id_history_history_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->get_prompt_history_entry_api_v1_prompts_id_prompt_id_history_history_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_id** | **str**|  | 
 **history_id** | **str**|  | 

### Return type

[**PromptHistoryModel**](PromptHistoryModel.md)

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

# **get_prompt_list_api_v1_prompts_list_get**
> PromptAccessListResponse get_prompt_list_api_v1_prompts_list_get(query=query, view_option=view_option, tag=tag, order_by=order_by, direction=direction, page=page)

Get Prompt List

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.prompt_access_list_response import PromptAccessListResponse
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
    api_instance = openwebui_client.PromptsApi(api_client)
    query = 'query_example' # str |  (optional)
    view_option = 'view_option_example' # str |  (optional)
    tag = 'tag_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    direction = 'direction_example' # str |  (optional)
    page = 56 # int |  (optional)

    try:
        # Get Prompt List
        api_response = await api_instance.get_prompt_list_api_v1_prompts_list_get(query=query, view_option=view_option, tag=tag, order_by=order_by, direction=direction, page=page)
        print("The response of PromptsApi->get_prompt_list_api_v1_prompts_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->get_prompt_list_api_v1_prompts_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **view_option** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 

### Return type

[**PromptAccessListResponse**](PromptAccessListResponse.md)

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

# **get_prompt_tags_api_v1_prompts_tags_get**
> List[Optional[str]] get_prompt_tags_api_v1_prompts_tags_get()

Get Prompt Tags

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
    api_instance = openwebui_client.PromptsApi(api_client)

    try:
        # Get Prompt Tags
        api_response = await api_instance.get_prompt_tags_api_v1_prompts_tags_get()
        print("The response of PromptsApi->get_prompt_tags_api_v1_prompts_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->get_prompt_tags_api_v1_prompts_tags_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[Optional[str]]**

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

# **get_prompts_api_v1_prompts_get**
> List[PromptModel] get_prompts_api_v1_prompts_get()

Get Prompts

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.prompt_model import PromptModel
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
    api_instance = openwebui_client.PromptsApi(api_client)

    try:
        # Get Prompts
        api_response = await api_instance.get_prompts_api_v1_prompts_get()
        print("The response of PromptsApi->get_prompts_api_v1_prompts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->get_prompts_api_v1_prompts_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PromptModel]**](PromptModel.md)

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

# **set_prompt_version_api_v1_prompts_id_prompt_id_update_version_post**
> PromptModel set_prompt_version_api_v1_prompts_id_prompt_id_update_version_post(prompt_id, prompt_version_update_form)

Set Prompt Version

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.prompt_model import PromptModel
from openwebui_client.models.prompt_version_update_form import PromptVersionUpdateForm
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
    api_instance = openwebui_client.PromptsApi(api_client)
    prompt_id = 'prompt_id_example' # str | 
    prompt_version_update_form = openwebui_client.PromptVersionUpdateForm() # PromptVersionUpdateForm | 

    try:
        # Set Prompt Version
        api_response = await api_instance.set_prompt_version_api_v1_prompts_id_prompt_id_update_version_post(prompt_id, prompt_version_update_form)
        print("The response of PromptsApi->set_prompt_version_api_v1_prompts_id_prompt_id_update_version_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->set_prompt_version_api_v1_prompts_id_prompt_id_update_version_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_id** | **str**|  | 
 **prompt_version_update_form** | [**PromptVersionUpdateForm**](PromptVersionUpdateForm.md)|  | 

### Return type

[**PromptModel**](PromptModel.md)

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

# **toggle_prompt_active_api_v1_prompts_id_prompt_id_toggle_post**
> PromptModel toggle_prompt_active_api_v1_prompts_id_prompt_id_toggle_post(prompt_id)

Toggle Prompt Active

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.prompt_model import PromptModel
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
    api_instance = openwebui_client.PromptsApi(api_client)
    prompt_id = 'prompt_id_example' # str | 

    try:
        # Toggle Prompt Active
        api_response = await api_instance.toggle_prompt_active_api_v1_prompts_id_prompt_id_toggle_post(prompt_id)
        print("The response of PromptsApi->toggle_prompt_active_api_v1_prompts_id_prompt_id_toggle_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->toggle_prompt_active_api_v1_prompts_id_prompt_id_toggle_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_id** | **str**|  | 

### Return type

[**PromptModel**](PromptModel.md)

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

# **update_prompt_access_by_id_api_v1_prompts_id_prompt_id_access_update_post**
> PromptModel update_prompt_access_by_id_api_v1_prompts_id_prompt_id_access_update_post(prompt_id, prompt_access_grants_form)

Update Prompt Access By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.prompt_access_grants_form import PromptAccessGrantsForm
from openwebui_client.models.prompt_model import PromptModel
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
    api_instance = openwebui_client.PromptsApi(api_client)
    prompt_id = 'prompt_id_example' # str | 
    prompt_access_grants_form = openwebui_client.PromptAccessGrantsForm() # PromptAccessGrantsForm | 

    try:
        # Update Prompt Access By Id
        api_response = await api_instance.update_prompt_access_by_id_api_v1_prompts_id_prompt_id_access_update_post(prompt_id, prompt_access_grants_form)
        print("The response of PromptsApi->update_prompt_access_by_id_api_v1_prompts_id_prompt_id_access_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->update_prompt_access_by_id_api_v1_prompts_id_prompt_id_access_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_id** | **str**|  | 
 **prompt_access_grants_form** | [**PromptAccessGrantsForm**](PromptAccessGrantsForm.md)|  | 

### Return type

[**PromptModel**](PromptModel.md)

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

# **update_prompt_by_id_api_v1_prompts_id_prompt_id_update_post**
> PromptModel update_prompt_by_id_api_v1_prompts_id_prompt_id_update_post(prompt_id, prompt_form)

Update Prompt By Id

Update a prompt's content, creating a new history entry if changed.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.prompt_form import PromptForm
from openwebui_client.models.prompt_model import PromptModel
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
    api_instance = openwebui_client.PromptsApi(api_client)
    prompt_id = 'prompt_id_example' # str | 
    prompt_form = openwebui_client.PromptForm() # PromptForm | 

    try:
        # Update Prompt By Id
        api_response = await api_instance.update_prompt_by_id_api_v1_prompts_id_prompt_id_update_post(prompt_id, prompt_form)
        print("The response of PromptsApi->update_prompt_by_id_api_v1_prompts_id_prompt_id_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->update_prompt_by_id_api_v1_prompts_id_prompt_id_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_id** | **str**|  | 
 **prompt_form** | [**PromptForm**](PromptForm.md)|  | 

### Return type

[**PromptModel**](PromptModel.md)

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

# **update_prompt_metadata_api_v1_prompts_id_prompt_id_update_meta_post**
> PromptModel update_prompt_metadata_api_v1_prompts_id_prompt_id_update_meta_post(prompt_id, prompt_metadata_form)

Update Prompt Metadata

Update prompt name and command only (no history created).

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.prompt_metadata_form import PromptMetadataForm
from openwebui_client.models.prompt_model import PromptModel
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
    api_instance = openwebui_client.PromptsApi(api_client)
    prompt_id = 'prompt_id_example' # str | 
    prompt_metadata_form = openwebui_client.PromptMetadataForm() # PromptMetadataForm | 

    try:
        # Update Prompt Metadata
        api_response = await api_instance.update_prompt_metadata_api_v1_prompts_id_prompt_id_update_meta_post(prompt_id, prompt_metadata_form)
        print("The response of PromptsApi->update_prompt_metadata_api_v1_prompts_id_prompt_id_update_meta_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->update_prompt_metadata_api_v1_prompts_id_prompt_id_update_meta_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_id** | **str**|  | 
 **prompt_metadata_form** | [**PromptMetadataForm**](PromptMetadataForm.md)|  | 

### Return type

[**PromptModel**](PromptModel.md)

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

