# rockset.Aliases

All URIs are relative to *https://api.use1a1.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](AliasesApi.md#create) | **POST** /v1/orgs/self/ws/{workspace}/aliases | Create Alias
[**delete**](AliasesApi.md#delete) | **DELETE** /v1/orgs/self/ws/{workspace}/aliases/{alias} | Delete Alias
[**get**](AliasesApi.md#get) | **GET** /v1/orgs/self/ws/{workspace}/aliases/{alias} | Retrieve Alias
[**list**](AliasesApi.md#list) | **GET** /v1/orgs/self/aliases | List Aliases
[**update**](AliasesApi.md#update) | **POST** /v1/orgs/self/ws/{workspace}/aliases/{alias} | Update Alias
[**workspace_aliases**](AliasesApi.md#workspace_aliases) | **GET** /v1/orgs/self/ws/{workspace}/aliases | List Aliases in Workspace


# **create**
> CreateAliasResponse create(create_alias_request)

Create Alias

Create new alias in a workspace.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create Alias
api_response = rs.Aliases.create(
    collections=["commons.foo","prod.demo"],
    name="aliasName",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Aliases->create: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create Alias
api_response = await rs.Aliases.create(
    collections=["commons.foo","prod.demo"],
    description="version alias",
    name="aliasName",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Aliases->create: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections** | **[str]** | List of fully qualified collection names referenced by alias. | 
 **description** | **str** | Optional description. | [optional]
 **name** | **str** | Alias name. | 
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

# **delete**
> DeleteAliasResponse delete(alias)

Delete Alias

Delete an alias.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Delete Alias
api_response = rs.Aliases.delete(
    alias="alias_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Aliases->delete: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Delete Alias
api_response = await rs.Aliases.delete(
    alias="alias_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Aliases->delete: %s\n" % e)
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

# **get**
> GetAliasResponse get(alias)

Retrieve Alias

Get details about an alias

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Retrieve Alias
api_response = rs.Aliases.get(
    alias="alias_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Aliases->get: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Retrieve Alias
api_response = await rs.Aliases.get(
    alias="alias_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Aliases->get: %s\n" % e)
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

# **list**
> ListAliasesResponse list()

List Aliases

Retrieve all aliases in an organization

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# List Aliases
api_response = rs.Aliases.list(
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Aliases->list: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# List Aliases
api_response = await rs.Aliases.list(
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Aliases->list: %s\n" % e)
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

# **update**
> GetAliasResponse update(alias, update_alias_request)

Update Alias

Update alias in a workspace.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Update Alias
api_response = rs.Aliases.update(
    alias="alias_example",
    collections=["commons.foo","prod.demo"],
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Aliases->update: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Update Alias
api_response = await rs.Aliases.update(
    alias="alias_example",
    collections=["commons.foo","prod.demo"],
    description="version alias",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Aliases->update: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str** | name of the alias |
 **collections** | **[str]** | List of fully qualified collection names referenced by alias. | 
 **description** | **str** | Optional description. | [optional]
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

# **workspace_aliases**
> ListAliasesResponse workspace_aliases()

List Aliases in Workspace

Retrieve all aliases in a workspace.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# List Aliases in Workspace
api_response = rs.Aliases.workspace_aliases(
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Aliases->workspace_aliases: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# List Aliases in Workspace
api_response = await rs.Aliases.workspace_aliases(
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Aliases->workspace_aliases: %s\n" % e)
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

