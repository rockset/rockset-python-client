# swagger_client.ViewsApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_view**](ViewsApi.md#create_view) | **POST** /v1/orgs/self/ws/{workspace}/views | Create View
[**delete_view**](ViewsApi.md#delete_view) | **DELETE** /v1/orgs/self/ws/{workspace}/views/{view} | Delete View
[**get_view**](ViewsApi.md#get_view) | **GET** /v1/orgs/self/ws/{workspace}/views/{view} | Retrieve View
[**list_views**](ViewsApi.md#list_views) | **GET** /v1/orgs/self/views | List Views
[**update_view**](ViewsApi.md#update_view) | **POST** /v1/orgs/self/ws/{workspace}/views/{view} | Update View
[**workspace_views**](ViewsApi.md#workspace_views) | **GET** /v1/orgs/self/ws/{workspace}/views | List Views in Workspace


# **create_view**
> CreateViewResponse create_view(workspace, body)

Create View

Create a view

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ViewsApi()
workspace = 'workspace_example' # str | name of the workspace
body = swagger_client.CreateViewRequest() # CreateViewRequest | JSON object

try:
    # Create View
    api_response = api_instance.create_view(workspace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewsApi->create_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **body** | [**CreateViewRequest**](CreateViewRequest.md)| JSON object | 

### Return type

[**CreateViewResponse**](CreateViewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_view**
> DeleteViewResponse delete_view(workspace, view)

Delete View

Delete a view

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ViewsApi()
workspace = 'workspace_example' # str | name of the workspace
view = 'view_example' # str | name of the view

try:
    # Delete View
    api_response = api_instance.delete_view(workspace, view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewsApi->delete_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **view** | **str**| name of the view | 

### Return type

[**DeleteViewResponse**](DeleteViewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_view**
> GetViewResponse get_view(workspace, view)

Retrieve View

Get details about a view

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ViewsApi()
workspace = 'workspace_example' # str | name of the workspace
view = 'view_example' # str | name of the view

try:
    # Retrieve View
    api_response = api_instance.get_view(workspace, view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewsApi->get_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **view** | **str**| name of the view | 

### Return type

[**GetViewResponse**](GetViewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_views**
> ListViewsResponse list_views()

List Views

Retrieve all views in an organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ViewsApi()

try:
    # List Views
    api_response = api_instance.list_views()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewsApi->list_views: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListViewsResponse**](ListViewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_view**
> UpdateViewResponse update_view(workspace, view, body)

Update View

Update a view

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ViewsApi()
workspace = 'workspace_example' # str | name of the workspace
view = 'view_example' # str | name of the view
body = swagger_client.UpdateViewRequest() # UpdateViewRequest | JSON object

try:
    # Update View
    api_response = api_instance.update_view(workspace, view, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewsApi->update_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **view** | **str**| name of the view | 
 **body** | [**UpdateViewRequest**](UpdateViewRequest.md)| JSON object | 

### Return type

[**UpdateViewResponse**](UpdateViewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_views**
> ListViewsResponse workspace_views(workspace)

List Views in Workspace

Retrieve all views in a workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ViewsApi()
workspace = 'workspace_example' # str | name of the workspace

try:
    # List Views in Workspace
    api_response = api_instance.workspace_views(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewsApi->workspace_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 

### Return type

[**ListViewsResponse**](ListViewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

