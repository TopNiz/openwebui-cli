# openwebui_client.FilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_files_api_v1_files_count_get**](FilesApi.md#count_files_api_v1_files_count_get) | **GET** /api/v1/files/count | Count Files
[**delete_all_files_api_v1_files_all_delete**](FilesApi.md#delete_all_files_api_v1_files_all_delete) | **DELETE** /api/v1/files/all | Delete All Files
[**delete_file_by_id_api_v1_files_id_delete**](FilesApi.md#delete_file_by_id_api_v1_files_id_delete) | **DELETE** /api/v1/files/{id} | Delete File By Id
[**get_file_by_id_api_v1_files_id_get**](FilesApi.md#get_file_by_id_api_v1_files_id_get) | **GET** /api/v1/files/{id} | Get File By Id
[**get_file_content_by_id_api_v1_files_id_content_file_name_get**](FilesApi.md#get_file_content_by_id_api_v1_files_id_content_file_name_get) | **GET** /api/v1/files/{id}/content/{file_name} | Get File Content By Id
[**get_file_content_by_id_api_v1_files_id_content_get**](FilesApi.md#get_file_content_by_id_api_v1_files_id_content_get) | **GET** /api/v1/files/{id}/content | Get File Content By Id
[**get_file_data_content_by_id_api_v1_files_id_data_content_get**](FilesApi.md#get_file_data_content_by_id_api_v1_files_id_data_content_get) | **GET** /api/v1/files/{id}/data/content | Get File Data Content By Id
[**get_file_process_status_api_v1_files_id_process_status_get**](FilesApi.md#get_file_process_status_api_v1_files_id_process_status_get) | **GET** /api/v1/files/{id}/process/status | Get File Process Status
[**get_html_file_content_by_id_api_v1_files_id_content_html_get**](FilesApi.md#get_html_file_content_by_id_api_v1_files_id_content_html_get) | **GET** /api/v1/files/{id}/content/html | Get Html File Content By Id
[**list_files_api_v1_files_get**](FilesApi.md#list_files_api_v1_files_get) | **GET** /api/v1/files/ | List Files
[**rename_file_by_id_api_v1_files_id_rename_post**](FilesApi.md#rename_file_by_id_api_v1_files_id_rename_post) | **POST** /api/v1/files/{id}/rename | Rename File By Id
[**search_files_api_v1_files_search_get**](FilesApi.md#search_files_api_v1_files_search_get) | **GET** /api/v1/files/search | Search Files
[**update_file_data_content_by_id_api_v1_files_id_data_content_update_post**](FilesApi.md#update_file_data_content_by_id_api_v1_files_id_data_content_update_post) | **POST** /api/v1/files/{id}/data/content/update | Update File Data Content By Id
[**upload_file_api_v1_files_post**](FilesApi.md#upload_file_api_v1_files_post) | **POST** /api/v1/files/ | Upload File


# **count_files_api_v1_files_count_get**
> int count_files_api_v1_files_count_get()

Count Files

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
    api_instance = openwebui_client.FilesApi(api_client)

    try:
        # Count Files
        api_response = await api_instance.count_files_api_v1_files_count_get()
        print("The response of FilesApi->count_files_api_v1_files_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->count_files_api_v1_files_count_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**int**

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

# **delete_all_files_api_v1_files_all_delete**
> object delete_all_files_api_v1_files_all_delete()

Delete All Files

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
    api_instance = openwebui_client.FilesApi(api_client)

    try:
        # Delete All Files
        api_response = await api_instance.delete_all_files_api_v1_files_all_delete()
        print("The response of FilesApi->delete_all_files_api_v1_files_all_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->delete_all_files_api_v1_files_all_delete: %s\n" % e)
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

# **delete_file_by_id_api_v1_files_id_delete**
> object delete_file_by_id_api_v1_files_id_delete(id)

Delete File By Id

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
    api_instance = openwebui_client.FilesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete File By Id
        api_response = await api_instance.delete_file_by_id_api_v1_files_id_delete(id)
        print("The response of FilesApi->delete_file_by_id_api_v1_files_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->delete_file_by_id_api_v1_files_id_delete: %s\n" % e)
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

# **get_file_by_id_api_v1_files_id_get**
> FileModel get_file_by_id_api_v1_files_id_get(id)

Get File By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.file_model import FileModel
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
    api_instance = openwebui_client.FilesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get File By Id
        api_response = await api_instance.get_file_by_id_api_v1_files_id_get(id)
        print("The response of FilesApi->get_file_by_id_api_v1_files_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file_by_id_api_v1_files_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FileModel**](FileModel.md)

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

# **get_file_content_by_id_api_v1_files_id_content_file_name_get**
> object get_file_content_by_id_api_v1_files_id_content_file_name_get(id, file_name)

Get File Content By Id

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
    api_instance = openwebui_client.FilesApi(api_client)
    id = 'id_example' # str | 
    file_name = 'file_name_example' # str | 

    try:
        # Get File Content By Id
        api_response = await api_instance.get_file_content_by_id_api_v1_files_id_content_file_name_get(id, file_name)
        print("The response of FilesApi->get_file_content_by_id_api_v1_files_id_content_file_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file_content_by_id_api_v1_files_id_content_file_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **file_name** | **str**|  | 

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

# **get_file_content_by_id_api_v1_files_id_content_get**
> object get_file_content_by_id_api_v1_files_id_content_get(id, attachment=attachment)

Get File Content By Id

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
    api_instance = openwebui_client.FilesApi(api_client)
    id = 'id_example' # str | 
    attachment = False # bool |  (optional) (default to False)

    try:
        # Get File Content By Id
        api_response = await api_instance.get_file_content_by_id_api_v1_files_id_content_get(id, attachment=attachment)
        print("The response of FilesApi->get_file_content_by_id_api_v1_files_id_content_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file_content_by_id_api_v1_files_id_content_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **attachment** | **bool**|  | [optional] [default to False]

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

# **get_file_data_content_by_id_api_v1_files_id_data_content_get**
> object get_file_data_content_by_id_api_v1_files_id_data_content_get(id)

Get File Data Content By Id

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
    api_instance = openwebui_client.FilesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get File Data Content By Id
        api_response = await api_instance.get_file_data_content_by_id_api_v1_files_id_data_content_get(id)
        print("The response of FilesApi->get_file_data_content_by_id_api_v1_files_id_data_content_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file_data_content_by_id_api_v1_files_id_data_content_get: %s\n" % e)
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

# **get_file_process_status_api_v1_files_id_process_status_get**
> object get_file_process_status_api_v1_files_id_process_status_get(id, stream=stream)

Get File Process Status

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
    api_instance = openwebui_client.FilesApi(api_client)
    id = 'id_example' # str | 
    stream = False # bool |  (optional) (default to False)

    try:
        # Get File Process Status
        api_response = await api_instance.get_file_process_status_api_v1_files_id_process_status_get(id, stream=stream)
        print("The response of FilesApi->get_file_process_status_api_v1_files_id_process_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file_process_status_api_v1_files_id_process_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **stream** | **bool**|  | [optional] [default to False]

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

# **get_html_file_content_by_id_api_v1_files_id_content_html_get**
> object get_html_file_content_by_id_api_v1_files_id_content_html_get(id)

Get Html File Content By Id

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
    api_instance = openwebui_client.FilesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Html File Content By Id
        api_response = await api_instance.get_html_file_content_by_id_api_v1_files_id_content_html_get(id)
        print("The response of FilesApi->get_html_file_content_by_id_api_v1_files_id_content_html_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_html_file_content_by_id_api_v1_files_id_content_html_get: %s\n" % e)
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

# **list_files_api_v1_files_get**
> FileListResponse list_files_api_v1_files_get(page=page, content=content)

List Files

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.file_list_response import FileListResponse
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
    api_instance = openwebui_client.FilesApi(api_client)
    page = 1 # int | Page number (1-indexed) (optional) (default to 1)
    content = True # bool |  (optional) (default to True)

    try:
        # List Files
        api_response = await api_instance.list_files_api_v1_files_get(page=page, content=content)
        print("The response of FilesApi->list_files_api_v1_files_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->list_files_api_v1_files_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (1-indexed) | [optional] [default to 1]
 **content** | **bool**|  | [optional] [default to True]

### Return type

[**FileListResponse**](FileListResponse.md)

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

# **rename_file_by_id_api_v1_files_id_rename_post**
> object rename_file_by_id_api_v1_files_id_rename_post(id, file_rename_form)

Rename File By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.file_rename_form import FileRenameForm
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
    api_instance = openwebui_client.FilesApi(api_client)
    id = 'id_example' # str | 
    file_rename_form = openwebui_client.FileRenameForm() # FileRenameForm | 

    try:
        # Rename File By Id
        api_response = await api_instance.rename_file_by_id_api_v1_files_id_rename_post(id, file_rename_form)
        print("The response of FilesApi->rename_file_by_id_api_v1_files_id_rename_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->rename_file_by_id_api_v1_files_id_rename_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **file_rename_form** | [**FileRenameForm**](FileRenameForm.md)|  | 

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

# **search_files_api_v1_files_search_get**
> List[FileModelResponse] search_files_api_v1_files_search_get(filename, content=content, skip=skip, limit=limit)

Search Files

Search for files by filename with support for wildcard patterns.
Uses SQL-based filtering with pagination for better performance.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.file_model_response import FileModelResponse
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
    api_instance = openwebui_client.FilesApi(api_client)
    filename = 'filename_example' # str | Filename pattern to search for. Supports wildcards such as '*.txt'
    content = True # bool |  (optional) (default to True)
    skip = 0 # int | Number of files to skip (optional) (default to 0)
    limit = 100 # int | Maximum number of files to return (optional) (default to 100)

    try:
        # Search Files
        api_response = await api_instance.search_files_api_v1_files_search_get(filename, content=content, skip=skip, limit=limit)
        print("The response of FilesApi->search_files_api_v1_files_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->search_files_api_v1_files_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Filename pattern to search for. Supports wildcards such as &#39;*.txt&#39; | 
 **content** | **bool**|  | [optional] [default to True]
 **skip** | **int**| Number of files to skip | [optional] [default to 0]
 **limit** | **int**| Maximum number of files to return | [optional] [default to 100]

### Return type

[**List[FileModelResponse]**](FileModelResponse.md)

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

# **update_file_data_content_by_id_api_v1_files_id_data_content_update_post**
> object update_file_data_content_by_id_api_v1_files_id_data_content_update_post(id, content_form)

Update File Data Content By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.content_form import ContentForm
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
    api_instance = openwebui_client.FilesApi(api_client)
    id = 'id_example' # str | 
    content_form = openwebui_client.ContentForm() # ContentForm | 

    try:
        # Update File Data Content By Id
        api_response = await api_instance.update_file_data_content_by_id_api_v1_files_id_data_content_update_post(id, content_form)
        print("The response of FilesApi->update_file_data_content_by_id_api_v1_files_id_data_content_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->update_file_data_content_by_id_api_v1_files_id_data_content_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_form** | [**ContentForm**](ContentForm.md)|  | 

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

# **upload_file_api_v1_files_post**
> FileModelResponse upload_file_api_v1_files_post(file, process=process, process_in_background=process_in_background, metadata=metadata)

Upload File

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.file_model_response import FileModelResponse
from openwebui_client.models.metadata import Metadata
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
    api_instance = openwebui_client.FilesApi(api_client)
    file = 'file_example' # str | 
    process = True # bool |  (optional) (default to True)
    process_in_background = True # bool |  (optional) (default to True)
    metadata = openwebui_client.Metadata() # Metadata |  (optional)

    try:
        # Upload File
        api_response = await api_instance.upload_file_api_v1_files_post(file, process=process, process_in_background=process_in_background, metadata=metadata)
        print("The response of FilesApi->upload_file_api_v1_files_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->upload_file_api_v1_files_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 
 **process** | **bool**|  | [optional] [default to True]
 **process_in_background** | **bool**|  | [optional] [default to True]
 **metadata** | [**Metadata**](Metadata.md)|  | [optional] 

### Return type

[**FileModelResponse**](FileModelResponse.md)

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

