# rockset.AliasesApi

All URIs are relative to *https://api.rs2.usw2.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alias**](AliasesApi.md#create_alias) | **POST** /v1/orgs/self/ws/{workspace}/aliases | Create Alias
[**delete_alias**](AliasesApi.md#delete_alias) | **DELETE** /v1/orgs/self/ws/{workspace}/aliases/{alias} | Delete Alias
[**get_alias**](AliasesApi.md#get_alias) | **GET** /v1/orgs/self/ws/{workspace}/aliases/{alias} | Retrieve Alias
[**list_aliases**](AliasesApi.md#list_aliases) | **GET** /v1/orgs/self/aliases | List Aliases
[**update_alias**](AliasesApi.md#update_alias) | **POST** /v1/orgs/self/ws/{workspace}/aliases/{alias} | Update Alias
[**workspace_aliases**](AliasesApi.md#workspace_aliases) | **GET** /v1/orgs/self/ws/{workspace}/aliases | List Aliases in Workspace


# **create_alias**
> CreateAliasResponse create_alias(create_alias_request)

Create Alias

Create new alias in a workspace.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.error_model import ErrorModel
from rockset.model.create_alias_response import CreateAliasResponse
from rockset.model.create_alias_request import CreateAliasRequest
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Create Alias
    api_response = rs.AliasesApi.create_alias(
        collections=["commons.foo","prod.demo"],
        name="aliasName",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling AliasesApi->create_alias: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create Alias
    api_response = await rs.AliasesApi.create_alias(
        collections=["commons.foo","prod.demo"],
        description="version alias",
        name="aliasName",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling AliasesApi->create_alias: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections** | **[str]** | list of fully qualified collection names referenced by alias | 
 **description** | **str** | optional description | [optional]
 **name** | **str** | Alias name | 
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**CreateAliasResponse**](CreateAliasResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | alias created successfully |  -  |
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

# **delete_alias**
> DeleteAliasResponse delete_alias(alias)

Delete Alias

Delete an alias.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.delete_alias_response import DeleteAliasResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Delete Alias
    api_response = rs.AliasesApi.delete_alias(
        alias="alias_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling AliasesApi->delete_alias: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Delete Alias
    api_response = await rs.AliasesApi.delete_alias(
        alias="alias_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling AliasesApi->delete_alias: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str** | name of the alias |
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**DeleteAliasResponse**](DeleteAliasResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | alias deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alias**
> GetAliasResponse get_alias(alias)

Retrieve Alias

Get details about an alias

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.error_model import ErrorModel
from rockset.model.get_alias_response import GetAliasResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Retrieve Alias
    api_response = rs.AliasesApi.get_alias(
        alias="alias_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling AliasesApi->get_alias: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Retrieve Alias
    api_response = await rs.AliasesApi.get_alias(
        alias="alias_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling AliasesApi->get_alias: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str** | name of the alias |
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**GetAliasResponse**](GetAliasResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | alias retrieved successfully |  -  |
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

# **list_aliases**
> ListAliasesResponse list_aliases()

List Aliases

Retrieve all aliases in an organization

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.error_model import ErrorModel
from rockset.model.list_aliases_response import ListAliasesResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # List Aliases
    api_response = rs.AliasesApi.list_aliases(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling AliasesApi->list_aliases: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # List Aliases
    api_response = await rs.AliasesApi.list_aliases(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling AliasesApi->list_aliases: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListAliasesResponse**](ListAliasesResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | aliases retrieved successfully |  -  |
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

# **update_alias**
> GetAliasResponse update_alias(alias, update_alias_request)

Update Alias

Update alias in a workspace.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.get_alias_response import GetAliasResponse
from rockset.model.update_alias_request import UpdateAliasRequest
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Update Alias
    api_response = rs.AliasesApi.update_alias(
        alias="alias_example",
        collections=["commons.foo","prod.demo"],
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling AliasesApi->update_alias: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Update Alias
    api_response = await rs.AliasesApi.update_alias(
        alias="alias_example",
        collections=["commons.foo","prod.demo"],
        description="version alias",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling AliasesApi->update_alias: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str** | name of the alias |
 **collections** | **[str]** | list of fully qualified collection names referenced by alias | 
 **description** | **str** | optional description | [optional]
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**GetAliasResponse**](GetAliasResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | alias updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_aliases**
> ListAliasesResponse workspace_aliases()

List Aliases in Workspace

Retrieve all aliases in a workspace.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.error_model import ErrorModel
from rockset.model.list_aliases_response import ListAliasesResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # List Aliases in Workspace
    api_response = rs.AliasesApi.workspace_aliases(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling AliasesApi->workspace_aliases: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # List Aliases in Workspace
    api_response = await rs.AliasesApi.workspace_aliases(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling AliasesApi->workspace_aliases: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**ListAliasesResponse**](ListAliasesResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | aliases retrieved successfully |  -  |
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

