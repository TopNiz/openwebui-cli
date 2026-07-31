# openwebui_client.NotesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_note_api_v1_notes_create_post**](NotesApi.md#create_new_note_api_v1_notes_create_post) | **POST** /api/v1/notes/create | Create New Note
[**create_note_chat_by_id_api_v1_notes_id_chat_post**](NotesApi.md#create_note_chat_by_id_api_v1_notes_id_chat_post) | **POST** /api/v1/notes/{id}/chat | Create Note Chat By Id
[**delete_note_by_id_api_v1_notes_id_delete_delete**](NotesApi.md#delete_note_by_id_api_v1_notes_id_delete_delete) | **DELETE** /api/v1/notes/{id}/delete | Delete Note By Id
[**get_note_by_id_api_v1_notes_id_get**](NotesApi.md#get_note_by_id_api_v1_notes_id_get) | **GET** /api/v1/notes/{id} | Get Note By Id
[**get_note_chat_by_id_api_v1_notes_id_chat_get**](NotesApi.md#get_note_chat_by_id_api_v1_notes_id_chat_get) | **GET** /api/v1/notes/{id}/chat | Get Note Chat By Id
[**get_note_chats_by_id_api_v1_notes_id_chats_get**](NotesApi.md#get_note_chats_by_id_api_v1_notes_id_chats_get) | **GET** /api/v1/notes/{id}/chats | Get Note Chats By Id
[**get_notes_api_v1_notes_get**](NotesApi.md#get_notes_api_v1_notes_get) | **GET** /api/v1/notes/ | Get Notes
[**get_pinned_notes_api_v1_notes_pinned_get**](NotesApi.md#get_pinned_notes_api_v1_notes_pinned_get) | **GET** /api/v1/notes/pinned | Get Pinned Notes
[**pin_note_by_id_api_v1_notes_id_pin_post**](NotesApi.md#pin_note_by_id_api_v1_notes_id_pin_post) | **POST** /api/v1/notes/{id}/pin | Pin Note By Id
[**search_notes_api_v1_notes_search_get**](NotesApi.md#search_notes_api_v1_notes_search_get) | **GET** /api/v1/notes/search | Search Notes
[**update_note_access_by_id_api_v1_notes_id_access_update_post**](NotesApi.md#update_note_access_by_id_api_v1_notes_id_access_update_post) | **POST** /api/v1/notes/{id}/access/update | Update Note Access By Id
[**update_note_by_id_api_v1_notes_id_update_post**](NotesApi.md#update_note_by_id_api_v1_notes_id_update_post) | **POST** /api/v1/notes/{id}/update | Update Note By Id


# **create_new_note_api_v1_notes_create_post**
> NoteModel create_new_note_api_v1_notes_create_post(note_form)

Create New Note

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.note_form import NoteForm
from openwebui_client.models.note_model import NoteModel
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
    api_instance = openwebui_client.NotesApi(api_client)
    note_form = openwebui_client.NoteForm() # NoteForm | 

    try:
        # Create New Note
        api_response = await api_instance.create_new_note_api_v1_notes_create_post(note_form)
        print("The response of NotesApi->create_new_note_api_v1_notes_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->create_new_note_api_v1_notes_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_form** | [**NoteForm**](NoteForm.md)|  | 

### Return type

[**NoteModel**](NoteModel.md)

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

# **create_note_chat_by_id_api_v1_notes_id_chat_post**
> ChatResponse create_note_chat_by_id_api_v1_notes_id_chat_post(id)

Create Note Chat By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_response import ChatResponse
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
    api_instance = openwebui_client.NotesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Create Note Chat By Id
        api_response = await api_instance.create_note_chat_by_id_api_v1_notes_id_chat_post(id)
        print("The response of NotesApi->create_note_chat_by_id_api_v1_notes_id_chat_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->create_note_chat_by_id_api_v1_notes_id_chat_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ChatResponse**](ChatResponse.md)

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

# **delete_note_by_id_api_v1_notes_id_delete_delete**
> bool delete_note_by_id_api_v1_notes_id_delete_delete(id)

Delete Note By Id

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
    api_instance = openwebui_client.NotesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Note By Id
        api_response = await api_instance.delete_note_by_id_api_v1_notes_id_delete_delete(id)
        print("The response of NotesApi->delete_note_by_id_api_v1_notes_id_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->delete_note_by_id_api_v1_notes_id_delete_delete: %s\n" % e)
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

# **get_note_by_id_api_v1_notes_id_get**
> NoteResponse get_note_by_id_api_v1_notes_id_get(id)

Get Note By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.note_response import NoteResponse
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
    api_instance = openwebui_client.NotesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Note By Id
        api_response = await api_instance.get_note_by_id_api_v1_notes_id_get(id)
        print("The response of NotesApi->get_note_by_id_api_v1_notes_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->get_note_by_id_api_v1_notes_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**NoteResponse**](NoteResponse.md)

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

# **get_note_chat_by_id_api_v1_notes_id_chat_get**
> ChatResponse get_note_chat_by_id_api_v1_notes_id_chat_get(id)

Get Note Chat By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_response import ChatResponse
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
    api_instance = openwebui_client.NotesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Note Chat By Id
        api_response = await api_instance.get_note_chat_by_id_api_v1_notes_id_chat_get(id)
        print("The response of NotesApi->get_note_chat_by_id_api_v1_notes_id_chat_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->get_note_chat_by_id_api_v1_notes_id_chat_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ChatResponse**](ChatResponse.md)

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

# **get_note_chats_by_id_api_v1_notes_id_chats_get**
> List[Optional[ChatResponse]] get_note_chats_by_id_api_v1_notes_id_chats_get(id)

Get Note Chats By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_response import ChatResponse
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
    api_instance = openwebui_client.NotesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Note Chats By Id
        api_response = await api_instance.get_note_chats_by_id_api_v1_notes_id_chats_get(id)
        print("The response of NotesApi->get_note_chats_by_id_api_v1_notes_id_chats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->get_note_chats_by_id_api_v1_notes_id_chats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[Optional[ChatResponse]]**](ChatResponse.md)

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

# **get_notes_api_v1_notes_get**
> List[NoteItemResponse] get_notes_api_v1_notes_get(page=page)

Get Notes

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.note_item_response import NoteItemResponse
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
    api_instance = openwebui_client.NotesApi(api_client)
    page = 56 # int |  (optional)

    try:
        # Get Notes
        api_response = await api_instance.get_notes_api_v1_notes_get(page=page)
        print("The response of NotesApi->get_notes_api_v1_notes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->get_notes_api_v1_notes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 

### Return type

[**List[NoteItemResponse]**](NoteItemResponse.md)

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

# **get_pinned_notes_api_v1_notes_pinned_get**
> List[NoteItemResponse] get_pinned_notes_api_v1_notes_pinned_get()

Get Pinned Notes

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.note_item_response import NoteItemResponse
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
    api_instance = openwebui_client.NotesApi(api_client)

    try:
        # Get Pinned Notes
        api_response = await api_instance.get_pinned_notes_api_v1_notes_pinned_get()
        print("The response of NotesApi->get_pinned_notes_api_v1_notes_pinned_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->get_pinned_notes_api_v1_notes_pinned_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[NoteItemResponse]**](NoteItemResponse.md)

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

# **pin_note_by_id_api_v1_notes_id_pin_post**
> NoteModel pin_note_by_id_api_v1_notes_id_pin_post(id)

Pin Note By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.note_model import NoteModel
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
    api_instance = openwebui_client.NotesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Pin Note By Id
        api_response = await api_instance.pin_note_by_id_api_v1_notes_id_pin_post(id)
        print("The response of NotesApi->pin_note_by_id_api_v1_notes_id_pin_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->pin_note_by_id_api_v1_notes_id_pin_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**NoteModel**](NoteModel.md)

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

# **search_notes_api_v1_notes_search_get**
> NoteListResponse search_notes_api_v1_notes_search_get(query=query, view_option=view_option, permission=permission, order_by=order_by, direction=direction, page=page)

Search Notes

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.note_list_response import NoteListResponse
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
    api_instance = openwebui_client.NotesApi(api_client)
    query = 'query_example' # str |  (optional)
    view_option = 'view_option_example' # str |  (optional)
    permission = 'permission_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    direction = 'direction_example' # str |  (optional)
    page = 56 # int |  (optional)

    try:
        # Search Notes
        api_response = await api_instance.search_notes_api_v1_notes_search_get(query=query, view_option=view_option, permission=permission, order_by=order_by, direction=direction, page=page)
        print("The response of NotesApi->search_notes_api_v1_notes_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->search_notes_api_v1_notes_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **view_option** | **str**|  | [optional] 
 **permission** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 

### Return type

[**NoteListResponse**](NoteListResponse.md)

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

# **update_note_access_by_id_api_v1_notes_id_access_update_post**
> NoteModel update_note_access_by_id_api_v1_notes_id_access_update_post(id, note_access_grants_form)

Update Note Access By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.note_access_grants_form import NoteAccessGrantsForm
from openwebui_client.models.note_model import NoteModel
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
    api_instance = openwebui_client.NotesApi(api_client)
    id = 'id_example' # str | 
    note_access_grants_form = openwebui_client.NoteAccessGrantsForm() # NoteAccessGrantsForm | 

    try:
        # Update Note Access By Id
        api_response = await api_instance.update_note_access_by_id_api_v1_notes_id_access_update_post(id, note_access_grants_form)
        print("The response of NotesApi->update_note_access_by_id_api_v1_notes_id_access_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->update_note_access_by_id_api_v1_notes_id_access_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **note_access_grants_form** | [**NoteAccessGrantsForm**](NoteAccessGrantsForm.md)|  | 

### Return type

[**NoteModel**](NoteModel.md)

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

# **update_note_by_id_api_v1_notes_id_update_post**
> NoteModel update_note_by_id_api_v1_notes_id_update_post(id, note_form)

Update Note By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.note_form import NoteForm
from openwebui_client.models.note_model import NoteModel
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
    api_instance = openwebui_client.NotesApi(api_client)
    id = 'id_example' # str | 
    note_form = openwebui_client.NoteForm() # NoteForm | 

    try:
        # Update Note By Id
        api_response = await api_instance.update_note_by_id_api_v1_notes_id_update_post(id, note_form)
        print("The response of NotesApi->update_note_by_id_api_v1_notes_id_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->update_note_by_id_api_v1_notes_id_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **note_form** | [**NoteForm**](NoteForm.md)|  | 

### Return type

[**NoteModel**](NoteModel.md)

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

