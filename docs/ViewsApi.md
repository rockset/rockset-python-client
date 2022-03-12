# rockset.ViewsApi

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
> CreateViewResponse create_view(create_view_request)

Create View

Create a view

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset.api import views_api
from rockset.model.create_view_request import CreateViewRequest
from rockset.model.create_view_response import CreateViewResponse
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
    api_instance = views_api.ViewsApi(api_client)
    create_view_request = CreateViewRequest(
        description="view of awesome collection",
        name="myAwesomeView",
        query="SELECT * FROM foo",
    ) # CreateViewRequest | JSON object

    # example passing only required values which don't have defaults set
    try:
        # Create View
        api_response = api_instance.create_view(create_view_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling ViewsApi->create_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_view_request** | [**CreateViewRequest**](CreateViewRequest.md)| JSON object |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**CreateViewResponse**](CreateViewResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
import time
import rockset
from rockset.api import views_api
from rockset.model.delete_view_response import DeleteViewResponse
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
    api_instance = views_api.ViewsApi(api_client)
    view = "view_example" # str | name of the view

    # example passing only required values which don't have defaults set
    try:
        # Delete View
        api_response = api_instance.delete_view(view)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling ViewsApi->delete_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| name of the view |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**DeleteViewResponse**](DeleteViewResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
import time
import rockset
from rockset.api import views_api
from rockset.model.error_model import ErrorModel
from rockset.model.get_view_response import GetViewResponse
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
    api_instance = views_api.ViewsApi(api_client)
    view = "view_example" # str | name of the view

    # example passing only required values which don't have defaults set
    try:
        # Retrieve View
        api_response = api_instance.get_view(view)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling ViewsApi->get_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| name of the view |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**GetViewResponse**](GetViewResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
import time
import rockset
from rockset.api import views_api
from rockset.model.error_model import ErrorModel
from rockset.model.list_views_response import ListViewsResponse
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
    api_instance = views_api.ViewsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Views
        api_response = api_instance.list_views()
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling ViewsApi->list_views: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListViewsResponse**](ListViewsResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
import time
import rockset
from rockset.api import views_api
from rockset.model.update_view_request import UpdateViewRequest
from rockset.model.update_view_response import UpdateViewResponse
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
    api_instance = views_api.ViewsApi(api_client)
    view = "view_example" # str | name of the view
    update_view_request = UpdateViewRequest(
        description="view of awesome collection",
        query="SELECT * FROM foo",
    ) # UpdateViewRequest | JSON object

    # example passing only required values which don't have defaults set
    try:
        # Update View
        api_response = api_instance.update_view(view, update_view_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling ViewsApi->update_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| name of the view |
 **update_view_request** | [**UpdateViewRequest**](UpdateViewRequest.md)| JSON object |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**UpdateViewResponse**](UpdateViewResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
import time
import rockset
from rockset.api import views_api
from rockset.model.error_model import ErrorModel
from rockset.model.list_views_response import ListViewsResponse
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
    api_instance = views_api.ViewsApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # List Views in Workspace
        api_response = api_instance.workspace_views()
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling ViewsApi->workspace_views: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**ListViewsResponse**](ListViewsResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
