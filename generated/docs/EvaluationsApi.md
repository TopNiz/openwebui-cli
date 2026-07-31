# openwebui_client.EvaluationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_feedback_api_v1_evaluations_feedback_post**](EvaluationsApi.md#create_feedback_api_v1_evaluations_feedback_post) | **POST** /api/v1/evaluations/feedback | Create Feedback
[**delete_all_feedbacks_api_v1_evaluations_feedbacks_all_delete**](EvaluationsApi.md#delete_all_feedbacks_api_v1_evaluations_feedbacks_all_delete) | **DELETE** /api/v1/evaluations/feedbacks/all | Delete All Feedbacks
[**delete_feedback_by_id_api_v1_evaluations_feedback_id_delete**](EvaluationsApi.md#delete_feedback_by_id_api_v1_evaluations_feedback_id_delete) | **DELETE** /api/v1/evaluations/feedback/{id} | Delete Feedback By Id
[**delete_feedbacks_api_v1_evaluations_feedbacks_delete**](EvaluationsApi.md#delete_feedbacks_api_v1_evaluations_feedbacks_delete) | **DELETE** /api/v1/evaluations/feedbacks | Delete Feedbacks
[**export_all_feedbacks_api_v1_evaluations_feedbacks_all_export_get**](EvaluationsApi.md#export_all_feedbacks_api_v1_evaluations_feedbacks_all_export_get) | **GET** /api/v1/evaluations/feedbacks/all/export | Export All Feedbacks
[**get_all_feedback_ids_api_v1_evaluations_feedbacks_all_ids_get**](EvaluationsApi.md#get_all_feedback_ids_api_v1_evaluations_feedbacks_all_ids_get) | **GET** /api/v1/evaluations/feedbacks/all/ids | Get All Feedback Ids
[**get_config_api_v1_evaluations_config_get**](EvaluationsApi.md#get_config_api_v1_evaluations_config_get) | **GET** /api/v1/evaluations/config | Get Config
[**get_feedback_by_id_api_v1_evaluations_feedback_id_get**](EvaluationsApi.md#get_feedback_by_id_api_v1_evaluations_feedback_id_get) | **GET** /api/v1/evaluations/feedback/{id} | Get Feedback By Id
[**get_feedback_model_ids_api_v1_evaluations_feedbacks_models_get**](EvaluationsApi.md#get_feedback_model_ids_api_v1_evaluations_feedbacks_models_get) | **GET** /api/v1/evaluations/feedbacks/models | Get Feedback Model Ids
[**get_feedbacks_api_v1_evaluations_feedbacks_list_get**](EvaluationsApi.md#get_feedbacks_api_v1_evaluations_feedbacks_list_get) | **GET** /api/v1/evaluations/feedbacks/list | Get Feedbacks
[**get_leaderboard_api_v1_evaluations_leaderboard_get**](EvaluationsApi.md#get_leaderboard_api_v1_evaluations_leaderboard_get) | **GET** /api/v1/evaluations/leaderboard | Get Leaderboard
[**get_model_history_api_v1_evaluations_leaderboard_model_id_history_get**](EvaluationsApi.md#get_model_history_api_v1_evaluations_leaderboard_model_id_history_get) | **GET** /api/v1/evaluations/leaderboard/{model_id}/history | Get Model History
[**get_user_feedbacks_api_v1_evaluations_feedbacks_user_get**](EvaluationsApi.md#get_user_feedbacks_api_v1_evaluations_feedbacks_user_get) | **GET** /api/v1/evaluations/feedbacks/user | Get User Feedbacks
[**update_config_api_v1_evaluations_config_post**](EvaluationsApi.md#update_config_api_v1_evaluations_config_post) | **POST** /api/v1/evaluations/config | Update Config
[**update_feedback_by_id_api_v1_evaluations_feedback_id_post**](EvaluationsApi.md#update_feedback_by_id_api_v1_evaluations_feedback_id_post) | **POST** /api/v1/evaluations/feedback/{id} | Update Feedback By Id


# **create_feedback_api_v1_evaluations_feedback_post**
> FeedbackModel create_feedback_api_v1_evaluations_feedback_post(feedback_form)

Create Feedback

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.feedback_form import FeedbackForm
from openwebui_client.models.feedback_model import FeedbackModel
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
    api_instance = openwebui_client.EvaluationsApi(api_client)
    feedback_form = openwebui_client.FeedbackForm() # FeedbackForm | 

    try:
        # Create Feedback
        api_response = await api_instance.create_feedback_api_v1_evaluations_feedback_post(feedback_form)
        print("The response of EvaluationsApi->create_feedback_api_v1_evaluations_feedback_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationsApi->create_feedback_api_v1_evaluations_feedback_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feedback_form** | [**FeedbackForm**](FeedbackForm.md)|  | 

### Return type

[**FeedbackModel**](FeedbackModel.md)

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

# **delete_all_feedbacks_api_v1_evaluations_feedbacks_all_delete**
> object delete_all_feedbacks_api_v1_evaluations_feedbacks_all_delete()

Delete All Feedbacks

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
    api_instance = openwebui_client.EvaluationsApi(api_client)

    try:
        # Delete All Feedbacks
        api_response = await api_instance.delete_all_feedbacks_api_v1_evaluations_feedbacks_all_delete()
        print("The response of EvaluationsApi->delete_all_feedbacks_api_v1_evaluations_feedbacks_all_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationsApi->delete_all_feedbacks_api_v1_evaluations_feedbacks_all_delete: %s\n" % e)
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

# **delete_feedback_by_id_api_v1_evaluations_feedback_id_delete**
> object delete_feedback_by_id_api_v1_evaluations_feedback_id_delete(id)

Delete Feedback By Id

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
    api_instance = openwebui_client.EvaluationsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Feedback By Id
        api_response = await api_instance.delete_feedback_by_id_api_v1_evaluations_feedback_id_delete(id)
        print("The response of EvaluationsApi->delete_feedback_by_id_api_v1_evaluations_feedback_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationsApi->delete_feedback_by_id_api_v1_evaluations_feedback_id_delete: %s\n" % e)
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

# **delete_feedbacks_api_v1_evaluations_feedbacks_delete**
> bool delete_feedbacks_api_v1_evaluations_feedbacks_delete()

Delete Feedbacks

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
    api_instance = openwebui_client.EvaluationsApi(api_client)

    try:
        # Delete Feedbacks
        api_response = await api_instance.delete_feedbacks_api_v1_evaluations_feedbacks_delete()
        print("The response of EvaluationsApi->delete_feedbacks_api_v1_evaluations_feedbacks_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationsApi->delete_feedbacks_api_v1_evaluations_feedbacks_delete: %s\n" % e)
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

# **export_all_feedbacks_api_v1_evaluations_feedbacks_all_export_get**
> List[FeedbackModel] export_all_feedbacks_api_v1_evaluations_feedbacks_all_export_get(model_id=model_id)

Export All Feedbacks

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.feedback_model import FeedbackModel
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
    api_instance = openwebui_client.EvaluationsApi(api_client)
    model_id = 'model_id_example' # str |  (optional)

    try:
        # Export All Feedbacks
        api_response = await api_instance.export_all_feedbacks_api_v1_evaluations_feedbacks_all_export_get(model_id=model_id)
        print("The response of EvaluationsApi->export_all_feedbacks_api_v1_evaluations_feedbacks_all_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationsApi->export_all_feedbacks_api_v1_evaluations_feedbacks_all_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | [optional] 

### Return type

[**List[FeedbackModel]**](FeedbackModel.md)

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

# **get_all_feedback_ids_api_v1_evaluations_feedbacks_all_ids_get**
> List[FeedbackIdResponse] get_all_feedback_ids_api_v1_evaluations_feedbacks_all_ids_get()

Get All Feedback Ids

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.feedback_id_response import FeedbackIdResponse
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
    api_instance = openwebui_client.EvaluationsApi(api_client)

    try:
        # Get All Feedback Ids
        api_response = await api_instance.get_all_feedback_ids_api_v1_evaluations_feedbacks_all_ids_get()
        print("The response of EvaluationsApi->get_all_feedback_ids_api_v1_evaluations_feedbacks_all_ids_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationsApi->get_all_feedback_ids_api_v1_evaluations_feedbacks_all_ids_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FeedbackIdResponse]**](FeedbackIdResponse.md)

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

# **get_config_api_v1_evaluations_config_get**
> object get_config_api_v1_evaluations_config_get()

Get Config

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
    api_instance = openwebui_client.EvaluationsApi(api_client)

    try:
        # Get Config
        api_response = await api_instance.get_config_api_v1_evaluations_config_get()
        print("The response of EvaluationsApi->get_config_api_v1_evaluations_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationsApi->get_config_api_v1_evaluations_config_get: %s\n" % e)
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

# **get_feedback_by_id_api_v1_evaluations_feedback_id_get**
> FeedbackModel get_feedback_by_id_api_v1_evaluations_feedback_id_get(id)

Get Feedback By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.feedback_model import FeedbackModel
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
    api_instance = openwebui_client.EvaluationsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Feedback By Id
        api_response = await api_instance.get_feedback_by_id_api_v1_evaluations_feedback_id_get(id)
        print("The response of EvaluationsApi->get_feedback_by_id_api_v1_evaluations_feedback_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationsApi->get_feedback_by_id_api_v1_evaluations_feedback_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FeedbackModel**](FeedbackModel.md)

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

# **get_feedback_model_ids_api_v1_evaluations_feedbacks_models_get**
> List[Optional[str]] get_feedback_model_ids_api_v1_evaluations_feedbacks_models_get()

Get Feedback Model Ids

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
    api_instance = openwebui_client.EvaluationsApi(api_client)

    try:
        # Get Feedback Model Ids
        api_response = await api_instance.get_feedback_model_ids_api_v1_evaluations_feedbacks_models_get()
        print("The response of EvaluationsApi->get_feedback_model_ids_api_v1_evaluations_feedbacks_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationsApi->get_feedback_model_ids_api_v1_evaluations_feedbacks_models_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[Optional[str]]**

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

# **get_feedbacks_api_v1_evaluations_feedbacks_list_get**
> FeedbackListResponse get_feedbacks_api_v1_evaluations_feedbacks_list_get(order_by=order_by, direction=direction, page=page, model_id=model_id)

Get Feedbacks

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.feedback_list_response import FeedbackListResponse
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
    api_instance = openwebui_client.EvaluationsApi(api_client)
    order_by = 'order_by_example' # str |  (optional)
    direction = 'direction_example' # str |  (optional)
    page = 56 # int |  (optional)
    model_id = 'model_id_example' # str |  (optional)

    try:
        # Get Feedbacks
        api_response = await api_instance.get_feedbacks_api_v1_evaluations_feedbacks_list_get(order_by=order_by, direction=direction, page=page, model_id=model_id)
        print("The response of EvaluationsApi->get_feedbacks_api_v1_evaluations_feedbacks_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationsApi->get_feedbacks_api_v1_evaluations_feedbacks_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_by** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **model_id** | **str**|  | [optional] 

### Return type

[**FeedbackListResponse**](FeedbackListResponse.md)

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

# **get_leaderboard_api_v1_evaluations_leaderboard_get**
> LeaderboardResponse get_leaderboard_api_v1_evaluations_leaderboard_get(query=query)

Get Leaderboard

Get model leaderboard with Elo ratings. Query filters by tag similarity.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.leaderboard_response import LeaderboardResponse
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
    api_instance = openwebui_client.EvaluationsApi(api_client)
    query = 'query_example' # str |  (optional)

    try:
        # Get Leaderboard
        api_response = await api_instance.get_leaderboard_api_v1_evaluations_leaderboard_get(query=query)
        print("The response of EvaluationsApi->get_leaderboard_api_v1_evaluations_leaderboard_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationsApi->get_leaderboard_api_v1_evaluations_leaderboard_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 

### Return type

[**LeaderboardResponse**](LeaderboardResponse.md)

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

# **get_model_history_api_v1_evaluations_leaderboard_model_id_history_get**
> ModelHistoryResponse get_model_history_api_v1_evaluations_leaderboard_model_id_history_get(model_id, days=days)

Get Model History

Get daily win/loss history for a specific model.

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.model_history_response import ModelHistoryResponse
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
    api_instance = openwebui_client.EvaluationsApi(api_client)
    model_id = 'model_id_example' # str | 
    days = 30 # int |  (optional) (default to 30)

    try:
        # Get Model History
        api_response = await api_instance.get_model_history_api_v1_evaluations_leaderboard_model_id_history_get(model_id, days=days)
        print("The response of EvaluationsApi->get_model_history_api_v1_evaluations_leaderboard_model_id_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationsApi->get_model_history_api_v1_evaluations_leaderboard_model_id_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | 
 **days** | **int**|  | [optional] [default to 30]

### Return type

[**ModelHistoryResponse**](ModelHistoryResponse.md)

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

# **get_user_feedbacks_api_v1_evaluations_feedbacks_user_get**
> FeedbackListResponse get_user_feedbacks_api_v1_evaluations_feedbacks_user_get(page=page)

Get User Feedbacks

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.feedback_list_response import FeedbackListResponse
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
    api_instance = openwebui_client.EvaluationsApi(api_client)
    page = 56 # int |  (optional)

    try:
        # Get User Feedbacks
        api_response = await api_instance.get_user_feedbacks_api_v1_evaluations_feedbacks_user_get(page=page)
        print("The response of EvaluationsApi->get_user_feedbacks_api_v1_evaluations_feedbacks_user_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationsApi->get_user_feedbacks_api_v1_evaluations_feedbacks_user_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 

### Return type

[**FeedbackListResponse**](FeedbackListResponse.md)

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

# **update_config_api_v1_evaluations_config_post**
> object update_config_api_v1_evaluations_config_post(update_config_form)

Update Config

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.update_config_form import UpdateConfigForm
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
    api_instance = openwebui_client.EvaluationsApi(api_client)
    update_config_form = openwebui_client.UpdateConfigForm() # UpdateConfigForm | 

    try:
        # Update Config
        api_response = await api_instance.update_config_api_v1_evaluations_config_post(update_config_form)
        print("The response of EvaluationsApi->update_config_api_v1_evaluations_config_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationsApi->update_config_api_v1_evaluations_config_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_config_form** | [**UpdateConfigForm**](UpdateConfigForm.md)|  | 

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

# **update_feedback_by_id_api_v1_evaluations_feedback_id_post**
> FeedbackModel update_feedback_by_id_api_v1_evaluations_feedback_id_post(id, feedback_form)

Update Feedback By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.feedback_form import FeedbackForm
from openwebui_client.models.feedback_model import FeedbackModel
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
    api_instance = openwebui_client.EvaluationsApi(api_client)
    id = 'id_example' # str | 
    feedback_form = openwebui_client.FeedbackForm() # FeedbackForm | 

    try:
        # Update Feedback By Id
        api_response = await api_instance.update_feedback_by_id_api_v1_evaluations_feedback_id_post(id, feedback_form)
        print("The response of EvaluationsApi->update_feedback_by_id_api_v1_evaluations_feedback_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EvaluationsApi->update_feedback_by_id_api_v1_evaluations_feedback_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **feedback_form** | [**FeedbackForm**](FeedbackForm.md)|  | 

### Return type

[**FeedbackModel**](FeedbackModel.md)

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

