# openwebui_client.MemoriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_memory_api_v1_memories_add_post**](MemoriesApi.md#add_memory_api_v1_memories_add_post) | **POST** /api/v1/memories/add | Add Memory
[**delete_memory_by_id_api_v1_memories_memory_id_delete**](MemoriesApi.md#delete_memory_by_id_api_v1_memories_memory_id_delete) | **DELETE** /api/v1/memories/{memory_id} | Delete Memory By Id
[**delete_memory_by_user_id_api_v1_memories_delete_user_delete**](MemoriesApi.md#delete_memory_by_user_id_api_v1_memories_delete_user_delete) | **DELETE** /api/v1/memories/delete/user | Delete Memory By User Id
[**get_memories_api_v1_memories_get**](MemoriesApi.md#get_memories_api_v1_memories_get) | **GET** /api/v1/memories/ | Get Memories
[**list_memory_paths_api_v1_memories_paths_post**](MemoriesApi.md#list_memory_paths_api_v1_memories_paths_post) | **POST** /api/v1/memories/paths | List Memory Paths
[**query_memory_api_v1_memories_query_post**](MemoriesApi.md#query_memory_api_v1_memories_query_post) | **POST** /api/v1/memories/query | Query Memory
[**read_memory_path_api_v1_memories_path_post**](MemoriesApi.md#read_memory_path_api_v1_memories_path_post) | **POST** /api/v1/memories/path | Read Memory Path
[**reset_memory_from_vector_db_api_v1_memories_reset_post**](MemoriesApi.md#reset_memory_from_vector_db_api_v1_memories_reset_post) | **POST** /api/v1/memories/reset | Reset Memory From Vector Db
[**search_memories_api_v1_memories_search_post**](MemoriesApi.md#search_memories_api_v1_memories_search_post) | **POST** /api/v1/memories/search | Search Memories
[**update_memories_api_v1_memories_update_post**](MemoriesApi.md#update_memories_api_v1_memories_update_post) | **POST** /api/v1/memories/update | Update Memories
[**update_memory_by_id_api_v1_memories_memory_id_update_post**](MemoriesApi.md#update_memory_by_id_api_v1_memories_memory_id_update_post) | **POST** /api/v1/memories/{memory_id}/update | Update Memory By Id


# **add_memory_api_v1_memories_add_post**
> MemoryModel add_memory_api_v1_memories_add_post(add_memory_form)

Add Memory

Persist a new memory and embed it into the user's vector collection.

Does NOT use ``Depends(get_async_session)`` — database operations manage their
own short-lived sessions so a connection is not held during the external
embedding API call (``EMBEDDING_FUNCTION``), which can take 1-5+ seconds.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.add_memory_form import AddMemoryForm
from openwebui_client.models.memory_model import MemoryModel
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
    api_instance = openwebui_client.MemoriesApi(api_client)
    add_memory_form = openwebui_client.AddMemoryForm() # AddMemoryForm | 

    try:
        # Add Memory
        api_response = await api_instance.add_memory_api_v1_memories_add_post(add_memory_form)
        print("The response of MemoriesApi->add_memory_api_v1_memories_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->add_memory_api_v1_memories_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_memory_form** | [**AddMemoryForm**](AddMemoryForm.md)|  | 

### Return type

[**MemoryModel**](MemoryModel.md)

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

# **delete_memory_by_id_api_v1_memories_memory_id_delete**
> bool delete_memory_by_id_api_v1_memories_memory_id_delete(memory_id)

Delete Memory By Id

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
    api_instance = openwebui_client.MemoriesApi(api_client)
    memory_id = 'memory_id_example' # str | 

    try:
        # Delete Memory By Id
        api_response = await api_instance.delete_memory_by_id_api_v1_memories_memory_id_delete(memory_id)
        print("The response of MemoriesApi->delete_memory_by_id_api_v1_memories_memory_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->delete_memory_by_id_api_v1_memories_memory_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memory_id** | **str**|  | 

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

# **delete_memory_by_user_id_api_v1_memories_delete_user_delete**
> bool delete_memory_by_user_id_api_v1_memories_delete_user_delete()

Delete Memory By User Id

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
    api_instance = openwebui_client.MemoriesApi(api_client)

    try:
        # Delete Memory By User Id
        api_response = await api_instance.delete_memory_by_user_id_api_v1_memories_delete_user_delete()
        print("The response of MemoriesApi->delete_memory_by_user_id_api_v1_memories_delete_user_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->delete_memory_by_user_id_api_v1_memories_delete_user_delete: %s\n" % e)
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

# **get_memories_api_v1_memories_get**
> List[MemoryModel] get_memories_api_v1_memories_get()

Get Memories

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.memory_model import MemoryModel
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
    api_instance = openwebui_client.MemoriesApi(api_client)

    try:
        # Get Memories
        api_response = await api_instance.get_memories_api_v1_memories_get()
        print("The response of MemoriesApi->get_memories_api_v1_memories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->get_memories_api_v1_memories_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MemoryModel]**](MemoryModel.md)

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

# **list_memory_paths_api_v1_memories_paths_post**
> object list_memory_paths_api_v1_memories_paths_post(list_memory_paths_form)

List Memory Paths

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.list_memory_paths_form import ListMemoryPathsForm
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
    api_instance = openwebui_client.MemoriesApi(api_client)
    list_memory_paths_form = openwebui_client.ListMemoryPathsForm() # ListMemoryPathsForm | 

    try:
        # List Memory Paths
        api_response = await api_instance.list_memory_paths_api_v1_memories_paths_post(list_memory_paths_form)
        print("The response of MemoriesApi->list_memory_paths_api_v1_memories_paths_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->list_memory_paths_api_v1_memories_paths_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_memory_paths_form** | [**ListMemoryPathsForm**](ListMemoryPathsForm.md)|  | 

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

# **query_memory_api_v1_memories_query_post**
> object query_memory_api_v1_memories_query_post(query_memory_form)

Query Memory

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.query_memory_form import QueryMemoryForm
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
    api_instance = openwebui_client.MemoriesApi(api_client)
    query_memory_form = openwebui_client.QueryMemoryForm() # QueryMemoryForm | 

    try:
        # Query Memory
        api_response = await api_instance.query_memory_api_v1_memories_query_post(query_memory_form)
        print("The response of MemoriesApi->query_memory_api_v1_memories_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->query_memory_api_v1_memories_query_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_memory_form** | [**QueryMemoryForm**](QueryMemoryForm.md)|  | 

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

# **read_memory_path_api_v1_memories_path_post**
> object read_memory_path_api_v1_memories_path_post(read_memory_path_form)

Read Memory Path

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.read_memory_path_form import ReadMemoryPathForm
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
    api_instance = openwebui_client.MemoriesApi(api_client)
    read_memory_path_form = openwebui_client.ReadMemoryPathForm() # ReadMemoryPathForm | 

    try:
        # Read Memory Path
        api_response = await api_instance.read_memory_path_api_v1_memories_path_post(read_memory_path_form)
        print("The response of MemoriesApi->read_memory_path_api_v1_memories_path_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->read_memory_path_api_v1_memories_path_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **read_memory_path_form** | [**ReadMemoryPathForm**](ReadMemoryPathForm.md)|  | 

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

# **reset_memory_from_vector_db_api_v1_memories_reset_post**
> bool reset_memory_from_vector_db_api_v1_memories_reset_post()

Reset Memory From Vector Db

Reset user's memory vector embeddings.

CRITICAL: We intentionally do NOT use Depends(get_async_session) here.
This endpoint generates embeddings for ALL user memories in parallel using
asyncio.gather(). A user with 100 memories would trigger 100 embedding API
calls simultaneously. With a session held, this could block a connection
for MINUTES, completely exhausting the connection pool.

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
    api_instance = openwebui_client.MemoriesApi(api_client)

    try:
        # Reset Memory From Vector Db
        api_response = await api_instance.reset_memory_from_vector_db_api_v1_memories_reset_post()
        print("The response of MemoriesApi->reset_memory_from_vector_db_api_v1_memories_reset_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->reset_memory_from_vector_db_api_v1_memories_reset_post: %s\n" % e)
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

# **search_memories_api_v1_memories_search_post**
> List[Optional[MemoryModel]] search_memories_api_v1_memories_search_post(search_memories_form)

Search Memories

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.memory_model import MemoryModel
from openwebui_client.models.search_memories_form import SearchMemoriesForm
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
    api_instance = openwebui_client.MemoriesApi(api_client)
    search_memories_form = openwebui_client.SearchMemoriesForm() # SearchMemoriesForm | 

    try:
        # Search Memories
        api_response = await api_instance.search_memories_api_v1_memories_search_post(search_memories_form)
        print("The response of MemoriesApi->search_memories_api_v1_memories_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->search_memories_api_v1_memories_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_memories_form** | [**SearchMemoriesForm**](SearchMemoriesForm.md)|  | 

### Return type

[**List[Optional[MemoryModel]]**](MemoryModel.md)

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

# **update_memories_api_v1_memories_update_post**
> List[Dict[str, object]] update_memories_api_v1_memories_update_post(update_memories_form)

Update Memories

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.update_memories_form import UpdateMemoriesForm
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
    api_instance = openwebui_client.MemoriesApi(api_client)
    update_memories_form = openwebui_client.UpdateMemoriesForm() # UpdateMemoriesForm | 

    try:
        # Update Memories
        api_response = await api_instance.update_memories_api_v1_memories_update_post(update_memories_form)
        print("The response of MemoriesApi->update_memories_api_v1_memories_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->update_memories_api_v1_memories_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_memories_form** | [**UpdateMemoriesForm**](UpdateMemoriesForm.md)|  | 

### Return type

**List[Dict[str, object]]**

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

# **update_memory_by_id_api_v1_memories_memory_id_update_post**
> MemoryModel update_memory_by_id_api_v1_memories_memory_id_update_post(memory_id, memory_update_model)

Update Memory By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.memory_model import MemoryModel
from openwebui_client.models.memory_update_model import MemoryUpdateModel
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
    api_instance = openwebui_client.MemoriesApi(api_client)
    memory_id = 'memory_id_example' # str | 
    memory_update_model = openwebui_client.MemoryUpdateModel() # MemoryUpdateModel | 

    try:
        # Update Memory By Id
        api_response = await api_instance.update_memory_by_id_api_v1_memories_memory_id_update_post(memory_id, memory_update_model)
        print("The response of MemoriesApi->update_memory_by_id_api_v1_memories_memory_id_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->update_memory_by_id_api_v1_memories_memory_id_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memory_id** | **str**|  | 
 **memory_update_model** | [**MemoryUpdateModel**](MemoryUpdateModel.md)|  | 

### Return type

[**MemoryModel**](MemoryModel.md)

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

