# rockset.WorkspacesApi

All URIs are relative to *https://api.rs2.usw2.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**child_workspaces**](WorkspacesApi.md#child_workspaces) | **GET** /v1/orgs/self/ws/{workspace}/ws | List Workspaces in Workspace
[**create_workspace**](WorkspacesApi.md#create_workspace) | **POST** /v1/orgs/self/ws | Create Workspace
[**delete_workspace**](WorkspacesApi.md#delete_workspace) | **DELETE** /v1/orgs/self/ws/{workspace} | Delete Workspace
[**get_workspace**](WorkspacesApi.md#get_workspace) | **GET** /v1/orgs/self/ws/{workspace} | Retrieve Workspace
[**list_workspaces**](WorkspacesApi.md#list_workspaces) | **GET** /v1/orgs/self/ws | List Workspaces


# **child_workspaces**
> ListWorkspacesResponse child_workspaces()

List Workspaces in Workspace

List workspaces under given workspace.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.list_workspaces_response import ListWorkspacesResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # List Workspaces in Workspace
    api_response = rs.WorkspacesApi.child_workspaces(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling WorkspacesApi->child_workspaces: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # List Workspaces in Workspace
    api_response = await rs.WorkspacesApi.child_workspaces(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling WorkspacesApi->child_workspaces: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str** | name of the workspace | defaults to "commons"

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

# **create_workspace**
> CreateWorkspaceResponse create_workspace(create_workspace_request)

Create Workspace

Create a new workspace.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.create_workspace_response import CreateWorkspaceResponse
from rockset.model.create_workspace_request import CreateWorkspaceRequest
from rockset.model.error_model import ErrorModel
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Create Workspace
    api_response = rs.WorkspacesApi.create_workspace(
        name="event_logs",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create Workspace
    api_response = await rs.WorkspacesApi.create_workspace(
        description="Datasets of system logs for the ops team.",
        name="event_logs",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
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
import time
import rockset
from rockset import RocksetClient
from rockset.model.error_model import ErrorModel
from rockset.model.delete_workspace_response import DeleteWorkspaceResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Delete Workspace
    api_response = rs.WorkspacesApi.delete_workspace(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling WorkspacesApi->delete_workspace: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Delete Workspace
    api_response = await rs.WorkspacesApi.delete_workspace(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling WorkspacesApi->delete_workspace: %s\n" % e)
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
import time
import rockset
from rockset import RocksetClient
from rockset.model.get_workspace_response import GetWorkspaceResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Retrieve Workspace
    api_response = rs.WorkspacesApi.get_workspace(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Retrieve Workspace
    api_response = await rs.WorkspacesApi.get_workspace(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)
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
import time
import rockset
from rockset import RocksetClient
from rockset.model.list_workspaces_response import ListWorkspacesResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # List Workspaces
    api_response = rs.WorkspacesApi.list_workspaces(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling WorkspacesApi->list_workspaces: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # List Workspaces
    api_response = await rs.WorkspacesApi.list_workspaces(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling WorkspacesApi->list_workspaces: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fetch_across_regions** | **bool** |  | [optional]

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

