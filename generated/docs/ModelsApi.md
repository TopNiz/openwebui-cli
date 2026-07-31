# openwebui_client.ModelsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_model_api_v1_models_create_post**](ModelsApi.md#create_new_model_api_v1_models_create_post) | **POST** /api/v1/models/create | Create New Model
[**delete_all_models_api_v1_models_delete_all_delete**](ModelsApi.md#delete_all_models_api_v1_models_delete_all_delete) | **DELETE** /api/v1/models/delete/all | Delete All Models
[**delete_model_by_id_api_v1_models_model_delete_post**](ModelsApi.md#delete_model_by_id_api_v1_models_model_delete_post) | **POST** /api/v1/models/model/delete | Delete Model By Id
[**export_models_api_v1_models_export_get**](ModelsApi.md#export_models_api_v1_models_export_get) | **GET** /api/v1/models/export | Export Models
[**get_base_model_tags_api_v1_models_base_tags_get**](ModelsApi.md#get_base_model_tags_api_v1_models_base_tags_get) | **GET** /api/v1/models/base/tags | Get Base Model Tags
[**get_base_models_api_v1_models_base_get**](ModelsApi.md#get_base_models_api_v1_models_base_get) | **GET** /api/v1/models/base | Get Base Models
[**get_model_by_id_api_v1_models_model_get**](ModelsApi.md#get_model_by_id_api_v1_models_model_get) | **GET** /api/v1/models/model | Get Model By Id
[**get_model_profile_image_api_v1_models_model_profile_image_get**](ModelsApi.md#get_model_profile_image_api_v1_models_model_profile_image_get) | **GET** /api/v1/models/model/profile/image | Get Model Profile Image
[**get_model_tags_api_v1_models_tags_get**](ModelsApi.md#get_model_tags_api_v1_models_tags_get) | **GET** /api/v1/models/tags | Get Model Tags
[**get_models_api_v1_models_list_get**](ModelsApi.md#get_models_api_v1_models_list_get) | **GET** /api/v1/models/list | Get Models
[**import_models_api_v1_models_import_post**](ModelsApi.md#import_models_api_v1_models_import_post) | **POST** /api/v1/models/import | Import Models
[**sync_models_api_v1_models_sync_post**](ModelsApi.md#sync_models_api_v1_models_sync_post) | **POST** /api/v1/models/sync | Sync Models
[**toggle_model_by_id_api_v1_models_model_toggle_post**](ModelsApi.md#toggle_model_by_id_api_v1_models_model_toggle_post) | **POST** /api/v1/models/model/toggle | Toggle Model By Id
[**update_model_access_by_id_api_v1_models_model_access_update_post**](ModelsApi.md#update_model_access_by_id_api_v1_models_model_access_update_post) | **POST** /api/v1/models/model/access/update | Update Model Access By Id
[**update_model_by_id_api_v1_models_model_update_post**](ModelsApi.md#update_model_by_id_api_v1_models_model_update_post) | **POST** /api/v1/models/model/update | Update Model By Id


# **create_new_model_api_v1_models_create_post**
> ModelModel create_new_model_api_v1_models_create_post(model_form)

Create New Model

Create a new workspace model entry.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.model_form import ModelForm
from openwebui_client.models.model_model import ModelModel
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
    api_instance = openwebui_client.ModelsApi(api_client)
    model_form = openwebui_client.ModelForm() # ModelForm | 

    try:
        # Create New Model
        api_response = await api_instance.create_new_model_api_v1_models_create_post(model_form)
        print("The response of ModelsApi->create_new_model_api_v1_models_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->create_new_model_api_v1_models_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_form** | [**ModelForm**](ModelForm.md)|  | 

### Return type

[**ModelModel**](ModelModel.md)

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

# **delete_all_models_api_v1_models_delete_all_delete**
> bool delete_all_models_api_v1_models_delete_all_delete()

Delete All Models

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
    api_instance = openwebui_client.ModelsApi(api_client)

    try:
        # Delete All Models
        api_response = await api_instance.delete_all_models_api_v1_models_delete_all_delete()
        print("The response of ModelsApi->delete_all_models_api_v1_models_delete_all_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->delete_all_models_api_v1_models_delete_all_delete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model_by_id_api_v1_models_model_delete_post**
> bool delete_model_by_id_api_v1_models_model_delete_post(model_id_form)

Delete Model By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.model_id_form import ModelIdForm
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
    api_instance = openwebui_client.ModelsApi(api_client)
    model_id_form = openwebui_client.ModelIdForm() # ModelIdForm | 

    try:
        # Delete Model By Id
        api_response = await api_instance.delete_model_by_id_api_v1_models_model_delete_post(model_id_form)
        print("The response of ModelsApi->delete_model_by_id_api_v1_models_model_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->delete_model_by_id_api_v1_models_model_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id_form** | [**ModelIdForm**](ModelIdForm.md)|  | 

### Return type

**bool**

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

# **export_models_api_v1_models_export_get**
> List[ModelModel] export_models_api_v1_models_export_get()

Export Models

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.model_model import ModelModel
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
    api_instance = openwebui_client.ModelsApi(api_client)

    try:
        # Export Models
        api_response = await api_instance.export_models_api_v1_models_export_get()
        print("The response of ModelsApi->export_models_api_v1_models_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->export_models_api_v1_models_export_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ModelModel]**](ModelModel.md)

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

# **get_base_model_tags_api_v1_models_base_tags_get**
> List[Optional[str]] get_base_model_tags_api_v1_models_base_tags_get()

Get Base Model Tags

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
    api_instance = openwebui_client.ModelsApi(api_client)

    try:
        # Get Base Model Tags
        api_response = await api_instance.get_base_model_tags_api_v1_models_base_tags_get()
        print("The response of ModelsApi->get_base_model_tags_api_v1_models_base_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_base_model_tags_api_v1_models_base_tags_get: %s\n" % e)
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

# **get_base_models_api_v1_models_base_get**
> List[ModelResponse] get_base_models_api_v1_models_base_get(tag=tag)

Get Base Models

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.model_response import ModelResponse
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
    api_instance = openwebui_client.ModelsApi(api_client)
    tag = 'tag_example' # str |  (optional)

    try:
        # Get Base Models
        api_response = await api_instance.get_base_models_api_v1_models_base_get(tag=tag)
        print("The response of ModelsApi->get_base_models_api_v1_models_base_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_base_models_api_v1_models_base_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**|  | [optional] 

### Return type

[**List[ModelResponse]**](ModelResponse.md)

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

# **get_model_by_id_api_v1_models_model_get**
> ModelAccessResponse get_model_by_id_api_v1_models_model_get(id)

Get Model By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.model_access_response import ModelAccessResponse
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
    api_instance = openwebui_client.ModelsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Model By Id
        api_response = await api_instance.get_model_by_id_api_v1_models_model_get(id)
        print("The response of ModelsApi->get_model_by_id_api_v1_models_model_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_model_by_id_api_v1_models_model_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ModelAccessResponse**](ModelAccessResponse.md)

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

# **get_model_profile_image_api_v1_models_model_profile_image_get**
> object get_model_profile_image_api_v1_models_model_profile_image_get(id)

Get Model Profile Image

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
    api_instance = openwebui_client.ModelsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Model Profile Image
        api_response = await api_instance.get_model_profile_image_api_v1_models_model_profile_image_get(id)
        print("The response of ModelsApi->get_model_profile_image_api_v1_models_model_profile_image_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_model_profile_image_api_v1_models_model_profile_image_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **get_model_tags_api_v1_models_tags_get**
> List[Optional[str]] get_model_tags_api_v1_models_tags_get()

Get Model Tags

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
    api_instance = openwebui_client.ModelsApi(api_client)

    try:
        # Get Model Tags
        api_response = await api_instance.get_model_tags_api_v1_models_tags_get()
        print("The response of ModelsApi->get_model_tags_api_v1_models_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_model_tags_api_v1_models_tags_get: %s\n" % e)
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

# **get_models_api_v1_models_list_get**
> ModelAccessListResponse get_models_api_v1_models_list_get(query=query, view_option=view_option, tag=tag, order_by=order_by, direction=direction, page=page)

Get Models

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.model_access_list_response import ModelAccessListResponse
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
    api_instance = openwebui_client.ModelsApi(api_client)
    query = 'query_example' # str |  (optional)
    view_option = 'view_option_example' # str |  (optional)
    tag = 'tag_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    direction = 'direction_example' # str |  (optional)
    page = 56 # int |  (optional)

    try:
        # Get Models
        api_response = await api_instance.get_models_api_v1_models_list_get(query=query, view_option=view_option, tag=tag, order_by=order_by, direction=direction, page=page)
        print("The response of ModelsApi->get_models_api_v1_models_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_models_api_v1_models_list_get: %s\n" % e)
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

[**ModelAccessListResponse**](ModelAccessListResponse.md)

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

# **import_models_api_v1_models_import_post**
> bool import_models_api_v1_models_import_post(models_import_form)

Import Models

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.models_import_form import ModelsImportForm
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
    api_instance = openwebui_client.ModelsApi(api_client)
    models_import_form = openwebui_client.ModelsImportForm() # ModelsImportForm | 

    try:
        # Import Models
        api_response = await api_instance.import_models_api_v1_models_import_post(models_import_form)
        print("The response of ModelsApi->import_models_api_v1_models_import_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->import_models_api_v1_models_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **models_import_form** | [**ModelsImportForm**](ModelsImportForm.md)|  | 

### Return type

**bool**

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

# **sync_models_api_v1_models_sync_post**
> List[ModelModel] sync_models_api_v1_models_sync_post(sync_models_form)

Sync Models

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.model_model import ModelModel
from openwebui_client.models.sync_models_form import SyncModelsForm
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
    api_instance = openwebui_client.ModelsApi(api_client)
    sync_models_form = openwebui_client.SyncModelsForm() # SyncModelsForm | 

    try:
        # Sync Models
        api_response = await api_instance.sync_models_api_v1_models_sync_post(sync_models_form)
        print("The response of ModelsApi->sync_models_api_v1_models_sync_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->sync_models_api_v1_models_sync_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_models_form** | [**SyncModelsForm**](SyncModelsForm.md)|  | 

### Return type

[**List[ModelModel]**](ModelModel.md)

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

# **toggle_model_by_id_api_v1_models_model_toggle_post**
> ModelResponse toggle_model_by_id_api_v1_models_model_toggle_post(id)

Toggle Model By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.model_response import ModelResponse
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
    api_instance = openwebui_client.ModelsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Toggle Model By Id
        api_response = await api_instance.toggle_model_by_id_api_v1_models_model_toggle_post(id)
        print("The response of ModelsApi->toggle_model_by_id_api_v1_models_model_toggle_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->toggle_model_by_id_api_v1_models_model_toggle_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ModelResponse**](ModelResponse.md)

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

# **update_model_access_by_id_api_v1_models_model_access_update_post**
> ModelModel update_model_access_by_id_api_v1_models_model_access_update_post(model_access_grants_form)

Update Model Access By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.model_access_grants_form import ModelAccessGrantsForm
from openwebui_client.models.model_model import ModelModel
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
    api_instance = openwebui_client.ModelsApi(api_client)
    model_access_grants_form = openwebui_client.ModelAccessGrantsForm() # ModelAccessGrantsForm | 

    try:
        # Update Model Access By Id
        api_response = await api_instance.update_model_access_by_id_api_v1_models_model_access_update_post(model_access_grants_form)
        print("The response of ModelsApi->update_model_access_by_id_api_v1_models_model_access_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->update_model_access_by_id_api_v1_models_model_access_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_access_grants_form** | [**ModelAccessGrantsForm**](ModelAccessGrantsForm.md)|  | 

### Return type

[**ModelModel**](ModelModel.md)

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

# **update_model_by_id_api_v1_models_model_update_post**
> ModelModel update_model_by_id_api_v1_models_model_update_post(model_form)

Update Model By Id

Update a workspace model's configuration.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.model_form import ModelForm
from openwebui_client.models.model_model import ModelModel
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
    api_instance = openwebui_client.ModelsApi(api_client)
    model_form = openwebui_client.ModelForm() # ModelForm | 

    try:
        # Update Model By Id
        api_response = await api_instance.update_model_by_id_api_v1_models_model_update_post(model_form)
        print("The response of ModelsApi->update_model_by_id_api_v1_models_model_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->update_model_by_id_api_v1_models_model_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_form** | [**ModelForm**](ModelForm.md)|  | 

### Return type

[**ModelModel**](ModelModel.md)

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

