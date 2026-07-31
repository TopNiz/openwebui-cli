# openwebui_client.TasksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_autocompletion_api_v1_tasks_auto_completions_post**](TasksApi.md#generate_autocompletion_api_v1_tasks_auto_completions_post) | **POST** /api/v1/tasks/auto/completions | Generate Autocompletion
[**generate_chat_tags_api_v1_tasks_tags_completions_post**](TasksApi.md#generate_chat_tags_api_v1_tasks_tags_completions_post) | **POST** /api/v1/tasks/tags/completions | Generate Chat Tags
[**generate_emoji_api_v1_tasks_emoji_completions_post**](TasksApi.md#generate_emoji_api_v1_tasks_emoji_completions_post) | **POST** /api/v1/tasks/emoji/completions | Generate Emoji
[**generate_follow_ups_api_v1_tasks_follow_up_completions_post**](TasksApi.md#generate_follow_ups_api_v1_tasks_follow_up_completions_post) | **POST** /api/v1/tasks/follow_up/completions | Generate Follow Ups
[**generate_image_prompt_api_v1_tasks_image_prompt_completions_post**](TasksApi.md#generate_image_prompt_api_v1_tasks_image_prompt_completions_post) | **POST** /api/v1/tasks/image_prompt/completions | Generate Image Prompt
[**generate_moa_response_api_v1_tasks_moa_completions_post**](TasksApi.md#generate_moa_response_api_v1_tasks_moa_completions_post) | **POST** /api/v1/tasks/moa/completions | Generate Moa Response
[**generate_queries_api_v1_tasks_queries_completions_post**](TasksApi.md#generate_queries_api_v1_tasks_queries_completions_post) | **POST** /api/v1/tasks/queries/completions | Generate Queries
[**generate_title_api_v1_tasks_title_completions_post**](TasksApi.md#generate_title_api_v1_tasks_title_completions_post) | **POST** /api/v1/tasks/title/completions | Generate Title
[**get_task_config_api_v1_tasks_config_get**](TasksApi.md#get_task_config_api_v1_tasks_config_get) | **GET** /api/v1/tasks/config | Get Task Config
[**update_task_config_api_v1_tasks_config_update_post**](TasksApi.md#update_task_config_api_v1_tasks_config_update_post) | **POST** /api/v1/tasks/config/update | Update Task Config


# **generate_autocompletion_api_v1_tasks_auto_completions_post**
> object generate_autocompletion_api_v1_tasks_auto_completions_post(request_body)

Generate Autocompletion

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
    api_instance = openwebui_client.TasksApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Generate Autocompletion
        api_response = await api_instance.generate_autocompletion_api_v1_tasks_auto_completions_post(request_body)
        print("The response of TasksApi->generate_autocompletion_api_v1_tasks_auto_completions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->generate_autocompletion_api_v1_tasks_auto_completions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **generate_chat_tags_api_v1_tasks_tags_completions_post**
> object generate_chat_tags_api_v1_tasks_tags_completions_post(request_body)

Generate Chat Tags

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
    api_instance = openwebui_client.TasksApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Generate Chat Tags
        api_response = await api_instance.generate_chat_tags_api_v1_tasks_tags_completions_post(request_body)
        print("The response of TasksApi->generate_chat_tags_api_v1_tasks_tags_completions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->generate_chat_tags_api_v1_tasks_tags_completions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **generate_emoji_api_v1_tasks_emoji_completions_post**
> object generate_emoji_api_v1_tasks_emoji_completions_post(request_body)

Generate Emoji

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
    api_instance = openwebui_client.TasksApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Generate Emoji
        api_response = await api_instance.generate_emoji_api_v1_tasks_emoji_completions_post(request_body)
        print("The response of TasksApi->generate_emoji_api_v1_tasks_emoji_completions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->generate_emoji_api_v1_tasks_emoji_completions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **generate_follow_ups_api_v1_tasks_follow_up_completions_post**
> object generate_follow_ups_api_v1_tasks_follow_up_completions_post(request_body)

Generate Follow Ups

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
    api_instance = openwebui_client.TasksApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Generate Follow Ups
        api_response = await api_instance.generate_follow_ups_api_v1_tasks_follow_up_completions_post(request_body)
        print("The response of TasksApi->generate_follow_ups_api_v1_tasks_follow_up_completions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->generate_follow_ups_api_v1_tasks_follow_up_completions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **generate_image_prompt_api_v1_tasks_image_prompt_completions_post**
> object generate_image_prompt_api_v1_tasks_image_prompt_completions_post(request_body)

Generate Image Prompt

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
    api_instance = openwebui_client.TasksApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Generate Image Prompt
        api_response = await api_instance.generate_image_prompt_api_v1_tasks_image_prompt_completions_post(request_body)
        print("The response of TasksApi->generate_image_prompt_api_v1_tasks_image_prompt_completions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->generate_image_prompt_api_v1_tasks_image_prompt_completions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **generate_moa_response_api_v1_tasks_moa_completions_post**
> object generate_moa_response_api_v1_tasks_moa_completions_post(request_body)

Generate Moa Response

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
    api_instance = openwebui_client.TasksApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Generate Moa Response
        api_response = await api_instance.generate_moa_response_api_v1_tasks_moa_completions_post(request_body)
        print("The response of TasksApi->generate_moa_response_api_v1_tasks_moa_completions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->generate_moa_response_api_v1_tasks_moa_completions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **generate_queries_api_v1_tasks_queries_completions_post**
> object generate_queries_api_v1_tasks_queries_completions_post(request_body)

Generate Queries

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
    api_instance = openwebui_client.TasksApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Generate Queries
        api_response = await api_instance.generate_queries_api_v1_tasks_queries_completions_post(request_body)
        print("The response of TasksApi->generate_queries_api_v1_tasks_queries_completions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->generate_queries_api_v1_tasks_queries_completions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **generate_title_api_v1_tasks_title_completions_post**
> object generate_title_api_v1_tasks_title_completions_post(request_body)

Generate Title

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
    api_instance = openwebui_client.TasksApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Generate Title
        api_response = await api_instance.generate_title_api_v1_tasks_title_completions_post(request_body)
        print("The response of TasksApi->generate_title_api_v1_tasks_title_completions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->generate_title_api_v1_tasks_title_completions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_task_config_api_v1_tasks_config_get**
> object get_task_config_api_v1_tasks_config_get()

Get Task Config

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
    api_instance = openwebui_client.TasksApi(api_client)

    try:
        # Get Task Config
        api_response = await api_instance.get_task_config_api_v1_tasks_config_get()
        print("The response of TasksApi->get_task_config_api_v1_tasks_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_config_api_v1_tasks_config_get: %s\n" % e)
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

# **update_task_config_api_v1_tasks_config_update_post**
> object update_task_config_api_v1_tasks_config_update_post(task_config_form)

Update Task Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.task_config_form import TaskConfigForm
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
    api_instance = openwebui_client.TasksApi(api_client)
    task_config_form = openwebui_client.TaskConfigForm() # TaskConfigForm | 

    try:
        # Update Task Config
        api_response = await api_instance.update_task_config_api_v1_tasks_config_update_post(task_config_form)
        print("The response of TasksApi->update_task_config_api_v1_tasks_config_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->update_task_config_api_v1_tasks_config_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_config_form** | [**TaskConfigForm**](TaskConfigForm.md)|  | 

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

