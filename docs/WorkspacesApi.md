# rockset.Workspaces

All URIs are relative to *https://api.rs2.usw2.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace**](WorkspacesApi.md#create_workspace) | **POST** /v1/orgs/self/ws | Create Workspace
[**delete_workspace**](WorkspacesApi.md#delete_workspace) | **DELETE** /v1/orgs/self/ws/{workspace} | Delete Workspace
[**get_workspace**](WorkspacesApi.md#get_workspace) | **GET** /v1/orgs/self/ws/{workspace} | Retrieve Workspace
[**list_workspaces**](WorkspacesApi.md#list_workspaces) | **GET** /v1/orgs/self/ws | List Workspaces


# **create_workspace**
> CreateWorkspaceResponse create_workspace(create_workspace_request)

Create Workspace

Create a new workspace.

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
    # Create Workspace
    api_response = rs.Workspaces.create_workspace(
        name="event_logs",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling Workspaces->create_workspace: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create Workspace
    api_response = await rs.Workspaces.create_workspace(
        description="Datasets of system logs for the ops team.",
        name="event_logs",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling Workspaces->create_workspace: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str** | longer explanation for the workspace | [optional]
 **name** | **str** | descriptive label and unique identifier | 

### Return type

[**CreateWorkspaceResponse**](CreateWorkspaceResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | workspace created successfully |  -  |
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

# **delete_workspace**
> DeleteWorkspaceResponse delete_workspace()

Delete Workspace

Remove a workspace.

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
    # Delete Workspace
    api_response = rs.Workspaces.delete_workspace(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling Workspaces->delete_workspace: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Delete Workspace
    api_response = await rs.Workspaces.delete_workspace(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling Workspaces->delete_workspace: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**DeleteWorkspaceResponse**](DeleteWorkspaceResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | workspace deleted successfully |  -  |
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

# **get_workspace**
> GetWorkspaceResponse get_workspace()

Retrieve Workspace

Get information about a single workspace.

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
    # Retrieve Workspace
    api_response = rs.Workspaces.get_workspace(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling Workspaces->get_workspace: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Retrieve Workspace
    api_response = await rs.Workspaces.get_workspace(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling Workspaces->get_workspace: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**GetWorkspaceResponse**](GetWorkspaceResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | workspace retrieved successfully |  -  |
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

# **list_workspaces**
> ListWorkspacesResponse list_workspaces()

List Workspaces

List all workspaces in an organization.

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
    # List Workspaces
    api_response = rs.Workspaces.list_workspaces(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling Workspaces->list_workspaces: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # List Workspaces
    api_response = await rs.Workspaces.list_workspaces(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling Workspaces->list_workspaces: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListWorkspacesResponse**](ListWorkspacesResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | workspaces retrieved successfully |  -  |
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

