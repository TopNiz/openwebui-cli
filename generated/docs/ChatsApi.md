# openwebui_client.ChatsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tag_by_id_and_tag_name_api_v1_chats_id_tags_post**](ChatsApi.md#add_tag_by_id_and_tag_name_api_v1_chats_id_tags_post) | **POST** /api/v1/chats/{id}/tags | Add Tag By Id And Tag Name
[**archive_all_chats_api_v1_chats_archive_all_post**](ChatsApi.md#archive_all_chats_api_v1_chats_archive_all_post) | **POST** /api/v1/chats/archive/all | Archive All Chats
[**archive_chat_by_id_api_v1_chats_id_archive_post**](ChatsApi.md#archive_chat_by_id_api_v1_chats_id_archive_post) | **POST** /api/v1/chats/{id}/archive | Archive Chat By Id
[**clone_chat_by_id_api_v1_chats_id_clone_post**](ChatsApi.md#clone_chat_by_id_api_v1_chats_id_clone_post) | **POST** /api/v1/chats/{id}/clone | Clone Chat By Id
[**clone_shared_chat_by_id_api_v1_chats_id_clone_shared_post**](ChatsApi.md#clone_shared_chat_by_id_api_v1_chats_id_clone_shared_post) | **POST** /api/v1/chats/{id}/clone/shared | Clone Shared Chat By Id
[**compact_chat_by_id_api_v1_chats_id_compact_post**](ChatsApi.md#compact_chat_by_id_api_v1_chats_id_compact_post) | **POST** /api/v1/chats/{id}/compact | Compact Chat By Id
[**create_new_chat_api_v1_chats_new_post**](ChatsApi.md#create_new_chat_api_v1_chats_new_post) | **POST** /api/v1/chats/new | Create New Chat
[**delete_all_user_chats_api_v1_chats_delete**](ChatsApi.md#delete_all_user_chats_api_v1_chats_delete) | **DELETE** /api/v1/chats/ | Delete All User Chats
[**delete_chat_by_id_api_v1_chats_id_delete**](ChatsApi.md#delete_chat_by_id_api_v1_chats_id_delete) | **DELETE** /api/v1/chats/{id} | Delete Chat By Id
[**delete_chat_message_by_id_api_v1_chats_id_messages_message_id_delete**](ChatsApi.md#delete_chat_message_by_id_api_v1_chats_id_messages_message_id_delete) | **DELETE** /api/v1/chats/{id}/messages/{message_id} | Delete Chat Message By Id
[**delete_shared_chat_by_id_api_v1_chats_id_share_delete**](ChatsApi.md#delete_shared_chat_by_id_api_v1_chats_id_share_delete) | **DELETE** /api/v1/chats/{id}/share | Delete Shared Chat By Id
[**delete_tag_by_id_and_tag_name_api_v1_chats_id_tags_delete**](ChatsApi.md#delete_tag_by_id_and_tag_name_api_v1_chats_id_tags_delete) | **DELETE** /api/v1/chats/{id}/tags | Delete Tag By Id And Tag Name
[**export_chat_stats_api_v1_chats_stats_export_get**](ChatsApi.md#export_chat_stats_api_v1_chats_stats_export_get) | **GET** /api/v1/chats/stats/export | Export Chat Stats
[**export_single_chat_stats_api_v1_chats_stats_export_chat_id_get**](ChatsApi.md#export_single_chat_stats_api_v1_chats_stats_export_chat_id_get) | **GET** /api/v1/chats/stats/export/{chat_id} | Export Single Chat Stats
[**fork_chat_by_id_api_v1_chats_id_fork_post**](ChatsApi.md#fork_chat_by_id_api_v1_chats_id_fork_post) | **POST** /api/v1/chats/{id}/fork | Fork Chat By Id
[**get_all_user_chats_in_db_api_v1_chats_all_db_get**](ChatsApi.md#get_all_user_chats_in_db_api_v1_chats_all_db_get) | **GET** /api/v1/chats/all/db | Get All User Chats In Db
[**get_all_user_tags_api_v1_chats_all_tags_get**](ChatsApi.md#get_all_user_tags_api_v1_chats_all_tags_get) | **GET** /api/v1/chats/all/tags | Get All User Tags
[**get_archived_session_user_chat_count_api_v1_chats_archived_count_get**](ChatsApi.md#get_archived_session_user_chat_count_api_v1_chats_archived_count_get) | **GET** /api/v1/chats/archived/count | Get Archived Session User Chat Count
[**get_archived_session_user_chat_list_api_v1_chats_archived_get**](ChatsApi.md#get_archived_session_user_chat_list_api_v1_chats_archived_get) | **GET** /api/v1/chats/archived | Get Archived Session User Chat List
[**get_chat_by_id_api_v1_chats_id_get**](ChatsApi.md#get_chat_by_id_api_v1_chats_id_get) | **GET** /api/v1/chats/{id} | Get Chat By Id
[**get_chat_config_api_v1_chats_config_get**](ChatsApi.md#get_chat_config_api_v1_chats_config_get) | **GET** /api/v1/chats/config | Get Chat Config
[**get_chat_list_by_folder_id_api_v1_chats_folder_folder_id_list_get**](ChatsApi.md#get_chat_list_by_folder_id_api_v1_chats_folder_folder_id_list_get) | **GET** /api/v1/chats/folder/{folder_id}/list | Get Chat List By Folder Id
[**get_chat_tags_by_id_api_v1_chats_id_tags_get**](ChatsApi.md#get_chat_tags_by_id_api_v1_chats_id_tags_get) | **GET** /api/v1/chats/{id}/tags | Get Chat Tags By Id
[**get_chats_by_folder_id_api_v1_chats_folder_folder_id_get**](ChatsApi.md#get_chats_by_folder_id_api_v1_chats_folder_folder_id_get) | **GET** /api/v1/chats/folder/{folder_id} | Get Chats By Folder Id
[**get_pinned_status_by_id_api_v1_chats_id_pinned_get**](ChatsApi.md#get_pinned_status_by_id_api_v1_chats_id_pinned_get) | **GET** /api/v1/chats/{id}/pinned | Get Pinned Status By Id
[**get_session_user_chat_list_api_v1_chats_get**](ChatsApi.md#get_session_user_chat_list_api_v1_chats_get) | **GET** /api/v1/chats/ | Get Session User Chat List
[**get_session_user_chat_list_api_v1_chats_list_get**](ChatsApi.md#get_session_user_chat_list_api_v1_chats_list_get) | **GET** /api/v1/chats/list | Get Session User Chat List
[**get_session_user_chat_usage_stats_api_v1_chats_stats_usage_get**](ChatsApi.md#get_session_user_chat_usage_stats_api_v1_chats_stats_usage_get) | **GET** /api/v1/chats/stats/usage | Get Session User Chat Usage Stats
[**get_shared_chat_access_by_id_api_v1_chats_shared_id_access_get**](ChatsApi.md#get_shared_chat_access_by_id_api_v1_chats_shared_id_access_get) | **GET** /api/v1/chats/shared/{id}/access | Get Shared Chat Access By Id
[**get_shared_chat_by_id_api_v1_chats_share_share_id_get**](ChatsApi.md#get_shared_chat_by_id_api_v1_chats_share_share_id_get) | **GET** /api/v1/chats/share/{share_id} | Get Shared Chat By Id
[**get_shared_session_user_chat_list_api_v1_chats_shared_get**](ChatsApi.md#get_shared_session_user_chat_list_api_v1_chats_shared_get) | **GET** /api/v1/chats/shared | Get Shared Session User Chat List
[**get_user_archived_chats_api_v1_chats_all_archived_get**](ChatsApi.md#get_user_archived_chats_api_v1_chats_all_archived_get) | **GET** /api/v1/chats/all/archived | Get User Archived Chats
[**get_user_chat_list_by_tag_name_api_v1_chats_tags_post**](ChatsApi.md#get_user_chat_list_by_tag_name_api_v1_chats_tags_post) | **POST** /api/v1/chats/tags | Get User Chat List By Tag Name
[**get_user_chat_list_by_user_id_api_v1_chats_list_user_user_id_get**](ChatsApi.md#get_user_chat_list_by_user_id_api_v1_chats_list_user_user_id_get) | **GET** /api/v1/chats/list/user/{user_id} | Get User Chat List By User Id
[**get_user_chats_api_v1_chats_all_get**](ChatsApi.md#get_user_chats_api_v1_chats_all_get) | **GET** /api/v1/chats/all | Get User Chats
[**get_user_pinned_chats_api_v1_chats_pinned_get**](ChatsApi.md#get_user_pinned_chats_api_v1_chats_pinned_get) | **GET** /api/v1/chats/pinned | Get User Pinned Chats
[**import_chats_api_v1_chats_import_post**](ChatsApi.md#import_chats_api_v1_chats_import_post) | **POST** /api/v1/chats/import | Import Chats
[**mark_chat_unread_by_id_api_v1_chats_id_unread_post**](ChatsApi.md#mark_chat_unread_by_id_api_v1_chats_id_unread_post) | **POST** /api/v1/chats/{id}/unread | Mark Chat Unread By Id
[**mark_chats_read_by_user_id_api_v1_chats_read_post**](ChatsApi.md#mark_chats_read_by_user_id_api_v1_chats_read_post) | **POST** /api/v1/chats/read | Mark Chats Read By User Id
[**pin_chat_by_id_api_v1_chats_id_pin_post**](ChatsApi.md#pin_chat_by_id_api_v1_chats_id_pin_post) | **POST** /api/v1/chats/{id}/pin | Pin Chat By Id
[**search_user_chats_api_v1_chats_search_get**](ChatsApi.md#search_user_chats_api_v1_chats_search_get) | **GET** /api/v1/chats/search | Search User Chats
[**send_chat_message_event_by_id_api_v1_chats_id_messages_message_id_event_post**](ChatsApi.md#send_chat_message_event_by_id_api_v1_chats_id_messages_message_id_event_post) | **POST** /api/v1/chats/{id}/messages/{message_id}/event | Send Chat Message Event By Id
[**set_chat_config_api_v1_chats_config_post**](ChatsApi.md#set_chat_config_api_v1_chats_config_post) | **POST** /api/v1/chats/config | Set Chat Config
[**share_chat_by_id_api_v1_chats_id_share_post**](ChatsApi.md#share_chat_by_id_api_v1_chats_id_share_post) | **POST** /api/v1/chats/{id}/share | Share Chat By Id
[**unarchive_all_chats_api_v1_chats_unarchive_all_post**](ChatsApi.md#unarchive_all_chats_api_v1_chats_unarchive_all_post) | **POST** /api/v1/chats/unarchive/all | Unarchive All Chats
[**unshare_all_chats_api_v1_chats_share_all_delete**](ChatsApi.md#unshare_all_chats_api_v1_chats_share_all_delete) | **DELETE** /api/v1/chats/share/all | Unshare All Chats
[**update_chat_by_id_api_v1_chats_id_post**](ChatsApi.md#update_chat_by_id_api_v1_chats_id_post) | **POST** /api/v1/chats/{id} | Update Chat By Id
[**update_chat_folder_id_by_id_api_v1_chats_id_folder_post**](ChatsApi.md#update_chat_folder_id_by_id_api_v1_chats_id_folder_post) | **POST** /api/v1/chats/{id}/folder | Update Chat Folder Id By Id
[**update_chat_message_by_id_api_v1_chats_id_messages_message_id_post**](ChatsApi.md#update_chat_message_by_id_api_v1_chats_id_messages_message_id_post) | **POST** /api/v1/chats/{id}/messages/{message_id} | Update Chat Message By Id
[**update_shared_chat_access_by_id_api_v1_chats_shared_id_access_update_post**](ChatsApi.md#update_shared_chat_access_by_id_api_v1_chats_shared_id_access_update_post) | **POST** /api/v1/chats/shared/{id}/access/update | Update Shared Chat Access By Id


# **add_tag_by_id_and_tag_name_api_v1_chats_id_tags_post**
> List[TagModel] add_tag_by_id_and_tag_name_api_v1_chats_id_tags_post(id, tag_form)

Add Tag By Id And Tag Name

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.tag_form import TagForm
from openwebui_client.models.tag_model import TagModel
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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 
    tag_form = openwebui_client.TagForm() # TagForm | 

    try:
        # Add Tag By Id And Tag Name
        api_response = await api_instance.add_tag_by_id_and_tag_name_api_v1_chats_id_tags_post(id, tag_form)
        print("The response of ChatsApi->add_tag_by_id_and_tag_name_api_v1_chats_id_tags_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->add_tag_by_id_and_tag_name_api_v1_chats_id_tags_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tag_form** | [**TagForm**](TagForm.md)|  | 

### Return type

[**List[TagModel]**](TagModel.md)

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

# **archive_all_chats_api_v1_chats_archive_all_post**
> bool archive_all_chats_api_v1_chats_archive_all_post()

Archive All Chats

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
    api_instance = openwebui_client.ChatsApi(api_client)

    try:
        # Archive All Chats
        api_response = await api_instance.archive_all_chats_api_v1_chats_archive_all_post()
        print("The response of ChatsApi->archive_all_chats_api_v1_chats_archive_all_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->archive_all_chats_api_v1_chats_archive_all_post: %s\n" % e)
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

# **archive_chat_by_id_api_v1_chats_id_archive_post**
> ChatResponse archive_chat_by_id_api_v1_chats_id_archive_post(id)

Archive Chat By Id

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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Archive Chat By Id
        api_response = await api_instance.archive_chat_by_id_api_v1_chats_id_archive_post(id)
        print("The response of ChatsApi->archive_chat_by_id_api_v1_chats_id_archive_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->archive_chat_by_id_api_v1_chats_id_archive_post: %s\n" % e)
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

# **clone_chat_by_id_api_v1_chats_id_clone_post**
> ChatResponse clone_chat_by_id_api_v1_chats_id_clone_post(id, clone_form)

Clone Chat By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_response import ChatResponse
from openwebui_client.models.clone_form import CloneForm
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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 
    clone_form = openwebui_client.CloneForm() # CloneForm | 

    try:
        # Clone Chat By Id
        api_response = await api_instance.clone_chat_by_id_api_v1_chats_id_clone_post(id, clone_form)
        print("The response of ChatsApi->clone_chat_by_id_api_v1_chats_id_clone_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->clone_chat_by_id_api_v1_chats_id_clone_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **clone_form** | [**CloneForm**](CloneForm.md)|  | 

### Return type

[**ChatResponse**](ChatResponse.md)

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

# **clone_shared_chat_by_id_api_v1_chats_id_clone_shared_post**
> ChatResponse clone_shared_chat_by_id_api_v1_chats_id_clone_shared_post(id)

Clone Shared Chat By Id

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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Clone Shared Chat By Id
        api_response = await api_instance.clone_shared_chat_by_id_api_v1_chats_id_clone_shared_post(id)
        print("The response of ChatsApi->clone_shared_chat_by_id_api_v1_chats_id_clone_shared_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->clone_shared_chat_by_id_api_v1_chats_id_clone_shared_post: %s\n" % e)
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

# **compact_chat_by_id_api_v1_chats_id_compact_post**
> object compact_chat_by_id_api_v1_chats_id_compact_post(id, compact_chat_form=compact_chat_form)

Compact Chat By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.compact_chat_form import CompactChatForm
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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 
    compact_chat_form = openwebui_client.CompactChatForm() # CompactChatForm |  (optional)

    try:
        # Compact Chat By Id
        api_response = await api_instance.compact_chat_by_id_api_v1_chats_id_compact_post(id, compact_chat_form=compact_chat_form)
        print("The response of ChatsApi->compact_chat_by_id_api_v1_chats_id_compact_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->compact_chat_by_id_api_v1_chats_id_compact_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **compact_chat_form** | [**CompactChatForm**](CompactChatForm.md)|  | [optional] 

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

# **create_new_chat_api_v1_chats_new_post**
> ChatResponse create_new_chat_api_v1_chats_new_post(chat_form)

Create New Chat

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_form import ChatForm
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
    api_instance = openwebui_client.ChatsApi(api_client)
    chat_form = openwebui_client.ChatForm() # ChatForm | 

    try:
        # Create New Chat
        api_response = await api_instance.create_new_chat_api_v1_chats_new_post(chat_form)
        print("The response of ChatsApi->create_new_chat_api_v1_chats_new_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->create_new_chat_api_v1_chats_new_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_form** | [**ChatForm**](ChatForm.md)|  | 

### Return type

[**ChatResponse**](ChatResponse.md)

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

# **delete_all_user_chats_api_v1_chats_delete**
> bool delete_all_user_chats_api_v1_chats_delete()

Delete All User Chats

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
    api_instance = openwebui_client.ChatsApi(api_client)

    try:
        # Delete All User Chats
        api_response = await api_instance.delete_all_user_chats_api_v1_chats_delete()
        print("The response of ChatsApi->delete_all_user_chats_api_v1_chats_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->delete_all_user_chats_api_v1_chats_delete: %s\n" % e)
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

# **delete_chat_by_id_api_v1_chats_id_delete**
> bool delete_chat_by_id_api_v1_chats_id_delete(id)

Delete Chat By Id

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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Chat By Id
        api_response = await api_instance.delete_chat_by_id_api_v1_chats_id_delete(id)
        print("The response of ChatsApi->delete_chat_by_id_api_v1_chats_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->delete_chat_by_id_api_v1_chats_id_delete: %s\n" % e)
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

# **delete_chat_message_by_id_api_v1_chats_id_messages_message_id_delete**
> ChatResponse delete_chat_message_by_id_api_v1_chats_id_messages_message_id_delete(id, message_id)

Delete Chat Message By Id

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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        # Delete Chat Message By Id
        api_response = await api_instance.delete_chat_message_by_id_api_v1_chats_id_messages_message_id_delete(id, message_id)
        print("The response of ChatsApi->delete_chat_message_by_id_api_v1_chats_id_messages_message_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->delete_chat_message_by_id_api_v1_chats_id_messages_message_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **message_id** | **str**|  | 

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

# **delete_shared_chat_by_id_api_v1_chats_id_share_delete**
> bool delete_shared_chat_by_id_api_v1_chats_id_share_delete(id)

Delete Shared Chat By Id

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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Shared Chat By Id
        api_response = await api_instance.delete_shared_chat_by_id_api_v1_chats_id_share_delete(id)
        print("The response of ChatsApi->delete_shared_chat_by_id_api_v1_chats_id_share_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->delete_shared_chat_by_id_api_v1_chats_id_share_delete: %s\n" % e)
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

# **delete_tag_by_id_and_tag_name_api_v1_chats_id_tags_delete**
> List[TagModel] delete_tag_by_id_and_tag_name_api_v1_chats_id_tags_delete(id, tag_form)

Delete Tag By Id And Tag Name

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.tag_form import TagForm
from openwebui_client.models.tag_model import TagModel
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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 
    tag_form = openwebui_client.TagForm() # TagForm | 

    try:
        # Delete Tag By Id And Tag Name
        api_response = await api_instance.delete_tag_by_id_and_tag_name_api_v1_chats_id_tags_delete(id, tag_form)
        print("The response of ChatsApi->delete_tag_by_id_and_tag_name_api_v1_chats_id_tags_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->delete_tag_by_id_and_tag_name_api_v1_chats_id_tags_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tag_form** | [**TagForm**](TagForm.md)|  | 

### Return type

[**List[TagModel]**](TagModel.md)

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

# **export_chat_stats_api_v1_chats_stats_export_get**
> ChatStatsExportList export_chat_stats_api_v1_chats_stats_export_get(updated_at=updated_at, page=page, stream=stream)

Export Chat Stats

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_stats_export_list import ChatStatsExportList
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
    api_instance = openwebui_client.ChatsApi(api_client)
    updated_at = 56 # int |  (optional)
    page = 56 # int |  (optional)
    stream = False # bool |  (optional) (default to False)

    try:
        # Export Chat Stats
        api_response = await api_instance.export_chat_stats_api_v1_chats_stats_export_get(updated_at=updated_at, page=page, stream=stream)
        print("The response of ChatsApi->export_chat_stats_api_v1_chats_stats_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->export_chat_stats_api_v1_chats_stats_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_at** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 
 **stream** | **bool**|  | [optional] [default to False]

### Return type

[**ChatStatsExportList**](ChatStatsExportList.md)

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

# **export_single_chat_stats_api_v1_chats_stats_export_chat_id_get**
> ChatStatsExport export_single_chat_stats_api_v1_chats_stats_export_chat_id_get(chat_id)

Export Single Chat Stats

Export stats for exactly one chat by ID.
Returns ChatStatsExport for the specified chat.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_stats_export import ChatStatsExport
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
    api_instance = openwebui_client.ChatsApi(api_client)
    chat_id = 'chat_id_example' # str | 

    try:
        # Export Single Chat Stats
        api_response = await api_instance.export_single_chat_stats_api_v1_chats_stats_export_chat_id_get(chat_id)
        print("The response of ChatsApi->export_single_chat_stats_api_v1_chats_stats_export_chat_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->export_single_chat_stats_api_v1_chats_stats_export_chat_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **str**|  | 

### Return type

[**ChatStatsExport**](ChatStatsExport.md)

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

# **fork_chat_by_id_api_v1_chats_id_fork_post**
> ChatResponse fork_chat_by_id_api_v1_chats_id_fork_post(id, fork_form=fork_form)

Fork Chat By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_response import ChatResponse
from openwebui_client.models.fork_form import ForkForm
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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 
    fork_form = openwebui_client.ForkForm() # ForkForm |  (optional)

    try:
        # Fork Chat By Id
        api_response = await api_instance.fork_chat_by_id_api_v1_chats_id_fork_post(id, fork_form=fork_form)
        print("The response of ChatsApi->fork_chat_by_id_api_v1_chats_id_fork_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->fork_chat_by_id_api_v1_chats_id_fork_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **fork_form** | [**ForkForm**](ForkForm.md)|  | [optional] 

### Return type

[**ChatResponse**](ChatResponse.md)

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

# **get_all_user_chats_in_db_api_v1_chats_all_db_get**
> List[ChatResponse] get_all_user_chats_in_db_api_v1_chats_all_db_get()

Get All User Chats In Db

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
    api_instance = openwebui_client.ChatsApi(api_client)

    try:
        # Get All User Chats In Db
        api_response = await api_instance.get_all_user_chats_in_db_api_v1_chats_all_db_get()
        print("The response of ChatsApi->get_all_user_chats_in_db_api_v1_chats_all_db_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_all_user_chats_in_db_api_v1_chats_all_db_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ChatResponse]**](ChatResponse.md)

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

# **get_all_user_tags_api_v1_chats_all_tags_get**
> List[TagModel] get_all_user_tags_api_v1_chats_all_tags_get()

Get All User Tags

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.tag_model import TagModel
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
    api_instance = openwebui_client.ChatsApi(api_client)

    try:
        # Get All User Tags
        api_response = await api_instance.get_all_user_tags_api_v1_chats_all_tags_get()
        print("The response of ChatsApi->get_all_user_tags_api_v1_chats_all_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_all_user_tags_api_v1_chats_all_tags_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TagModel]**](TagModel.md)

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

# **get_archived_session_user_chat_count_api_v1_chats_archived_count_get**
> int get_archived_session_user_chat_count_api_v1_chats_archived_count_get()

Get Archived Session User Chat Count

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
    api_instance = openwebui_client.ChatsApi(api_client)

    try:
        # Get Archived Session User Chat Count
        api_response = await api_instance.get_archived_session_user_chat_count_api_v1_chats_archived_count_get()
        print("The response of ChatsApi->get_archived_session_user_chat_count_api_v1_chats_archived_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_archived_session_user_chat_count_api_v1_chats_archived_count_get: %s\n" % e)
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

# **get_archived_session_user_chat_list_api_v1_chats_archived_get**
> List[ChatTitleIdResponse] get_archived_session_user_chat_list_api_v1_chats_archived_get(page=page, query=query, order_by=order_by, direction=direction)

Get Archived Session User Chat List

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_title_id_response import ChatTitleIdResponse
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
    api_instance = openwebui_client.ChatsApi(api_client)
    page = 56 # int |  (optional)
    query = 'query_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    direction = 'direction_example' # str |  (optional)

    try:
        # Get Archived Session User Chat List
        api_response = await api_instance.get_archived_session_user_chat_list_api_v1_chats_archived_get(page=page, query=query, order_by=order_by, direction=direction)
        print("The response of ChatsApi->get_archived_session_user_chat_list_api_v1_chats_archived_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_archived_session_user_chat_list_api_v1_chats_archived_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **query** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] 

### Return type

[**List[ChatTitleIdResponse]**](ChatTitleIdResponse.md)

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

# **get_chat_by_id_api_v1_chats_id_get**
> ChatResponse get_chat_by_id_api_v1_chats_id_get(id)

Get Chat By Id

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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Chat By Id
        api_response = await api_instance.get_chat_by_id_api_v1_chats_id_get(id)
        print("The response of ChatsApi->get_chat_by_id_api_v1_chats_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_chat_by_id_api_v1_chats_id_get: %s\n" % e)
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

# **get_chat_config_api_v1_chats_config_get**
> ChatConfigForm get_chat_config_api_v1_chats_config_get()

Get Chat Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_config_form import ChatConfigForm
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
    api_instance = openwebui_client.ChatsApi(api_client)

    try:
        # Get Chat Config
        api_response = await api_instance.get_chat_config_api_v1_chats_config_get()
        print("The response of ChatsApi->get_chat_config_api_v1_chats_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_chat_config_api_v1_chats_config_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ChatConfigForm**](ChatConfigForm.md)

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

# **get_chat_list_by_folder_id_api_v1_chats_folder_folder_id_list_get**
> List[ChatTitleIdResponse] get_chat_list_by_folder_id_api_v1_chats_folder_folder_id_list_get(folder_id, page=page, sort_by=sort_by, sort_dir=sort_dir)

Get Chat List By Folder Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_title_id_response import ChatTitleIdResponse
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
    api_instance = openwebui_client.ChatsApi(api_client)
    folder_id = 'folder_id_example' # str | 
    page = 56 # int |  (optional)
    sort_by = 'unread_updated_at' # str |  (optional) (default to 'unread_updated_at')
    sort_dir = 'desc' # str |  (optional) (default to 'desc')

    try:
        # Get Chat List By Folder Id
        api_response = await api_instance.get_chat_list_by_folder_id_api_v1_chats_folder_folder_id_list_get(folder_id, page=page, sort_by=sort_by, sort_dir=sort_dir)
        print("The response of ChatsApi->get_chat_list_by_folder_id_api_v1_chats_folder_folder_id_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_chat_list_by_folder_id_api_v1_chats_folder_folder_id_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 
 **page** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;unread_updated_at&#39;]
 **sort_dir** | **str**|  | [optional] [default to &#39;desc&#39;]

### Return type

[**List[ChatTitleIdResponse]**](ChatTitleIdResponse.md)

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

# **get_chat_tags_by_id_api_v1_chats_id_tags_get**
> List[TagModel] get_chat_tags_by_id_api_v1_chats_id_tags_get(id)

Get Chat Tags By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.tag_model import TagModel
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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Chat Tags By Id
        api_response = await api_instance.get_chat_tags_by_id_api_v1_chats_id_tags_get(id)
        print("The response of ChatsApi->get_chat_tags_by_id_api_v1_chats_id_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_chat_tags_by_id_api_v1_chats_id_tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[TagModel]**](TagModel.md)

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

# **get_chats_by_folder_id_api_v1_chats_folder_folder_id_get**
> List[ChatResponse] get_chats_by_folder_id_api_v1_chats_folder_folder_id_get(folder_id)

Get Chats By Folder Id

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
    api_instance = openwebui_client.ChatsApi(api_client)
    folder_id = 'folder_id_example' # str | 

    try:
        # Get Chats By Folder Id
        api_response = await api_instance.get_chats_by_folder_id_api_v1_chats_folder_folder_id_get(folder_id)
        print("The response of ChatsApi->get_chats_by_folder_id_api_v1_chats_folder_folder_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_chats_by_folder_id_api_v1_chats_folder_folder_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 

### Return type

[**List[ChatResponse]**](ChatResponse.md)

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

# **get_pinned_status_by_id_api_v1_chats_id_pinned_get**
> bool get_pinned_status_by_id_api_v1_chats_id_pinned_get(id)

Get Pinned Status By Id

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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Pinned Status By Id
        api_response = await api_instance.get_pinned_status_by_id_api_v1_chats_id_pinned_get(id)
        print("The response of ChatsApi->get_pinned_status_by_id_api_v1_chats_id_pinned_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_pinned_status_by_id_api_v1_chats_id_pinned_get: %s\n" % e)
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

# **get_session_user_chat_list_api_v1_chats_get**
> List[ChatTitleIdResponse] get_session_user_chat_list_api_v1_chats_get(page=page, include_pinned=include_pinned, include_folders=include_folders, sort_by=sort_by, sort_dir=sort_dir)

Get Session User Chat List

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_title_id_response import ChatTitleIdResponse
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
    api_instance = openwebui_client.ChatsApi(api_client)
    page = 56 # int |  (optional)
    include_pinned = True # bool |  (optional)
    include_folders = True # bool |  (optional)
    sort_by = 'updated_at' # str |  (optional) (default to 'updated_at')
    sort_dir = 'desc' # str |  (optional) (default to 'desc')

    try:
        # Get Session User Chat List
        api_response = await api_instance.get_session_user_chat_list_api_v1_chats_get(page=page, include_pinned=include_pinned, include_folders=include_folders, sort_by=sort_by, sort_dir=sort_dir)
        print("The response of ChatsApi->get_session_user_chat_list_api_v1_chats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_session_user_chat_list_api_v1_chats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **include_pinned** | **bool**|  | [optional] 
 **include_folders** | **bool**|  | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;updated_at&#39;]
 **sort_dir** | **str**|  | [optional] [default to &#39;desc&#39;]

### Return type

[**List[ChatTitleIdResponse]**](ChatTitleIdResponse.md)

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

# **get_session_user_chat_list_api_v1_chats_list_get**
> List[ChatTitleIdResponse] get_session_user_chat_list_api_v1_chats_list_get(page=page, include_pinned=include_pinned, include_folders=include_folders, sort_by=sort_by, sort_dir=sort_dir)

Get Session User Chat List

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_title_id_response import ChatTitleIdResponse
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
    api_instance = openwebui_client.ChatsApi(api_client)
    page = 56 # int |  (optional)
    include_pinned = True # bool |  (optional)
    include_folders = True # bool |  (optional)
    sort_by = 'updated_at' # str |  (optional) (default to 'updated_at')
    sort_dir = 'desc' # str |  (optional) (default to 'desc')

    try:
        # Get Session User Chat List
        api_response = await api_instance.get_session_user_chat_list_api_v1_chats_list_get(page=page, include_pinned=include_pinned, include_folders=include_folders, sort_by=sort_by, sort_dir=sort_dir)
        print("The response of ChatsApi->get_session_user_chat_list_api_v1_chats_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_session_user_chat_list_api_v1_chats_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **include_pinned** | **bool**|  | [optional] 
 **include_folders** | **bool**|  | [optional] 
 **sort_by** | **str**|  | [optional] [default to &#39;updated_at&#39;]
 **sort_dir** | **str**|  | [optional] [default to &#39;desc&#39;]

### Return type

[**List[ChatTitleIdResponse]**](ChatTitleIdResponse.md)

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

# **get_session_user_chat_usage_stats_api_v1_chats_stats_usage_get**
> ChatUsageStatsListResponse get_session_user_chat_usage_stats_api_v1_chats_stats_usage_get(items_per_page=items_per_page, page=page)

Get Session User Chat Usage Stats

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_usage_stats_list_response import ChatUsageStatsListResponse
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
    api_instance = openwebui_client.ChatsApi(api_client)
    items_per_page = 56 # int |  (optional)
    page = 56 # int |  (optional)

    try:
        # Get Session User Chat Usage Stats
        api_response = await api_instance.get_session_user_chat_usage_stats_api_v1_chats_stats_usage_get(items_per_page=items_per_page, page=page)
        print("The response of ChatsApi->get_session_user_chat_usage_stats_api_v1_chats_stats_usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_session_user_chat_usage_stats_api_v1_chats_stats_usage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **items_per_page** | **int**|  | [optional] 
 **page** | **int**|  | [optional] 

### Return type

[**ChatUsageStatsListResponse**](ChatUsageStatsListResponse.md)

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

# **get_shared_chat_access_by_id_api_v1_chats_shared_id_access_get**
> List[object] get_shared_chat_access_by_id_api_v1_chats_shared_id_access_get(id)

Get Shared Chat Access By Id

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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Shared Chat Access By Id
        api_response = await api_instance.get_shared_chat_access_by_id_api_v1_chats_shared_id_access_get(id)
        print("The response of ChatsApi->get_shared_chat_access_by_id_api_v1_chats_shared_id_access_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_shared_chat_access_by_id_api_v1_chats_shared_id_access_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**List[object]**

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

# **get_shared_chat_by_id_api_v1_chats_share_share_id_get**
> ChatResponse get_shared_chat_by_id_api_v1_chats_share_share_id_get(share_id)

Get Shared Chat By Id

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
    api_instance = openwebui_client.ChatsApi(api_client)
    share_id = 'share_id_example' # str | 

    try:
        # Get Shared Chat By Id
        api_response = await api_instance.get_shared_chat_by_id_api_v1_chats_share_share_id_get(share_id)
        print("The response of ChatsApi->get_shared_chat_by_id_api_v1_chats_share_share_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_shared_chat_by_id_api_v1_chats_share_share_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_id** | **str**|  | 

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

# **get_shared_session_user_chat_list_api_v1_chats_shared_get**
> List[SharedChatResponse] get_shared_session_user_chat_list_api_v1_chats_shared_get(page=page, query=query, order_by=order_by, direction=direction)

Get Shared Session User Chat List

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.shared_chat_response import SharedChatResponse
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
    api_instance = openwebui_client.ChatsApi(api_client)
    page = 56 # int |  (optional)
    query = 'query_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    direction = 'direction_example' # str |  (optional)

    try:
        # Get Shared Session User Chat List
        api_response = await api_instance.get_shared_session_user_chat_list_api_v1_chats_shared_get(page=page, query=query, order_by=order_by, direction=direction)
        print("The response of ChatsApi->get_shared_session_user_chat_list_api_v1_chats_shared_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_shared_session_user_chat_list_api_v1_chats_shared_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **query** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] 

### Return type

[**List[SharedChatResponse]**](SharedChatResponse.md)

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

# **get_user_archived_chats_api_v1_chats_all_archived_get**
> List[ChatResponse] get_user_archived_chats_api_v1_chats_all_archived_get()

Get User Archived Chats

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
    api_instance = openwebui_client.ChatsApi(api_client)

    try:
        # Get User Archived Chats
        api_response = await api_instance.get_user_archived_chats_api_v1_chats_all_archived_get()
        print("The response of ChatsApi->get_user_archived_chats_api_v1_chats_all_archived_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_user_archived_chats_api_v1_chats_all_archived_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ChatResponse]**](ChatResponse.md)

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

# **get_user_chat_list_by_tag_name_api_v1_chats_tags_post**
> List[ChatTitleIdResponse] get_user_chat_list_by_tag_name_api_v1_chats_tags_post(tag_filter_form)

Get User Chat List By Tag Name

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_title_id_response import ChatTitleIdResponse
from openwebui_client.models.tag_filter_form import TagFilterForm
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
    api_instance = openwebui_client.ChatsApi(api_client)
    tag_filter_form = openwebui_client.TagFilterForm() # TagFilterForm | 

    try:
        # Get User Chat List By Tag Name
        api_response = await api_instance.get_user_chat_list_by_tag_name_api_v1_chats_tags_post(tag_filter_form)
        print("The response of ChatsApi->get_user_chat_list_by_tag_name_api_v1_chats_tags_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_user_chat_list_by_tag_name_api_v1_chats_tags_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_filter_form** | [**TagFilterForm**](TagFilterForm.md)|  | 

### Return type

[**List[ChatTitleIdResponse]**](ChatTitleIdResponse.md)

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

# **get_user_chat_list_by_user_id_api_v1_chats_list_user_user_id_get**
> List[ChatTitleIdResponse] get_user_chat_list_by_user_id_api_v1_chats_list_user_user_id_get(user_id, page=page, query=query, order_by=order_by, direction=direction)

Get User Chat List By User Id

List chat summaries for a given user (admin-only endpoint).

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_title_id_response import ChatTitleIdResponse
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
    api_instance = openwebui_client.ChatsApi(api_client)
    user_id = 'user_id_example' # str | 
    page = 56 # int |  (optional)
    query = 'query_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    direction = 'direction_example' # str |  (optional)

    try:
        # Get User Chat List By User Id
        api_response = await api_instance.get_user_chat_list_by_user_id_api_v1_chats_list_user_user_id_get(user_id, page=page, query=query, order_by=order_by, direction=direction)
        print("The response of ChatsApi->get_user_chat_list_by_user_id_api_v1_chats_list_user_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_user_chat_list_by_user_id_api_v1_chats_list_user_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **page** | **int**|  | [optional] 
 **query** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] 

### Return type

[**List[ChatTitleIdResponse]**](ChatTitleIdResponse.md)

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

# **get_user_chats_api_v1_chats_all_get**
> object get_user_chats_api_v1_chats_all_get()

Get User Chats

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
    api_instance = openwebui_client.ChatsApi(api_client)

    try:
        # Get User Chats
        api_response = await api_instance.get_user_chats_api_v1_chats_all_get()
        print("The response of ChatsApi->get_user_chats_api_v1_chats_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_user_chats_api_v1_chats_all_get: %s\n" % e)
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

# **get_user_pinned_chats_api_v1_chats_pinned_get**
> List[ChatTitleIdResponse] get_user_pinned_chats_api_v1_chats_pinned_get()

Get User Pinned Chats

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_title_id_response import ChatTitleIdResponse
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
    api_instance = openwebui_client.ChatsApi(api_client)

    try:
        # Get User Pinned Chats
        api_response = await api_instance.get_user_pinned_chats_api_v1_chats_pinned_get()
        print("The response of ChatsApi->get_user_pinned_chats_api_v1_chats_pinned_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->get_user_pinned_chats_api_v1_chats_pinned_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ChatTitleIdResponse]**](ChatTitleIdResponse.md)

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

# **import_chats_api_v1_chats_import_post**
> List[ChatResponse] import_chats_api_v1_chats_import_post(chats_import_form)

Import Chats

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_response import ChatResponse
from openwebui_client.models.chats_import_form import ChatsImportForm
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
    api_instance = openwebui_client.ChatsApi(api_client)
    chats_import_form = openwebui_client.ChatsImportForm() # ChatsImportForm | 

    try:
        # Import Chats
        api_response = await api_instance.import_chats_api_v1_chats_import_post(chats_import_form)
        print("The response of ChatsApi->import_chats_api_v1_chats_import_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->import_chats_api_v1_chats_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chats_import_form** | [**ChatsImportForm**](ChatsImportForm.md)|  | 

### Return type

[**List[ChatResponse]**](ChatResponse.md)

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

# **mark_chat_unread_by_id_api_v1_chats_id_unread_post**
> object mark_chat_unread_by_id_api_v1_chats_id_unread_post(id)

Mark Chat Unread By Id

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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Mark Chat Unread By Id
        api_response = await api_instance.mark_chat_unread_by_id_api_v1_chats_id_unread_post(id)
        print("The response of ChatsApi->mark_chat_unread_by_id_api_v1_chats_id_unread_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->mark_chat_unread_by_id_api_v1_chats_id_unread_post: %s\n" % e)
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

# **mark_chats_read_by_user_id_api_v1_chats_read_post**
> object mark_chats_read_by_user_id_api_v1_chats_read_post()

Mark Chats Read By User Id

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
    api_instance = openwebui_client.ChatsApi(api_client)

    try:
        # Mark Chats Read By User Id
        api_response = await api_instance.mark_chats_read_by_user_id_api_v1_chats_read_post()
        print("The response of ChatsApi->mark_chats_read_by_user_id_api_v1_chats_read_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->mark_chats_read_by_user_id_api_v1_chats_read_post: %s\n" % e)
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

# **pin_chat_by_id_api_v1_chats_id_pin_post**
> ChatResponse pin_chat_by_id_api_v1_chats_id_pin_post(id)

Pin Chat By Id

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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Pin Chat By Id
        api_response = await api_instance.pin_chat_by_id_api_v1_chats_id_pin_post(id)
        print("The response of ChatsApi->pin_chat_by_id_api_v1_chats_id_pin_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->pin_chat_by_id_api_v1_chats_id_pin_post: %s\n" % e)
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

# **search_user_chats_api_v1_chats_search_get**
> List[ChatTitleIdResponse] search_user_chats_api_v1_chats_search_get(text, page=page)

Search User Chats

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_title_id_response import ChatTitleIdResponse
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
    api_instance = openwebui_client.ChatsApi(api_client)
    text = 'text_example' # str | 
    page = 56 # int |  (optional)

    try:
        # Search User Chats
        api_response = await api_instance.search_user_chats_api_v1_chats_search_get(text, page=page)
        print("The response of ChatsApi->search_user_chats_api_v1_chats_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->search_user_chats_api_v1_chats_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**|  | 
 **page** | **int**|  | [optional] 

### Return type

[**List[ChatTitleIdResponse]**](ChatTitleIdResponse.md)

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

# **send_chat_message_event_by_id_api_v1_chats_id_messages_message_id_event_post**
> bool send_chat_message_event_by_id_api_v1_chats_id_messages_message_id_event_post(id, message_id, event_form)

Send Chat Message Event By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.event_form import EventForm
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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 
    message_id = 'message_id_example' # str | 
    event_form = openwebui_client.EventForm() # EventForm | 

    try:
        # Send Chat Message Event By Id
        api_response = await api_instance.send_chat_message_event_by_id_api_v1_chats_id_messages_message_id_event_post(id, message_id, event_form)
        print("The response of ChatsApi->send_chat_message_event_by_id_api_v1_chats_id_messages_message_id_event_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->send_chat_message_event_by_id_api_v1_chats_id_messages_message_id_event_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **message_id** | **str**|  | 
 **event_form** | [**EventForm**](EventForm.md)|  | 

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

# **set_chat_config_api_v1_chats_config_post**
> ChatConfigForm set_chat_config_api_v1_chats_config_post(chat_config_form)

Set Chat Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_config_form import ChatConfigForm
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
    api_instance = openwebui_client.ChatsApi(api_client)
    chat_config_form = openwebui_client.ChatConfigForm() # ChatConfigForm | 

    try:
        # Set Chat Config
        api_response = await api_instance.set_chat_config_api_v1_chats_config_post(chat_config_form)
        print("The response of ChatsApi->set_chat_config_api_v1_chats_config_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->set_chat_config_api_v1_chats_config_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_config_form** | [**ChatConfigForm**](ChatConfigForm.md)|  | 

### Return type

[**ChatConfigForm**](ChatConfigForm.md)

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

# **share_chat_by_id_api_v1_chats_id_share_post**
> ChatResponse share_chat_by_id_api_v1_chats_id_share_post(id)

Share Chat By Id

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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Share Chat By Id
        api_response = await api_instance.share_chat_by_id_api_v1_chats_id_share_post(id)
        print("The response of ChatsApi->share_chat_by_id_api_v1_chats_id_share_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->share_chat_by_id_api_v1_chats_id_share_post: %s\n" % e)
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

# **unarchive_all_chats_api_v1_chats_unarchive_all_post**
> bool unarchive_all_chats_api_v1_chats_unarchive_all_post()

Unarchive All Chats

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
    api_instance = openwebui_client.ChatsApi(api_client)

    try:
        # Unarchive All Chats
        api_response = await api_instance.unarchive_all_chats_api_v1_chats_unarchive_all_post()
        print("The response of ChatsApi->unarchive_all_chats_api_v1_chats_unarchive_all_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->unarchive_all_chats_api_v1_chats_unarchive_all_post: %s\n" % e)
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

# **unshare_all_chats_api_v1_chats_share_all_delete**
> bool unshare_all_chats_api_v1_chats_share_all_delete()

Unshare All Chats

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
    api_instance = openwebui_client.ChatsApi(api_client)

    try:
        # Unshare All Chats
        api_response = await api_instance.unshare_all_chats_api_v1_chats_share_all_delete()
        print("The response of ChatsApi->unshare_all_chats_api_v1_chats_share_all_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->unshare_all_chats_api_v1_chats_share_all_delete: %s\n" % e)
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

# **update_chat_by_id_api_v1_chats_id_post**
> ChatResponse update_chat_by_id_api_v1_chats_id_post(id, chat_form)

Update Chat By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_form import ChatForm
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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 
    chat_form = openwebui_client.ChatForm() # ChatForm | 

    try:
        # Update Chat By Id
        api_response = await api_instance.update_chat_by_id_api_v1_chats_id_post(id, chat_form)
        print("The response of ChatsApi->update_chat_by_id_api_v1_chats_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->update_chat_by_id_api_v1_chats_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **chat_form** | [**ChatForm**](ChatForm.md)|  | 

### Return type

[**ChatResponse**](ChatResponse.md)

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

# **update_chat_folder_id_by_id_api_v1_chats_id_folder_post**
> ChatResponse update_chat_folder_id_by_id_api_v1_chats_id_folder_post(id, chat_folder_id_form)

Update Chat Folder Id By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_folder_id_form import ChatFolderIdForm
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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 
    chat_folder_id_form = openwebui_client.ChatFolderIdForm() # ChatFolderIdForm | 

    try:
        # Update Chat Folder Id By Id
        api_response = await api_instance.update_chat_folder_id_by_id_api_v1_chats_id_folder_post(id, chat_folder_id_form)
        print("The response of ChatsApi->update_chat_folder_id_by_id_api_v1_chats_id_folder_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->update_chat_folder_id_by_id_api_v1_chats_id_folder_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **chat_folder_id_form** | [**ChatFolderIdForm**](ChatFolderIdForm.md)|  | 

### Return type

[**ChatResponse**](ChatResponse.md)

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

# **update_chat_message_by_id_api_v1_chats_id_messages_message_id_post**
> ChatResponse update_chat_message_by_id_api_v1_chats_id_messages_message_id_post(id, message_id, open_webui_routers_chats_message_form)

Update Chat Message By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_response import ChatResponse
from openwebui_client.models.open_webui_routers_chats_message_form import OpenWebuiRoutersChatsMessageForm
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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 
    message_id = 'message_id_example' # str | 
    open_webui_routers_chats_message_form = openwebui_client.OpenWebuiRoutersChatsMessageForm() # OpenWebuiRoutersChatsMessageForm | 

    try:
        # Update Chat Message By Id
        api_response = await api_instance.update_chat_message_by_id_api_v1_chats_id_messages_message_id_post(id, message_id, open_webui_routers_chats_message_form)
        print("The response of ChatsApi->update_chat_message_by_id_api_v1_chats_id_messages_message_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->update_chat_message_by_id_api_v1_chats_id_messages_message_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **message_id** | **str**|  | 
 **open_webui_routers_chats_message_form** | [**OpenWebuiRoutersChatsMessageForm**](OpenWebuiRoutersChatsMessageForm.md)|  | 

### Return type

[**ChatResponse**](ChatResponse.md)

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

# **update_shared_chat_access_by_id_api_v1_chats_shared_id_access_update_post**
> ChatResponse update_shared_chat_access_by_id_api_v1_chats_shared_id_access_update_post(id, chat_access_grants_form)

Update Shared Chat Access By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_access_grants_form import ChatAccessGrantsForm
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
    api_instance = openwebui_client.ChatsApi(api_client)
    id = 'id_example' # str | 
    chat_access_grants_form = openwebui_client.ChatAccessGrantsForm() # ChatAccessGrantsForm | 

    try:
        # Update Shared Chat Access By Id
        api_response = await api_instance.update_shared_chat_access_by_id_api_v1_chats_shared_id_access_update_post(id, chat_access_grants_form)
        print("The response of ChatsApi->update_shared_chat_access_by_id_api_v1_chats_shared_id_access_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatsApi->update_shared_chat_access_by_id_api_v1_chats_shared_id_access_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **chat_access_grants_form** | [**ChatAccessGrantsForm**](ChatAccessGrantsForm.md)|  | 

### Return type

[**ChatResponse**](ChatResponse.md)

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

