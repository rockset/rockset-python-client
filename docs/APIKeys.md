# rockset.APIKeys

All URIs are relative to *https://api.rs2.usw2.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](APIKeys.md#create_api_key) | **POST** /v1/orgs/self/users/self/apikeys | Create API Key
[**delete_api_key**](APIKeys.md#delete_api_key) | **DELETE** /v1/orgs/self/users/{user}/apikeys/{name} | Delete API Key
[**get_api_key**](APIKeys.md#get_api_key) | **GET** /v1/orgs/self/users/{user}/apikeys/{name} | Retrieve API Key
[**list_api_keys**](APIKeys.md#list_api_keys) | **GET** /v1/orgs/self/users/{user}/apikeys | List API Keys
[**update_api_key**](APIKeys.md#update_api_key) | **POST** /v1/orgs/self/users/{user}/apikeys/{name} | Update API Key State


# **create_api_key**
> CreateApiKeyResponse create_api_key(create_api_key_request)

Create API Key

Create a new API key for the authenticated user.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Create API Key
    api_response = rs.APIKeys.create_api_key(
        name="my-app",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling APIKeys->create_api_key: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create API Key
    api_response = await rs.APIKeys.create_api_key(
        name="my-app",
        role="string_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling APIKeys->create_api_key: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str** | Name for this API key. | 
 **role** | **str** |  | [optional]

### Return type

[**CreateApiKeyResponse**](CreateApiKeyResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Delete API Key
    api_response = rs.APIKeys.delete_api_key(
        name="my-key",
        user="admin@me.com",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling APIKeys->delete_api_key: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Delete API Key
    api_response = await rs.APIKeys.delete_api_key(
        name="my-key",
        user="admin@me.com",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling APIKeys->delete_api_key: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str** | Name of the API key. |
 **user** | **str** | Email of the API key owner. Use &#x60;self&#x60; to specify the currently authenticated user. |

### Return type

[**DeleteApiKeyResponse**](DeleteApiKeyResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Retrieve API Key
    api_response = rs.APIKeys.get_api_key(
        user="admin@me.com",
        name="my-key",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling APIKeys->get_api_key: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Retrieve API Key
    api_response = await rs.APIKeys.get_api_key(
        user="admin@me.com",
        name="my-key",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling APIKeys->get_api_key: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str** | Email of the API key owner. Use &#x60;self&#x60; to specify the currently authenticated user. |
 **name** | **str** | Name of the API key. |
 **reveal** | **bool** | Reveal full key. | [optional]

### Return type

[**GetApiKeyResponse**](GetApiKeyResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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

List API Keys

List API key metadata for any user in your organization.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # List API Keys
    api_response = rs.APIKeys.list_api_keys(
        user="admin@me.com",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling APIKeys->list_api_keys: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # List API Keys
    api_response = await rs.APIKeys.list_api_keys(
        user="admin@me.com",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling APIKeys->list_api_keys: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str** | Email of the API key owner. Use &#x60;self&#x60; to specify the currently authenticated user. |

### Return type

[**ListApiKeysResponse**](ListApiKeysResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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

Update API Key State

Update the state of an API key for any user in your organization.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Update API Key State
    api_response = rs.APIKeys.update_api_key(
        name="my-key",
        user="admin@me.com",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling APIKeys->update_api_key: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Update API Key State
    api_response = await rs.APIKeys.update_api_key(
        name="my-key",
        user="admin@me.com",
        state="ACTIVE",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling APIKeys->update_api_key: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str** | Name of the API key. |
 **user** | **str** | Email of the API key owner. Use &#x60;self&#x60; to specify the currently authenticated user. |
 **state** | **str** | State that the api key should be set to. | [optional]

### Return type

[**UpdateApiKeyResponse**](UpdateApiKeyResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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

