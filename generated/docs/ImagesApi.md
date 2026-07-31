# openwebui_client.ImagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_images_api_v1_images_edit_post**](ImagesApi.md#edit_images_api_v1_images_edit_post) | **POST** /api/v1/images/edit | Edit Images
[**generate_images_api_v1_images_generations_post**](ImagesApi.md#generate_images_api_v1_images_generations_post) | **POST** /api/v1/images/generations | Generate Images
[**get_config_api_v1_images_config_get**](ImagesApi.md#get_config_api_v1_images_config_get) | **GET** /api/v1/images/config | Get Config
[**get_models_api_v1_images_models_get**](ImagesApi.md#get_models_api_v1_images_models_get) | **GET** /api/v1/images/models | Get Models
[**update_config_api_v1_images_config_update_post**](ImagesApi.md#update_config_api_v1_images_config_update_post) | **POST** /api/v1/images/config/update | Update Config
[**verify_url_api_v1_images_config_url_verify_get**](ImagesApi.md#verify_url_api_v1_images_config_url_verify_get) | **GET** /api/v1/images/config/url/verify | Verify Url


# **edit_images_api_v1_images_edit_post**
> object edit_images_api_v1_images_edit_post(edit_image_form)

Edit Images

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.edit_image_form import EditImageForm
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
    api_instance = openwebui_client.ImagesApi(api_client)
    edit_image_form = openwebui_client.EditImageForm() # EditImageForm | 

    try:
        # Edit Images
        api_response = await api_instance.edit_images_api_v1_images_edit_post(edit_image_form)
        print("The response of ImagesApi->edit_images_api_v1_images_edit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->edit_images_api_v1_images_edit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_image_form** | [**EditImageForm**](EditImageForm.md)|  | 

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

# **generate_images_api_v1_images_generations_post**
> object generate_images_api_v1_images_generations_post(create_image_form)

Generate Images

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.create_image_form import CreateImageForm
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
    api_instance = openwebui_client.ImagesApi(api_client)
    create_image_form = openwebui_client.CreateImageForm() # CreateImageForm | 

    try:
        # Generate Images
        api_response = await api_instance.generate_images_api_v1_images_generations_post(create_image_form)
        print("The response of ImagesApi->generate_images_api_v1_images_generations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->generate_images_api_v1_images_generations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_image_form** | [**CreateImageForm**](CreateImageForm.md)|  | 

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

# **get_config_api_v1_images_config_get**
> ImagesConfig get_config_api_v1_images_config_get()

Get Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.images_config import ImagesConfig
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
    api_instance = openwebui_client.ImagesApi(api_client)

    try:
        # Get Config
        api_response = await api_instance.get_config_api_v1_images_config_get()
        print("The response of ImagesApi->get_config_api_v1_images_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->get_config_api_v1_images_config_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ImagesConfig**](ImagesConfig.md)

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

# **get_models_api_v1_images_models_get**
> object get_models_api_v1_images_models_get()

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
    api_instance = openwebui_client.ImagesApi(api_client)

    try:
        # Get Models
        api_response = await api_instance.get_models_api_v1_images_models_get()
        print("The response of ImagesApi->get_models_api_v1_images_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->get_models_api_v1_images_models_get: %s\n" % e)
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

# **update_config_api_v1_images_config_update_post**
> object update_config_api_v1_images_config_update_post(images_config)

Update Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.images_config import ImagesConfig
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
    api_instance = openwebui_client.ImagesApi(api_client)
    images_config = openwebui_client.ImagesConfig() # ImagesConfig | 

    try:
        # Update Config
        api_response = await api_instance.update_config_api_v1_images_config_update_post(images_config)
        print("The response of ImagesApi->update_config_api_v1_images_config_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->update_config_api_v1_images_config_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **images_config** | [**ImagesConfig**](ImagesConfig.md)|  | 

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

# **verify_url_api_v1_images_config_url_verify_get**
> object verify_url_api_v1_images_config_url_verify_get()

Verify Url

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
    api_instance = openwebui_client.ImagesApi(api_client)

    try:
        # Verify Url
        api_response = await api_instance.verify_url_api_v1_images_config_url_verify_get()
        print("The response of ImagesApi->verify_url_api_v1_images_config_url_verify_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->verify_url_api_v1_images_config_url_verify_get: %s\n" % e)
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

