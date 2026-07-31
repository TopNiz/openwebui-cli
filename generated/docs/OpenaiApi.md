# openwebui_client.OpenaiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_chat_completion_openai_chat_completions_post**](OpenaiApi.md#generate_chat_completion_openai_chat_completions_post) | **POST** /openai/chat/completions | Generate Chat Completion
[**get_config_openai_config_get**](OpenaiApi.md#get_config_openai_config_get) | **GET** /openai/config | Get Config
[**get_models_openai_models_get**](OpenaiApi.md#get_models_openai_models_get) | **GET** /openai/models | Get Models
[**get_models_openai_models_url_idx_get**](OpenaiApi.md#get_models_openai_models_url_idx_get) | **GET** /openai/models/{url_idx} | Get Models
[**proxy_openai_path_post**](OpenaiApi.md#proxy_openai_path_post) | **GET** /openai/{path} | Proxy
[**proxy_openai_path_post_delete2e256bd09e**](OpenaiApi.md#proxy_openai_path_post_delete2e256bd09e) | **DELETE** /openai/{path} | Proxy
[**proxy_openai_path_post_post0eaa356982**](OpenaiApi.md#proxy_openai_path_post_post0eaa356982) | **POST** /openai/{path} | Proxy
[**proxy_openai_path_post_put_edfea91598**](OpenaiApi.md#proxy_openai_path_post_put_edfea91598) | **PUT** /openai/{path} | Proxy
[**responses_openai_responses_post**](OpenaiApi.md#responses_openai_responses_post) | **POST** /openai/responses | Responses
[**speech_openai_audio_speech_post**](OpenaiApi.md#speech_openai_audio_speech_post) | **POST** /openai/audio/speech | Speech
[**update_config_openai_config_update_post**](OpenaiApi.md#update_config_openai_config_update_post) | **POST** /openai/config/update | Update Config
[**verify_connection_openai_verify_post**](OpenaiApi.md#verify_connection_openai_verify_post) | **POST** /openai/verify | Verify Connection


# **generate_chat_completion_openai_chat_completions_post**
> object generate_chat_completion_openai_chat_completions_post(request_body)

Generate Chat Completion

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
    api_instance = openwebui_client.OpenaiApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Generate Chat Completion
        api_response = await api_instance.generate_chat_completion_openai_chat_completions_post(request_body)
        print("The response of OpenaiApi->generate_chat_completion_openai_chat_completions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->generate_chat_completion_openai_chat_completions_post: %s\n" % e)
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

# **get_config_openai_config_get**
> object get_config_openai_config_get()

Get Config

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
    api_instance = openwebui_client.OpenaiApi(api_client)

    try:
        # Get Config
        api_response = await api_instance.get_config_openai_config_get()
        print("The response of OpenaiApi->get_config_openai_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->get_config_openai_config_get: %s\n" % e)
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

# **get_models_openai_models_get**
> object get_models_openai_models_get(url_idx=url_idx)

Get Models

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
    api_instance = openwebui_client.OpenaiApi(api_client)
    url_idx = 56 # int |  (optional)

    try:
        # Get Models
        api_response = await api_instance.get_models_openai_models_get(url_idx=url_idx)
        print("The response of OpenaiApi->get_models_openai_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->get_models_openai_models_get: %s\n" % e)
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

# **get_models_openai_models_url_idx_get**
> object get_models_openai_models_url_idx_get(url_idx)

Get Models

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
    api_instance = openwebui_client.OpenaiApi(api_client)
    url_idx = 56 # int | 

    try:
        # Get Models
        api_response = await api_instance.get_models_openai_models_url_idx_get(url_idx)
        print("The response of OpenaiApi->get_models_openai_models_url_idx_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->get_models_openai_models_url_idx_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **proxy_openai_path_post**
> object proxy_openai_path_post(path)

Proxy

Deprecated: proxy all requests to OpenAI API.
Disabled by default. Set ENABLE_OPENAI_API_PASSTHROUGH=True to enable.

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
    api_instance = openwebui_client.OpenaiApi(api_client)
    path = 'path_example' # str | 

    try:
        # Proxy
        api_response = await api_instance.proxy_openai_path_post(path)
        print("The response of OpenaiApi->proxy_openai_path_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->proxy_openai_path_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **proxy_openai_path_post_delete2e256bd09e**
> object proxy_openai_path_post_delete2e256bd09e(path)

Proxy

Deprecated: proxy all requests to OpenAI API.
Disabled by default. Set ENABLE_OPENAI_API_PASSTHROUGH=True to enable.

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
    api_instance = openwebui_client.OpenaiApi(api_client)
    path = 'path_example' # str | 

    try:
        # Proxy
        api_response = await api_instance.proxy_openai_path_post_delete2e256bd09e(path)
        print("The response of OpenaiApi->proxy_openai_path_post_delete2e256bd09e:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->proxy_openai_path_post_delete2e256bd09e: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **proxy_openai_path_post_post0eaa356982**
> object proxy_openai_path_post_post0eaa356982(path)

Proxy

Deprecated: proxy all requests to OpenAI API.
Disabled by default. Set ENABLE_OPENAI_API_PASSTHROUGH=True to enable.

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
    api_instance = openwebui_client.OpenaiApi(api_client)
    path = 'path_example' # str | 

    try:
        # Proxy
        api_response = await api_instance.proxy_openai_path_post_post0eaa356982(path)
        print("The response of OpenaiApi->proxy_openai_path_post_post0eaa356982:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->proxy_openai_path_post_post0eaa356982: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **proxy_openai_path_post_put_edfea91598**
> object proxy_openai_path_post_put_edfea91598(path)

Proxy

Deprecated: proxy all requests to OpenAI API.
Disabled by default. Set ENABLE_OPENAI_API_PASSTHROUGH=True to enable.

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
    api_instance = openwebui_client.OpenaiApi(api_client)
    path = 'path_example' # str | 

    try:
        # Proxy
        api_response = await api_instance.proxy_openai_path_post_put_edfea91598(path)
        print("The response of OpenaiApi->proxy_openai_path_post_put_edfea91598:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->proxy_openai_path_post_put_edfea91598: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **responses_openai_responses_post**
> object responses_openai_responses_post(open_webui_routers_openai_responses_form)

Responses

Forward requests to the OpenAI Responses API endpoint.
Routes to the correct upstream backend based on the model field.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.open_webui_routers_openai_responses_form import OpenWebuiRoutersOpenaiResponsesForm
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
    api_instance = openwebui_client.OpenaiApi(api_client)
    open_webui_routers_openai_responses_form = openwebui_client.OpenWebuiRoutersOpenaiResponsesForm() # OpenWebuiRoutersOpenaiResponsesForm | 

    try:
        # Responses
        api_response = await api_instance.responses_openai_responses_post(open_webui_routers_openai_responses_form)
        print("The response of OpenaiApi->responses_openai_responses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->responses_openai_responses_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_webui_routers_openai_responses_form** | [**OpenWebuiRoutersOpenaiResponsesForm**](OpenWebuiRoutersOpenaiResponsesForm.md)|  | 

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

# **speech_openai_audio_speech_post**
> object speech_openai_audio_speech_post()

Speech

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
    api_instance = openwebui_client.OpenaiApi(api_client)

    try:
        # Speech
        api_response = await api_instance.speech_openai_audio_speech_post()
        print("The response of OpenaiApi->speech_openai_audio_speech_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->speech_openai_audio_speech_post: %s\n" % e)
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

# **update_config_openai_config_update_post**
> object update_config_openai_config_update_post(open_webui_routers_openai_open_ai_config_form)

Update Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.open_webui_routers_openai_open_ai_config_form import OpenWebuiRoutersOpenaiOpenAIConfigForm
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
    api_instance = openwebui_client.OpenaiApi(api_client)
    open_webui_routers_openai_open_ai_config_form = openwebui_client.OpenWebuiRoutersOpenaiOpenAIConfigForm() # OpenWebuiRoutersOpenaiOpenAIConfigForm | 

    try:
        # Update Config
        api_response = await api_instance.update_config_openai_config_update_post(open_webui_routers_openai_open_ai_config_form)
        print("The response of OpenaiApi->update_config_openai_config_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->update_config_openai_config_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_webui_routers_openai_open_ai_config_form** | [**OpenWebuiRoutersOpenaiOpenAIConfigForm**](OpenWebuiRoutersOpenaiOpenAIConfigForm.md)|  | 

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

# **verify_connection_openai_verify_post**
> object verify_connection_openai_verify_post(open_webui_routers_openai_connection_verification_form)

Verify Connection

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.open_webui_routers_openai_connection_verification_form import OpenWebuiRoutersOpenaiConnectionVerificationForm
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
    api_instance = openwebui_client.OpenaiApi(api_client)
    open_webui_routers_openai_connection_verification_form = openwebui_client.OpenWebuiRoutersOpenaiConnectionVerificationForm() # OpenWebuiRoutersOpenaiConnectionVerificationForm | 

    try:
        # Verify Connection
        api_response = await api_instance.verify_connection_openai_verify_post(open_webui_routers_openai_connection_verification_form)
        print("The response of OpenaiApi->verify_connection_openai_verify_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenaiApi->verify_connection_openai_verify_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_webui_routers_openai_connection_verification_form** | [**OpenWebuiRoutersOpenaiConnectionVerificationForm**](OpenWebuiRoutersOpenaiConnectionVerificationForm.md)|  | 

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

