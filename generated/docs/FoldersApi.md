# openwebui_client.FoldersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_folder_api_v1_folders_post**](FoldersApi.md#create_folder_api_v1_folders_post) | **POST** /api/v1/folders/ | Create Folder
[**delete_folder_by_id_api_v1_folders_id_delete**](FoldersApi.md#delete_folder_by_id_api_v1_folders_id_delete) | **DELETE** /api/v1/folders/{id} | Delete Folder By Id
[**get_folder_by_id_api_v1_folders_id_get**](FoldersApi.md#get_folder_by_id_api_v1_folders_id_get) | **GET** /api/v1/folders/{id} | Get Folder By Id
[**get_folders_api_v1_folders_get**](FoldersApi.md#get_folders_api_v1_folders_get) | **GET** /api/v1/folders/ | Get Folders
[**get_shared_folder_chats_api_v1_folders_id_shared_chats_get**](FoldersApi.md#get_shared_folder_chats_api_v1_folders_id_shared_chats_get) | **GET** /api/v1/folders/{id}/shared/chats | Get Shared Folder Chats
[**get_shared_folders_api_v1_folders_shared_get**](FoldersApi.md#get_shared_folders_api_v1_folders_shared_get) | **GET** /api/v1/folders/shared | Get Shared Folders
[**mark_folder_chats_read_by_id_api_v1_folders_id_read_post**](FoldersApi.md#mark_folder_chats_read_by_id_api_v1_folders_id_read_post) | **POST** /api/v1/folders/{id}/read | Mark Folder Chats Read By Id
[**update_folder_access_by_id_api_v1_folders_id_access_update_post**](FoldersApi.md#update_folder_access_by_id_api_v1_folders_id_access_update_post) | **POST** /api/v1/folders/{id}/access/update | Update Folder Access By Id
[**update_folder_is_expanded_by_id_api_v1_folders_id_update_expanded_post**](FoldersApi.md#update_folder_is_expanded_by_id_api_v1_folders_id_update_expanded_post) | **POST** /api/v1/folders/{id}/update/expanded | Update Folder Is Expanded By Id
[**update_folder_name_by_id_api_v1_folders_id_update_post**](FoldersApi.md#update_folder_name_by_id_api_v1_folders_id_update_post) | **POST** /api/v1/folders/{id}/update | Update Folder Name By Id
[**update_folder_parent_id_by_id_api_v1_folders_id_update_parent_post**](FoldersApi.md#update_folder_parent_id_by_id_api_v1_folders_id_update_parent_post) | **POST** /api/v1/folders/{id}/update/parent | Update Folder Parent Id By Id


# **create_folder_api_v1_folders_post**
> object create_folder_api_v1_folders_post(folder_form)

Create Folder

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.folder_form import FolderForm
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
    api_instance = openwebui_client.FoldersApi(api_client)
    folder_form = openwebui_client.FolderForm() # FolderForm | 

    try:
        # Create Folder
        api_response = await api_instance.create_folder_api_v1_folders_post(folder_form)
        print("The response of FoldersApi->create_folder_api_v1_folders_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->create_folder_api_v1_folders_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_form** | [**FolderForm**](FolderForm.md)|  | 

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

# **delete_folder_by_id_api_v1_folders_id_delete**
> object delete_folder_by_id_api_v1_folders_id_delete(id, delete_contents=delete_contents)

Delete Folder By Id

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
    api_instance = openwebui_client.FoldersApi(api_client)
    id = 'id_example' # str | 
    delete_contents = True # bool |  (optional)

    try:
        # Delete Folder By Id
        api_response = await api_instance.delete_folder_by_id_api_v1_folders_id_delete(id, delete_contents=delete_contents)
        print("The response of FoldersApi->delete_folder_by_id_api_v1_folders_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->delete_folder_by_id_api_v1_folders_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **delete_contents** | **bool**|  | [optional] 

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

# **get_folder_by_id_api_v1_folders_id_get**
> object get_folder_by_id_api_v1_folders_id_get(id)

Get Folder By Id

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
    api_instance = openwebui_client.FoldersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Folder By Id
        api_response = await api_instance.get_folder_by_id_api_v1_folders_id_get(id)
        print("The response of FoldersApi->get_folder_by_id_api_v1_folders_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_folder_by_id_api_v1_folders_id_get: %s\n" % e)
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

# **get_folders_api_v1_folders_get**
> List[FolderNameIdResponse] get_folders_api_v1_folders_get()

Get Folders

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.folder_name_id_response import FolderNameIdResponse
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
    api_instance = openwebui_client.FoldersApi(api_client)

    try:
        # Get Folders
        api_response = await api_instance.get_folders_api_v1_folders_get()
        print("The response of FoldersApi->get_folders_api_v1_folders_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_folders_api_v1_folders_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FolderNameIdResponse]**](FolderNameIdResponse.md)

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

# **get_shared_folder_chats_api_v1_folders_id_shared_chats_get**
> object get_shared_folder_chats_api_v1_folders_id_shared_chats_get(id, page=page, sort_by=sort_by, sort_dir=sort_dir)

Get Shared Folder Chats

Get chats within a shared folder. Returns readonly flag based on permission.

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
    api_instance = openwebui_client.FoldersApi(api_client)
    id = 'id_example' # str | 
    page = 56 # int |  (optional)
    sort_by = 'unread_updated_at' # str |  (optional) (default to 'unread_updated_at')
    sort_dir = 'desc' # str |  (optional) (default to 'desc')

    try:
        # Get Shared Folder Chats
        api_response = await api_instance.get_shared_folder_chats_api_v1_folders_id_shared_chats_get(id, page=page, sort_by=sort_by, sort_dir=sort_dir)
        print("The response of FoldersApi->get_shared_folder_chats_api_v1_folders_id_shared_chats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_shared_folder_chats_api_v1_folders_id_shared_chats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **page** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;unread_updated_at&#39;]
 **sort_dir** | **str**|  | [optional] [default to &#39;desc&#39;]

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

# **get_shared_folders_api_v1_folders_shared_get**
> object get_shared_folders_api_v1_folders_shared_get()

Get Shared Folders

Get all folders shared with the current user (not owned by them).

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
    api_instance = openwebui_client.FoldersApi(api_client)

    try:
        # Get Shared Folders
        api_response = await api_instance.get_shared_folders_api_v1_folders_shared_get()
        print("The response of FoldersApi->get_shared_folders_api_v1_folders_shared_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_shared_folders_api_v1_folders_shared_get: %s\n" % e)
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

# **mark_folder_chats_read_by_id_api_v1_folders_id_read_post**
> object mark_folder_chats_read_by_id_api_v1_folders_id_read_post(id)

Mark Folder Chats Read By Id

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
    api_instance = openwebui_client.FoldersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Mark Folder Chats Read By Id
        api_response = await api_instance.mark_folder_chats_read_by_id_api_v1_folders_id_read_post(id)
        print("The response of FoldersApi->mark_folder_chats_read_by_id_api_v1_folders_id_read_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->mark_folder_chats_read_by_id_api_v1_folders_id_read_post: %s\n" % e)
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

# **update_folder_access_by_id_api_v1_folders_id_access_update_post**
> object update_folder_access_by_id_api_v1_folders_id_access_update_post(id, folder_access_grants_form)

Update Folder Access By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.folder_access_grants_form import FolderAccessGrantsForm
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
    api_instance = openwebui_client.FoldersApi(api_client)
    id = 'id_example' # str | 
    folder_access_grants_form = openwebui_client.FolderAccessGrantsForm() # FolderAccessGrantsForm | 

    try:
        # Update Folder Access By Id
        api_response = await api_instance.update_folder_access_by_id_api_v1_folders_id_access_update_post(id, folder_access_grants_form)
        print("The response of FoldersApi->update_folder_access_by_id_api_v1_folders_id_access_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->update_folder_access_by_id_api_v1_folders_id_access_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **folder_access_grants_form** | [**FolderAccessGrantsForm**](FolderAccessGrantsForm.md)|  | 

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

# **update_folder_is_expanded_by_id_api_v1_folders_id_update_expanded_post**
> object update_folder_is_expanded_by_id_api_v1_folders_id_update_expanded_post(id, folder_is_expanded_form)

Update Folder Is Expanded By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.folder_is_expanded_form import FolderIsExpandedForm
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
    api_instance = openwebui_client.FoldersApi(api_client)
    id = 'id_example' # str | 
    folder_is_expanded_form = openwebui_client.FolderIsExpandedForm() # FolderIsExpandedForm | 

    try:
        # Update Folder Is Expanded By Id
        api_response = await api_instance.update_folder_is_expanded_by_id_api_v1_folders_id_update_expanded_post(id, folder_is_expanded_form)
        print("The response of FoldersApi->update_folder_is_expanded_by_id_api_v1_folders_id_update_expanded_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->update_folder_is_expanded_by_id_api_v1_folders_id_update_expanded_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **folder_is_expanded_form** | [**FolderIsExpandedForm**](FolderIsExpandedForm.md)|  | 

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

# **update_folder_name_by_id_api_v1_folders_id_update_post**
> object update_folder_name_by_id_api_v1_folders_id_update_post(id, folder_update_form)

Update Folder Name By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.folder_update_form import FolderUpdateForm
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
    api_instance = openwebui_client.FoldersApi(api_client)
    id = 'id_example' # str | 
    folder_update_form = openwebui_client.FolderUpdateForm() # FolderUpdateForm | 

    try:
        # Update Folder Name By Id
        api_response = await api_instance.update_folder_name_by_id_api_v1_folders_id_update_post(id, folder_update_form)
        print("The response of FoldersApi->update_folder_name_by_id_api_v1_folders_id_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->update_folder_name_by_id_api_v1_folders_id_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **folder_update_form** | [**FolderUpdateForm**](FolderUpdateForm.md)|  | 

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

# **update_folder_parent_id_by_id_api_v1_folders_id_update_parent_post**
> object update_folder_parent_id_by_id_api_v1_folders_id_update_parent_post(id, folder_parent_id_form)

Update Folder Parent Id By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.folder_parent_id_form import FolderParentIdForm
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
    api_instance = openwebui_client.FoldersApi(api_client)
    id = 'id_example' # str | 
    folder_parent_id_form = openwebui_client.FolderParentIdForm() # FolderParentIdForm | 

    try:
        # Update Folder Parent Id By Id
        api_response = await api_instance.update_folder_parent_id_by_id_api_v1_folders_id_update_parent_post(id, folder_parent_id_form)
        print("The response of FoldersApi->update_folder_parent_id_by_id_api_v1_folders_id_update_parent_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->update_folder_parent_id_by_id_api_v1_folders_id_update_parent_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **folder_parent_id_form** | [**FolderParentIdForm**](FolderParentIdForm.md)|  | 

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

