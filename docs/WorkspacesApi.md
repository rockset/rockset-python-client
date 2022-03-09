# rockset.WorkspacesApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

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
from rockset.api import workspaces_api
from rockset.model.list_workspaces_response import ListWorkspacesResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with rockset.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspaces_api.WorkspacesApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # List Workspaces in Workspace
        api_response = api_instance.child_workspaces()
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling WorkspacesApi->child_workspaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**ListWorkspacesResponse**](ListWorkspacesResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
from rockset.api import workspaces_api
from rockset.model.create_workspace_response import CreateWorkspaceResponse
from rockset.model.create_workspace_request import CreateWorkspaceRequest
from rockset.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with rockset.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspaces_api.WorkspacesApi(api_client)
    create_workspace_request = CreateWorkspaceRequest(
        description="Datasets of system logs for the ops team.",
        name="event_logs",
    ) # CreateWorkspaceRequest | workspace details

    # example passing only required values which don't have defaults set
    try:
        # Create Workspace
        api_response = api_instance.create_workspace(create_workspace_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling WorkspacesApi->create_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workspace_request** | [**CreateWorkspaceRequest**](CreateWorkspaceRequest.md)| workspace details |

### Return type

[**CreateWorkspaceResponse**](CreateWorkspaceResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
from rockset.api import workspaces_api
from rockset.model.error_model import ErrorModel
from rockset.model.delete_workspace_response import DeleteWorkspaceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with rockset.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspaces_api.WorkspacesApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Delete Workspace
        api_response = api_instance.delete_workspace()
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling WorkspacesApi->delete_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**DeleteWorkspaceResponse**](DeleteWorkspaceResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
from rockset.api import workspaces_api
from rockset.model.get_workspace_response import GetWorkspaceResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with rockset.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspaces_api.WorkspacesApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Workspace
        api_response = api_instance.get_workspace()
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**GetWorkspaceResponse**](GetWorkspaceResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
from rockset.api import workspaces_api
from rockset.model.list_workspaces_response import ListWorkspacesResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with rockset.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workspaces_api.WorkspacesApi(api_client)
    fetch_across_regions = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Workspaces
        api_response = api_instance.list_workspaces(fetch_across_regions=fetch_across_regions)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling WorkspacesApi->list_workspaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fetch_across_regions** | **bool**|  | [optional]

### Return type

[**ListWorkspacesResponse**](ListWorkspacesResponse.md)

### Authorization

[apikey](../README.md#apikey)

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

