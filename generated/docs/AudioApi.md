# openwebui_client.AudioApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audio_config_api_v1_audio_config_get**](AudioApi.md#get_audio_config_api_v1_audio_config_get) | **GET** /api/v1/audio/config | Get Audio Config
[**get_models_api_v1_audio_models_get**](AudioApi.md#get_models_api_v1_audio_models_get) | **GET** /api/v1/audio/models | Get Models
[**get_voices_api_v1_audio_voices_get**](AudioApi.md#get_voices_api_v1_audio_voices_get) | **GET** /api/v1/audio/voices | Get Voices
[**speech_api_v1_audio_speech_post**](AudioApi.md#speech_api_v1_audio_speech_post) | **POST** /api/v1/audio/speech | Speech
[**transcription_api_v1_audio_transcriptions_post**](AudioApi.md#transcription_api_v1_audio_transcriptions_post) | **POST** /api/v1/audio/transcriptions | Transcription
[**update_audio_config_api_v1_audio_config_update_post**](AudioApi.md#update_audio_config_api_v1_audio_config_update_post) | **POST** /api/v1/audio/config/update | Update Audio Config


# **get_audio_config_api_v1_audio_config_get**
> object get_audio_config_api_v1_audio_config_get()

Get Audio Config

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
    api_instance = openwebui_client.AudioApi(api_client)

    try:
        # Get Audio Config
        api_response = await api_instance.get_audio_config_api_v1_audio_config_get()
        print("The response of AudioApi->get_audio_config_api_v1_audio_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudioApi->get_audio_config_api_v1_audio_config_get: %s\n" % e)
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

# **get_models_api_v1_audio_models_get**
> object get_models_api_v1_audio_models_get()

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
    api_instance = openwebui_client.AudioApi(api_client)

    try:
        # Get Models
        api_response = await api_instance.get_models_api_v1_audio_models_get()
        print("The response of AudioApi->get_models_api_v1_audio_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudioApi->get_models_api_v1_audio_models_get: %s\n" % e)
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

# **get_voices_api_v1_audio_voices_get**
> object get_voices_api_v1_audio_voices_get()

Get Voices

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
    api_instance = openwebui_client.AudioApi(api_client)

    try:
        # Get Voices
        api_response = await api_instance.get_voices_api_v1_audio_voices_get()
        print("The response of AudioApi->get_voices_api_v1_audio_voices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudioApi->get_voices_api_v1_audio_voices_get: %s\n" % e)
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

# **speech_api_v1_audio_speech_post**
> object speech_api_v1_audio_speech_post()

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
    api_instance = openwebui_client.AudioApi(api_client)

    try:
        # Speech
        api_response = await api_instance.speech_api_v1_audio_speech_post()
        print("The response of AudioApi->speech_api_v1_audio_speech_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudioApi->speech_api_v1_audio_speech_post: %s\n" % e)
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

# **transcription_api_v1_audio_transcriptions_post**
> object transcription_api_v1_audio_transcriptions_post(file, language=language)

Transcription

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
    api_instance = openwebui_client.AudioApi(api_client)
    file = 'file_example' # str | 
    language = 'language_example' # str |  (optional)

    try:
        # Transcription
        api_response = await api_instance.transcription_api_v1_audio_transcriptions_post(file, language=language)
        print("The response of AudioApi->transcription_api_v1_audio_transcriptions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudioApi->transcription_api_v1_audio_transcriptions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **language** | **str**|  | [optional] 

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

# **update_audio_config_api_v1_audio_config_update_post**
> object update_audio_config_api_v1_audio_config_update_post(audio_config_update_form)

Update Audio Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.audio_config_update_form import AudioConfigUpdateForm
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
    api_instance = openwebui_client.AudioApi(api_client)
    audio_config_update_form = openwebui_client.AudioConfigUpdateForm() # AudioConfigUpdateForm | 

    try:
        # Update Audio Config
        api_response = await api_instance.update_audio_config_api_v1_audio_config_update_post(audio_config_update_form)
        print("The response of AudioApi->update_audio_config_api_v1_audio_config_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudioApi->update_audio_config_api_v1_audio_config_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audio_config_update_form** | [**AudioConfigUpdateForm**](AudioConfigUpdateForm.md)|  | 

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

