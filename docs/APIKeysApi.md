# rockset.APIKeysApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](APIKeysApi.md#create_api_key) | **POST** /v1/orgs/self/users/self/apikeys | Create API Key
[**delete_api_key**](APIKeysApi.md#delete_api_key) | **DELETE** /v1/orgs/self/users/{user}/apikeys/{name} | Delete API Key
[**get_api_key**](APIKeysApi.md#get_api_key) | **GET** /v1/orgs/self/users/{user}/apikeys/{name} | Retrieve API Key
[**list_api_keys**](APIKeysApi.md#list_api_keys) | **GET** /v1/orgs/self/users/{user}/apikeys | List API Keys.
[**update_api_key**](APIKeysApi.md#update_api_key) | **POST** /v1/orgs/self/users/{user}/apikeys/{name} | Update an API key&#39;s state


# **create_api_key**
> CreateApiKeyResponse create_api_key(create_api_key_request)

Create API Key

Create a new API key for the authenticated user.

### Example


```python
import time
import rockset
from rockset.api import api_keys_api
from rockset.model.create_api_key_request import CreateApiKeyRequest
from rockset.model.error_model import ErrorModel
from rockset.model.create_api_key_response import CreateApiKeyResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_keys_api.APIKeysApi(api_client)
    create_api_key_request = CreateApiKeyRequest(
        name="my-app",
        role="role_example",
    ) # CreateApiKeyRequest | JSON object

    # example passing only required values which don't have defaults set
    try:
        # Create API Key
        api_response = api_instance.create_api_key(create_api_key_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling APIKeysApi->create_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_api_key_request** | [**CreateApiKeyRequest**](CreateApiKeyRequest.md)| JSON object |

### Return type

[**CreateApiKeyResponse**](CreateApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API key created successfully |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> DeleteApiKeyResponse delete_api_key(name, user)

Delete API Key

Delete an API key for any user in your organization.

### Example


```python
import time
import rockset
from rockset.api import api_keys_api
from rockset.model.delete_api_key_response import DeleteApiKeyResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_keys_api.APIKeysApi(api_client)
    name = "my-key" # str | Name of the API key.
    user = "admin@me.com" # str | Email of the API key owner. Use `self` to specify the currently authenticated user.

    # example passing only required values which don't have defaults set
    try:
        # Delete API Key
        api_response = api_instance.delete_api_key(name, user)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling APIKeysApi->delete_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the API key. |
 **user** | **str**| Email of the API key owner. Use &#x60;self&#x60; to specify the currently authenticated user. |

### Return type

[**DeleteApiKeyResponse**](DeleteApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API key deleted successfully |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key**
> GetApiKeyResponse get_api_key(user, name)

Retrieve API Key

Retrieve a particular API key for any user in your organization.

### Example


```python
import time
import rockset
from rockset.api import api_keys_api
from rockset.model.error_model import ErrorModel
from rockset.model.get_api_key_response import GetApiKeyResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_keys_api.APIKeysApi(api_client)
    user = "admin@me.com" # str | Email of the API key owner. Use `self` to specify the currently authenticated user.
    name = "my-key" # str | Name of the API key.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve API Key
        api_response = api_instance.get_api_key(user, name)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling APIKeysApi->get_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Email of the API key owner. Use &#x60;self&#x60; to specify the currently authenticated user. |
 **name** | **str**| Name of the API key. |

### Return type

[**GetApiKeyResponse**](GetApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API key retrieved successfully |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_keys**
> ListApiKeysResponse list_api_keys(user)

List API Keys.

List API key metadata for any user in your organization.

### Example


```python
import time
import rockset
from rockset.api import api_keys_api
from rockset.model.list_api_keys_response import ListApiKeysResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_keys_api.APIKeysApi(api_client)
    user = "admin@me.com" # str | Email of the API key owner. Use `self` to specify the currently authenticated user.

    # example passing only required values which don't have defaults set
    try:
        # List API Keys.
        api_response = api_instance.list_api_keys(user)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling APIKeysApi->list_api_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Email of the API key owner. Use &#x60;self&#x60; to specify the currently authenticated user. |

### Return type

[**ListApiKeysResponse**](ListApiKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API keys retrieved successfully |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key**
> UpdateApiKeyResponse update_api_key(name, user, update_api_key_request)

Update an API key's state

Update the state of an API key for any user in your organization.

### Example


```python
import time
import rockset
from rockset.api import api_keys_api
from rockset.model.error_model import ErrorModel
from rockset.model.update_api_key_request import UpdateApiKeyRequest
from rockset.model.update_api_key_response import UpdateApiKeyResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = api_keys_api.APIKeysApi(api_client)
    name = "my-key" # str | Name of the API key.
    user = "admin@me.com" # str | Email of the API key owner. Use `self` to specify the currently authenticated user.
    update_api_key_request = UpdateApiKeyRequest(
        state="ACTIVE",
    ) # UpdateApiKeyRequest | JSON object

    # example passing only required values which don't have defaults set
    try:
        # Update an API key's state
        api_response = api_instance.update_api_key(name, user, update_api_key_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling APIKeysApi->update_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the API key. |
 **user** | **str**| Email of the API key owner. Use &#x60;self&#x60; to specify the currently authenticated user. |
 **update_api_key_request** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)| JSON object |

### Return type

[**UpdateApiKeyResponse**](UpdateApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API key successfully updated |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

