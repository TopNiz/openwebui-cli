# openwebui_client.KnowledgeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_file_to_knowledge_by_id_api_v1_knowledge_id_file_add_post**](KnowledgeApi.md#add_file_to_knowledge_by_id_api_v1_knowledge_id_file_add_post) | **POST** /api/v1/knowledge/{id}/file/add | Add File To Knowledge By Id
[**add_files_to_knowledge_batch_api_v1_knowledge_id_files_batch_add_post**](KnowledgeApi.md#add_files_to_knowledge_batch_api_v1_knowledge_id_files_batch_add_post) | **POST** /api/v1/knowledge/{id}/files/batch/add | Add Files To Knowledge Batch
[**create_external_knowledge_api_v1_knowledge_external_knowledge_create_post**](KnowledgeApi.md#create_external_knowledge_api_v1_knowledge_external_knowledge_create_post) | **POST** /api/v1/knowledge/external/knowledge/create | Create External Knowledge
[**create_external_knowledge_connection_api_v1_knowledge_external_connections_post**](KnowledgeApi.md#create_external_knowledge_connection_api_v1_knowledge_external_connections_post) | **POST** /api/v1/knowledge/external/connections | Create External Knowledge Connection
[**create_external_knowledge_source_api_v1_knowledge_external_source_create_post**](KnowledgeApi.md#create_external_knowledge_source_api_v1_knowledge_external_source_create_post) | **POST** /api/v1/knowledge/external/source/create | Create External Knowledge Source
[**create_knowledge_directory_api_v1_knowledge_id_dirs_create_post**](KnowledgeApi.md#create_knowledge_directory_api_v1_knowledge_id_dirs_create_post) | **POST** /api/v1/knowledge/{id}/dirs/create | Create Knowledge Directory
[**create_new_knowledge_api_v1_knowledge_create_post**](KnowledgeApi.md#create_new_knowledge_api_v1_knowledge_create_post) | **POST** /api/v1/knowledge/create | Create New Knowledge
[**delete_external_knowledge_connection_api_v1_knowledge_external_connections_id_delete**](KnowledgeApi.md#delete_external_knowledge_connection_api_v1_knowledge_external_connections_id_delete) | **DELETE** /api/v1/knowledge/external/connections/{id} | Delete External Knowledge Connection
[**delete_knowledge_by_id_api_v1_knowledge_id_delete_delete**](KnowledgeApi.md#delete_knowledge_by_id_api_v1_knowledge_id_delete_delete) | **DELETE** /api/v1/knowledge/{id}/delete | Delete Knowledge By Id
[**delete_knowledge_directory_api_v1_knowledge_id_dirs_dir_id_delete_delete**](KnowledgeApi.md#delete_knowledge_directory_api_v1_knowledge_id_dirs_dir_id_delete_delete) | **DELETE** /api/v1/knowledge/{id}/dirs/{dir_id}/delete | Delete Knowledge Directory
[**export_knowledge_by_id_api_v1_knowledge_id_export_get**](KnowledgeApi.md#export_knowledge_by_id_api_v1_knowledge_id_export_get) | **GET** /api/v1/knowledge/{id}/export | Export Knowledge By Id
[**get_external_knowledge_connection_api_v1_knowledge_external_connections_id_get**](KnowledgeApi.md#get_external_knowledge_connection_api_v1_knowledge_external_connections_id_get) | **GET** /api/v1/knowledge/external/connections/{id} | Get External Knowledge Connection
[**get_external_knowledge_connections_api_v1_knowledge_external_connections_get**](KnowledgeApi.md#get_external_knowledge_connections_api_v1_knowledge_external_connections_get) | **GET** /api/v1/knowledge/external/connections | Get External Knowledge Connections
[**get_knowledge_bases_api_v1_knowledge_get**](KnowledgeApi.md#get_knowledge_bases_api_v1_knowledge_get) | **GET** /api/v1/knowledge/ | Get Knowledge Bases
[**get_knowledge_by_id_api_v1_knowledge_id_get**](KnowledgeApi.md#get_knowledge_by_id_api_v1_knowledge_id_get) | **GET** /api/v1/knowledge/{id} | Get Knowledge By Id
[**get_knowledge_files_by_id_api_v1_knowledge_id_files_get**](KnowledgeApi.md#get_knowledge_files_by_id_api_v1_knowledge_id_files_get) | **GET** /api/v1/knowledge/{id}/files | Get Knowledge Files By Id
[**get_pending_knowledge_files_api_v1_knowledge_id_files_pending_get**](KnowledgeApi.md#get_pending_knowledge_files_api_v1_knowledge_id_files_pending_get) | **GET** /api/v1/knowledge/{id}/files/pending | Get Pending Knowledge Files
[**move_file_in_knowledge_api_v1_knowledge_id_file_move_post**](KnowledgeApi.md#move_file_in_knowledge_api_v1_knowledge_id_file_move_post) | **POST** /api/v1/knowledge/{id}/file/move | Move File In Knowledge
[**reindex_knowledge_base_metadata_embeddings_api_v1_knowledge_metadata_reindex_post**](KnowledgeApi.md#reindex_knowledge_base_metadata_embeddings_api_v1_knowledge_metadata_reindex_post) | **POST** /api/v1/knowledge/metadata/reindex | Reindex Knowledge Base Metadata Embeddings
[**reindex_knowledge_files_api_v1_knowledge_reindex_post**](KnowledgeApi.md#reindex_knowledge_files_api_v1_knowledge_reindex_post) | **POST** /api/v1/knowledge/reindex | Reindex Knowledge Files
[**remove_file_from_knowledge_by_id_api_v1_knowledge_id_file_remove_post**](KnowledgeApi.md#remove_file_from_knowledge_by_id_api_v1_knowledge_id_file_remove_post) | **POST** /api/v1/knowledge/{id}/file/remove | Remove File From Knowledge By Id
[**reset_knowledge_by_id_api_v1_knowledge_id_reset_post**](KnowledgeApi.md#reset_knowledge_by_id_api_v1_knowledge_id_reset_post) | **POST** /api/v1/knowledge/{id}/reset | Reset Knowledge By Id
[**search_knowledge_bases_api_v1_knowledge_search_get**](KnowledgeApi.md#search_knowledge_bases_api_v1_knowledge_search_get) | **GET** /api/v1/knowledge/search | Search Knowledge Bases
[**search_knowledge_files_api_v1_knowledge_search_files_get**](KnowledgeApi.md#search_knowledge_files_api_v1_knowledge_search_files_get) | **GET** /api/v1/knowledge/search/files | Search Knowledge Files
[**sync_knowledge_cleanup_api_v1_knowledge_id_sync_cleanup_post**](KnowledgeApi.md#sync_knowledge_cleanup_api_v1_knowledge_id_sync_cleanup_post) | **POST** /api/v1/knowledge/{id}/sync/cleanup | Sync Knowledge Cleanup
[**sync_knowledge_diff_api_v1_knowledge_id_sync_diff_post**](KnowledgeApi.md#sync_knowledge_diff_api_v1_knowledge_id_sync_diff_post) | **POST** /api/v1/knowledge/{id}/sync/diff | Sync Knowledge Diff
[**test_external_knowledge_connection_api_v1_knowledge_external_connections_id_test_post**](KnowledgeApi.md#test_external_knowledge_connection_api_v1_knowledge_external_connections_id_test_post) | **POST** /api/v1/knowledge/external/connections/{id}/test | Test External Knowledge Connection
[**test_external_knowledge_retrieval_api_v1_knowledge_external_connections_id_retrieve_test_post**](KnowledgeApi.md#test_external_knowledge_retrieval_api_v1_knowledge_external_connections_id_retrieve_test_post) | **POST** /api/v1/knowledge/external/connections/{id}/retrieve-test | Test External Knowledge Retrieval
[**test_external_knowledge_source_api_v1_knowledge_external_source_test_post**](KnowledgeApi.md#test_external_knowledge_source_api_v1_knowledge_external_source_test_post) | **POST** /api/v1/knowledge/external/source/test | Test External Knowledge Source
[**update_external_knowledge_connection_api_v1_knowledge_external_connections_id_patch**](KnowledgeApi.md#update_external_knowledge_connection_api_v1_knowledge_external_connections_id_patch) | **PATCH** /api/v1/knowledge/external/connections/{id} | Update External Knowledge Connection
[**update_external_knowledge_source_api_v1_knowledge_external_source_id_patch**](KnowledgeApi.md#update_external_knowledge_source_api_v1_knowledge_external_source_id_patch) | **PATCH** /api/v1/knowledge/external/source/{id} | Update External Knowledge Source
[**update_file_from_knowledge_by_id_api_v1_knowledge_id_file_update_post**](KnowledgeApi.md#update_file_from_knowledge_by_id_api_v1_knowledge_id_file_update_post) | **POST** /api/v1/knowledge/{id}/file/update | Update File From Knowledge By Id
[**update_knowledge_access_by_id_api_v1_knowledge_id_access_update_post**](KnowledgeApi.md#update_knowledge_access_by_id_api_v1_knowledge_id_access_update_post) | **POST** /api/v1/knowledge/{id}/access/update | Update Knowledge Access By Id
[**update_knowledge_by_id_api_v1_knowledge_id_update_post**](KnowledgeApi.md#update_knowledge_by_id_api_v1_knowledge_id_update_post) | **POST** /api/v1/knowledge/{id}/update | Update Knowledge By Id
[**update_knowledge_directory_api_v1_knowledge_id_dirs_dir_id_update_post**](KnowledgeApi.md#update_knowledge_directory_api_v1_knowledge_id_dirs_dir_id_update_post) | **POST** /api/v1/knowledge/{id}/dirs/{dir_id}/update | Update Knowledge Directory


# **add_file_to_knowledge_by_id_api_v1_knowledge_id_file_add_post**
> KnowledgeFilesResponse add_file_to_knowledge_by_id_api_v1_knowledge_id_file_add_post(id, knowledge_file_id_form)

Add File To Knowledge By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.knowledge_file_id_form import KnowledgeFileIdForm
from openwebui_client.models.knowledge_files_response import KnowledgeFilesResponse
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 
    knowledge_file_id_form = openwebui_client.KnowledgeFileIdForm() # KnowledgeFileIdForm | 

    try:
        # Add File To Knowledge By Id
        api_response = await api_instance.add_file_to_knowledge_by_id_api_v1_knowledge_id_file_add_post(id, knowledge_file_id_form)
        print("The response of KnowledgeApi->add_file_to_knowledge_by_id_api_v1_knowledge_id_file_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->add_file_to_knowledge_by_id_api_v1_knowledge_id_file_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **knowledge_file_id_form** | [**KnowledgeFileIdForm**](KnowledgeFileIdForm.md)|  | 

### Return type

[**KnowledgeFilesResponse**](KnowledgeFilesResponse.md)

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

# **add_files_to_knowledge_batch_api_v1_knowledge_id_files_batch_add_post**
> KnowledgeFilesResponse add_files_to_knowledge_batch_api_v1_knowledge_id_files_batch_add_post(id, knowledge_file_id_form)

Add Files To Knowledge Batch

Add multiple files to a knowledge base

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.knowledge_file_id_form import KnowledgeFileIdForm
from openwebui_client.models.knowledge_files_response import KnowledgeFilesResponse
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 
    knowledge_file_id_form = [openwebui_client.KnowledgeFileIdForm()] # List[KnowledgeFileIdForm] | 

    try:
        # Add Files To Knowledge Batch
        api_response = await api_instance.add_files_to_knowledge_batch_api_v1_knowledge_id_files_batch_add_post(id, knowledge_file_id_form)
        print("The response of KnowledgeApi->add_files_to_knowledge_batch_api_v1_knowledge_id_files_batch_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->add_files_to_knowledge_batch_api_v1_knowledge_id_files_batch_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **knowledge_file_id_form** | [**List[KnowledgeFileIdForm]**](KnowledgeFileIdForm.md)|  | 

### Return type

[**KnowledgeFilesResponse**](KnowledgeFilesResponse.md)

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

# **create_external_knowledge_api_v1_knowledge_external_knowledge_create_post**
> KnowledgeResponse create_external_knowledge_api_v1_knowledge_external_knowledge_create_post(external_knowledge_create_form)

Create External Knowledge

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.external_knowledge_create_form import ExternalKnowledgeCreateForm
from openwebui_client.models.knowledge_response import KnowledgeResponse
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    external_knowledge_create_form = openwebui_client.ExternalKnowledgeCreateForm() # ExternalKnowledgeCreateForm | 

    try:
        # Create External Knowledge
        api_response = await api_instance.create_external_knowledge_api_v1_knowledge_external_knowledge_create_post(external_knowledge_create_form)
        print("The response of KnowledgeApi->create_external_knowledge_api_v1_knowledge_external_knowledge_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->create_external_knowledge_api_v1_knowledge_external_knowledge_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_knowledge_create_form** | [**ExternalKnowledgeCreateForm**](ExternalKnowledgeCreateForm.md)|  | 

### Return type

[**KnowledgeResponse**](KnowledgeResponse.md)

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

# **create_external_knowledge_connection_api_v1_knowledge_external_connections_post**
> Dict[str, object] create_external_knowledge_connection_api_v1_knowledge_external_connections_post(external_knowledge_connection_form)

Create External Knowledge Connection

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.external_knowledge_connection_form import ExternalKnowledgeConnectionForm
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    external_knowledge_connection_form = openwebui_client.ExternalKnowledgeConnectionForm() # ExternalKnowledgeConnectionForm | 

    try:
        # Create External Knowledge Connection
        api_response = await api_instance.create_external_knowledge_connection_api_v1_knowledge_external_connections_post(external_knowledge_connection_form)
        print("The response of KnowledgeApi->create_external_knowledge_connection_api_v1_knowledge_external_connections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->create_external_knowledge_connection_api_v1_knowledge_external_connections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_knowledge_connection_form** | [**ExternalKnowledgeConnectionForm**](ExternalKnowledgeConnectionForm.md)|  | 

### Return type

**Dict[str, object]**

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

# **create_external_knowledge_source_api_v1_knowledge_external_source_create_post**
> KnowledgeResponse create_external_knowledge_source_api_v1_knowledge_external_source_create_post(external_knowledge_source_create_form)

Create External Knowledge Source

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.external_knowledge_source_create_form import ExternalKnowledgeSourceCreateForm
from openwebui_client.models.knowledge_response import KnowledgeResponse
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    external_knowledge_source_create_form = openwebui_client.ExternalKnowledgeSourceCreateForm() # ExternalKnowledgeSourceCreateForm | 

    try:
        # Create External Knowledge Source
        api_response = await api_instance.create_external_knowledge_source_api_v1_knowledge_external_source_create_post(external_knowledge_source_create_form)
        print("The response of KnowledgeApi->create_external_knowledge_source_api_v1_knowledge_external_source_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->create_external_knowledge_source_api_v1_knowledge_external_source_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_knowledge_source_create_form** | [**ExternalKnowledgeSourceCreateForm**](ExternalKnowledgeSourceCreateForm.md)|  | 

### Return type

[**KnowledgeResponse**](KnowledgeResponse.md)

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

# **create_knowledge_directory_api_v1_knowledge_id_dirs_create_post**
> KnowledgeDirectoryModel create_knowledge_directory_api_v1_knowledge_id_dirs_create_post(id, knowledge_directory_create_form)

Create Knowledge Directory

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.knowledge_directory_create_form import KnowledgeDirectoryCreateForm
from openwebui_client.models.knowledge_directory_model import KnowledgeDirectoryModel
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 
    knowledge_directory_create_form = openwebui_client.KnowledgeDirectoryCreateForm() # KnowledgeDirectoryCreateForm | 

    try:
        # Create Knowledge Directory
        api_response = await api_instance.create_knowledge_directory_api_v1_knowledge_id_dirs_create_post(id, knowledge_directory_create_form)
        print("The response of KnowledgeApi->create_knowledge_directory_api_v1_knowledge_id_dirs_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->create_knowledge_directory_api_v1_knowledge_id_dirs_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **knowledge_directory_create_form** | [**KnowledgeDirectoryCreateForm**](KnowledgeDirectoryCreateForm.md)|  | 

### Return type

[**KnowledgeDirectoryModel**](KnowledgeDirectoryModel.md)

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

# **create_new_knowledge_api_v1_knowledge_create_post**
> KnowledgeResponse create_new_knowledge_api_v1_knowledge_create_post(knowledge_form)

Create New Knowledge

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.knowledge_form import KnowledgeForm
from openwebui_client.models.knowledge_response import KnowledgeResponse
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    knowledge_form = openwebui_client.KnowledgeForm() # KnowledgeForm | 

    try:
        # Create New Knowledge
        api_response = await api_instance.create_new_knowledge_api_v1_knowledge_create_post(knowledge_form)
        print("The response of KnowledgeApi->create_new_knowledge_api_v1_knowledge_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->create_new_knowledge_api_v1_knowledge_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **knowledge_form** | [**KnowledgeForm**](KnowledgeForm.md)|  | 

### Return type

[**KnowledgeResponse**](KnowledgeResponse.md)

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

# **delete_external_knowledge_connection_api_v1_knowledge_external_connections_id_delete**
> bool delete_external_knowledge_connection_api_v1_knowledge_external_connections_id_delete(id)

Delete External Knowledge Connection

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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete External Knowledge Connection
        api_response = await api_instance.delete_external_knowledge_connection_api_v1_knowledge_external_connections_id_delete(id)
        print("The response of KnowledgeApi->delete_external_knowledge_connection_api_v1_knowledge_external_connections_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->delete_external_knowledge_connection_api_v1_knowledge_external_connections_id_delete: %s\n" % e)
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

# **delete_knowledge_by_id_api_v1_knowledge_id_delete_delete**
> bool delete_knowledge_by_id_api_v1_knowledge_id_delete_delete(id)

Delete Knowledge By Id

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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Knowledge By Id
        api_response = await api_instance.delete_knowledge_by_id_api_v1_knowledge_id_delete_delete(id)
        print("The response of KnowledgeApi->delete_knowledge_by_id_api_v1_knowledge_id_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->delete_knowledge_by_id_api_v1_knowledge_id_delete_delete: %s\n" % e)
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

# **delete_knowledge_directory_api_v1_knowledge_id_dirs_dir_id_delete_delete**
> object delete_knowledge_directory_api_v1_knowledge_id_dirs_dir_id_delete_delete(id, dir_id, move_files=move_files)

Delete Knowledge Directory

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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 
    dir_id = 'dir_id_example' # str | 
    move_files = True # bool | If true, move contained files to parent. If false, delete them. (optional) (default to True)

    try:
        # Delete Knowledge Directory
        api_response = await api_instance.delete_knowledge_directory_api_v1_knowledge_id_dirs_dir_id_delete_delete(id, dir_id, move_files=move_files)
        print("The response of KnowledgeApi->delete_knowledge_directory_api_v1_knowledge_id_dirs_dir_id_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->delete_knowledge_directory_api_v1_knowledge_id_dirs_dir_id_delete_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **dir_id** | **str**|  | 
 **move_files** | **bool**| If true, move contained files to parent. If false, delete them. | [optional] [default to True]

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

# **export_knowledge_by_id_api_v1_knowledge_id_export_get**
> object export_knowledge_by_id_api_v1_knowledge_id_export_get(id)

Export Knowledge By Id

Export a knowledge base as a zip file containing .txt files.
Admin only.

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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 

    try:
        # Export Knowledge By Id
        api_response = await api_instance.export_knowledge_by_id_api_v1_knowledge_id_export_get(id)
        print("The response of KnowledgeApi->export_knowledge_by_id_api_v1_knowledge_id_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->export_knowledge_by_id_api_v1_knowledge_id_export_get: %s\n" % e)
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

# **get_external_knowledge_connection_api_v1_knowledge_external_connections_id_get**
> Dict[str, object] get_external_knowledge_connection_api_v1_knowledge_external_connections_id_get(id)

Get External Knowledge Connection

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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get External Knowledge Connection
        api_response = await api_instance.get_external_knowledge_connection_api_v1_knowledge_external_connections_id_get(id)
        print("The response of KnowledgeApi->get_external_knowledge_connection_api_v1_knowledge_external_connections_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->get_external_knowledge_connection_api_v1_knowledge_external_connections_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**Dict[str, object]**

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

# **get_external_knowledge_connections_api_v1_knowledge_external_connections_get**
> ExternalKnowledgeConnectionListResponse get_external_knowledge_connections_api_v1_knowledge_external_connections_get()

Get External Knowledge Connections

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.external_knowledge_connection_list_response import ExternalKnowledgeConnectionListResponse
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
    api_instance = openwebui_client.KnowledgeApi(api_client)

    try:
        # Get External Knowledge Connections
        api_response = await api_instance.get_external_knowledge_connections_api_v1_knowledge_external_connections_get()
        print("The response of KnowledgeApi->get_external_knowledge_connections_api_v1_knowledge_external_connections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->get_external_knowledge_connections_api_v1_knowledge_external_connections_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ExternalKnowledgeConnectionListResponse**](ExternalKnowledgeConnectionListResponse.md)

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

# **get_knowledge_bases_api_v1_knowledge_get**
> KnowledgeAccessListResponse get_knowledge_bases_api_v1_knowledge_get(page=page)

Get Knowledge Bases

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.knowledge_access_list_response import KnowledgeAccessListResponse
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    page = 56 # int |  (optional)

    try:
        # Get Knowledge Bases
        api_response = await api_instance.get_knowledge_bases_api_v1_knowledge_get(page=page)
        print("The response of KnowledgeApi->get_knowledge_bases_api_v1_knowledge_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->get_knowledge_bases_api_v1_knowledge_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 

### Return type

[**KnowledgeAccessListResponse**](KnowledgeAccessListResponse.md)

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

# **get_knowledge_by_id_api_v1_knowledge_id_get**
> KnowledgeFilesResponse get_knowledge_by_id_api_v1_knowledge_id_get(id)

Get Knowledge By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.knowledge_files_response import KnowledgeFilesResponse
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Knowledge By Id
        api_response = await api_instance.get_knowledge_by_id_api_v1_knowledge_id_get(id)
        print("The response of KnowledgeApi->get_knowledge_by_id_api_v1_knowledge_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->get_knowledge_by_id_api_v1_knowledge_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**KnowledgeFilesResponse**](KnowledgeFilesResponse.md)

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

# **get_knowledge_files_by_id_api_v1_knowledge_id_files_get**
> KnowledgeFileListResponse get_knowledge_files_by_id_api_v1_knowledge_id_files_get(id, query=query, include_content=include_content, view_option=view_option, order_by=order_by, direction=direction, directory_id=directory_id, page=page, limit=limit)

Get Knowledge Files By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.knowledge_file_list_response import KnowledgeFileListResponse
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 
    query = 'query_example' # str |  (optional)
    include_content = False # bool | Include file content in search (expensive). (optional) (default to False)
    view_option = 'view_option_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    direction = 'direction_example' # str |  (optional)
    directory_id = 'directory_id_example' # str | Filter by directory ID. Pass empty string for root. (optional)
    page = 56 # int |  (optional)
    limit = 56 # int | Page size (admin only). Defaults to 30. (optional)

    try:
        # Get Knowledge Files By Id
        api_response = await api_instance.get_knowledge_files_by_id_api_v1_knowledge_id_files_get(id, query=query, include_content=include_content, view_option=view_option, order_by=order_by, direction=direction, directory_id=directory_id, page=page, limit=limit)
        print("The response of KnowledgeApi->get_knowledge_files_by_id_api_v1_knowledge_id_files_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->get_knowledge_files_by_id_api_v1_knowledge_id_files_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **query** | **str**|  | [optional] 
 **include_content** | **bool**| Include file content in search (expensive). | [optional] [default to False]
 **view_option** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] 
 **directory_id** | **str**| Filter by directory ID. Pass empty string for root. | [optional] 
 **page** | **int**|  | [optional] 
 **limit** | **int**| Page size (admin only). Defaults to 30. | [optional] 

### Return type

[**KnowledgeFileListResponse**](KnowledgeFileListResponse.md)

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

# **get_pending_knowledge_files_api_v1_knowledge_id_files_pending_get**
> object get_pending_knowledge_files_api_v1_knowledge_id_files_pending_get(id, stream=stream)

Get Pending Knowledge Files

Return files that are being processed for this knowledge base but not yet linked.

After a file is uploaded with ``knowledge_id`` in its metadata, the backend
processes it in a background task before linking it to the ``knowledge_file``
join table.  During this window the file is invisible to the normal file
list endpoint.  This endpoint exposes those in-flight files so the frontend
can show them with a processing indicator even after a page reload.

When ``stream=true``, returns an SSE stream that polls every 3 seconds
and emits the current pending file list.  Closes when no files remain.

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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 
    stream = False # bool |  (optional) (default to False)

    try:
        # Get Pending Knowledge Files
        api_response = await api_instance.get_pending_knowledge_files_api_v1_knowledge_id_files_pending_get(id, stream=stream)
        print("The response of KnowledgeApi->get_pending_knowledge_files_api_v1_knowledge_id_files_pending_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->get_pending_knowledge_files_api_v1_knowledge_id_files_pending_get: %s\n" % e)
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

# **move_file_in_knowledge_api_v1_knowledge_id_file_move_post**
> object move_file_in_knowledge_api_v1_knowledge_id_file_move_post(id, knowledge_file_move_form)

Move File In Knowledge

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.knowledge_file_move_form import KnowledgeFileMoveForm
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 
    knowledge_file_move_form = openwebui_client.KnowledgeFileMoveForm() # KnowledgeFileMoveForm | 

    try:
        # Move File In Knowledge
        api_response = await api_instance.move_file_in_knowledge_api_v1_knowledge_id_file_move_post(id, knowledge_file_move_form)
        print("The response of KnowledgeApi->move_file_in_knowledge_api_v1_knowledge_id_file_move_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->move_file_in_knowledge_api_v1_knowledge_id_file_move_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **knowledge_file_move_form** | [**KnowledgeFileMoveForm**](KnowledgeFileMoveForm.md)|  | 

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

# **reindex_knowledge_base_metadata_embeddings_api_v1_knowledge_metadata_reindex_post**
> Dict[str, object] reindex_knowledge_base_metadata_embeddings_api_v1_knowledge_metadata_reindex_post()

Reindex Knowledge Base Metadata Embeddings

Batch embed all existing knowledge bases. Admin only.

NOTE: We intentionally do NOT use Depends(get_async_session) here.
This endpoint loops through ALL knowledge bases and calls embed_knowledge_base_metadata()
for each one, making N external embedding API calls. Holding a session during
this entire operation would exhaust the connection pool.

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
    api_instance = openwebui_client.KnowledgeApi(api_client)

    try:
        # Reindex Knowledge Base Metadata Embeddings
        api_response = await api_instance.reindex_knowledge_base_metadata_embeddings_api_v1_knowledge_metadata_reindex_post()
        print("The response of KnowledgeApi->reindex_knowledge_base_metadata_embeddings_api_v1_knowledge_metadata_reindex_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->reindex_knowledge_base_metadata_embeddings_api_v1_knowledge_metadata_reindex_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

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

# **reindex_knowledge_files_api_v1_knowledge_reindex_post**
> bool reindex_knowledge_files_api_v1_knowledge_reindex_post()

Reindex Knowledge Files

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
    api_instance = openwebui_client.KnowledgeApi(api_client)

    try:
        # Reindex Knowledge Files
        api_response = await api_instance.reindex_knowledge_files_api_v1_knowledge_reindex_post()
        print("The response of KnowledgeApi->reindex_knowledge_files_api_v1_knowledge_reindex_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->reindex_knowledge_files_api_v1_knowledge_reindex_post: %s\n" % e)
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

# **remove_file_from_knowledge_by_id_api_v1_knowledge_id_file_remove_post**
> KnowledgeFilesResponse remove_file_from_knowledge_by_id_api_v1_knowledge_id_file_remove_post(id, knowledge_file_id_form, delete_file=delete_file)

Remove File From Knowledge By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.knowledge_file_id_form import KnowledgeFileIdForm
from openwebui_client.models.knowledge_files_response import KnowledgeFilesResponse
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 
    knowledge_file_id_form = openwebui_client.KnowledgeFileIdForm() # KnowledgeFileIdForm | 
    delete_file = True # bool |  (optional) (default to True)

    try:
        # Remove File From Knowledge By Id
        api_response = await api_instance.remove_file_from_knowledge_by_id_api_v1_knowledge_id_file_remove_post(id, knowledge_file_id_form, delete_file=delete_file)
        print("The response of KnowledgeApi->remove_file_from_knowledge_by_id_api_v1_knowledge_id_file_remove_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->remove_file_from_knowledge_by_id_api_v1_knowledge_id_file_remove_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **knowledge_file_id_form** | [**KnowledgeFileIdForm**](KnowledgeFileIdForm.md)|  | 
 **delete_file** | **bool**|  | [optional] [default to True]

### Return type

[**KnowledgeFilesResponse**](KnowledgeFilesResponse.md)

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

# **reset_knowledge_by_id_api_v1_knowledge_id_reset_post**
> KnowledgeResponse reset_knowledge_by_id_api_v1_knowledge_id_reset_post(id, include_directories=include_directories)

Reset Knowledge By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.knowledge_response import KnowledgeResponse
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 
    include_directories = True # bool |  (optional) (default to True)

    try:
        # Reset Knowledge By Id
        api_response = await api_instance.reset_knowledge_by_id_api_v1_knowledge_id_reset_post(id, include_directories=include_directories)
        print("The response of KnowledgeApi->reset_knowledge_by_id_api_v1_knowledge_id_reset_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->reset_knowledge_by_id_api_v1_knowledge_id_reset_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **include_directories** | **bool**|  | [optional] [default to True]

### Return type

[**KnowledgeResponse**](KnowledgeResponse.md)

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

# **search_knowledge_bases_api_v1_knowledge_search_get**
> KnowledgeAccessListResponse search_knowledge_bases_api_v1_knowledge_search_get(query=query, view_option=view_option, source=source, page=page, order_by=order_by, direction=direction)

Search Knowledge Bases

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.knowledge_access_list_response import KnowledgeAccessListResponse
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    query = 'query_example' # str |  (optional)
    view_option = 'view_option_example' # str |  (optional)
    source = 'source_example' # str |  (optional)
    page = 56 # int |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    direction = 'direction_example' # str |  (optional)

    try:
        # Search Knowledge Bases
        api_response = await api_instance.search_knowledge_bases_api_v1_knowledge_search_get(query=query, view_option=view_option, source=source, page=page, order_by=order_by, direction=direction)
        print("The response of KnowledgeApi->search_knowledge_bases_api_v1_knowledge_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->search_knowledge_bases_api_v1_knowledge_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **view_option** | **str**|  | [optional] 
 **source** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] 

### Return type

[**KnowledgeAccessListResponse**](KnowledgeAccessListResponse.md)

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

# **search_knowledge_files_api_v1_knowledge_search_files_get**
> KnowledgeFileListResponse search_knowledge_files_api_v1_knowledge_search_files_get(query=query, include_content=include_content, page=page)

Search Knowledge Files

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.knowledge_file_list_response import KnowledgeFileListResponse
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    query = 'query_example' # str |  (optional)
    include_content = False # bool | Include file content in search (expensive). (optional) (default to False)
    page = 56 # int |  (optional)

    try:
        # Search Knowledge Files
        api_response = await api_instance.search_knowledge_files_api_v1_knowledge_search_files_get(query=query, include_content=include_content, page=page)
        print("The response of KnowledgeApi->search_knowledge_files_api_v1_knowledge_search_files_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->search_knowledge_files_api_v1_knowledge_search_files_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **include_content** | **bool**| Include file content in search (expensive). | [optional] [default to False]
 **page** | **int**|  | [optional] 

### Return type

[**KnowledgeFileListResponse**](KnowledgeFileListResponse.md)

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

# **sync_knowledge_cleanup_api_v1_knowledge_id_sync_cleanup_post**
> object sync_knowledge_cleanup_api_v1_knowledge_id_sync_cleanup_post(id, sync_cleanup_form)

Sync Knowledge Cleanup

Remove stale files and orphaned directories from a knowledge base
after an incremental sync.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.sync_cleanup_form import SyncCleanupForm
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 
    sync_cleanup_form = openwebui_client.SyncCleanupForm() # SyncCleanupForm | 

    try:
        # Sync Knowledge Cleanup
        api_response = await api_instance.sync_knowledge_cleanup_api_v1_knowledge_id_sync_cleanup_post(id, sync_cleanup_form)
        print("The response of KnowledgeApi->sync_knowledge_cleanup_api_v1_knowledge_id_sync_cleanup_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->sync_knowledge_cleanup_api_v1_knowledge_id_sync_cleanup_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sync_cleanup_form** | [**SyncCleanupForm**](SyncCleanupForm.md)|  | 

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

# **sync_knowledge_diff_api_v1_knowledge_id_sync_diff_post**
> SyncDiffResponse sync_knowledge_diff_api_v1_knowledge_id_sync_diff_post(id, sync_diff_form)

Sync Knowledge Diff

Compare a local file manifest against the knowledge base to determine
which files need uploading, removing, and which directories to create/remove.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.sync_diff_form import SyncDiffForm
from openwebui_client.models.sync_diff_response import SyncDiffResponse
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 
    sync_diff_form = openwebui_client.SyncDiffForm() # SyncDiffForm | 

    try:
        # Sync Knowledge Diff
        api_response = await api_instance.sync_knowledge_diff_api_v1_knowledge_id_sync_diff_post(id, sync_diff_form)
        print("The response of KnowledgeApi->sync_knowledge_diff_api_v1_knowledge_id_sync_diff_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->sync_knowledge_diff_api_v1_knowledge_id_sync_diff_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sync_diff_form** | [**SyncDiffForm**](SyncDiffForm.md)|  | 

### Return type

[**SyncDiffResponse**](SyncDiffResponse.md)

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

# **test_external_knowledge_connection_api_v1_knowledge_external_connections_id_test_post**
> Dict[str, object] test_external_knowledge_connection_api_v1_knowledge_external_connections_id_test_post(id)

Test External Knowledge Connection

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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 

    try:
        # Test External Knowledge Connection
        api_response = await api_instance.test_external_knowledge_connection_api_v1_knowledge_external_connections_id_test_post(id)
        print("The response of KnowledgeApi->test_external_knowledge_connection_api_v1_knowledge_external_connections_id_test_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->test_external_knowledge_connection_api_v1_knowledge_external_connections_id_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**Dict[str, object]**

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

# **test_external_knowledge_retrieval_api_v1_knowledge_external_connections_id_retrieve_test_post**
> Dict[str, object] test_external_knowledge_retrieval_api_v1_knowledge_external_connections_id_retrieve_test_post(id, external_knowledge_retrieve_test_form)

Test External Knowledge Retrieval

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.external_knowledge_retrieve_test_form import ExternalKnowledgeRetrieveTestForm
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 
    external_knowledge_retrieve_test_form = openwebui_client.ExternalKnowledgeRetrieveTestForm() # ExternalKnowledgeRetrieveTestForm | 

    try:
        # Test External Knowledge Retrieval
        api_response = await api_instance.test_external_knowledge_retrieval_api_v1_knowledge_external_connections_id_retrieve_test_post(id, external_knowledge_retrieve_test_form)
        print("The response of KnowledgeApi->test_external_knowledge_retrieval_api_v1_knowledge_external_connections_id_retrieve_test_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->test_external_knowledge_retrieval_api_v1_knowledge_external_connections_id_retrieve_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **external_knowledge_retrieve_test_form** | [**ExternalKnowledgeRetrieveTestForm**](ExternalKnowledgeRetrieveTestForm.md)|  | 

### Return type

**Dict[str, object]**

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

# **test_external_knowledge_source_api_v1_knowledge_external_source_test_post**
> Dict[str, object] test_external_knowledge_source_api_v1_knowledge_external_source_test_post(external_knowledge_source_test_form)

Test External Knowledge Source

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.external_knowledge_source_test_form import ExternalKnowledgeSourceTestForm
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    external_knowledge_source_test_form = openwebui_client.ExternalKnowledgeSourceTestForm() # ExternalKnowledgeSourceTestForm | 

    try:
        # Test External Knowledge Source
        api_response = await api_instance.test_external_knowledge_source_api_v1_knowledge_external_source_test_post(external_knowledge_source_test_form)
        print("The response of KnowledgeApi->test_external_knowledge_source_api_v1_knowledge_external_source_test_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->test_external_knowledge_source_api_v1_knowledge_external_source_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_knowledge_source_test_form** | [**ExternalKnowledgeSourceTestForm**](ExternalKnowledgeSourceTestForm.md)|  | 

### Return type

**Dict[str, object]**

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

# **update_external_knowledge_connection_api_v1_knowledge_external_connections_id_patch**
> Dict[str, object] update_external_knowledge_connection_api_v1_knowledge_external_connections_id_patch(id, external_knowledge_connection_form)

Update External Knowledge Connection

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.external_knowledge_connection_form import ExternalKnowledgeConnectionForm
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 
    external_knowledge_connection_form = openwebui_client.ExternalKnowledgeConnectionForm() # ExternalKnowledgeConnectionForm | 

    try:
        # Update External Knowledge Connection
        api_response = await api_instance.update_external_knowledge_connection_api_v1_knowledge_external_connections_id_patch(id, external_knowledge_connection_form)
        print("The response of KnowledgeApi->update_external_knowledge_connection_api_v1_knowledge_external_connections_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->update_external_knowledge_connection_api_v1_knowledge_external_connections_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **external_knowledge_connection_form** | [**ExternalKnowledgeConnectionForm**](ExternalKnowledgeConnectionForm.md)|  | 

### Return type

**Dict[str, object]**

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

# **update_external_knowledge_source_api_v1_knowledge_external_source_id_patch**
> KnowledgeResponse update_external_knowledge_source_api_v1_knowledge_external_source_id_patch(id, external_knowledge_source_update_form)

Update External Knowledge Source

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.external_knowledge_source_update_form import ExternalKnowledgeSourceUpdateForm
from openwebui_client.models.knowledge_response import KnowledgeResponse
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 
    external_knowledge_source_update_form = openwebui_client.ExternalKnowledgeSourceUpdateForm() # ExternalKnowledgeSourceUpdateForm | 

    try:
        # Update External Knowledge Source
        api_response = await api_instance.update_external_knowledge_source_api_v1_knowledge_external_source_id_patch(id, external_knowledge_source_update_form)
        print("The response of KnowledgeApi->update_external_knowledge_source_api_v1_knowledge_external_source_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->update_external_knowledge_source_api_v1_knowledge_external_source_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **external_knowledge_source_update_form** | [**ExternalKnowledgeSourceUpdateForm**](ExternalKnowledgeSourceUpdateForm.md)|  | 

### Return type

[**KnowledgeResponse**](KnowledgeResponse.md)

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

# **update_file_from_knowledge_by_id_api_v1_knowledge_id_file_update_post**
> KnowledgeFilesResponse update_file_from_knowledge_by_id_api_v1_knowledge_id_file_update_post(id, knowledge_file_id_form)

Update File From Knowledge By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.knowledge_file_id_form import KnowledgeFileIdForm
from openwebui_client.models.knowledge_files_response import KnowledgeFilesResponse
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 
    knowledge_file_id_form = openwebui_client.KnowledgeFileIdForm() # KnowledgeFileIdForm | 

    try:
        # Update File From Knowledge By Id
        api_response = await api_instance.update_file_from_knowledge_by_id_api_v1_knowledge_id_file_update_post(id, knowledge_file_id_form)
        print("The response of KnowledgeApi->update_file_from_knowledge_by_id_api_v1_knowledge_id_file_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->update_file_from_knowledge_by_id_api_v1_knowledge_id_file_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **knowledge_file_id_form** | [**KnowledgeFileIdForm**](KnowledgeFileIdForm.md)|  | 

### Return type

[**KnowledgeFilesResponse**](KnowledgeFilesResponse.md)

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

# **update_knowledge_access_by_id_api_v1_knowledge_id_access_update_post**
> KnowledgeFilesResponse update_knowledge_access_by_id_api_v1_knowledge_id_access_update_post(id, knowledge_access_grants_form)

Update Knowledge Access By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.knowledge_access_grants_form import KnowledgeAccessGrantsForm
from openwebui_client.models.knowledge_files_response import KnowledgeFilesResponse
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 
    knowledge_access_grants_form = openwebui_client.KnowledgeAccessGrantsForm() # KnowledgeAccessGrantsForm | 

    try:
        # Update Knowledge Access By Id
        api_response = await api_instance.update_knowledge_access_by_id_api_v1_knowledge_id_access_update_post(id, knowledge_access_grants_form)
        print("The response of KnowledgeApi->update_knowledge_access_by_id_api_v1_knowledge_id_access_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->update_knowledge_access_by_id_api_v1_knowledge_id_access_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **knowledge_access_grants_form** | [**KnowledgeAccessGrantsForm**](KnowledgeAccessGrantsForm.md)|  | 

### Return type

[**KnowledgeFilesResponse**](KnowledgeFilesResponse.md)

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

# **update_knowledge_by_id_api_v1_knowledge_id_update_post**
> KnowledgeFilesResponse update_knowledge_by_id_api_v1_knowledge_id_update_post(id, knowledge_form)

Update Knowledge By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.knowledge_files_response import KnowledgeFilesResponse
from openwebui_client.models.knowledge_form import KnowledgeForm
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 
    knowledge_form = openwebui_client.KnowledgeForm() # KnowledgeForm | 

    try:
        # Update Knowledge By Id
        api_response = await api_instance.update_knowledge_by_id_api_v1_knowledge_id_update_post(id, knowledge_form)
        print("The response of KnowledgeApi->update_knowledge_by_id_api_v1_knowledge_id_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->update_knowledge_by_id_api_v1_knowledge_id_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **knowledge_form** | [**KnowledgeForm**](KnowledgeForm.md)|  | 

### Return type

[**KnowledgeFilesResponse**](KnowledgeFilesResponse.md)

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

# **update_knowledge_directory_api_v1_knowledge_id_dirs_dir_id_update_post**
> KnowledgeDirectoryModel update_knowledge_directory_api_v1_knowledge_id_dirs_dir_id_update_post(id, dir_id, knowledge_directory_update_form)

Update Knowledge Directory

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.knowledge_directory_model import KnowledgeDirectoryModel
from openwebui_client.models.knowledge_directory_update_form import KnowledgeDirectoryUpdateForm
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
    api_instance = openwebui_client.KnowledgeApi(api_client)
    id = 'id_example' # str | 
    dir_id = 'dir_id_example' # str | 
    knowledge_directory_update_form = openwebui_client.KnowledgeDirectoryUpdateForm() # KnowledgeDirectoryUpdateForm | 

    try:
        # Update Knowledge Directory
        api_response = await api_instance.update_knowledge_directory_api_v1_knowledge_id_dirs_dir_id_update_post(id, dir_id, knowledge_directory_update_form)
        print("The response of KnowledgeApi->update_knowledge_directory_api_v1_knowledge_id_dirs_dir_id_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->update_knowledge_directory_api_v1_knowledge_id_dirs_dir_id_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **dir_id** | **str**|  | 
 **knowledge_directory_update_form** | [**KnowledgeDirectoryUpdateForm**](KnowledgeDirectoryUpdateForm.md)|  | 

### Return type

[**KnowledgeDirectoryModel**](KnowledgeDirectoryModel.md)

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

