# openwebui_client.RetrievalApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_entries_from_collection_api_v1_retrieval_delete_post**](RetrievalApi.md#delete_entries_from_collection_api_v1_retrieval_delete_post) | **POST** /api/v1/retrieval/delete | Delete Entries From Collection
[**get_embedding_config_api_v1_retrieval_embedding_get**](RetrievalApi.md#get_embedding_config_api_v1_retrieval_embedding_get) | **GET** /api/v1/retrieval/embedding | Get Embedding Config
[**get_embeddings_api_v1_retrieval_ef_text_get**](RetrievalApi.md#get_embeddings_api_v1_retrieval_ef_text_get) | **GET** /api/v1/retrieval/ef/{text} | Get Embeddings
[**get_rag_config_api_v1_retrieval_config_get**](RetrievalApi.md#get_rag_config_api_v1_retrieval_config_get) | **GET** /api/v1/retrieval/config | Get Rag Config
[**process_file_api_v1_retrieval_process_file_post**](RetrievalApi.md#process_file_api_v1_retrieval_process_file_post) | **POST** /api/v1/retrieval/process/file | Process File
[**process_files_batch_api_v1_retrieval_process_files_batch_post**](RetrievalApi.md#process_files_batch_api_v1_retrieval_process_files_batch_post) | **POST** /api/v1/retrieval/process/files/batch | Process Files Batch
[**process_text_api_v1_retrieval_process_text_post**](RetrievalApi.md#process_text_api_v1_retrieval_process_text_post) | **POST** /api/v1/retrieval/process/text | Process Text
[**process_web_api_v1_retrieval_process_web_post**](RetrievalApi.md#process_web_api_v1_retrieval_process_web_post) | **POST** /api/v1/retrieval/process/web | Process Web
[**process_web_api_v1_retrieval_process_youtube_post**](RetrievalApi.md#process_web_api_v1_retrieval_process_youtube_post) | **POST** /api/v1/retrieval/process/youtube | Process Web
[**process_web_search_api_v1_retrieval_process_web_search_post**](RetrievalApi.md#process_web_search_api_v1_retrieval_process_web_search_post) | **POST** /api/v1/retrieval/process/web/search | Process Web Search
[**query_collection_handler_api_v1_retrieval_query_collection_post**](RetrievalApi.md#query_collection_handler_api_v1_retrieval_query_collection_post) | **POST** /api/v1/retrieval/query/collection | Query Collection Handler
[**query_doc_handler_api_v1_retrieval_query_doc_post**](RetrievalApi.md#query_doc_handler_api_v1_retrieval_query_doc_post) | **POST** /api/v1/retrieval/query/doc | Query Doc Handler
[**reset_upload_dir_api_v1_retrieval_reset_uploads_post**](RetrievalApi.md#reset_upload_dir_api_v1_retrieval_reset_uploads_post) | **POST** /api/v1/retrieval/reset/uploads | Reset Upload Dir
[**reset_vector_db_api_v1_retrieval_reset_db_post**](RetrievalApi.md#reset_vector_db_api_v1_retrieval_reset_db_post) | **POST** /api/v1/retrieval/reset/db | Reset Vector Db
[**update_embedding_config_api_v1_retrieval_embedding_update_post**](RetrievalApi.md#update_embedding_config_api_v1_retrieval_embedding_update_post) | **POST** /api/v1/retrieval/embedding/update | Update Embedding Config
[**update_rag_config_api_v1_retrieval_config_update_post**](RetrievalApi.md#update_rag_config_api_v1_retrieval_config_update_post) | **POST** /api/v1/retrieval/config/update | Update Rag Config


# **delete_entries_from_collection_api_v1_retrieval_delete_post**
> object delete_entries_from_collection_api_v1_retrieval_delete_post(delete_form)

Delete Entries From Collection

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.delete_form import DeleteForm
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
    api_instance = openwebui_client.RetrievalApi(api_client)
    delete_form = openwebui_client.DeleteForm() # DeleteForm | 

    try:
        # Delete Entries From Collection
        api_response = await api_instance.delete_entries_from_collection_api_v1_retrieval_delete_post(delete_form)
        print("The response of RetrievalApi->delete_entries_from_collection_api_v1_retrieval_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrievalApi->delete_entries_from_collection_api_v1_retrieval_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_form** | [**DeleteForm**](DeleteForm.md)|  | 

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

# **get_embedding_config_api_v1_retrieval_embedding_get**
> object get_embedding_config_api_v1_retrieval_embedding_get()

Get Embedding Config

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
    api_instance = openwebui_client.RetrievalApi(api_client)

    try:
        # Get Embedding Config
        api_response = await api_instance.get_embedding_config_api_v1_retrieval_embedding_get()
        print("The response of RetrievalApi->get_embedding_config_api_v1_retrieval_embedding_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrievalApi->get_embedding_config_api_v1_retrieval_embedding_get: %s\n" % e)
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

# **get_embeddings_api_v1_retrieval_ef_text_get**
> object get_embeddings_api_v1_retrieval_ef_text_get(text)

Get Embeddings

### Example


```python
import openwebui_client
from openwebui_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openwebui_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openwebui_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openwebui_client.RetrievalApi(api_client)
    text = 'text_example' # str | 

    try:
        # Get Embeddings
        api_response = await api_instance.get_embeddings_api_v1_retrieval_ef_text_get(text)
        print("The response of RetrievalApi->get_embeddings_api_v1_retrieval_ef_text_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrievalApi->get_embeddings_api_v1_retrieval_ef_text_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rag_config_api_v1_retrieval_config_get**
> object get_rag_config_api_v1_retrieval_config_get()

Get Rag Config

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
    api_instance = openwebui_client.RetrievalApi(api_client)

    try:
        # Get Rag Config
        api_response = await api_instance.get_rag_config_api_v1_retrieval_config_get()
        print("The response of RetrievalApi->get_rag_config_api_v1_retrieval_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrievalApi->get_rag_config_api_v1_retrieval_config_get: %s\n" % e)
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

# **process_file_api_v1_retrieval_process_file_post**
> object process_file_api_v1_retrieval_process_file_post(process_file_form)

Process File

Process a file and save its content to the vector database.
Process a file and save its content to the vector database.
Note: granular session management is used to prevent connection pool exhaustion.
The session is committed before external API calls, and updates use a fresh session.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.process_file_form import ProcessFileForm
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
    api_instance = openwebui_client.RetrievalApi(api_client)
    process_file_form = openwebui_client.ProcessFileForm() # ProcessFileForm | 

    try:
        # Process File
        api_response = await api_instance.process_file_api_v1_retrieval_process_file_post(process_file_form)
        print("The response of RetrievalApi->process_file_api_v1_retrieval_process_file_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrievalApi->process_file_api_v1_retrieval_process_file_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_file_form** | [**ProcessFileForm**](ProcessFileForm.md)|  | 

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

# **process_files_batch_api_v1_retrieval_process_files_batch_post**
> BatchProcessFilesResponse process_files_batch_api_v1_retrieval_process_files_batch_post(batch_process_files_form, db=db)

Process Files Batch

Process a batch of files and save them to the vector database.

NOTE: We intentionally do NOT use Depends(get_async_session) here.
The save_docs_to_vector_db() call makes external embedding API calls which
can take 5-60+ seconds for batch operations. Database operations after
embedding (Files.update_file_by_id) manage their own short-lived sessions.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.batch_process_files_form import BatchProcessFilesForm
from openwebui_client.models.batch_process_files_response import BatchProcessFilesResponse
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
    api_instance = openwebui_client.RetrievalApi(api_client)
    batch_process_files_form = openwebui_client.BatchProcessFilesForm() # BatchProcessFilesForm | 
    db = None # object |  (optional)

    try:
        # Process Files Batch
        api_response = await api_instance.process_files_batch_api_v1_retrieval_process_files_batch_post(batch_process_files_form, db=db)
        print("The response of RetrievalApi->process_files_batch_api_v1_retrieval_process_files_batch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrievalApi->process_files_batch_api_v1_retrieval_process_files_batch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_process_files_form** | [**BatchProcessFilesForm**](BatchProcessFilesForm.md)|  | 
 **db** | [**object**](.md)|  | [optional] 

### Return type

[**BatchProcessFilesResponse**](BatchProcessFilesResponse.md)

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

# **process_text_api_v1_retrieval_process_text_post**
> object process_text_api_v1_retrieval_process_text_post(process_text_form)

Process Text

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.process_text_form import ProcessTextForm
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
    api_instance = openwebui_client.RetrievalApi(api_client)
    process_text_form = openwebui_client.ProcessTextForm() # ProcessTextForm | 

    try:
        # Process Text
        api_response = await api_instance.process_text_api_v1_retrieval_process_text_post(process_text_form)
        print("The response of RetrievalApi->process_text_api_v1_retrieval_process_text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrievalApi->process_text_api_v1_retrieval_process_text_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_text_form** | [**ProcessTextForm**](ProcessTextForm.md)|  | 

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

# **process_web_api_v1_retrieval_process_web_post**
> object process_web_api_v1_retrieval_process_web_post(process_url_form, process=process, overwrite=overwrite)

Process Web

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.process_url_form import ProcessUrlForm
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
    api_instance = openwebui_client.RetrievalApi(api_client)
    process_url_form = openwebui_client.ProcessUrlForm() # ProcessUrlForm | 
    process = True # bool | Whether to process and save the content (optional) (default to True)
    overwrite = True # bool | Whether to overwrite existing collection (optional) (default to True)

    try:
        # Process Web
        api_response = await api_instance.process_web_api_v1_retrieval_process_web_post(process_url_form, process=process, overwrite=overwrite)
        print("The response of RetrievalApi->process_web_api_v1_retrieval_process_web_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrievalApi->process_web_api_v1_retrieval_process_web_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_url_form** | [**ProcessUrlForm**](ProcessUrlForm.md)|  | 
 **process** | **bool**| Whether to process and save the content | [optional] [default to True]
 **overwrite** | **bool**| Whether to overwrite existing collection | [optional] [default to True]

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

# **process_web_api_v1_retrieval_process_youtube_post**
> object process_web_api_v1_retrieval_process_youtube_post(process_url_form, process=process, overwrite=overwrite)

Process Web

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.process_url_form import ProcessUrlForm
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
    api_instance = openwebui_client.RetrievalApi(api_client)
    process_url_form = openwebui_client.ProcessUrlForm() # ProcessUrlForm | 
    process = True # bool | Whether to process and save the content (optional) (default to True)
    overwrite = True # bool | Whether to overwrite existing collection (optional) (default to True)

    try:
        # Process Web
        api_response = await api_instance.process_web_api_v1_retrieval_process_youtube_post(process_url_form, process=process, overwrite=overwrite)
        print("The response of RetrievalApi->process_web_api_v1_retrieval_process_youtube_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrievalApi->process_web_api_v1_retrieval_process_youtube_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_url_form** | [**ProcessUrlForm**](ProcessUrlForm.md)|  | 
 **process** | **bool**| Whether to process and save the content | [optional] [default to True]
 **overwrite** | **bool**| Whether to overwrite existing collection | [optional] [default to True]

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

# **process_web_search_api_v1_retrieval_process_web_search_post**
> object process_web_search_api_v1_retrieval_process_web_search_post(search_form)

Process Web Search

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.search_form import SearchForm
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
    api_instance = openwebui_client.RetrievalApi(api_client)
    search_form = openwebui_client.SearchForm() # SearchForm | 

    try:
        # Process Web Search
        api_response = await api_instance.process_web_search_api_v1_retrieval_process_web_search_post(search_form)
        print("The response of RetrievalApi->process_web_search_api_v1_retrieval_process_web_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrievalApi->process_web_search_api_v1_retrieval_process_web_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_form** | [**SearchForm**](SearchForm.md)|  | 

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

# **query_collection_handler_api_v1_retrieval_query_collection_post**
> object query_collection_handler_api_v1_retrieval_query_collection_post(query_collections_form)

Query Collection Handler

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.query_collections_form import QueryCollectionsForm
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
    api_instance = openwebui_client.RetrievalApi(api_client)
    query_collections_form = openwebui_client.QueryCollectionsForm() # QueryCollectionsForm | 

    try:
        # Query Collection Handler
        api_response = await api_instance.query_collection_handler_api_v1_retrieval_query_collection_post(query_collections_form)
        print("The response of RetrievalApi->query_collection_handler_api_v1_retrieval_query_collection_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrievalApi->query_collection_handler_api_v1_retrieval_query_collection_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_collections_form** | [**QueryCollectionsForm**](QueryCollectionsForm.md)|  | 

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

# **query_doc_handler_api_v1_retrieval_query_doc_post**
> object query_doc_handler_api_v1_retrieval_query_doc_post(query_doc_form)

Query Doc Handler

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.query_doc_form import QueryDocForm
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
    api_instance = openwebui_client.RetrievalApi(api_client)
    query_doc_form = openwebui_client.QueryDocForm() # QueryDocForm | 

    try:
        # Query Doc Handler
        api_response = await api_instance.query_doc_handler_api_v1_retrieval_query_doc_post(query_doc_form)
        print("The response of RetrievalApi->query_doc_handler_api_v1_retrieval_query_doc_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrievalApi->query_doc_handler_api_v1_retrieval_query_doc_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_doc_form** | [**QueryDocForm**](QueryDocForm.md)|  | 

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

# **reset_upload_dir_api_v1_retrieval_reset_uploads_post**
> bool reset_upload_dir_api_v1_retrieval_reset_uploads_post()

Reset Upload Dir

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
    api_instance = openwebui_client.RetrievalApi(api_client)

    try:
        # Reset Upload Dir
        api_response = await api_instance.reset_upload_dir_api_v1_retrieval_reset_uploads_post()
        print("The response of RetrievalApi->reset_upload_dir_api_v1_retrieval_reset_uploads_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrievalApi->reset_upload_dir_api_v1_retrieval_reset_uploads_post: %s\n" % e)
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

# **reset_vector_db_api_v1_retrieval_reset_db_post**
> object reset_vector_db_api_v1_retrieval_reset_db_post()

Reset Vector Db

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
    api_instance = openwebui_client.RetrievalApi(api_client)

    try:
        # Reset Vector Db
        api_response = await api_instance.reset_vector_db_api_v1_retrieval_reset_db_post()
        print("The response of RetrievalApi->reset_vector_db_api_v1_retrieval_reset_db_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrievalApi->reset_vector_db_api_v1_retrieval_reset_db_post: %s\n" % e)
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

# **update_embedding_config_api_v1_retrieval_embedding_update_post**
> object update_embedding_config_api_v1_retrieval_embedding_update_post(embedding_model_update_form)

Update Embedding Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.embedding_model_update_form import EmbeddingModelUpdateForm
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
    api_instance = openwebui_client.RetrievalApi(api_client)
    embedding_model_update_form = openwebui_client.EmbeddingModelUpdateForm() # EmbeddingModelUpdateForm | 

    try:
        # Update Embedding Config
        api_response = await api_instance.update_embedding_config_api_v1_retrieval_embedding_update_post(embedding_model_update_form)
        print("The response of RetrievalApi->update_embedding_config_api_v1_retrieval_embedding_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrievalApi->update_embedding_config_api_v1_retrieval_embedding_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embedding_model_update_form** | [**EmbeddingModelUpdateForm**](EmbeddingModelUpdateForm.md)|  | 

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

# **update_rag_config_api_v1_retrieval_config_update_post**
> object update_rag_config_api_v1_retrieval_config_update_post(config_form)

Update Rag Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.config_form import ConfigForm
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
    api_instance = openwebui_client.RetrievalApi(api_client)
    config_form = openwebui_client.ConfigForm() # ConfigForm | 

    try:
        # Update Rag Config
        api_response = await api_instance.update_rag_config_api_v1_retrieval_config_update_post(config_form)
        print("The response of RetrievalApi->update_rag_config_api_v1_retrieval_config_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetrievalApi->update_rag_config_api_v1_retrieval_config_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_form** | [**ConfigForm**](ConfigForm.md)|  | 

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

