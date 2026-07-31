# openwebui_client.UtilsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_chat_as_pdf_api_v1_utils_pdf_post**](UtilsApi.md#download_chat_as_pdf_api_v1_utils_pdf_post) | **POST** /api/v1/utils/pdf | Download Chat As Pdf
[**download_db_api_v1_utils_db_download_get**](UtilsApi.md#download_db_api_v1_utils_db_download_get) | **GET** /api/v1/utils/db/download | Download Db
[**execute_code_api_v1_utils_code_execute_post**](UtilsApi.md#execute_code_api_v1_utils_code_execute_post) | **POST** /api/v1/utils/code/execute | Execute Code
[**format_code_api_v1_utils_code_format_post**](UtilsApi.md#format_code_api_v1_utils_code_format_post) | **POST** /api/v1/utils/code/format | Format Code
[**get_gravatar_api_v1_utils_gravatar_get**](UtilsApi.md#get_gravatar_api_v1_utils_gravatar_get) | **GET** /api/v1/utils/gravatar | Get Gravatar


# **download_chat_as_pdf_api_v1_utils_pdf_post**
> object download_chat_as_pdf_api_v1_utils_pdf_post(chat_title_messages_form)

Download Chat As Pdf

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.chat_title_messages_form import ChatTitleMessagesForm
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
    api_instance = openwebui_client.UtilsApi(api_client)
    chat_title_messages_form = openwebui_client.ChatTitleMessagesForm() # ChatTitleMessagesForm | 

    try:
        # Download Chat As Pdf
        api_response = await api_instance.download_chat_as_pdf_api_v1_utils_pdf_post(chat_title_messages_form)
        print("The response of UtilsApi->download_chat_as_pdf_api_v1_utils_pdf_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->download_chat_as_pdf_api_v1_utils_pdf_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_title_messages_form** | [**ChatTitleMessagesForm**](ChatTitleMessagesForm.md)|  | 

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

# **download_db_api_v1_utils_db_download_get**
> object download_db_api_v1_utils_db_download_get()

Download Db

Download the raw SQLite database file (admin-only, SQLite deployments only).

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
    api_instance = openwebui_client.UtilsApi(api_client)

    try:
        # Download Db
        api_response = await api_instance.download_db_api_v1_utils_db_download_get()
        print("The response of UtilsApi->download_db_api_v1_utils_db_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->download_db_api_v1_utils_db_download_get: %s\n" % e)
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

# **execute_code_api_v1_utils_code_execute_post**
> object execute_code_api_v1_utils_code_execute_post(code_form)

Execute Code

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.code_form import CodeForm
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
    api_instance = openwebui_client.UtilsApi(api_client)
    code_form = openwebui_client.CodeForm() # CodeForm | 

    try:
        # Execute Code
        api_response = await api_instance.execute_code_api_v1_utils_code_execute_post(code_form)
        print("The response of UtilsApi->execute_code_api_v1_utils_code_execute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->execute_code_api_v1_utils_code_execute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_form** | [**CodeForm**](CodeForm.md)|  | 

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

# **format_code_api_v1_utils_code_format_post**
> object format_code_api_v1_utils_code_format_post(code_form)

Format Code

### Example

* Bearer Authentication (HTTPBearer):

```python
import openwebui_client
from openwebui_client.models.code_form import CodeForm
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
    api_instance = openwebui_client.UtilsApi(api_client)
    code_form = openwebui_client.CodeForm() # CodeForm | 

    try:
        # Format Code
        api_response = await api_instance.format_code_api_v1_utils_code_format_post(code_form)
        print("The response of UtilsApi->format_code_api_v1_utils_code_format_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->format_code_api_v1_utils_code_format_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_form** | [**CodeForm**](CodeForm.md)|  | 

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

# **get_gravatar_api_v1_utils_gravatar_get**
> object get_gravatar_api_v1_utils_gravatar_get(email)

Get Gravatar

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
    api_instance = openwebui_client.UtilsApi(api_client)
    email = 'email_example' # str | 

    try:
        # Get Gravatar
        api_response = await api_instance.get_gravatar_api_v1_utils_gravatar_get(email)
        print("The response of UtilsApi->get_gravatar_api_v1_utils_gravatar_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->get_gravatar_api_v1_utils_gravatar_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

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

