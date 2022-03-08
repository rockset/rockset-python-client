# rockset.AliasesApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

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


```python
import time
import rockset
from rockset.api import aliases_api
from rockset.model.error_model import ErrorModel
from rockset.model.create_alias_response import CreateAliasResponse
from rockset.model.create_alias_request import CreateAliasRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = aliases_api.AliasesApi(api_client)
    create_alias_request = CreateAliasRequest(
        collections=[
            "["commons.foo", "prod.demo"]",
        ],
        description="version alias",
        name="aliasName",
    ) # CreateAliasRequest | JSON object

    # example passing only required values which don't have defaults set
    try:
        # Create Alias
        api_response = api_instance.create_alias(create_alias_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling AliasesApi->create_alias: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_alias_request** | [**CreateAliasRequest**](CreateAliasRequest.md)| JSON object |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**CreateAliasResponse**](CreateAliasResponse.md)

### Authorization

No authorization required

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


```python
import time
import rockset
from rockset.api import aliases_api
from rockset.model.delete_alias_response import DeleteAliasResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = aliases_api.AliasesApi(api_client)
    alias = "alias_example" # str | name of the alias

    # example passing only required values which don't have defaults set
    try:
        # Delete Alias
        api_response = api_instance.delete_alias(alias)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling AliasesApi->delete_alias: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| name of the alias |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**DeleteAliasResponse**](DeleteAliasResponse.md)

### Authorization

No authorization required

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


```python
import time
import rockset
from rockset.api import aliases_api
from rockset.model.error_model import ErrorModel
from rockset.model.get_alias_response import GetAliasResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = aliases_api.AliasesApi(api_client)
    alias = "alias_example" # str | name of the alias

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Alias
        api_response = api_instance.get_alias(alias)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling AliasesApi->get_alias: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| name of the alias |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**GetAliasResponse**](GetAliasResponse.md)

### Authorization

No authorization required

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


```python
import time
import rockset
from rockset.api import aliases_api
from rockset.model.error_model import ErrorModel
from rockset.model.list_aliases_response import ListAliasesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = aliases_api.AliasesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Aliases
        api_response = api_instance.list_aliases()
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling AliasesApi->list_aliases: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListAliasesResponse**](ListAliasesResponse.md)

### Authorization

No authorization required

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


```python
import time
import rockset
from rockset.api import aliases_api
from rockset.model.get_alias_response import GetAliasResponse
from rockset.model.update_alias_request import UpdateAliasRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = aliases_api.AliasesApi(api_client)
    alias = "alias_example" # str | name of the alias
    update_alias_request = UpdateAliasRequest(
        collections=[
            "["commons.foo", "prod.demo"]",
        ],
        description="version alias",
    ) # UpdateAliasRequest | JSON object

    # example passing only required values which don't have defaults set
    try:
        # Update Alias
        api_response = api_instance.update_alias(alias, update_alias_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling AliasesApi->update_alias: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| name of the alias |
 **update_alias_request** | [**UpdateAliasRequest**](UpdateAliasRequest.md)| JSON object |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**GetAliasResponse**](GetAliasResponse.md)

### Authorization

No authorization required

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


```python
import time
import rockset
from rockset.api import aliases_api
from rockset.model.error_model import ErrorModel
from rockset.model.list_aliases_response import ListAliasesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = aliases_api.AliasesApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # List Aliases in Workspace
        api_response = api_instance.workspace_aliases()
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling AliasesApi->workspace_aliases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**ListAliasesResponse**](ListAliasesResponse.md)

### Authorization

No authorization required

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

