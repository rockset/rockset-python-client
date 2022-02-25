# swagger_client.AliasesApi

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
> CreateAliasResponse create_alias(workspace, body)

Create Alias

Create new alias in a workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AliasesApi()
workspace = 'workspace_example' # str | name of the workspace
body = swagger_client.CreateAliasRequest() # CreateAliasRequest | JSON object

try:
    # Create Alias
    api_response = api_instance.create_alias(workspace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasesApi->create_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **body** | [**CreateAliasRequest**](CreateAliasRequest.md)| JSON object | 

### Return type

[**CreateAliasResponse**](CreateAliasResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alias**
> DeleteAliasResponse delete_alias(workspace, alias)

Delete Alias

Delete an alias.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AliasesApi()
workspace = 'workspace_example' # str | name of the workspace
alias = 'alias_example' # str | name of the alias

try:
    # Delete Alias
    api_response = api_instance.delete_alias(workspace, alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasesApi->delete_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **alias** | **str**| name of the alias | 

### Return type

[**DeleteAliasResponse**](DeleteAliasResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alias**
> GetAliasResponse get_alias(workspace, alias)

Retrieve Alias

Get details about an alias

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AliasesApi()
workspace = 'workspace_example' # str | name of the workspace
alias = 'alias_example' # str | name of the alias

try:
    # Retrieve Alias
    api_response = api_instance.get_alias(workspace, alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasesApi->get_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **alias** | **str**| name of the alias | 

### Return type

[**GetAliasResponse**](GetAliasResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_aliases**
> ListAliasesResponse list_aliases()

List Aliases

Retrieve all aliases in an organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AliasesApi()

try:
    # List Aliases
    api_response = api_instance.list_aliases()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasesApi->list_aliases: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListAliasesResponse**](ListAliasesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alias**
> GetAliasResponse update_alias(workspace, alias, body)

Update Alias

Update alias in a workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AliasesApi()
workspace = 'workspace_example' # str | name of the workspace
alias = 'alias_example' # str | name of the alias
body = swagger_client.UpdateAliasRequest() # UpdateAliasRequest | JSON object

try:
    # Update Alias
    api_response = api_instance.update_alias(workspace, alias, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasesApi->update_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **alias** | **str**| name of the alias | 
 **body** | [**UpdateAliasRequest**](UpdateAliasRequest.md)| JSON object | 

### Return type

[**GetAliasResponse**](GetAliasResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_aliases**
> ListAliasesResponse workspace_aliases(workspace)

List Aliases in Workspace

Retrieve all aliases in a workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AliasesApi()
workspace = 'workspace_example' # str | name of the workspace

try:
    # List Aliases in Workspace
    api_response = api_instance.workspace_aliases(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AliasesApi->workspace_aliases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 

### Return type

[**ListAliasesResponse**](ListAliasesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

