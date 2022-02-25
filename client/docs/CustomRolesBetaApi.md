# swagger_client.CustomRolesBetaApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](CustomRolesBetaApi.md#create_role) | **POST** /v1/orgs/self/roles | Create a Role
[**delete_role**](CustomRolesBetaApi.md#delete_role) | **DELETE** /v1/orgs/self/roles/{roleName} | Delete a Role
[**list_roles**](CustomRolesBetaApi.md#list_roles) | **GET** /v1/orgs/self/roles | List Roles
[**update_role**](CustomRolesBetaApi.md#update_role) | **POST** /v1/orgs/self/roles/{roleName} | Update a Role


# **create_role**
> RoleResponse create_role(body)

Create a Role

Create a role for your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomRolesBetaApi()
body = swagger_client.CreateRoleRequest() # CreateRoleRequest | JSON Object

try:
    # Create a Role
    api_response = api_instance.create_role(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomRolesBetaApi->create_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRoleRequest**](CreateRoleRequest.md)| JSON Object | 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> RoleResponse delete_role(role_name)

Delete a Role

Delete a role for your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomRolesBetaApi()
role_name = 'role_name_example' # str | 

try:
    # Delete a Role
    api_response = api_instance.delete_role(role_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomRolesBetaApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**|  | 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles**
> ListRolesResponse list_roles()

List Roles

List all roles for your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomRolesBetaApi()

try:
    # List Roles
    api_response = api_instance.list_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomRolesBetaApi->list_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListRolesResponse**](ListRolesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> RoleResponse update_role(role_name, body)

Update a Role

Update a role for your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomRolesBetaApi()
role_name = 'role_name_example' # str | 
body = swagger_client.UpdateRoleRequest() # UpdateRoleRequest | JSON Object

try:
    # Update a Role
    api_response = api_instance.update_role(role_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomRolesBetaApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**|  | 
 **body** | [**UpdateRoleRequest**](UpdateRoleRequest.md)| JSON Object | 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

