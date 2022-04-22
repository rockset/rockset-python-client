# rockset.ViewsApi

All URIs are relative to *https://api.rs2.usw2.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_view**](ViewsApi.md#create_view) | **POST** /v1/orgs/self/ws/{workspace}/views | Create View
[**delete_view**](ViewsApi.md#delete_view) | **DELETE** /v1/orgs/self/ws/{workspace}/views/{view} | Delete View
[**get_view**](ViewsApi.md#get_view) | **GET** /v1/orgs/self/ws/{workspace}/views/{view} | Retrieve View
[**list_views**](ViewsApi.md#list_views) | **GET** /v1/orgs/self/views | List Views
[**update_view**](ViewsApi.md#update_view) | **POST** /v1/orgs/self/ws/{workspace}/views/{view} | Update View
[**workspace_views**](ViewsApi.md#workspace_views) | **GET** /v1/orgs/self/ws/{workspace}/views | List Views in Workspace


# **create_view**
> CreateViewResponse create_view(create_view_request)

Create View

Create a view

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
    # Create View
    api_response = rs.ViewsApi.create_view(
        name="myAwesomeView",
        query="SELECT * FROM foo",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling ViewsApi->create_view: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create View
    api_response = await rs.ViewsApi.create_view(
        description="view of awesome collection",
        name="myAwesomeView",
        query="SELECT * FROM foo",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling ViewsApi->create_view: %s\n" % e)
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

# **delete_view**
> DeleteViewResponse delete_view(view)

Delete View

Delete a view

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
    # Delete View
    api_response = rs.ViewsApi.delete_view(
        view="view_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling ViewsApi->delete_view: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Delete View
    api_response = await rs.ViewsApi.delete_view(
        view="view_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling ViewsApi->delete_view: %s\n" % e)
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

# **get_view**
> GetViewResponse get_view(view)

Retrieve View

Get details about a view

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
    # Retrieve View
    api_response = rs.ViewsApi.get_view(
        view="view_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling ViewsApi->get_view: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Retrieve View
    api_response = await rs.ViewsApi.get_view(
        view="view_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling ViewsApi->get_view: %s\n" % e)
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

# **list_views**
> ListViewsResponse list_views()

List Views

Retrieve all views in an organization

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
    # List Views
    api_response = rs.ViewsApi.list_views(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling ViewsApi->list_views: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # List Views
    api_response = await rs.ViewsApi.list_views(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling ViewsApi->list_views: %s\n" % e)
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

# **update_view**
> UpdateViewResponse update_view(view, update_view_request)

Update View

Update a view

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
    # Update View
    api_response = rs.ViewsApi.update_view(
        view="view_example",
        query="SELECT * FROM foo",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling ViewsApi->update_view: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Update View
    api_response = await rs.ViewsApi.update_view(
        view="view_example",
        description="view of awesome collection",
        query="SELECT * FROM foo",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling ViewsApi->update_view: %s\n" % e)
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
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # List Views in Workspace
    api_response = rs.ViewsApi.workspace_views(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling ViewsApi->workspace_views: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # List Views in Workspace
    api_response = await rs.ViewsApi.workspace_views(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling ViewsApi->workspace_views: %s\n" % e)
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

