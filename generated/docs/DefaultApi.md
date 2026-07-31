# openwebui_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat_action_api_chat_actions_action_id_post**](DefaultApi.md#chat_action_api_chat_actions_action_id_post) | **POST** /api/chat/actions/{action_id} | Chat Action
[**chat_completed_api_chat_completed_post**](DefaultApi.md#chat_completed_api_chat_completed_post) | **POST** /api/chat/completed | Chat Completed
[**chat_completion_api_chat_completions_post**](DefaultApi.md#chat_completion_api_chat_completions_post) | **POST** /api/chat/completions | Chat Completion
[**chat_completion_api_v1_chat_completions_post**](DefaultApi.md#chat_completion_api_v1_chat_completions_post) | **POST** /api/v1/chat/completions | Chat Completion
[**check_db_health_health_db_get**](DefaultApi.md#check_db_health_health_db_get) | **GET** /health/db | Check Db Health
[**count_message_tokens_api_message_count_tokens_post**](DefaultApi.md#count_message_tokens_api_message_count_tokens_post) | **POST** /api/message/count_tokens | Count Message Tokens
[**count_message_tokens_api_v1_messages_count_tokens_post**](DefaultApi.md#count_message_tokens_api_v1_messages_count_tokens_post) | **POST** /api/v1/messages/count_tokens | Count Message Tokens
[**create_event_webhook_api_events_webhooks_post**](DefaultApi.md#create_event_webhook_api_events_webhooks_post) | **POST** /api/events/webhooks | Create Event Webhook
[**delete_event_webhook_api_api_events_webhooks_webhook_id_delete**](DefaultApi.md#delete_event_webhook_api_api_events_webhooks_webhook_id_delete) | **DELETE** /api/events/webhooks/{webhook_id} | Delete Event Webhook Api
[**embeddings_api_embeddings_post**](DefaultApi.md#embeddings_api_embeddings_post) | **POST** /api/embeddings | Embeddings
[**embeddings_api_v1_embeddings_post**](DefaultApi.md#embeddings_api_v1_embeddings_post) | **POST** /api/v1/embeddings | Embeddings
[**generate_messages_api_message_post**](DefaultApi.md#generate_messages_api_message_post) | **POST** /api/message | Generate Messages
[**generate_messages_api_v1_messages_post**](DefaultApi.md#generate_messages_api_v1_messages_post) | **POST** /api/v1/messages | Generate Messages
[**get_app_changelog_api_changelog_get**](DefaultApi.md#get_app_changelog_api_changelog_get) | **GET** /api/changelog | Get App Changelog
[**get_app_config_api_config_get**](DefaultApi.md#get_app_config_api_config_get) | **GET** /api/config | Get App Config
[**get_app_latest_release_version_api_version_updates_get**](DefaultApi.md#get_app_latest_release_version_api_version_updates_get) | **GET** /api/version/updates | Get App Latest Release Version
[**get_app_version_api_version_get**](DefaultApi.md#get_app_version_api_version_get) | **GET** /api/version | Get App Version
[**get_base_models_api_models_base_get**](DefaultApi.md#get_base_models_api_models_base_get) | **GET** /api/models/base | Get Base Models
[**get_current_usage_api_usage_get**](DefaultApi.md#get_current_usage_api_usage_get) | **GET** /api/usage | Get Current Usage
[**get_event_catalog_api_events_get**](DefaultApi.md#get_event_catalog_api_events_get) | **GET** /api/events | Get Event Catalog
[**get_event_webhooks_api_api_events_webhooks_get**](DefaultApi.md#get_event_webhooks_api_api_events_webhooks_get) | **GET** /api/events/webhooks | Get Event Webhooks Api
[**get_manifest_json_manifest_json_get**](DefaultApi.md#get_manifest_json_manifest_json_get) | **GET** /manifest.json | Get Manifest Json
[**get_models_api_models_get**](DefaultApi.md#get_models_api_models_get) | **GET** /api/models | Get Models
[**get_models_api_v1_models_get**](DefaultApi.md#get_models_api_v1_models_get) | **GET** /api/v1/models | Get Models
[**get_opensearch_xml_opensearch_xml_get**](DefaultApi.md#get_opensearch_xml_opensearch_xml_get) | **GET** /opensearch.xml | Get Opensearch Xml
[**healthcheck_health_get**](DefaultApi.md#healthcheck_health_get) | **GET** /health | Healthcheck
[**list_tasks_by_chat_id_endpoint_api_tasks_chat_chat_id_get**](DefaultApi.md#list_tasks_by_chat_id_endpoint_api_tasks_chat_chat_id_get) | **GET** /api/tasks/chat/{chat_id} | List Tasks By Chat Id Endpoint
[**list_tasks_endpoint_api_tasks_get**](DefaultApi.md#list_tasks_endpoint_api_tasks_get) | **GET** /api/tasks | List Tasks Endpoint
[**oauth_backchannel_logout_oauth_backchannel_logout_post**](DefaultApi.md#oauth_backchannel_logout_oauth_backchannel_logout_post) | **POST** /oauth/backchannel-logout | Oauth Backchannel Logout
[**oauth_client_authorize_oauth_clients_client_id_authorize_get**](DefaultApi.md#oauth_client_authorize_oauth_clients_client_id_authorize_get) | **GET** /oauth/clients/{client_id}/authorize | Oauth Client Authorize
[**oauth_client_callback_oauth_clients_client_id_callback_get**](DefaultApi.md#oauth_client_callback_oauth_clients_client_id_callback_get) | **GET** /oauth/clients/{client_id}/callback | Oauth Client Callback
[**oauth_login_callback_oauth_provider_callback_get**](DefaultApi.md#oauth_login_callback_oauth_provider_callback_get) | **GET** /oauth/{provider}/callback | Oauth Login Callback
[**oauth_login_callback_oauth_provider_login_callback_get**](DefaultApi.md#oauth_login_callback_oauth_provider_login_callback_get) | **GET** /oauth/{provider}/login/callback | Oauth Login Callback
[**oauth_login_oauth_provider_login_get**](DefaultApi.md#oauth_login_oauth_provider_login_get) | **GET** /oauth/{provider}/login | Oauth Login
[**readiness_check_ready_get**](DefaultApi.md#readiness_check_ready_get) | **GET** /ready | Readiness Check
[**serve_cache_file_cache_path_get**](DefaultApi.md#serve_cache_file_cache_path_get) | **GET** /cache/{path} | Serve Cache File
[**stop_task_endpoint_api_tasks_stop_task_id_post**](DefaultApi.md#stop_task_endpoint_api_tasks_stop_task_id_post) | **POST** /api/tasks/stop/{task_id} | Stop Task Endpoint
[**stop_tasks_by_chat_id_endpoint_api_tasks_chat_chat_id_stop_post**](DefaultApi.md#stop_tasks_by_chat_id_endpoint_api_tasks_chat_chat_id_stop_post) | **POST** /api/tasks/chat/{chat_id}/stop | Stop Tasks By Chat Id Endpoint
[**unload_model_api_models_unload_post**](DefaultApi.md#unload_model_api_models_unload_post) | **POST** /api/models/unload | Unload Model
[**update_event_webhook_api_events_webhooks_webhook_id_put**](DefaultApi.md#update_event_webhook_api_events_webhooks_webhook_id_put) | **PUT** /api/events/webhooks/{webhook_id} | Update Event Webhook


# **chat_action_api_chat_actions_action_id_post**
> object chat_action_api_chat_actions_action_id_post(action_id, request_body)

Chat Action

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
    api_instance = openwebui_client.DefaultApi(api_client)
    action_id = 'action_id_example' # str | 
    request_body = None # Dict[str, object] | 

    try:
        # Chat Action
        api_response = await api_instance.chat_action_api_chat_actions_action_id_post(action_id, request_body)
        print("The response of DefaultApi->chat_action_api_chat_actions_action_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->chat_action_api_chat_actions_action_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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

# **chat_completed_api_chat_completed_post**
> object chat_completed_api_chat_completed_post(request_body)

Chat Completed

Deprecated: outlet filters now run inline during chat completion.
Kept for backward compatibility with external integrations.

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
    api_instance = openwebui_client.DefaultApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Chat Completed
        api_response = await api_instance.chat_completed_api_chat_completed_post(request_body)
        print("The response of DefaultApi->chat_completed_api_chat_completed_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->chat_completed_api_chat_completed_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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

# **chat_completion_api_chat_completions_post**
> object chat_completion_api_chat_completions_post(request_body)

Chat Completion

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
    api_instance = openwebui_client.DefaultApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Chat Completion
        api_response = await api_instance.chat_completion_api_chat_completions_post(request_body)
        print("The response of DefaultApi->chat_completion_api_chat_completions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->chat_completion_api_chat_completions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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

# **chat_completion_api_v1_chat_completions_post**
> object chat_completion_api_v1_chat_completions_post(request_body)

Chat Completion

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
    api_instance = openwebui_client.DefaultApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Chat Completion
        api_response = await api_instance.chat_completion_api_v1_chat_completions_post(request_body)
        print("The response of DefaultApi->chat_completion_api_v1_chat_completions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->chat_completion_api_v1_chat_completions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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

# **check_db_health_health_db_get**
> object check_db_health_health_db_get()

Check Db Health

Verify database connectivity by issuing a lightweight ping.

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
    api_instance = openwebui_client.DefaultApi(api_client)

    try:
        # Check Db Health
        api_response = await api_instance.check_db_health_health_db_get()
        print("The response of DefaultApi->check_db_health_health_db_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->check_db_health_health_db_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_message_tokens_api_message_count_tokens_post**
> object count_message_tokens_api_message_count_tokens_post(request_body)

Count Message Tokens

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
    api_instance = openwebui_client.DefaultApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Count Message Tokens
        api_response = await api_instance.count_message_tokens_api_message_count_tokens_post(request_body)
        print("The response of DefaultApi->count_message_tokens_api_message_count_tokens_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->count_message_tokens_api_message_count_tokens_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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

# **count_message_tokens_api_v1_messages_count_tokens_post**
> object count_message_tokens_api_v1_messages_count_tokens_post(request_body)

Count Message Tokens

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
    api_instance = openwebui_client.DefaultApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Count Message Tokens
        api_response = await api_instance.count_message_tokens_api_v1_messages_count_tokens_post(request_body)
        print("The response of DefaultApi->count_message_tokens_api_v1_messages_count_tokens_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->count_message_tokens_api_v1_messages_count_tokens_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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

# **create_event_webhook_api_events_webhooks_post**
> object create_event_webhook_api_events_webhooks_post(event_webhook_form)

Create Event Webhook

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.event_webhook_form import EventWebhookForm
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
    api_instance = openwebui_client.DefaultApi(api_client)
    event_webhook_form = openwebui_client.EventWebhookForm() # EventWebhookForm | 

    try:
        # Create Event Webhook
        api_response = await api_instance.create_event_webhook_api_events_webhooks_post(event_webhook_form)
        print("The response of DefaultApi->create_event_webhook_api_events_webhooks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_event_webhook_api_events_webhooks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_webhook_form** | [**EventWebhookForm**](EventWebhookForm.md)|  | 

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

# **delete_event_webhook_api_api_events_webhooks_webhook_id_delete**
> object delete_event_webhook_api_api_events_webhooks_webhook_id_delete(webhook_id)

Delete Event Webhook Api

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
    api_instance = openwebui_client.DefaultApi(api_client)
    webhook_id = 'webhook_id_example' # str | 

    try:
        # Delete Event Webhook Api
        api_response = await api_instance.delete_event_webhook_api_api_events_webhooks_webhook_id_delete(webhook_id)
        print("The response of DefaultApi->delete_event_webhook_api_api_events_webhooks_webhook_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_event_webhook_api_api_events_webhooks_webhook_id_delete: %s\n" % e)
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

# **embeddings_api_embeddings_post**
> object embeddings_api_embeddings_post(request_body)

Embeddings

OpenAI-compatible embeddings endpoint.

This handler:
  - Performs user/model checks and dispatches to the correct backend.
  - Supports OpenAI, Ollama, arena models, pipelines, and any compatible provider.

Args:
    request (Request): Request context.
    form_data (dict): OpenAI-like payload (e.g., {"model": "...", "input": [...]})
    user (UserModel): Authenticated user.

Returns:
    dict: OpenAI-compatible embeddings response.

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
    api_instance = openwebui_client.DefaultApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Embeddings
        api_response = await api_instance.embeddings_api_embeddings_post(request_body)
        print("The response of DefaultApi->embeddings_api_embeddings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->embeddings_api_embeddings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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

# **embeddings_api_v1_embeddings_post**
> object embeddings_api_v1_embeddings_post(request_body)

Embeddings

OpenAI-compatible embeddings endpoint.

This handler:
  - Performs user/model checks and dispatches to the correct backend.
  - Supports OpenAI, Ollama, arena models, pipelines, and any compatible provider.

Args:
    request (Request): Request context.
    form_data (dict): OpenAI-like payload (e.g., {"model": "...", "input": [...]})
    user (UserModel): Authenticated user.

Returns:
    dict: OpenAI-compatible embeddings response.

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
    api_instance = openwebui_client.DefaultApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Embeddings
        api_response = await api_instance.embeddings_api_v1_embeddings_post(request_body)
        print("The response of DefaultApi->embeddings_api_v1_embeddings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->embeddings_api_v1_embeddings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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

# **generate_messages_api_message_post**
> object generate_messages_api_message_post(request_body)

Generate Messages

Anthropic Messages API compatible endpoint.

Accepts the Anthropic Messages API format, converts internally to OpenAI
Chat Completions format, routes through the existing chat completion
pipeline, then converts the response back to Anthropic Messages format.

Supports both streaming and non-streaming requests.
All models configured in Open WebUI are accessible via this endpoint.

Authentication: Supports both standard Authorization header and
Anthropic's x-api-key header (via middleware translation).

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
    api_instance = openwebui_client.DefaultApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Generate Messages
        api_response = await api_instance.generate_messages_api_message_post(request_body)
        print("The response of DefaultApi->generate_messages_api_message_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->generate_messages_api_message_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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

# **generate_messages_api_v1_messages_post**
> object generate_messages_api_v1_messages_post(request_body)

Generate Messages

Anthropic Messages API compatible endpoint.

Accepts the Anthropic Messages API format, converts internally to OpenAI
Chat Completions format, routes through the existing chat completion
pipeline, then converts the response back to Anthropic Messages format.

Supports both streaming and non-streaming requests.
All models configured in Open WebUI are accessible via this endpoint.

Authentication: Supports both standard Authorization header and
Anthropic's x-api-key header (via middleware translation).

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
    api_instance = openwebui_client.DefaultApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Generate Messages
        api_response = await api_instance.generate_messages_api_v1_messages_post(request_body)
        print("The response of DefaultApi->generate_messages_api_v1_messages_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->generate_messages_api_v1_messages_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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

# **get_app_changelog_api_changelog_get**
> object get_app_changelog_api_changelog_get()

Get App Changelog

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
    api_instance = openwebui_client.DefaultApi(api_client)

    try:
        # Get App Changelog
        api_response = await api_instance.get_app_changelog_api_changelog_get()
        print("The response of DefaultApi->get_app_changelog_api_changelog_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_app_changelog_api_changelog_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_config_api_config_get**
> object get_app_config_api_config_get()

Get App Config

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
    api_instance = openwebui_client.DefaultApi(api_client)

    try:
        # Get App Config
        api_response = await api_instance.get_app_config_api_config_get()
        print("The response of DefaultApi->get_app_config_api_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_app_config_api_config_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_latest_release_version_api_version_updates_get**
> object get_app_latest_release_version_api_version_updates_get()

Get App Latest Release Version

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
    api_instance = openwebui_client.DefaultApi(api_client)

    try:
        # Get App Latest Release Version
        api_response = await api_instance.get_app_latest_release_version_api_version_updates_get()
        print("The response of DefaultApi->get_app_latest_release_version_api_version_updates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_app_latest_release_version_api_version_updates_get: %s\n" % e)
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

# **get_app_version_api_version_get**
> object get_app_version_api_version_get()

Get App Version

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
    api_instance = openwebui_client.DefaultApi(api_client)

    try:
        # Get App Version
        api_response = await api_instance.get_app_version_api_version_get()
        print("The response of DefaultApi->get_app_version_api_version_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_app_version_api_version_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_base_models_api_models_base_get**
> object get_base_models_api_models_base_get()

Get Base Models

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
    api_instance = openwebui_client.DefaultApi(api_client)

    try:
        # Get Base Models
        api_response = await api_instance.get_base_models_api_models_base_get()
        print("The response of DefaultApi->get_base_models_api_models_base_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_base_models_api_models_base_get: %s\n" % e)
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

# **get_current_usage_api_usage_get**
> object get_current_usage_api_usage_get()

Get Current Usage

Get current usage statistics for Open WebUI.
This is an experimental endpoint and subject to change.

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
    api_instance = openwebui_client.DefaultApi(api_client)

    try:
        # Get Current Usage
        api_response = await api_instance.get_current_usage_api_usage_get()
        print("The response of DefaultApi->get_current_usage_api_usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_current_usage_api_usage_get: %s\n" % e)
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

# **get_event_catalog_api_events_get**
> object get_event_catalog_api_events_get()

Get Event Catalog

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
    api_instance = openwebui_client.DefaultApi(api_client)

    try:
        # Get Event Catalog
        api_response = await api_instance.get_event_catalog_api_events_get()
        print("The response of DefaultApi->get_event_catalog_api_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_event_catalog_api_events_get: %s\n" % e)
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

# **get_event_webhooks_api_api_events_webhooks_get**
> object get_event_webhooks_api_api_events_webhooks_get()

Get Event Webhooks Api

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
    api_instance = openwebui_client.DefaultApi(api_client)

    try:
        # Get Event Webhooks Api
        api_response = await api_instance.get_event_webhooks_api_api_events_webhooks_get()
        print("The response of DefaultApi->get_event_webhooks_api_api_events_webhooks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_event_webhooks_api_api_events_webhooks_get: %s\n" % e)
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

# **get_manifest_json_manifest_json_get**
> object get_manifest_json_manifest_json_get()

Get Manifest Json

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
    api_instance = openwebui_client.DefaultApi(api_client)

    try:
        # Get Manifest Json
        api_response = await api_instance.get_manifest_json_manifest_json_get()
        print("The response of DefaultApi->get_manifest_json_manifest_json_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_manifest_json_manifest_json_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_models_api_models_get**
> object get_models_api_models_get(refresh=refresh)

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
    api_instance = openwebui_client.DefaultApi(api_client)
    refresh = False # bool |  (optional) (default to False)

    try:
        # Get Models
        api_response = await api_instance.get_models_api_models_get(refresh=refresh)
        print("The response of DefaultApi->get_models_api_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_models_api_models_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**|  | [optional] [default to False]

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

# **get_models_api_v1_models_get**
> object get_models_api_v1_models_get(refresh=refresh)

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
    api_instance = openwebui_client.DefaultApi(api_client)
    refresh = False # bool |  (optional) (default to False)

    try:
        # Get Models
        api_response = await api_instance.get_models_api_v1_models_get(refresh=refresh)
        print("The response of DefaultApi->get_models_api_v1_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_models_api_v1_models_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**|  | [optional] [default to False]

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

# **get_opensearch_xml_opensearch_xml_get**
> object get_opensearch_xml_opensearch_xml_get()

Get Opensearch Xml

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
    api_instance = openwebui_client.DefaultApi(api_client)

    try:
        # Get Opensearch Xml
        api_response = await api_instance.get_opensearch_xml_opensearch_xml_get()
        print("The response of DefaultApi->get_opensearch_xml_opensearch_xml_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_opensearch_xml_opensearch_xml_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **healthcheck_health_get**
> object healthcheck_health_get()

Healthcheck

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
    api_instance = openwebui_client.DefaultApi(api_client)

    try:
        # Healthcheck
        api_response = await api_instance.healthcheck_health_get()
        print("The response of DefaultApi->healthcheck_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->healthcheck_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks_by_chat_id_endpoint_api_tasks_chat_chat_id_get**
> object list_tasks_by_chat_id_endpoint_api_tasks_chat_chat_id_get(chat_id)

List Tasks By Chat Id Endpoint

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
    api_instance = openwebui_client.DefaultApi(api_client)
    chat_id = 'chat_id_example' # str | 

    try:
        # List Tasks By Chat Id Endpoint
        api_response = await api_instance.list_tasks_by_chat_id_endpoint_api_tasks_chat_chat_id_get(chat_id)
        print("The response of DefaultApi->list_tasks_by_chat_id_endpoint_api_tasks_chat_chat_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_tasks_by_chat_id_endpoint_api_tasks_chat_chat_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **str**|  | 

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

# **list_tasks_endpoint_api_tasks_get**
> object list_tasks_endpoint_api_tasks_get()

List Tasks Endpoint

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
    api_instance = openwebui_client.DefaultApi(api_client)

    try:
        # List Tasks Endpoint
        api_response = await api_instance.list_tasks_endpoint_api_tasks_get()
        print("The response of DefaultApi->list_tasks_endpoint_api_tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_tasks_endpoint_api_tasks_get: %s\n" % e)
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

# **oauth_backchannel_logout_oauth_backchannel_logout_post**
> object oauth_backchannel_logout_oauth_backchannel_logout_post()

Oauth Backchannel Logout

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
    api_instance = openwebui_client.DefaultApi(api_client)

    try:
        # Oauth Backchannel Logout
        api_response = await api_instance.oauth_backchannel_logout_oauth_backchannel_logout_post()
        print("The response of DefaultApi->oauth_backchannel_logout_oauth_backchannel_logout_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->oauth_backchannel_logout_oauth_backchannel_logout_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_client_authorize_oauth_clients_client_id_authorize_get**
> object oauth_client_authorize_oauth_clients_client_id_authorize_get(client_id)

Oauth Client Authorize

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
    api_instance = openwebui_client.DefaultApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Oauth Client Authorize
        api_response = await api_instance.oauth_client_authorize_oauth_clients_client_id_authorize_get(client_id)
        print("The response of DefaultApi->oauth_client_authorize_oauth_clients_client_id_authorize_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->oauth_client_authorize_oauth_clients_client_id_authorize_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

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

# **oauth_client_callback_oauth_clients_client_id_callback_get**
> object oauth_client_callback_oauth_clients_client_id_callback_get(client_id)

Oauth Client Callback

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
    api_instance = openwebui_client.DefaultApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Oauth Client Callback
        api_response = await api_instance.oauth_client_callback_oauth_clients_client_id_callback_get(client_id)
        print("The response of DefaultApi->oauth_client_callback_oauth_clients_client_id_callback_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->oauth_client_callback_oauth_clients_client_id_callback_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

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

# **oauth_login_callback_oauth_provider_callback_get**
> object oauth_login_callback_oauth_provider_callback_get(provider)

Oauth Login Callback

Handle the OAuth provider callback.

Resolution order:
1. Match by subject ID bound to the provider.
2. If ``OAUTH_MERGE_ACCOUNTS_BY_EMAIL`` is enabled, match by email
   (note: some providers do not verify email addresses).
3. If no match and ``ENABLE_OAUTH_SIGNUP`` is enabled, create a new user
   (fails if the email is already registered).

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
    api_instance = openwebui_client.DefaultApi(api_client)
    provider = 'provider_example' # str | 

    try:
        # Oauth Login Callback
        api_response = await api_instance.oauth_login_callback_oauth_provider_callback_get(provider)
        print("The response of DefaultApi->oauth_login_callback_oauth_provider_callback_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->oauth_login_callback_oauth_provider_callback_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 

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

# **oauth_login_callback_oauth_provider_login_callback_get**
> object oauth_login_callback_oauth_provider_login_callback_get(provider)

Oauth Login Callback

Handle the OAuth provider callback.

Resolution order:
1. Match by subject ID bound to the provider.
2. If ``OAUTH_MERGE_ACCOUNTS_BY_EMAIL`` is enabled, match by email
   (note: some providers do not verify email addresses).
3. If no match and ``ENABLE_OAUTH_SIGNUP`` is enabled, create a new user
   (fails if the email is already registered).

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
    api_instance = openwebui_client.DefaultApi(api_client)
    provider = 'provider_example' # str | 

    try:
        # Oauth Login Callback
        api_response = await api_instance.oauth_login_callback_oauth_provider_login_callback_get(provider)
        print("The response of DefaultApi->oauth_login_callback_oauth_provider_login_callback_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->oauth_login_callback_oauth_provider_login_callback_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 

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

# **oauth_login_oauth_provider_login_get**
> object oauth_login_oauth_provider_login_get(provider)

Oauth Login

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
    api_instance = openwebui_client.DefaultApi(api_client)
    provider = 'provider_example' # str | 

    try:
        # Oauth Login
        api_response = await api_instance.oauth_login_oauth_provider_login_get(provider)
        print("The response of DefaultApi->oauth_login_oauth_provider_login_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->oauth_login_oauth_provider_login_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 

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

# **readiness_check_ready_get**
> object readiness_check_ready_get()

Readiness Check

Returns 200 only when the application is ready to accept traffic.

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
    api_instance = openwebui_client.DefaultApi(api_client)

    try:
        # Readiness Check
        api_response = await api_instance.readiness_check_ready_get()
        print("The response of DefaultApi->readiness_check_ready_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->readiness_check_ready_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serve_cache_file_cache_path_get**
> object serve_cache_file_cache_path_get(path)

Serve Cache File

Serve cached files (e.g. tool outputs) with path-traversal protection.

Only ``image/*``, ``audio/*``, and ``video/*`` MIME types are served inline;
everything else gets a ``Content-Disposition: attachment`` header to prevent
XSS from user-generated HTML stored in the cache directory.

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
    api_instance = openwebui_client.DefaultApi(api_client)
    path = 'path_example' # str | 

    try:
        # Serve Cache File
        api_response = await api_instance.serve_cache_file_cache_path_get(path)
        print("The response of DefaultApi->serve_cache_file_cache_path_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->serve_cache_file_cache_path_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

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

# **stop_task_endpoint_api_tasks_stop_task_id_post**
> object stop_task_endpoint_api_tasks_stop_task_id_post(task_id)

Stop Task Endpoint

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
    api_instance = openwebui_client.DefaultApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Stop Task Endpoint
        api_response = await api_instance.stop_task_endpoint_api_tasks_stop_task_id_post(task_id)
        print("The response of DefaultApi->stop_task_endpoint_api_tasks_stop_task_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->stop_task_endpoint_api_tasks_stop_task_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

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

# **stop_tasks_by_chat_id_endpoint_api_tasks_chat_chat_id_stop_post**
> object stop_tasks_by_chat_id_endpoint_api_tasks_chat_chat_id_stop_post(chat_id)

Stop Tasks By Chat Id Endpoint

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
    api_instance = openwebui_client.DefaultApi(api_client)
    chat_id = 'chat_id_example' # str | 

    try:
        # Stop Tasks By Chat Id Endpoint
        api_response = await api_instance.stop_tasks_by_chat_id_endpoint_api_tasks_chat_chat_id_stop_post(chat_id)
        print("The response of DefaultApi->stop_tasks_by_chat_id_endpoint_api_tasks_chat_chat_id_stop_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->stop_tasks_by_chat_id_endpoint_api_tasks_chat_chat_id_stop_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **str**|  | 

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

# **unload_model_api_models_unload_post**
> object unload_model_api_models_unload_post(model_unload_form)

Unload Model

Unified model unload endpoint.
Resolves the provider that owns the model and calls its native unload mechanism.
Supports: Ollama (keep_alive=0) and llama.cpp (/models/unload).

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.model_unload_form import ModelUnloadForm
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
    api_instance = openwebui_client.DefaultApi(api_client)
    model_unload_form = openwebui_client.ModelUnloadForm() # ModelUnloadForm | 

    try:
        # Unload Model
        api_response = await api_instance.unload_model_api_models_unload_post(model_unload_form)
        print("The response of DefaultApi->unload_model_api_models_unload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->unload_model_api_models_unload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_unload_form** | [**ModelUnloadForm**](ModelUnloadForm.md)|  | 

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

# **update_event_webhook_api_events_webhooks_webhook_id_put**
> object update_event_webhook_api_events_webhooks_webhook_id_put(webhook_id, event_webhook_update_form)

Update Event Webhook

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.event_webhook_update_form import EventWebhookUpdateForm
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
    api_instance = openwebui_client.DefaultApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    event_webhook_update_form = openwebui_client.EventWebhookUpdateForm() # EventWebhookUpdateForm | 

    try:
        # Update Event Webhook
        api_response = await api_instance.update_event_webhook_api_events_webhooks_webhook_id_put(webhook_id, event_webhook_update_form)
        print("The response of DefaultApi->update_event_webhook_api_events_webhooks_webhook_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_event_webhook_api_events_webhooks_webhook_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **event_webhook_update_form** | [**EventWebhookUpdateForm**](EventWebhookUpdateForm.md)|  | 

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

