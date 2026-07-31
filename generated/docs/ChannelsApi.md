# openwebui_client.ChannelsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_members_by_id_api_v1_channels_id_update_members_add_post**](ChannelsApi.md#add_members_by_id_api_v1_channels_id_update_members_add_post) | **POST** /api/v1/channels/{id}/update/members/add | Add Members By Id
[**add_reaction_to_message_api_v1_channels_id_messages_message_id_reactions_add_post**](ChannelsApi.md#add_reaction_to_message_api_v1_channels_id_messages_message_id_reactions_add_post) | **POST** /api/v1/channels/{id}/messages/{message_id}/reactions/add | Add Reaction To Message
[**create_channel_webhook_api_v1_channels_id_webhooks_create_post**](ChannelsApi.md#create_channel_webhook_api_v1_channels_id_webhooks_create_post) | **POST** /api/v1/channels/{id}/webhooks/create | Create Channel Webhook
[**create_new_channel_api_v1_channels_create_post**](ChannelsApi.md#create_new_channel_api_v1_channels_create_post) | **POST** /api/v1/channels/create | Create New Channel
[**delete_channel_by_id_api_v1_channels_id_delete_delete**](ChannelsApi.md#delete_channel_by_id_api_v1_channels_id_delete_delete) | **DELETE** /api/v1/channels/{id}/delete | Delete Channel By Id
[**delete_channel_webhook_api_v1_channels_id_webhooks_webhook_id_delete_delete**](ChannelsApi.md#delete_channel_webhook_api_v1_channels_id_webhooks_webhook_id_delete_delete) | **DELETE** /api/v1/channels/{id}/webhooks/{webhook_id}/delete | Delete Channel Webhook
[**delete_message_by_id_api_v1_channels_id_messages_message_id_delete_delete**](ChannelsApi.md#delete_message_by_id_api_v1_channels_id_messages_message_id_delete_delete) | **DELETE** /api/v1/channels/{id}/messages/{message_id}/delete | Delete Message By Id
[**get_all_channels_api_v1_channels_list_get**](ChannelsApi.md#get_all_channels_api_v1_channels_list_get) | **GET** /api/v1/channels/list | Get All Channels
[**get_channel_by_id_api_v1_channels_id_get**](ChannelsApi.md#get_channel_by_id_api_v1_channels_id_get) | **GET** /api/v1/channels/{id} | Get Channel By Id
[**get_channel_members_by_id_api_v1_channels_id_members_get**](ChannelsApi.md#get_channel_members_by_id_api_v1_channels_id_members_get) | **GET** /api/v1/channels/{id}/members | Get Channel Members By Id
[**get_channel_message_api_v1_channels_id_messages_message_id_get**](ChannelsApi.md#get_channel_message_api_v1_channels_id_messages_message_id_get) | **GET** /api/v1/channels/{id}/messages/{message_id} | Get Channel Message
[**get_channel_message_data_api_v1_channels_id_messages_message_id_data_get**](ChannelsApi.md#get_channel_message_data_api_v1_channels_id_messages_message_id_data_get) | **GET** /api/v1/channels/{id}/messages/{message_id}/data | Get Channel Message Data
[**get_channel_messages_api_v1_channels_id_messages_get**](ChannelsApi.md#get_channel_messages_api_v1_channels_id_messages_get) | **GET** /api/v1/channels/{id}/messages | Get Channel Messages
[**get_channel_thread_messages_api_v1_channels_id_messages_message_id_thread_get**](ChannelsApi.md#get_channel_thread_messages_api_v1_channels_id_messages_message_id_thread_get) | **GET** /api/v1/channels/{id}/messages/{message_id}/thread | Get Channel Thread Messages
[**get_channel_webhooks_api_v1_channels_id_webhooks_get**](ChannelsApi.md#get_channel_webhooks_api_v1_channels_id_webhooks_get) | **GET** /api/v1/channels/{id}/webhooks | Get Channel Webhooks
[**get_channels_api_v1_channels_get**](ChannelsApi.md#get_channels_api_v1_channels_get) | **GET** /api/v1/channels/ | Get Channels
[**get_dm_channel_by_user_id_api_v1_channels_users_user_id_get**](ChannelsApi.md#get_dm_channel_by_user_id_api_v1_channels_users_user_id_get) | **GET** /api/v1/channels/users/{user_id} | Get Dm Channel By User Id
[**get_pinned_channel_messages_api_v1_channels_id_messages_pinned_get**](ChannelsApi.md#get_pinned_channel_messages_api_v1_channels_id_messages_pinned_get) | **GET** /api/v1/channels/{id}/messages/pinned | Get Pinned Channel Messages
[**get_webhook_profile_image_api_v1_channels_webhooks_webhook_id_profile_image_get**](ChannelsApi.md#get_webhook_profile_image_api_v1_channels_webhooks_webhook_id_profile_image_get) | **GET** /api/v1/channels/webhooks/{webhook_id}/profile/image | Get Webhook Profile Image
[**pin_channel_message_api_v1_channels_id_messages_message_id_pin_post**](ChannelsApi.md#pin_channel_message_api_v1_channels_id_messages_message_id_pin_post) | **POST** /api/v1/channels/{id}/messages/{message_id}/pin | Pin Channel Message
[**post_new_message_api_v1_channels_id_messages_post_post**](ChannelsApi.md#post_new_message_api_v1_channels_id_messages_post_post) | **POST** /api/v1/channels/{id}/messages/post | Post New Message
[**post_webhook_message_api_v1_channels_webhooks_webhook_id_token_post**](ChannelsApi.md#post_webhook_message_api_v1_channels_webhooks_webhook_id_token_post) | **POST** /api/v1/channels/webhooks/{webhook_id}/{token} | Post Webhook Message
[**remove_members_by_id_api_v1_channels_id_update_members_remove_post**](ChannelsApi.md#remove_members_by_id_api_v1_channels_id_update_members_remove_post) | **POST** /api/v1/channels/{id}/update/members/remove | Remove Members By Id
[**remove_reaction_by_id_and_user_id_and_name_api_v1_channels_id_messages_message_id_reactions_remove_post**](ChannelsApi.md#remove_reaction_by_id_and_user_id_and_name_api_v1_channels_id_messages_message_id_reactions_remove_post) | **POST** /api/v1/channels/{id}/messages/{message_id}/reactions/remove | Remove Reaction By Id And User Id And Name
[**update_channel_by_id_api_v1_channels_id_update_post**](ChannelsApi.md#update_channel_by_id_api_v1_channels_id_update_post) | **POST** /api/v1/channels/{id}/update | Update Channel By Id
[**update_channel_webhook_api_v1_channels_id_webhooks_webhook_id_update_post**](ChannelsApi.md#update_channel_webhook_api_v1_channels_id_webhooks_webhook_id_update_post) | **POST** /api/v1/channels/{id}/webhooks/{webhook_id}/update | Update Channel Webhook
[**update_is_active_member_by_id_and_user_id_api_v1_channels_id_members_active_post**](ChannelsApi.md#update_is_active_member_by_id_and_user_id_api_v1_channels_id_members_active_post) | **POST** /api/v1/channels/{id}/members/active | Update Is Active Member By Id And User Id
[**update_message_by_id_api_v1_channels_id_messages_message_id_update_post**](ChannelsApi.md#update_message_by_id_api_v1_channels_id_messages_message_id_update_post) | **POST** /api/v1/channels/{id}/messages/{message_id}/update | Update Message By Id


# **add_members_by_id_api_v1_channels_id_update_members_add_post**
> object add_members_by_id_api_v1_channels_id_update_members_add_post(id, update_members_form)

Add Members By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.update_members_form import UpdateMembersForm
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    update_members_form = openwebui_client.UpdateMembersForm() # UpdateMembersForm | 

    try:
        # Add Members By Id
        api_response = await api_instance.add_members_by_id_api_v1_channels_id_update_members_add_post(id, update_members_form)
        print("The response of ChannelsApi->add_members_by_id_api_v1_channels_id_update_members_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->add_members_by_id_api_v1_channels_id_update_members_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_members_form** | [**UpdateMembersForm**](UpdateMembersForm.md)|  | 

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

# **add_reaction_to_message_api_v1_channels_id_messages_message_id_reactions_add_post**
> bool add_reaction_to_message_api_v1_channels_id_messages_message_id_reactions_add_post(id, message_id, reaction_form)

Add Reaction To Message

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.reaction_form import ReactionForm
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    message_id = 'message_id_example' # str | 
    reaction_form = openwebui_client.ReactionForm() # ReactionForm | 

    try:
        # Add Reaction To Message
        api_response = await api_instance.add_reaction_to_message_api_v1_channels_id_messages_message_id_reactions_add_post(id, message_id, reaction_form)
        print("The response of ChannelsApi->add_reaction_to_message_api_v1_channels_id_messages_message_id_reactions_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->add_reaction_to_message_api_v1_channels_id_messages_message_id_reactions_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **message_id** | **str**|  | 
 **reaction_form** | [**ReactionForm**](ReactionForm.md)|  | 

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

# **create_channel_webhook_api_v1_channels_id_webhooks_create_post**
> ChannelWebhookModel create_channel_webhook_api_v1_channels_id_webhooks_create_post(id, channel_webhook_form)

Create Channel Webhook

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.channel_webhook_form import ChannelWebhookForm
from openwebui_client.models.channel_webhook_model import ChannelWebhookModel
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    channel_webhook_form = openwebui_client.ChannelWebhookForm() # ChannelWebhookForm | 

    try:
        # Create Channel Webhook
        api_response = await api_instance.create_channel_webhook_api_v1_channels_id_webhooks_create_post(id, channel_webhook_form)
        print("The response of ChannelsApi->create_channel_webhook_api_v1_channels_id_webhooks_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->create_channel_webhook_api_v1_channels_id_webhooks_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **channel_webhook_form** | [**ChannelWebhookForm**](ChannelWebhookForm.md)|  | 

### Return type

[**ChannelWebhookModel**](ChannelWebhookModel.md)

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

# **create_new_channel_api_v1_channels_create_post**
> ChannelModel create_new_channel_api_v1_channels_create_post(create_channel_form)

Create New Channel

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.channel_model import ChannelModel
from openwebui_client.models.create_channel_form import CreateChannelForm
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    create_channel_form = openwebui_client.CreateChannelForm() # CreateChannelForm | 

    try:
        # Create New Channel
        api_response = await api_instance.create_new_channel_api_v1_channels_create_post(create_channel_form)
        print("The response of ChannelsApi->create_new_channel_api_v1_channels_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->create_new_channel_api_v1_channels_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_channel_form** | [**CreateChannelForm**](CreateChannelForm.md)|  | 

### Return type

[**ChannelModel**](ChannelModel.md)

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

# **delete_channel_by_id_api_v1_channels_id_delete_delete**
> bool delete_channel_by_id_api_v1_channels_id_delete_delete(id)

Delete Channel By Id

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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Channel By Id
        api_response = await api_instance.delete_channel_by_id_api_v1_channels_id_delete_delete(id)
        print("The response of ChannelsApi->delete_channel_by_id_api_v1_channels_id_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->delete_channel_by_id_api_v1_channels_id_delete_delete: %s\n" % e)
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

# **delete_channel_webhook_api_v1_channels_id_webhooks_webhook_id_delete_delete**
> bool delete_channel_webhook_api_v1_channels_id_webhooks_webhook_id_delete_delete(id, webhook_id)

Delete Channel Webhook

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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    webhook_id = 'webhook_id_example' # str | 

    try:
        # Delete Channel Webhook
        api_response = await api_instance.delete_channel_webhook_api_v1_channels_id_webhooks_webhook_id_delete_delete(id, webhook_id)
        print("The response of ChannelsApi->delete_channel_webhook_api_v1_channels_id_webhooks_webhook_id_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->delete_channel_webhook_api_v1_channels_id_webhooks_webhook_id_delete_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **webhook_id** | **str**|  | 

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

# **delete_message_by_id_api_v1_channels_id_messages_message_id_delete_delete**
> bool delete_message_by_id_api_v1_channels_id_messages_message_id_delete_delete(id, message_id)

Delete Message By Id

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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        # Delete Message By Id
        api_response = await api_instance.delete_message_by_id_api_v1_channels_id_messages_message_id_delete_delete(id, message_id)
        print("The response of ChannelsApi->delete_message_by_id_api_v1_channels_id_messages_message_id_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->delete_message_by_id_api_v1_channels_id_messages_message_id_delete_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **message_id** | **str**|  | 

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

# **get_all_channels_api_v1_channels_list_get**
> List[ChannelModel] get_all_channels_api_v1_channels_list_get()

Get All Channels

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.channel_model import ChannelModel
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
    api_instance = openwebui_client.ChannelsApi(api_client)

    try:
        # Get All Channels
        api_response = await api_instance.get_all_channels_api_v1_channels_list_get()
        print("The response of ChannelsApi->get_all_channels_api_v1_channels_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_all_channels_api_v1_channels_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ChannelModel]**](ChannelModel.md)

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

# **get_channel_by_id_api_v1_channels_id_get**
> ChannelFullResponse get_channel_by_id_api_v1_channels_id_get(id)

Get Channel By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.channel_full_response import ChannelFullResponse
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Channel By Id
        api_response = await api_instance.get_channel_by_id_api_v1_channels_id_get(id)
        print("The response of ChannelsApi->get_channel_by_id_api_v1_channels_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_channel_by_id_api_v1_channels_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ChannelFullResponse**](ChannelFullResponse.md)

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

# **get_channel_members_by_id_api_v1_channels_id_members_get**
> ChannelMemberListResponse get_channel_members_by_id_api_v1_channels_id_members_get(id, query=query, order_by=order_by, direction=direction, page=page)

Get Channel Members By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.channel_member_list_response import ChannelMemberListResponse
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    query = 'query_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    direction = 'direction_example' # str |  (optional)
    page = 56 # int |  (optional)

    try:
        # Get Channel Members By Id
        api_response = await api_instance.get_channel_members_by_id_api_v1_channels_id_members_get(id, query=query, order_by=order_by, direction=direction, page=page)
        print("The response of ChannelsApi->get_channel_members_by_id_api_v1_channels_id_members_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_channel_members_by_id_api_v1_channels_id_members_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **query** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 

### Return type

[**ChannelMemberListResponse**](ChannelMemberListResponse.md)

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

# **get_channel_message_api_v1_channels_id_messages_message_id_get**
> MessageResponse get_channel_message_api_v1_channels_id_messages_message_id_get(id, message_id)

Get Channel Message

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.message_response import MessageResponse
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        # Get Channel Message
        api_response = await api_instance.get_channel_message_api_v1_channels_id_messages_message_id_get(id, message_id)
        print("The response of ChannelsApi->get_channel_message_api_v1_channels_id_messages_message_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_channel_message_api_v1_channels_id_messages_message_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **message_id** | **str**|  | 

### Return type

[**MessageResponse**](MessageResponse.md)

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

# **get_channel_message_data_api_v1_channels_id_messages_message_id_data_get**
> Dict[str, object] get_channel_message_data_api_v1_channels_id_messages_message_id_data_get(id, message_id)

Get Channel Message Data

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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        # Get Channel Message Data
        api_response = await api_instance.get_channel_message_data_api_v1_channels_id_messages_message_id_data_get(id, message_id)
        print("The response of ChannelsApi->get_channel_message_data_api_v1_channels_id_messages_message_id_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_channel_message_data_api_v1_channels_id_messages_message_id_data_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **message_id** | **str**|  | 

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

# **get_channel_messages_api_v1_channels_id_messages_get**
> List[MessageUserResponse] get_channel_messages_api_v1_channels_id_messages_get(id, skip=skip, limit=limit)

Get Channel Messages

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.message_user_response import MessageUserResponse
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    skip = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # Get Channel Messages
        api_response = await api_instance.get_channel_messages_api_v1_channels_id_messages_get(id, skip=skip, limit=limit)
        print("The response of ChannelsApi->get_channel_messages_api_v1_channels_id_messages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_channel_messages_api_v1_channels_id_messages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**List[MessageUserResponse]**](MessageUserResponse.md)

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

# **get_channel_thread_messages_api_v1_channels_id_messages_message_id_thread_get**
> List[Optional[MessageUserResponse]] get_channel_thread_messages_api_v1_channels_id_messages_message_id_thread_get(id, message_id, skip=skip, limit=limit)

Get Channel Thread Messages

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.message_user_response import MessageUserResponse
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    message_id = 'message_id_example' # str | 
    skip = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # Get Channel Thread Messages
        api_response = await api_instance.get_channel_thread_messages_api_v1_channels_id_messages_message_id_thread_get(id, message_id, skip=skip, limit=limit)
        print("The response of ChannelsApi->get_channel_thread_messages_api_v1_channels_id_messages_message_id_thread_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_channel_thread_messages_api_v1_channels_id_messages_message_id_thread_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **message_id** | **str**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**List[Optional[MessageUserResponse]]**](MessageUserResponse.md)

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

# **get_channel_webhooks_api_v1_channels_id_webhooks_get**
> List[ChannelWebhookModel] get_channel_webhooks_api_v1_channels_id_webhooks_get(id)

Get Channel Webhooks

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.channel_webhook_model import ChannelWebhookModel
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Channel Webhooks
        api_response = await api_instance.get_channel_webhooks_api_v1_channels_id_webhooks_get(id)
        print("The response of ChannelsApi->get_channel_webhooks_api_v1_channels_id_webhooks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_channel_webhooks_api_v1_channels_id_webhooks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[ChannelWebhookModel]**](ChannelWebhookModel.md)

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

# **get_channels_api_v1_channels_get**
> List[ChannelListItemResponse] get_channels_api_v1_channels_get()

Get Channels

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.channel_list_item_response import ChannelListItemResponse
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
    api_instance = openwebui_client.ChannelsApi(api_client)

    try:
        # Get Channels
        api_response = await api_instance.get_channels_api_v1_channels_get()
        print("The response of ChannelsApi->get_channels_api_v1_channels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_channels_api_v1_channels_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ChannelListItemResponse]**](ChannelListItemResponse.md)

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

# **get_dm_channel_by_user_id_api_v1_channels_users_user_id_get**
> ChannelModel get_dm_channel_by_user_id_api_v1_channels_users_user_id_get(user_id)

Get Dm Channel By User Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.channel_model import ChannelModel
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get Dm Channel By User Id
        api_response = await api_instance.get_dm_channel_by_user_id_api_v1_channels_users_user_id_get(user_id)
        print("The response of ChannelsApi->get_dm_channel_by_user_id_api_v1_channels_users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_dm_channel_by_user_id_api_v1_channels_users_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**ChannelModel**](ChannelModel.md)

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

# **get_pinned_channel_messages_api_v1_channels_id_messages_pinned_get**
> List[MessageWithReactionsResponse] get_pinned_channel_messages_api_v1_channels_id_messages_pinned_get(id, page=page)

Get Pinned Channel Messages

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.message_with_reactions_response import MessageWithReactionsResponse
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    page = 1 # int |  (optional) (default to 1)

    try:
        # Get Pinned Channel Messages
        api_response = await api_instance.get_pinned_channel_messages_api_v1_channels_id_messages_pinned_get(id, page=page)
        print("The response of ChannelsApi->get_pinned_channel_messages_api_v1_channels_id_messages_pinned_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_pinned_channel_messages_api_v1_channels_id_messages_pinned_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]

### Return type

[**List[MessageWithReactionsResponse]**](MessageWithReactionsResponse.md)

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

# **get_webhook_profile_image_api_v1_channels_webhooks_webhook_id_profile_image_get**
> object get_webhook_profile_image_api_v1_channels_webhooks_webhook_id_profile_image_get(webhook_id)

Get Webhook Profile Image

Get webhook profile image by webhook ID.

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
    api_instance = openwebui_client.ChannelsApi(api_client)
    webhook_id = 'webhook_id_example' # str | 

    try:
        # Get Webhook Profile Image
        api_response = await api_instance.get_webhook_profile_image_api_v1_channels_webhooks_webhook_id_profile_image_get(webhook_id)
        print("The response of ChannelsApi->get_webhook_profile_image_api_v1_channels_webhooks_webhook_id_profile_image_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_webhook_profile_image_api_v1_channels_webhooks_webhook_id_profile_image_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 

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

# **pin_channel_message_api_v1_channels_id_messages_message_id_pin_post**
> MessageUserResponse pin_channel_message_api_v1_channels_id_messages_message_id_pin_post(id, message_id, pin_message_form)

Pin Channel Message

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.message_user_response import MessageUserResponse
from openwebui_client.models.pin_message_form import PinMessageForm
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    message_id = 'message_id_example' # str | 
    pin_message_form = openwebui_client.PinMessageForm() # PinMessageForm | 

    try:
        # Pin Channel Message
        api_response = await api_instance.pin_channel_message_api_v1_channels_id_messages_message_id_pin_post(id, message_id, pin_message_form)
        print("The response of ChannelsApi->pin_channel_message_api_v1_channels_id_messages_message_id_pin_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->pin_channel_message_api_v1_channels_id_messages_message_id_pin_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **message_id** | **str**|  | 
 **pin_message_form** | [**PinMessageForm**](PinMessageForm.md)|  | 

### Return type

[**MessageUserResponse**](MessageUserResponse.md)

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

# **post_new_message_api_v1_channels_id_messages_post_post**
> MessageModel post_new_message_api_v1_channels_id_messages_post_post(id, open_webui_models_messages_message_form)

Post New Message

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.message_model import MessageModel
from openwebui_client.models.open_webui_models_messages_message_form import OpenWebuiModelsMessagesMessageForm
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    open_webui_models_messages_message_form = openwebui_client.OpenWebuiModelsMessagesMessageForm() # OpenWebuiModelsMessagesMessageForm | 

    try:
        # Post New Message
        api_response = await api_instance.post_new_message_api_v1_channels_id_messages_post_post(id, open_webui_models_messages_message_form)
        print("The response of ChannelsApi->post_new_message_api_v1_channels_id_messages_post_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->post_new_message_api_v1_channels_id_messages_post_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **open_webui_models_messages_message_form** | [**OpenWebuiModelsMessagesMessageForm**](OpenWebuiModelsMessagesMessageForm.md)|  | 

### Return type

[**MessageModel**](MessageModel.md)

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

# **post_webhook_message_api_v1_channels_webhooks_webhook_id_token_post**
> object post_webhook_message_api_v1_channels_webhooks_webhook_id_token_post(webhook_id, token, webhook_message_form)

Post Webhook Message

Public endpoint to post messages via webhook. No authentication required.

### Example


```python
import openwebui_client
from openwebui_client.models.webhook_message_form import WebhookMessageForm
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    token = 'token_example' # str | 
    webhook_message_form = openwebui_client.WebhookMessageForm() # WebhookMessageForm | 

    try:
        # Post Webhook Message
        api_response = await api_instance.post_webhook_message_api_v1_channels_webhooks_webhook_id_token_post(webhook_id, token, webhook_message_form)
        print("The response of ChannelsApi->post_webhook_message_api_v1_channels_webhooks_webhook_id_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->post_webhook_message_api_v1_channels_webhooks_webhook_id_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **token** | **str**|  | 
 **webhook_message_form** | [**WebhookMessageForm**](WebhookMessageForm.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_members_by_id_api_v1_channels_id_update_members_remove_post**
> object remove_members_by_id_api_v1_channels_id_update_members_remove_post(id, remove_members_form)

Remove Members By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.remove_members_form import RemoveMembersForm
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    remove_members_form = openwebui_client.RemoveMembersForm() # RemoveMembersForm | 

    try:
        # Remove Members By Id
        api_response = await api_instance.remove_members_by_id_api_v1_channels_id_update_members_remove_post(id, remove_members_form)
        print("The response of ChannelsApi->remove_members_by_id_api_v1_channels_id_update_members_remove_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->remove_members_by_id_api_v1_channels_id_update_members_remove_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **remove_members_form** | [**RemoveMembersForm**](RemoveMembersForm.md)|  | 

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

# **remove_reaction_by_id_and_user_id_and_name_api_v1_channels_id_messages_message_id_reactions_remove_post**
> bool remove_reaction_by_id_and_user_id_and_name_api_v1_channels_id_messages_message_id_reactions_remove_post(id, message_id, reaction_form)

Remove Reaction By Id And User Id And Name

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.reaction_form import ReactionForm
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    message_id = 'message_id_example' # str | 
    reaction_form = openwebui_client.ReactionForm() # ReactionForm | 

    try:
        # Remove Reaction By Id And User Id And Name
        api_response = await api_instance.remove_reaction_by_id_and_user_id_and_name_api_v1_channels_id_messages_message_id_reactions_remove_post(id, message_id, reaction_form)
        print("The response of ChannelsApi->remove_reaction_by_id_and_user_id_and_name_api_v1_channels_id_messages_message_id_reactions_remove_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->remove_reaction_by_id_and_user_id_and_name_api_v1_channels_id_messages_message_id_reactions_remove_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **message_id** | **str**|  | 
 **reaction_form** | [**ReactionForm**](ReactionForm.md)|  | 

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

# **update_channel_by_id_api_v1_channels_id_update_post**
> ChannelModel update_channel_by_id_api_v1_channels_id_update_post(id, channel_form)

Update Channel By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.channel_form import ChannelForm
from openwebui_client.models.channel_model import ChannelModel
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    channel_form = openwebui_client.ChannelForm() # ChannelForm | 

    try:
        # Update Channel By Id
        api_response = await api_instance.update_channel_by_id_api_v1_channels_id_update_post(id, channel_form)
        print("The response of ChannelsApi->update_channel_by_id_api_v1_channels_id_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->update_channel_by_id_api_v1_channels_id_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **channel_form** | [**ChannelForm**](ChannelForm.md)|  | 

### Return type

[**ChannelModel**](ChannelModel.md)

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

# **update_channel_webhook_api_v1_channels_id_webhooks_webhook_id_update_post**
> ChannelWebhookModel update_channel_webhook_api_v1_channels_id_webhooks_webhook_id_update_post(id, webhook_id, channel_webhook_form)

Update Channel Webhook

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.channel_webhook_form import ChannelWebhookForm
from openwebui_client.models.channel_webhook_model import ChannelWebhookModel
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    webhook_id = 'webhook_id_example' # str | 
    channel_webhook_form = openwebui_client.ChannelWebhookForm() # ChannelWebhookForm | 

    try:
        # Update Channel Webhook
        api_response = await api_instance.update_channel_webhook_api_v1_channels_id_webhooks_webhook_id_update_post(id, webhook_id, channel_webhook_form)
        print("The response of ChannelsApi->update_channel_webhook_api_v1_channels_id_webhooks_webhook_id_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->update_channel_webhook_api_v1_channels_id_webhooks_webhook_id_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **webhook_id** | **str**|  | 
 **channel_webhook_form** | [**ChannelWebhookForm**](ChannelWebhookForm.md)|  | 

### Return type

[**ChannelWebhookModel**](ChannelWebhookModel.md)

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

# **update_is_active_member_by_id_and_user_id_api_v1_channels_id_members_active_post**
> bool update_is_active_member_by_id_and_user_id_api_v1_channels_id_members_active_post(id, update_active_member_form)

Update Is Active Member By Id And User Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.update_active_member_form import UpdateActiveMemberForm
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    update_active_member_form = openwebui_client.UpdateActiveMemberForm() # UpdateActiveMemberForm | 

    try:
        # Update Is Active Member By Id And User Id
        api_response = await api_instance.update_is_active_member_by_id_and_user_id_api_v1_channels_id_members_active_post(id, update_active_member_form)
        print("The response of ChannelsApi->update_is_active_member_by_id_and_user_id_api_v1_channels_id_members_active_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->update_is_active_member_by_id_and_user_id_api_v1_channels_id_members_active_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_active_member_form** | [**UpdateActiveMemberForm**](UpdateActiveMemberForm.md)|  | 

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

# **update_message_by_id_api_v1_channels_id_messages_message_id_update_post**
> MessageModel update_message_by_id_api_v1_channels_id_messages_message_id_update_post(id, message_id, open_webui_models_messages_message_form)

Update Message By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.message_model import MessageModel
from openwebui_client.models.open_webui_models_messages_message_form import OpenWebuiModelsMessagesMessageForm
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
    api_instance = openwebui_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    message_id = 'message_id_example' # str | 
    open_webui_models_messages_message_form = openwebui_client.OpenWebuiModelsMessagesMessageForm() # OpenWebuiModelsMessagesMessageForm | 

    try:
        # Update Message By Id
        api_response = await api_instance.update_message_by_id_api_v1_channels_id_messages_message_id_update_post(id, message_id, open_webui_models_messages_message_form)
        print("The response of ChannelsApi->update_message_by_id_api_v1_channels_id_messages_message_id_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->update_message_by_id_api_v1_channels_id_messages_message_id_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **message_id** | **str**|  | 
 **open_webui_models_messages_message_form** | [**OpenWebuiModelsMessagesMessageForm**](OpenWebuiModelsMessagesMessageForm.md)|  | 

### Return type

[**MessageModel**](MessageModel.md)

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

