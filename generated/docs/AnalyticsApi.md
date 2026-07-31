# openwebui_client.AnalyticsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_daily_stats_api_v1_analytics_daily_get**](AnalyticsApi.md#get_daily_stats_api_v1_analytics_daily_get) | **GET** /api/v1/analytics/daily | Get Daily Stats
[**get_messages_api_v1_analytics_messages_get**](AnalyticsApi.md#get_messages_api_v1_analytics_messages_get) | **GET** /api/v1/analytics/messages | Get Messages
[**get_model_analytics_api_v1_analytics_models_get**](AnalyticsApi.md#get_model_analytics_api_v1_analytics_models_get) | **GET** /api/v1/analytics/models | Get Model Analytics
[**get_model_chats_api_v1_analytics_models_model_id_chats_get**](AnalyticsApi.md#get_model_chats_api_v1_analytics_models_model_id_chats_get) | **GET** /api/v1/analytics/models/{model_id}/chats | Get Model Chats
[**get_model_overview_api_v1_analytics_models_model_id_overview_get**](AnalyticsApi.md#get_model_overview_api_v1_analytics_models_model_id_overview_get) | **GET** /api/v1/analytics/models/{model_id}/overview | Get Model Overview
[**get_summary_api_v1_analytics_summary_get**](AnalyticsApi.md#get_summary_api_v1_analytics_summary_get) | **GET** /api/v1/analytics/summary | Get Summary
[**get_token_usage_api_v1_analytics_tokens_get**](AnalyticsApi.md#get_token_usage_api_v1_analytics_tokens_get) | **GET** /api/v1/analytics/tokens | Get Token Usage
[**get_user_analytics_api_v1_analytics_users_get**](AnalyticsApi.md#get_user_analytics_api_v1_analytics_users_get) | **GET** /api/v1/analytics/users | Get User Analytics


# **get_daily_stats_api_v1_analytics_daily_get**
> DailyStatsResponse get_daily_stats_api_v1_analytics_daily_get(start_date=start_date, end_date=end_date, group_id=group_id, granularity=granularity)

Get Daily Stats

Get message counts grouped by model for time-series chart.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.daily_stats_response import DailyStatsResponse
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
    api_instance = openwebui_client.AnalyticsApi(api_client)
    start_date = 56 # int | Start timestamp (epoch) (optional)
    end_date = 56 # int | End timestamp (epoch) (optional)
    group_id = 'group_id_example' # str | Filter by user group ID (optional)
    granularity = 'daily' # str | Granularity: 'hourly' or 'daily' (optional) (default to 'daily')

    try:
        # Get Daily Stats
        api_response = await api_instance.get_daily_stats_api_v1_analytics_daily_get(start_date=start_date, end_date=end_date, group_id=group_id, granularity=granularity)
        print("The response of AnalyticsApi->get_daily_stats_api_v1_analytics_daily_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_daily_stats_api_v1_analytics_daily_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| Start timestamp (epoch) | [optional] 
 **end_date** | **int**| End timestamp (epoch) | [optional] 
 **group_id** | **str**| Filter by user group ID | [optional] 
 **granularity** | **str**| Granularity: &#39;hourly&#39; or &#39;daily&#39; | [optional] [default to &#39;daily&#39;]

### Return type

[**DailyStatsResponse**](DailyStatsResponse.md)

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

# **get_messages_api_v1_analytics_messages_get**
> List[ChatMessageModel] get_messages_api_v1_analytics_messages_get(model_id=model_id, user_id=user_id, chat_id=chat_id, start_date=start_date, end_date=end_date, skip=skip, limit=limit)

Get Messages

Query messages with filters.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_message_model import ChatMessageModel
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
    api_instance = openwebui_client.AnalyticsApi(api_client)
    model_id = 'model_id_example' # str | Filter by model ID (optional)
    user_id = 'user_id_example' # str | Filter by user ID (optional)
    chat_id = 'chat_id_example' # str | Filter by chat ID (optional)
    start_date = 56 # int | Start timestamp (epoch) (optional)
    end_date = 56 # int | End timestamp (epoch) (optional)
    skip = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # Get Messages
        api_response = await api_instance.get_messages_api_v1_analytics_messages_get(model_id=model_id, user_id=user_id, chat_id=chat_id, start_date=start_date, end_date=end_date, skip=skip, limit=limit)
        print("The response of AnalyticsApi->get_messages_api_v1_analytics_messages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_messages_api_v1_analytics_messages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**| Filter by model ID | [optional] 
 **user_id** | **str**| Filter by user ID | [optional] 
 **chat_id** | **str**| Filter by chat ID | [optional] 
 **start_date** | **int**| Start timestamp (epoch) | [optional] 
 **end_date** | **int**| End timestamp (epoch) | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**List[ChatMessageModel]**](ChatMessageModel.md)

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

# **get_model_analytics_api_v1_analytics_models_get**
> ModelAnalyticsResponse get_model_analytics_api_v1_analytics_models_get(start_date=start_date, end_date=end_date, group_id=group_id)

Get Model Analytics

Get message counts per model.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.model_analytics_response import ModelAnalyticsResponse
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
    api_instance = openwebui_client.AnalyticsApi(api_client)
    start_date = 56 # int | Start timestamp (epoch) (optional)
    end_date = 56 # int | End timestamp (epoch) (optional)
    group_id = 'group_id_example' # str | Filter by user group ID (optional)

    try:
        # Get Model Analytics
        api_response = await api_instance.get_model_analytics_api_v1_analytics_models_get(start_date=start_date, end_date=end_date, group_id=group_id)
        print("The response of AnalyticsApi->get_model_analytics_api_v1_analytics_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_model_analytics_api_v1_analytics_models_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| Start timestamp (epoch) | [optional] 
 **end_date** | **int**| End timestamp (epoch) | [optional] 
 **group_id** | **str**| Filter by user group ID | [optional] 

### Return type

[**ModelAnalyticsResponse**](ModelAnalyticsResponse.md)

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

# **get_model_chats_api_v1_analytics_models_model_id_chats_get**
> ModelChatsResponse get_model_chats_api_v1_analytics_models_model_id_chats_get(model_id, start_date=start_date, end_date=end_date, skip=skip, limit=limit, order_by=order_by, direction=direction)

Get Model Chats

Get chats that used a specific model, with preview and feedback info.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.model_chats_response import ModelChatsResponse
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
    api_instance = openwebui_client.AnalyticsApi(api_client)
    model_id = 'model_id_example' # str | 
    start_date = 56 # int |  (optional)
    end_date = 56 # int |  (optional)
    skip = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)
    order_by = 'updated_at' # str |  (optional) (default to 'updated_at')
    direction = 'desc' # str |  (optional) (default to 'desc')

    try:
        # Get Model Chats
        api_response = await api_instance.get_model_chats_api_v1_analytics_models_model_id_chats_get(model_id, start_date=start_date, end_date=end_date, skip=skip, limit=limit, order_by=order_by, direction=direction)
        print("The response of AnalyticsApi->get_model_chats_api_v1_analytics_models_model_id_chats_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_model_chats_api_v1_analytics_models_model_id_chats_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | 
 **start_date** | **int**|  | [optional] 
 **end_date** | **int**|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]
 **order_by** | **str**|  | [optional] [default to &#39;updated_at&#39;]
 **direction** | **str**|  | [optional] [default to &#39;desc&#39;]

### Return type

[**ModelChatsResponse**](ModelChatsResponse.md)

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

# **get_model_overview_api_v1_analytics_models_model_id_overview_get**
> ModelOverviewResponse get_model_overview_api_v1_analytics_models_model_id_overview_get(model_id, days=days)

Get Model Overview

Get model overview with feedback history and chat tags.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.model_overview_response import ModelOverviewResponse
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
    api_instance = openwebui_client.AnalyticsApi(api_client)
    model_id = 'model_id_example' # str | 
    days = 30 # int | Number of days of history (0 for all) (optional) (default to 30)

    try:
        # Get Model Overview
        api_response = await api_instance.get_model_overview_api_v1_analytics_models_model_id_overview_get(model_id, days=days)
        print("The response of AnalyticsApi->get_model_overview_api_v1_analytics_models_model_id_overview_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_model_overview_api_v1_analytics_models_model_id_overview_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | 
 **days** | **int**| Number of days of history (0 for all) | [optional] [default to 30]

### Return type

[**ModelOverviewResponse**](ModelOverviewResponse.md)

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

# **get_summary_api_v1_analytics_summary_get**
> SummaryResponse get_summary_api_v1_analytics_summary_get(start_date=start_date, end_date=end_date, group_id=group_id)

Get Summary

Get summary statistics for the dashboard.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.summary_response import SummaryResponse
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
    api_instance = openwebui_client.AnalyticsApi(api_client)
    start_date = 56 # int | Start timestamp (epoch) (optional)
    end_date = 56 # int | End timestamp (epoch) (optional)
    group_id = 'group_id_example' # str | Filter by user group ID (optional)

    try:
        # Get Summary
        api_response = await api_instance.get_summary_api_v1_analytics_summary_get(start_date=start_date, end_date=end_date, group_id=group_id)
        print("The response of AnalyticsApi->get_summary_api_v1_analytics_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_summary_api_v1_analytics_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| Start timestamp (epoch) | [optional] 
 **end_date** | **int**| End timestamp (epoch) | [optional] 
 **group_id** | **str**| Filter by user group ID | [optional] 

### Return type

[**SummaryResponse**](SummaryResponse.md)

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

# **get_token_usage_api_v1_analytics_tokens_get**
> TokenUsageResponse get_token_usage_api_v1_analytics_tokens_get(start_date=start_date, end_date=end_date, group_id=group_id)

Get Token Usage

Get token usage aggregated by model.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.token_usage_response import TokenUsageResponse
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
    api_instance = openwebui_client.AnalyticsApi(api_client)
    start_date = 56 # int |  (optional)
    end_date = 56 # int |  (optional)
    group_id = 'group_id_example' # str | Filter by user group ID (optional)

    try:
        # Get Token Usage
        api_response = await api_instance.get_token_usage_api_v1_analytics_tokens_get(start_date=start_date, end_date=end_date, group_id=group_id)
        print("The response of AnalyticsApi->get_token_usage_api_v1_analytics_tokens_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_token_usage_api_v1_analytics_tokens_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**|  | [optional] 
 **end_date** | **int**|  | [optional] 
 **group_id** | **str**| Filter by user group ID | [optional] 

### Return type

[**TokenUsageResponse**](TokenUsageResponse.md)

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

# **get_user_analytics_api_v1_analytics_users_get**
> UserAnalyticsResponse get_user_analytics_api_v1_analytics_users_get(start_date=start_date, end_date=end_date, group_id=group_id, limit=limit)

Get User Analytics

Get message counts and token usage per user with user info.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.user_analytics_response import UserAnalyticsResponse
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
    api_instance = openwebui_client.AnalyticsApi(api_client)
    start_date = 56 # int | Start timestamp (epoch) (optional)
    end_date = 56 # int | End timestamp (epoch) (optional)
    group_id = 'group_id_example' # str | Filter by user group ID (optional)
    limit = 50 # int | Max users to return (optional) (default to 50)

    try:
        # Get User Analytics
        api_response = await api_instance.get_user_analytics_api_v1_analytics_users_get(start_date=start_date, end_date=end_date, group_id=group_id, limit=limit)
        print("The response of AnalyticsApi->get_user_analytics_api_v1_analytics_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_user_analytics_api_v1_analytics_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| Start timestamp (epoch) | [optional] 
 **end_date** | **int**| End timestamp (epoch) | [optional] 
 **group_id** | **str**| Filter by user group ID | [optional] 
 **limit** | **int**| Max users to return | [optional] [default to 50]

### Return type

[**UserAnalyticsResponse**](UserAnalyticsResponse.md)

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

