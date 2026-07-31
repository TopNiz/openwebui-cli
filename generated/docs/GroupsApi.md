# openwebui_client.GroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_to_group_api_v1_groups_id_id_users_add_post**](GroupsApi.md#add_user_to_group_api_v1_groups_id_id_users_add_post) | **POST** /api/v1/groups/id/{id}/users/add | Add User To Group
[**create_new_group_api_v1_groups_create_post**](GroupsApi.md#create_new_group_api_v1_groups_create_post) | **POST** /api/v1/groups/create | Create New Group
[**delete_group_by_id_api_v1_groups_id_id_delete_delete**](GroupsApi.md#delete_group_by_id_api_v1_groups_id_id_delete_delete) | **DELETE** /api/v1/groups/id/{id}/delete | Delete Group By Id
[**export_group_by_id_api_v1_groups_id_id_export_get**](GroupsApi.md#export_group_by_id_api_v1_groups_id_id_export_get) | **GET** /api/v1/groups/id/{id}/export | Export Group By Id
[**get_group_by_id_api_v1_groups_id_id_get**](GroupsApi.md#get_group_by_id_api_v1_groups_id_id_get) | **GET** /api/v1/groups/id/{id} | Get Group By Id
[**get_group_info_by_id_api_v1_groups_id_id_info_get**](GroupsApi.md#get_group_info_by_id_api_v1_groups_id_id_info_get) | **GET** /api/v1/groups/id/{id}/info | Get Group Info By Id
[**get_groups_api_v1_groups_get**](GroupsApi.md#get_groups_api_v1_groups_get) | **GET** /api/v1/groups/ | Get Groups
[**get_users_in_group_api_v1_groups_id_id_users_post**](GroupsApi.md#get_users_in_group_api_v1_groups_id_id_users_post) | **POST** /api/v1/groups/id/{id}/users | Get Users In Group
[**preview_group_access_api_v1_groups_id_id_preview_get**](GroupsApi.md#preview_group_access_api_v1_groups_id_id_preview_get) | **GET** /api/v1/groups/id/{id}/preview | Preview Group Access
[**remove_users_from_group_api_v1_groups_id_id_users_remove_post**](GroupsApi.md#remove_users_from_group_api_v1_groups_id_id_users_remove_post) | **POST** /api/v1/groups/id/{id}/users/remove | Remove Users From Group
[**update_group_by_id_api_v1_groups_id_id_update_post**](GroupsApi.md#update_group_by_id_api_v1_groups_id_id_update_post) | **POST** /api/v1/groups/id/{id}/update | Update Group By Id


# **add_user_to_group_api_v1_groups_id_id_users_add_post**
> GroupResponse add_user_to_group_api_v1_groups_id_id_users_add_post(id, user_ids_form)

Add User To Group

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.group_response import GroupResponse
from openwebui_client.models.user_ids_form import UserIdsForm
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
    api_instance = openwebui_client.GroupsApi(api_client)
    id = 'id_example' # str | 
    user_ids_form = openwebui_client.UserIdsForm() # UserIdsForm | 

    try:
        # Add User To Group
        api_response = await api_instance.add_user_to_group_api_v1_groups_id_id_users_add_post(id, user_ids_form)
        print("The response of GroupsApi->add_user_to_group_api_v1_groups_id_id_users_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->add_user_to_group_api_v1_groups_id_id_users_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user_ids_form** | [**UserIdsForm**](UserIdsForm.md)|  | 

### Return type

[**GroupResponse**](GroupResponse.md)

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

# **create_new_group_api_v1_groups_create_post**
> GroupResponse create_new_group_api_v1_groups_create_post(group_form)

Create New Group

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.group_form import GroupForm
from openwebui_client.models.group_response import GroupResponse
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
    api_instance = openwebui_client.GroupsApi(api_client)
    group_form = openwebui_client.GroupForm() # GroupForm | 

    try:
        # Create New Group
        api_response = await api_instance.create_new_group_api_v1_groups_create_post(group_form)
        print("The response of GroupsApi->create_new_group_api_v1_groups_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->create_new_group_api_v1_groups_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_form** | [**GroupForm**](GroupForm.md)|  | 

### Return type

[**GroupResponse**](GroupResponse.md)

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

# **delete_group_by_id_api_v1_groups_id_id_delete_delete**
> bool delete_group_by_id_api_v1_groups_id_id_delete_delete(id)

Delete Group By Id

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
    api_instance = openwebui_client.GroupsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Group By Id
        api_response = await api_instance.delete_group_by_id_api_v1_groups_id_id_delete_delete(id)
        print("The response of GroupsApi->delete_group_by_id_api_v1_groups_id_id_delete_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->delete_group_by_id_api_v1_groups_id_id_delete_delete: %s\n" % e)
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

# **export_group_by_id_api_v1_groups_id_id_export_get**
> GroupExportResponse export_group_by_id_api_v1_groups_id_id_export_get(id)

Export Group By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.group_export_response import GroupExportResponse
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
    api_instance = openwebui_client.GroupsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Export Group By Id
        api_response = await api_instance.export_group_by_id_api_v1_groups_id_id_export_get(id)
        print("The response of GroupsApi->export_group_by_id_api_v1_groups_id_id_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->export_group_by_id_api_v1_groups_id_id_export_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GroupExportResponse**](GroupExportResponse.md)

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

# **get_group_by_id_api_v1_groups_id_id_get**
> GroupResponse get_group_by_id_api_v1_groups_id_id_get(id)

Get Group By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.group_response import GroupResponse
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
    api_instance = openwebui_client.GroupsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Group By Id
        api_response = await api_instance.get_group_by_id_api_v1_groups_id_id_get(id)
        print("The response of GroupsApi->get_group_by_id_api_v1_groups_id_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group_by_id_api_v1_groups_id_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GroupResponse**](GroupResponse.md)

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

# **get_group_info_by_id_api_v1_groups_id_id_info_get**
> GroupInfoResponse get_group_info_by_id_api_v1_groups_id_id_info_get(id)

Get Group Info By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.group_info_response import GroupInfoResponse
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
    api_instance = openwebui_client.GroupsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Group Info By Id
        api_response = await api_instance.get_group_info_by_id_api_v1_groups_id_id_info_get(id)
        print("The response of GroupsApi->get_group_info_by_id_api_v1_groups_id_id_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group_info_by_id_api_v1_groups_id_id_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GroupInfoResponse**](GroupInfoResponse.md)

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

# **get_groups_api_v1_groups_get**
> List[GroupResponse] get_groups_api_v1_groups_get(share=share)

Get Groups

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.group_response import GroupResponse
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
    api_instance = openwebui_client.GroupsApi(api_client)
    share = True # bool |  (optional)

    try:
        # Get Groups
        api_response = await api_instance.get_groups_api_v1_groups_get(share=share)
        print("The response of GroupsApi->get_groups_api_v1_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_groups_api_v1_groups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share** | **bool**|  | [optional] 

### Return type

[**List[GroupResponse]**](GroupResponse.md)

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

# **get_users_in_group_api_v1_groups_id_id_users_post**
> List[UserInfoResponse] get_users_in_group_api_v1_groups_id_id_users_post(id)

Get Users In Group

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.user_info_response import UserInfoResponse
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
    api_instance = openwebui_client.GroupsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Users In Group
        api_response = await api_instance.get_users_in_group_api_v1_groups_id_id_users_post(id)
        print("The response of GroupsApi->get_users_in_group_api_v1_groups_id_id_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_users_in_group_api_v1_groups_id_id_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[UserInfoResponse]**](UserInfoResponse.md)

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

# **preview_group_access_api_v1_groups_id_id_preview_get**
> object preview_group_access_api_v1_groups_id_id_preview_get(id)

Preview Group Access

Show what resources a group can access (preview audit).

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
    api_instance = openwebui_client.GroupsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Preview Group Access
        api_response = await api_instance.preview_group_access_api_v1_groups_id_id_preview_get(id)
        print("The response of GroupsApi->preview_group_access_api_v1_groups_id_id_preview_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->preview_group_access_api_v1_groups_id_id_preview_get: %s\n" % e)
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

# **remove_users_from_group_api_v1_groups_id_id_users_remove_post**
> GroupResponse remove_users_from_group_api_v1_groups_id_id_users_remove_post(id, user_ids_form)

Remove Users From Group

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.group_response import GroupResponse
from openwebui_client.models.user_ids_form import UserIdsForm
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
    api_instance = openwebui_client.GroupsApi(api_client)
    id = 'id_example' # str | 
    user_ids_form = openwebui_client.UserIdsForm() # UserIdsForm | 

    try:
        # Remove Users From Group
        api_response = await api_instance.remove_users_from_group_api_v1_groups_id_id_users_remove_post(id, user_ids_form)
        print("The response of GroupsApi->remove_users_from_group_api_v1_groups_id_id_users_remove_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->remove_users_from_group_api_v1_groups_id_id_users_remove_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **user_ids_form** | [**UserIdsForm**](UserIdsForm.md)|  | 

### Return type

[**GroupResponse**](GroupResponse.md)

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

# **update_group_by_id_api_v1_groups_id_id_update_post**
> GroupResponse update_group_by_id_api_v1_groups_id_id_update_post(id, group_update_form)

Update Group By Id

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.group_response import GroupResponse
from openwebui_client.models.group_update_form import GroupUpdateForm
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
    api_instance = openwebui_client.GroupsApi(api_client)
    id = 'id_example' # str | 
    group_update_form = openwebui_client.GroupUpdateForm() # GroupUpdateForm | 

    try:
        # Update Group By Id
        api_response = await api_instance.update_group_by_id_api_v1_groups_id_id_update_post(id, group_update_form)
        print("The response of GroupsApi->update_group_by_id_api_v1_groups_id_id_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->update_group_by_id_api_v1_groups_id_id_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **group_update_form** | [**GroupUpdateForm**](GroupUpdateForm.md)|  | 

### Return type

[**GroupResponse**](GroupResponse.md)

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

