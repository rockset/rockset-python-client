# rockset.Views

All URIs are relative to *https://api.use1a1.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ViewsApi.md#create) | **POST** /v1/orgs/self/ws/{workspace}/views | Create View
[**delete**](ViewsApi.md#delete) | **DELETE** /v1/orgs/self/ws/{workspace}/views/{view} | Delete View
[**get**](ViewsApi.md#get) | **GET** /v1/orgs/self/ws/{workspace}/views/{view} | Retrieve View
[**list**](ViewsApi.md#list) | **GET** /v1/orgs/self/views | List Views
[**update**](ViewsApi.md#update) | **POST** /v1/orgs/self/ws/{workspace}/views/{view} | Update View
[**workspace_views**](ViewsApi.md#workspace_views) | **GET** /v1/orgs/self/ws/{workspace}/views | List Views in Workspace


# **create**
> CreateViewResponse create(create_view_request)

Create View

Create a view

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create View
api_response = rs.Views.create(
    name="myAwesomeView",
    query="SELECT * FROM foo",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Views->create: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create View
api_response = await rs.Views.create(
    description="view of awesome collection",
    name="myAwesomeView",
    query="SELECT * FROM foo",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Views->create: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str** | optional description | [optional]
 **name** | **str** | View name | 
 **query** | **str** | SQL for this view | 
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**CreateViewResponse**](CreateViewResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | view created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> DeleteViewResponse delete(view)

Delete View

Delete a view

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Delete View
api_response = rs.Views.delete(
    view="view_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Views->delete: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Delete View
api_response = await rs.Views.delete(
    view="view_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Views->delete: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str** | name of the view |
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**DeleteViewResponse**](DeleteViewResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | view deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> GetViewResponse get(view)

Retrieve View

Get details about a view

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Retrieve View
api_response = rs.Views.get(
    view="view_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Views->get: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Retrieve View
api_response = await rs.Views.get(
    view="view_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Views->get: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str** | name of the view |
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**GetViewResponse**](GetViewResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | view retrieved successfully |  -  |
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
> ListViewsResponse list()

List Views

Retrieve all views in an organization

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# List Views
api_response = rs.Views.list(
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Views->list: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# List Views
api_response = await rs.Views.list(
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Views->list: %s\n" % e)
    return
pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListViewsResponse**](ListViewsResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | views retrieved successfully |  -  |
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
> UpdateViewResponse update(view, update_view_request)

Update View

Update a view

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Update View
api_response = rs.Views.update(
    view="view_example",
    query="SELECT * FROM foo",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Views->update: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Update View
api_response = await rs.Views.update(
    view="view_example",
    description="view of awesome collection",
    query="SELECT * FROM foo",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Views->update: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str** | name of the view |
 **description** | **str** | optional description | [optional]
 **query** | **str** | SQL for this view | 
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**UpdateViewResponse**](UpdateViewResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | view updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_views**
> ListViewsResponse workspace_views()

List Views in Workspace

Retrieve all views in a workspace.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# List Views in Workspace
api_response = rs.Views.workspace_views(
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Views->workspace_views: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# List Views in Workspace
api_response = await rs.Views.workspace_views(
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Views->workspace_views: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**ListViewsResponse**](ListViewsResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | views retrieved successfully |  -  |
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

