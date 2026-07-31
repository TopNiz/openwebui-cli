# openwebui_client.AutomationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_automation_api_v1_automations_create_post**](AutomationsApi.md#create_new_automation_api_v1_automations_create_post) | **POST** /api/v1/automations/create | Create New Automation
[**delete_automation_by_id_api_v1_automations_id_delete_delete**](AutomationsApi.md#delete_automation_by_id_api_v1_automations_id_delete_delete) | **DELETE** /api/v1/automations/{id}/delete | Delete Automation By Id
[**get_automation_by_id_api_v1_automations_id_get**](AutomationsApi.md#get_automation_by_id_api_v1_automations_id_get) | **GET** /api/v1/automations/{id} | Get Automation By Id
[**get_automation_items_api_v1_automations_list_get**](AutomationsApi.md#get_automation_items_api_v1_automations_list_get) | **GET** /api/v1/automations/list | Get Automation Items
[**get_automation_runs_api_v1_automations_id_runs_get**](AutomationsApi.md#get_automation_runs_api_v1_automations_id_runs_get) | **GET** /api/v1/automations/{id}/runs | Get Automation Runs
[**run_automation_by_id_api_v1_automations_id_run_post**](AutomationsApi.md#run_automation_by_id_api_v1_automations_id_run_post) | **POST** /api/v1/automations/{id}/run | Run Automation By Id
[**toggle_automation_by_id_api_v1_automations_id_toggle_post**](AutomationsApi.md#toggle_automation_by_id_api_v1_automations_id_toggle_post) | **POST** /api/v1/automations/{id}/toggle | Toggle Automation By Id
[**update_automation_by_id_api_v1_automations_id_update_post**](AutomationsApi.md#update_automation_by_id_api_v1_automations_id_update_post) | **POST** /api/v1/automations/{id}/update | Update Automation By Id


# **create_new_automation_api_v1_automations_create_post**
> AutomationResponse create_new_automation_api_v1_automations_create_post(automation_form)

Create New Automation

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.automation_form import AutomationForm
from openwebui_client.models.automation_response import AutomationResponse
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
    api_instance = openwebui_client.AutomationsApi(api_client)
    automation_form = openwebui_client.AutomationForm() # AutomationForm | 

    try:
        # Create New Automation
        api_response = await api_instance.create_new_automation_api_v1_automations_create_post(automation_form)
        print("The response of AutomationsApi->create_new_automation_api_v1_automations_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationsApi->create_new_automation_api_v1_automations_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automation_form** | [**AutomationForm**](AutomationForm.md)|  | 

### Return type

[**AutomationResponse**](AutomationResponse.md)

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

# **delete_automation_by_id_api_v1_automations_id_delete_delete**
> object delete_automation_by_id_api_v1_automations_id_delete_delete(id)

Delete Automation By Id

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
    api_instance = openwebui_client.AutomationsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Automation By Id
        api_response = await api_instance.delete_automation_by_id_api_v1_automations_id_delete_delete(id)
        print("The response of AutomationsApi->delete_automation_by_id_api_v1_automations_id_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationsApi->delete_automation_by_id_api_v1_automations_id_delete_delete: %s\n" % e)
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

# **get_automation_by_id_api_v1_automations_id_get**
> AutomationResponse get_automation_by_id_api_v1_automations_id_get(id)

Get Automation By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.automation_response import AutomationResponse
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
    api_instance = openwebui_client.AutomationsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Automation By Id
        api_response = await api_instance.get_automation_by_id_api_v1_automations_id_get(id)
        print("The response of AutomationsApi->get_automation_by_id_api_v1_automations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationsApi->get_automation_by_id_api_v1_automations_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AutomationResponse**](AutomationResponse.md)

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

# **get_automation_items_api_v1_automations_list_get**
> object get_automation_items_api_v1_automations_list_get(query=query, status=status, folder_id=folder_id, page=page)

Get Automation Items

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
    api_instance = openwebui_client.AutomationsApi(api_client)
    query = 'query_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    folder_id = 'folder_id_example' # str |  (optional)
    page = 56 # int |  (optional)

    try:
        # Get Automation Items
        api_response = await api_instance.get_automation_items_api_v1_automations_list_get(query=query, status=status, folder_id=folder_id, page=page)
        print("The response of AutomationsApi->get_automation_items_api_v1_automations_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationsApi->get_automation_items_api_v1_automations_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **folder_id** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 

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

# **get_automation_runs_api_v1_automations_id_runs_get**
> List[AutomationRunModel] get_automation_runs_api_v1_automations_id_runs_get(id, skip=skip, limit=limit)

Get Automation Runs

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.automation_run_model import AutomationRunModel
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
    api_instance = openwebui_client.AutomationsApi(api_client)
    id = 'id_example' # str | 
    skip = 0 # int |  (optional) (default to 0)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # Get Automation Runs
        api_response = await api_instance.get_automation_runs_api_v1_automations_id_runs_get(id, skip=skip, limit=limit)
        print("The response of AutomationsApi->get_automation_runs_api_v1_automations_id_runs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationsApi->get_automation_runs_api_v1_automations_id_runs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**List[AutomationRunModel]**](AutomationRunModel.md)

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

# **run_automation_by_id_api_v1_automations_id_run_post**
> object run_automation_by_id_api_v1_automations_id_run_post(id)

Run Automation By Id

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
    api_instance = openwebui_client.AutomationsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Run Automation By Id
        api_response = await api_instance.run_automation_by_id_api_v1_automations_id_run_post(id)
        print("The response of AutomationsApi->run_automation_by_id_api_v1_automations_id_run_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationsApi->run_automation_by_id_api_v1_automations_id_run_post: %s\n" % e)
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

# **toggle_automation_by_id_api_v1_automations_id_toggle_post**
> AutomationResponse toggle_automation_by_id_api_v1_automations_id_toggle_post(id)

Toggle Automation By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.automation_response import AutomationResponse
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
    api_instance = openwebui_client.AutomationsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Toggle Automation By Id
        api_response = await api_instance.toggle_automation_by_id_api_v1_automations_id_toggle_post(id)
        print("The response of AutomationsApi->toggle_automation_by_id_api_v1_automations_id_toggle_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationsApi->toggle_automation_by_id_api_v1_automations_id_toggle_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AutomationResponse**](AutomationResponse.md)

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

# **update_automation_by_id_api_v1_automations_id_update_post**
> AutomationResponse update_automation_by_id_api_v1_automations_id_update_post(id, automation_form)

Update Automation By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.automation_form import AutomationForm
from openwebui_client.models.automation_response import AutomationResponse
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
    api_instance = openwebui_client.AutomationsApi(api_client)
    id = 'id_example' # str | 
    automation_form = openwebui_client.AutomationForm() # AutomationForm | 

    try:
        # Update Automation By Id
        api_response = await api_instance.update_automation_by_id_api_v1_automations_id_update_post(id, automation_form)
        print("The response of AutomationsApi->update_automation_by_id_api_v1_automations_id_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationsApi->update_automation_by_id_api_v1_automations_id_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **automation_form** | [**AutomationForm**](AutomationForm.md)|  | 

### Return type

[**AutomationResponse**](AutomationResponse.md)

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

