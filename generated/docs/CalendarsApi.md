# openwebui_client.CalendarsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_calendar_api_v1_calendars_create_post**](CalendarsApi.md#create_calendar_api_v1_calendars_create_post) | **POST** /api/v1/calendars/create | Create Calendar
[**create_event_api_v1_calendars_events_create_post**](CalendarsApi.md#create_event_api_v1_calendars_events_create_post) | **POST** /api/v1/calendars/events/create | Create Event
[**delete_calendar_api_v1_calendars_calendar_id_delete_delete**](CalendarsApi.md#delete_calendar_api_v1_calendars_calendar_id_delete_delete) | **DELETE** /api/v1/calendars/{calendar_id}/delete | Delete Calendar
[**delete_event_api_v1_calendars_events_event_id_delete_delete**](CalendarsApi.md#delete_event_api_v1_calendars_events_event_id_delete_delete) | **DELETE** /api/v1/calendars/events/{event_id}/delete | Delete Event
[**get_calendar_by_id_api_v1_calendars_calendar_id_get**](CalendarsApi.md#get_calendar_by_id_api_v1_calendars_calendar_id_get) | **GET** /api/v1/calendars/{calendar_id} | Get Calendar By Id
[**get_calendars_api_v1_calendars_get**](CalendarsApi.md#get_calendars_api_v1_calendars_get) | **GET** /api/v1/calendars/ | Get Calendars
[**get_event_api_v1_calendars_events_event_id_get**](CalendarsApi.md#get_event_api_v1_calendars_events_event_id_get) | **GET** /api/v1/calendars/events/{event_id} | Get Event
[**get_events_api_v1_calendars_events_get**](CalendarsApi.md#get_events_api_v1_calendars_events_get) | **GET** /api/v1/calendars/events | Get Events
[**rsvp_event_api_v1_calendars_events_event_id_rsvp_post**](CalendarsApi.md#rsvp_event_api_v1_calendars_events_event_id_rsvp_post) | **POST** /api/v1/calendars/events/{event_id}/rsvp | Rsvp Event
[**search_events_api_v1_calendars_events_search_get**](CalendarsApi.md#search_events_api_v1_calendars_events_search_get) | **GET** /api/v1/calendars/events/search | Search Events
[**set_default_calendar_api_v1_calendars_calendar_id_default_post**](CalendarsApi.md#set_default_calendar_api_v1_calendars_calendar_id_default_post) | **POST** /api/v1/calendars/{calendar_id}/default | Set Default Calendar
[**update_calendar_api_v1_calendars_calendar_id_update_post**](CalendarsApi.md#update_calendar_api_v1_calendars_calendar_id_update_post) | **POST** /api/v1/calendars/{calendar_id}/update | Update Calendar
[**update_event_api_v1_calendars_events_event_id_update_post**](CalendarsApi.md#update_event_api_v1_calendars_events_event_id_update_post) | **POST** /api/v1/calendars/events/{event_id}/update | Update Event


# **create_calendar_api_v1_calendars_create_post**
> CalendarModel create_calendar_api_v1_calendars_create_post(calendar_form)

Create Calendar

Create a new user calendar.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.calendar_form import CalendarForm
from openwebui_client.models.calendar_model import CalendarModel
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
    api_instance = openwebui_client.CalendarsApi(api_client)
    calendar_form = openwebui_client.CalendarForm() # CalendarForm | 

    try:
        # Create Calendar
        api_response = await api_instance.create_calendar_api_v1_calendars_create_post(calendar_form)
        print("The response of CalendarsApi->create_calendar_api_v1_calendars_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->create_calendar_api_v1_calendars_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar_form** | [**CalendarForm**](CalendarForm.md)|  | 

### Return type

[**CalendarModel**](CalendarModel.md)

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

# **create_event_api_v1_calendars_events_create_post**
> CalendarEventModel create_event_api_v1_calendars_events_create_post(calendar_event_form)

Create Event

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.calendar_event_form import CalendarEventForm
from openwebui_client.models.calendar_event_model import CalendarEventModel
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
    api_instance = openwebui_client.CalendarsApi(api_client)
    calendar_event_form = openwebui_client.CalendarEventForm() # CalendarEventForm | 

    try:
        # Create Event
        api_response = await api_instance.create_event_api_v1_calendars_events_create_post(calendar_event_form)
        print("The response of CalendarsApi->create_event_api_v1_calendars_events_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->create_event_api_v1_calendars_events_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar_event_form** | [**CalendarEventForm**](CalendarEventForm.md)|  | 

### Return type

[**CalendarEventModel**](CalendarEventModel.md)

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

# **delete_calendar_api_v1_calendars_calendar_id_delete_delete**
> object delete_calendar_api_v1_calendars_calendar_id_delete_delete(calendar_id)

Delete Calendar

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
    api_instance = openwebui_client.CalendarsApi(api_client)
    calendar_id = 'calendar_id_example' # str | 

    try:
        # Delete Calendar
        api_response = await api_instance.delete_calendar_api_v1_calendars_calendar_id_delete_delete(calendar_id)
        print("The response of CalendarsApi->delete_calendar_api_v1_calendars_calendar_id_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->delete_calendar_api_v1_calendars_calendar_id_delete_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar_id** | **str**|  | 

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

# **delete_event_api_v1_calendars_events_event_id_delete_delete**
> object delete_event_api_v1_calendars_events_event_id_delete_delete(event_id)

Delete Event

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
    api_instance = openwebui_client.CalendarsApi(api_client)
    event_id = 'event_id_example' # str | 

    try:
        # Delete Event
        api_response = await api_instance.delete_event_api_v1_calendars_events_event_id_delete_delete(event_id)
        print("The response of CalendarsApi->delete_event_api_v1_calendars_events_event_id_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->delete_event_api_v1_calendars_events_event_id_delete_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 

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

# **get_calendar_by_id_api_v1_calendars_calendar_id_get**
> CalendarModel get_calendar_by_id_api_v1_calendars_calendar_id_get(calendar_id)

Get Calendar By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.calendar_model import CalendarModel
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
    api_instance = openwebui_client.CalendarsApi(api_client)
    calendar_id = 'calendar_id_example' # str | 

    try:
        # Get Calendar By Id
        api_response = await api_instance.get_calendar_by_id_api_v1_calendars_calendar_id_get(calendar_id)
        print("The response of CalendarsApi->get_calendar_by_id_api_v1_calendars_calendar_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->get_calendar_by_id_api_v1_calendars_calendar_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar_id** | **str**|  | 

### Return type

[**CalendarModel**](CalendarModel.md)

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

# **get_calendars_api_v1_calendars_get**
> List[CalendarModel] get_calendars_api_v1_calendars_get()

Get Calendars

List user's calendars (owned + shared), plus a virtual Scheduled Tasks calendar
when automations are available.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.calendar_model import CalendarModel
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
    api_instance = openwebui_client.CalendarsApi(api_client)

    try:
        # Get Calendars
        api_response = await api_instance.get_calendars_api_v1_calendars_get()
        print("The response of CalendarsApi->get_calendars_api_v1_calendars_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->get_calendars_api_v1_calendars_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CalendarModel]**](CalendarModel.md)

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

# **get_event_api_v1_calendars_events_event_id_get**
> CalendarEventModel get_event_api_v1_calendars_events_event_id_get(event_id)

Get Event

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.calendar_event_model import CalendarEventModel
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
    api_instance = openwebui_client.CalendarsApi(api_client)
    event_id = 'event_id_example' # str | 

    try:
        # Get Event
        api_response = await api_instance.get_event_api_v1_calendars_events_event_id_get(event_id)
        print("The response of CalendarsApi->get_event_api_v1_calendars_events_event_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->get_event_api_v1_calendars_events_event_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 

### Return type

[**CalendarEventModel**](CalendarEventModel.md)

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

# **get_events_api_v1_calendars_events_get**
> object get_events_api_v1_calendars_events_get(start, end, calendar_ids=calendar_ids)

Get Events

Get events in date range.

Args:
    start: ISO 8601 datetime string (e.g. 2026-04-01T00:00:00)
    end:   ISO 8601 datetime string (e.g. 2026-05-01T00:00:00)
    calendar_ids: optional comma-separated list to filter

Includes:
- Stored events from the database
- Virtual events computed from active automation RRULEs (Scheduled Tasks calendar)

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
    api_instance = openwebui_client.CalendarsApi(api_client)
    start = 'start_example' # str | 
    end = 'end_example' # str | 
    calendar_ids = 'calendar_ids_example' # str |  (optional)

    try:
        # Get Events
        api_response = await api_instance.get_events_api_v1_calendars_events_get(start, end, calendar_ids=calendar_ids)
        print("The response of CalendarsApi->get_events_api_v1_calendars_events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->get_events_api_v1_calendars_events_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **str**|  | 
 **end** | **str**|  | 
 **calendar_ids** | **str**|  | [optional] 

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

# **rsvp_event_api_v1_calendars_events_event_id_rsvp_post**
> Dict[str, object] rsvp_event_api_v1_calendars_events_event_id_rsvp_post(event_id, rsvp_form)

Rsvp Event

Update own RSVP status for an event.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.rsvp_form import RSVPForm
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
    api_instance = openwebui_client.CalendarsApi(api_client)
    event_id = 'event_id_example' # str | 
    rsvp_form = openwebui_client.RSVPForm() # RSVPForm | 

    try:
        # Rsvp Event
        api_response = await api_instance.rsvp_event_api_v1_calendars_events_event_id_rsvp_post(event_id, rsvp_form)
        print("The response of CalendarsApi->rsvp_event_api_v1_calendars_events_event_id_rsvp_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->rsvp_event_api_v1_calendars_events_event_id_rsvp_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 
 **rsvp_form** | [**RSVPForm**](RSVPForm.md)|  | 

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

# **search_events_api_v1_calendars_events_search_get**
> CalendarEventListResponse search_events_api_v1_calendars_events_search_get(query=query, skip=skip, limit=limit)

Search Events

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.calendar_event_list_response import CalendarEventListResponse
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
    api_instance = openwebui_client.CalendarsApi(api_client)
    query = 'query_example' # str |  (optional)
    skip = 0 # int |  (optional) (default to 0)
    limit = 30 # int |  (optional) (default to 30)

    try:
        # Search Events
        api_response = await api_instance.search_events_api_v1_calendars_events_search_get(query=query, skip=skip, limit=limit)
        print("The response of CalendarsApi->search_events_api_v1_calendars_events_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->search_events_api_v1_calendars_events_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 30]

### Return type

[**CalendarEventListResponse**](CalendarEventListResponse.md)

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

# **set_default_calendar_api_v1_calendars_calendar_id_default_post**
> object set_default_calendar_api_v1_calendars_calendar_id_default_post(calendar_id)

Set Default Calendar

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
    api_instance = openwebui_client.CalendarsApi(api_client)
    calendar_id = 'calendar_id_example' # str | 

    try:
        # Set Default Calendar
        api_response = await api_instance.set_default_calendar_api_v1_calendars_calendar_id_default_post(calendar_id)
        print("The response of CalendarsApi->set_default_calendar_api_v1_calendars_calendar_id_default_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->set_default_calendar_api_v1_calendars_calendar_id_default_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar_id** | **str**|  | 

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

# **update_calendar_api_v1_calendars_calendar_id_update_post**
> CalendarModel update_calendar_api_v1_calendars_calendar_id_update_post(calendar_id, calendar_update_form)

Update Calendar

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.calendar_model import CalendarModel
from openwebui_client.models.calendar_update_form import CalendarUpdateForm
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
    api_instance = openwebui_client.CalendarsApi(api_client)
    calendar_id = 'calendar_id_example' # str | 
    calendar_update_form = openwebui_client.CalendarUpdateForm() # CalendarUpdateForm | 

    try:
        # Update Calendar
        api_response = await api_instance.update_calendar_api_v1_calendars_calendar_id_update_post(calendar_id, calendar_update_form)
        print("The response of CalendarsApi->update_calendar_api_v1_calendars_calendar_id_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->update_calendar_api_v1_calendars_calendar_id_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar_id** | **str**|  | 
 **calendar_update_form** | [**CalendarUpdateForm**](CalendarUpdateForm.md)|  | 

### Return type

[**CalendarModel**](CalendarModel.md)

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

# **update_event_api_v1_calendars_events_event_id_update_post**
> CalendarEventModel update_event_api_v1_calendars_events_event_id_update_post(event_id, calendar_event_update_form)

Update Event

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.calendar_event_model import CalendarEventModel
from openwebui_client.models.calendar_event_update_form import CalendarEventUpdateForm
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
    api_instance = openwebui_client.CalendarsApi(api_client)
    event_id = 'event_id_example' # str | 
    calendar_event_update_form = openwebui_client.CalendarEventUpdateForm() # CalendarEventUpdateForm | 

    try:
        # Update Event
        api_response = await api_instance.update_event_api_v1_calendars_events_event_id_update_post(event_id, calendar_event_update_form)
        print("The response of CalendarsApi->update_event_api_v1_calendars_events_event_id_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalendarsApi->update_event_api_v1_calendars_events_event_id_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 
 **calendar_event_update_form** | [**CalendarEventUpdateForm**](CalendarEventUpdateForm.md)|  | 

### Return type

[**CalendarEventModel**](CalendarEventModel.md)

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

