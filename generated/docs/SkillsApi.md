# openwebui_client.SkillsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_skill_api_v1_skills_create_post**](SkillsApi.md#create_new_skill_api_v1_skills_create_post) | **POST** /api/v1/skills/create | Create New Skill
[**delete_skill_by_id_api_v1_skills_id_id_delete_delete**](SkillsApi.md#delete_skill_by_id_api_v1_skills_id_id_delete_delete) | **DELETE** /api/v1/skills/id/{id}/delete | Delete Skill By Id
[**export_skills_api_v1_skills_export_get**](SkillsApi.md#export_skills_api_v1_skills_export_get) | **GET** /api/v1/skills/export | Export Skills
[**get_skill_by_id_api_v1_skills_id_id_get**](SkillsApi.md#get_skill_by_id_api_v1_skills_id_id_get) | **GET** /api/v1/skills/id/{id} | Get Skill By Id
[**get_skill_list_api_v1_skills_list_get**](SkillsApi.md#get_skill_list_api_v1_skills_list_get) | **GET** /api/v1/skills/list | Get Skill List
[**get_skills_api_v1_skills_get**](SkillsApi.md#get_skills_api_v1_skills_get) | **GET** /api/v1/skills/ | Get Skills
[**toggle_skill_by_id_api_v1_skills_id_id_toggle_post**](SkillsApi.md#toggle_skill_by_id_api_v1_skills_id_id_toggle_post) | **POST** /api/v1/skills/id/{id}/toggle | Toggle Skill By Id
[**update_skill_access_by_id_api_v1_skills_id_id_access_update_post**](SkillsApi.md#update_skill_access_by_id_api_v1_skills_id_id_access_update_post) | **POST** /api/v1/skills/id/{id}/access/update | Update Skill Access By Id
[**update_skill_by_id_api_v1_skills_id_id_update_post**](SkillsApi.md#update_skill_by_id_api_v1_skills_id_id_update_post) | **POST** /api/v1/skills/id/{id}/update | Update Skill By Id


# **create_new_skill_api_v1_skills_create_post**
> SkillResponse create_new_skill_api_v1_skills_create_post(skill_form)

Create New Skill

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.skill_form import SkillForm
from openwebui_client.models.skill_response import SkillResponse
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
    api_instance = openwebui_client.SkillsApi(api_client)
    skill_form = openwebui_client.SkillForm() # SkillForm | 

    try:
        # Create New Skill
        api_response = await api_instance.create_new_skill_api_v1_skills_create_post(skill_form)
        print("The response of SkillsApi->create_new_skill_api_v1_skills_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SkillsApi->create_new_skill_api_v1_skills_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skill_form** | [**SkillForm**](SkillForm.md)|  | 

### Return type

[**SkillResponse**](SkillResponse.md)

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

# **delete_skill_by_id_api_v1_skills_id_id_delete_delete**
> bool delete_skill_by_id_api_v1_skills_id_id_delete_delete(id)

Delete Skill By Id

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
    api_instance = openwebui_client.SkillsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Skill By Id
        api_response = await api_instance.delete_skill_by_id_api_v1_skills_id_id_delete_delete(id)
        print("The response of SkillsApi->delete_skill_by_id_api_v1_skills_id_id_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SkillsApi->delete_skill_by_id_api_v1_skills_id_id_delete_delete: %s\n" % e)
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

# **export_skills_api_v1_skills_export_get**
> List[SkillModel] export_skills_api_v1_skills_export_get()

Export Skills

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.skill_model import SkillModel
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
    api_instance = openwebui_client.SkillsApi(api_client)

    try:
        # Export Skills
        api_response = await api_instance.export_skills_api_v1_skills_export_get()
        print("The response of SkillsApi->export_skills_api_v1_skills_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SkillsApi->export_skills_api_v1_skills_export_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SkillModel]**](SkillModel.md)

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

# **get_skill_by_id_api_v1_skills_id_id_get**
> SkillAccessResponse get_skill_by_id_api_v1_skills_id_id_get(id)

Get Skill By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.skill_access_response import SkillAccessResponse
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
    api_instance = openwebui_client.SkillsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Skill By Id
        api_response = await api_instance.get_skill_by_id_api_v1_skills_id_id_get(id)
        print("The response of SkillsApi->get_skill_by_id_api_v1_skills_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SkillsApi->get_skill_by_id_api_v1_skills_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SkillAccessResponse**](SkillAccessResponse.md)

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

# **get_skill_list_api_v1_skills_list_get**
> SkillAccessListResponse get_skill_list_api_v1_skills_list_get(query=query, view_option=view_option, order_by=order_by, direction=direction, page=page)

Get Skill List

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.skill_access_list_response import SkillAccessListResponse
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
    api_instance = openwebui_client.SkillsApi(api_client)
    query = 'query_example' # str |  (optional)
    view_option = 'view_option_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    direction = 'direction_example' # str |  (optional)
    page = 56 # int |  (optional)

    try:
        # Get Skill List
        api_response = await api_instance.get_skill_list_api_v1_skills_list_get(query=query, view_option=view_option, order_by=order_by, direction=direction, page=page)
        print("The response of SkillsApi->get_skill_list_api_v1_skills_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SkillsApi->get_skill_list_api_v1_skills_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **view_option** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **direction** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 

### Return type

[**SkillAccessListResponse**](SkillAccessListResponse.md)

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

# **get_skills_api_v1_skills_get**
> List[SkillUserResponse] get_skills_api_v1_skills_get()

Get Skills

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.skill_user_response import SkillUserResponse
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
    api_instance = openwebui_client.SkillsApi(api_client)

    try:
        # Get Skills
        api_response = await api_instance.get_skills_api_v1_skills_get()
        print("The response of SkillsApi->get_skills_api_v1_skills_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SkillsApi->get_skills_api_v1_skills_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SkillUserResponse]**](SkillUserResponse.md)

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

# **toggle_skill_by_id_api_v1_skills_id_id_toggle_post**
> SkillModel toggle_skill_by_id_api_v1_skills_id_id_toggle_post(id)

Toggle Skill By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.skill_model import SkillModel
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
    api_instance = openwebui_client.SkillsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Toggle Skill By Id
        api_response = await api_instance.toggle_skill_by_id_api_v1_skills_id_id_toggle_post(id)
        print("The response of SkillsApi->toggle_skill_by_id_api_v1_skills_id_id_toggle_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SkillsApi->toggle_skill_by_id_api_v1_skills_id_id_toggle_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SkillModel**](SkillModel.md)

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

# **update_skill_access_by_id_api_v1_skills_id_id_access_update_post**
> SkillModel update_skill_access_by_id_api_v1_skills_id_id_access_update_post(id, skill_access_grants_form)

Update Skill Access By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.skill_access_grants_form import SkillAccessGrantsForm
from openwebui_client.models.skill_model import SkillModel
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
    api_instance = openwebui_client.SkillsApi(api_client)
    id = 'id_example' # str | 
    skill_access_grants_form = openwebui_client.SkillAccessGrantsForm() # SkillAccessGrantsForm | 

    try:
        # Update Skill Access By Id
        api_response = await api_instance.update_skill_access_by_id_api_v1_skills_id_id_access_update_post(id, skill_access_grants_form)
        print("The response of SkillsApi->update_skill_access_by_id_api_v1_skills_id_id_access_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SkillsApi->update_skill_access_by_id_api_v1_skills_id_id_access_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **skill_access_grants_form** | [**SkillAccessGrantsForm**](SkillAccessGrantsForm.md)|  | 

### Return type

[**SkillModel**](SkillModel.md)

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

# **update_skill_by_id_api_v1_skills_id_id_update_post**
> SkillModel update_skill_by_id_api_v1_skills_id_id_update_post(id, skill_form)

Update Skill By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.skill_form import SkillForm
from openwebui_client.models.skill_model import SkillModel
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
    api_instance = openwebui_client.SkillsApi(api_client)
    id = 'id_example' # str | 
    skill_form = openwebui_client.SkillForm() # SkillForm | 

    try:
        # Update Skill By Id
        api_response = await api_instance.update_skill_by_id_api_v1_skills_id_id_update_post(id, skill_form)
        print("The response of SkillsApi->update_skill_by_id_api_v1_skills_id_id_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SkillsApi->update_skill_by_id_api_v1_skills_id_id_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **skill_form** | [**SkillForm**](SkillForm.md)|  | 

### Return type

[**SkillModel**](SkillModel.md)

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

