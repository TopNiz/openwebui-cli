# openwebui_client.NotificationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification_target_api_v1_notifications_targets_post**](NotificationsApi.md#create_notification_target_api_v1_notifications_targets_post) | **POST** /api/v1/notifications/targets | Create Notification Target
[**delete_notification_target_api_v1_notifications_targets_target_id_delete**](NotificationsApi.md#delete_notification_target_api_v1_notifications_targets_target_id_delete) | **DELETE** /api/v1/notifications/targets/{target_id} | Delete Notification Target
[**get_notification_events_api_v1_notifications_events_get**](NotificationsApi.md#get_notification_events_api_v1_notifications_events_get) | **GET** /api/v1/notifications/events | Get Notification Events
[**get_notification_targets_api_v1_notifications_targets_get**](NotificationsApi.md#get_notification_targets_api_v1_notifications_targets_get) | **GET** /api/v1/notifications/targets | Get Notification Targets
[**set_default_notification_target_api_v1_notifications_targets_target_id_default_put**](NotificationsApi.md#set_default_notification_target_api_v1_notifications_targets_target_id_default_put) | **PUT** /api/v1/notifications/targets/{target_id}/default | Set Default Notification Target
[**test_notification_target_api_v1_notifications_targets_target_id_test_post**](NotificationsApi.md#test_notification_target_api_v1_notifications_targets_target_id_test_post) | **POST** /api/v1/notifications/targets/{target_id}/test | Test Notification Target
[**update_notification_target_api_v1_notifications_targets_target_id_put**](NotificationsApi.md#update_notification_target_api_v1_notifications_targets_target_id_put) | **PUT** /api/v1/notifications/targets/{target_id} | Update Notification Target


# **create_notification_target_api_v1_notifications_targets_post**
> object create_notification_target_api_v1_notifications_targets_post(notification_target_form)

Create Notification Target

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.notification_target_form import NotificationTargetForm
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
    api_instance = openwebui_client.NotificationsApi(api_client)
    notification_target_form = openwebui_client.NotificationTargetForm() # NotificationTargetForm | 

    try:
        # Create Notification Target
        api_response = await api_instance.create_notification_target_api_v1_notifications_targets_post(notification_target_form)
        print("The response of NotificationsApi->create_notification_target_api_v1_notifications_targets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->create_notification_target_api_v1_notifications_targets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_target_form** | [**NotificationTargetForm**](NotificationTargetForm.md)|  | 

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

# **delete_notification_target_api_v1_notifications_targets_target_id_delete**
> object delete_notification_target_api_v1_notifications_targets_target_id_delete(target_id)

Delete Notification Target

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
    api_instance = openwebui_client.NotificationsApi(api_client)
    target_id = 'target_id_example' # str | 

    try:
        # Delete Notification Target
        api_response = await api_instance.delete_notification_target_api_v1_notifications_targets_target_id_delete(target_id)
        print("The response of NotificationsApi->delete_notification_target_api_v1_notifications_targets_target_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->delete_notification_target_api_v1_notifications_targets_target_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 

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

# **get_notification_events_api_v1_notifications_events_get**
> object get_notification_events_api_v1_notifications_events_get()

Get Notification Events

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
    api_instance = openwebui_client.NotificationsApi(api_client)

    try:
        # Get Notification Events
        api_response = await api_instance.get_notification_events_api_v1_notifications_events_get()
        print("The response of NotificationsApi->get_notification_events_api_v1_notifications_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notification_events_api_v1_notifications_events_get: %s\n" % e)
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

# **get_notification_targets_api_v1_notifications_targets_get**
> object get_notification_targets_api_v1_notifications_targets_get()

Get Notification Targets

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
    api_instance = openwebui_client.NotificationsApi(api_client)

    try:
        # Get Notification Targets
        api_response = await api_instance.get_notification_targets_api_v1_notifications_targets_get()
        print("The response of NotificationsApi->get_notification_targets_api_v1_notifications_targets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notification_targets_api_v1_notifications_targets_get: %s\n" % e)
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

# **set_default_notification_target_api_v1_notifications_targets_target_id_default_put**
> object set_default_notification_target_api_v1_notifications_targets_target_id_default_put(target_id)

Set Default Notification Target

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
    api_instance = openwebui_client.NotificationsApi(api_client)
    target_id = 'target_id_example' # str | 

    try:
        # Set Default Notification Target
        api_response = await api_instance.set_default_notification_target_api_v1_notifications_targets_target_id_default_put(target_id)
        print("The response of NotificationsApi->set_default_notification_target_api_v1_notifications_targets_target_id_default_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->set_default_notification_target_api_v1_notifications_targets_target_id_default_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 

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

# **test_notification_target_api_v1_notifications_targets_target_id_test_post**
> object test_notification_target_api_v1_notifications_targets_target_id_test_post(target_id)

Test Notification Target

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
    api_instance = openwebui_client.NotificationsApi(api_client)
    target_id = 'target_id_example' # str | 

    try:
        # Test Notification Target
        api_response = await api_instance.test_notification_target_api_v1_notifications_targets_target_id_test_post(target_id)
        print("The response of NotificationsApi->test_notification_target_api_v1_notifications_targets_target_id_test_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->test_notification_target_api_v1_notifications_targets_target_id_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 

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

# **update_notification_target_api_v1_notifications_targets_target_id_put**
> object update_notification_target_api_v1_notifications_targets_target_id_put(target_id, notification_target_form)

Update Notification Target

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.notification_target_form import NotificationTargetForm
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
    api_instance = openwebui_client.NotificationsApi(api_client)
    target_id = 'target_id_example' # str | 
    notification_target_form = openwebui_client.NotificationTargetForm() # NotificationTargetForm | 

    try:
        # Update Notification Target
        api_response = await api_instance.update_notification_target_api_v1_notifications_targets_target_id_put(target_id, notification_target_form)
        print("The response of NotificationsApi->update_notification_target_api_v1_notifications_targets_target_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->update_notification_target_api_v1_notifications_targets_target_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**|  | 
 **notification_target_form** | [**NotificationTargetForm**](NotificationTargetForm.md)|  | 

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

