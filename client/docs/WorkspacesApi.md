# swagger_client.WorkspacesApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**child_workspaces**](WorkspacesApi.md#child_workspaces) | **GET** /v1/orgs/self/ws/{workspace}/ws | List Workspaces in Workspace
[**create_workspace**](WorkspacesApi.md#create_workspace) | **POST** /v1/orgs/self/ws | Create Workspace
[**delete_workspace**](WorkspacesApi.md#delete_workspace) | **DELETE** /v1/orgs/self/ws/{workspace} | Delete Workspace
[**get_workspace**](WorkspacesApi.md#get_workspace) | **GET** /v1/orgs/self/ws/{workspace} | Retrieve Workspace
[**list_workspaces**](WorkspacesApi.md#list_workspaces) | **GET** /v1/orgs/self/ws | List Workspaces


# **child_workspaces**
> ListWorkspacesResponse child_workspaces(workspace)

List Workspaces in Workspace

List workspaces under given workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
workspace = 'workspace_example' # str | name of the workspace

try:
    # List Workspaces in Workspace
    api_response = api_instance.child_workspaces(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->child_workspaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 

### Return type

[**ListWorkspacesResponse**](ListWorkspacesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace**
> CreateWorkspaceResponse create_workspace(body)

Create Workspace

Create a new workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
body = swagger_client.CreateWorkspaceRequest() # CreateWorkspaceRequest | workspace details

try:
    # Create Workspace
    api_response = api_instance.create_workspace(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWorkspaceRequest**](CreateWorkspaceRequest.md)| workspace details | 

### Return type

[**CreateWorkspaceResponse**](CreateWorkspaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace**
> DeleteWorkspaceResponse delete_workspace(workspace)

Delete Workspace

Remove a workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
workspace = 'workspace_example' # str | name of the workspace

try:
    # Delete Workspace
    api_response = api_instance.delete_workspace(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->delete_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 

### Return type

[**DeleteWorkspaceResponse**](DeleteWorkspaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace**
> GetWorkspaceResponse get_workspace(workspace)

Retrieve Workspace

Get information about a single workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
workspace = 'workspace_example' # str | name of the workspace

try:
    # Retrieve Workspace
    api_response = api_instance.get_workspace(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 

### Return type

[**GetWorkspaceResponse**](GetWorkspaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspaces**
> ListWorkspacesResponse list_workspaces(fetch_across_regions=fetch_across_regions)

List Workspaces

List all workspaces in an organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkspacesApi()
fetch_across_regions = true # bool |  (optional)

try:
    # List Workspaces
    api_response = api_instance.list_workspaces(fetch_across_regions=fetch_across_regions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspacesApi->list_workspaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fetch_across_regions** | **bool**|  | [optional] 

### Return type

[**ListWorkspacesResponse**](ListWorkspacesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

