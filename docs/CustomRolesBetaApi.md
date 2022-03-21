# rockset.CustomRolesBetaApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](CustomRolesBetaApi.md#create_role) | **POST** /v1/orgs/self/roles | Create a Role
[**delete_role**](CustomRolesBetaApi.md#delete_role) | **DELETE** /v1/orgs/self/roles/{roleName} | Delete a Role
[**list_roles**](CustomRolesBetaApi.md#list_roles) | **GET** /v1/orgs/self/roles | List Roles
[**update_role**](CustomRolesBetaApi.md#update_role) | **POST** /v1/orgs/self/roles/{roleName} | Update a Role


# **create_role**
> RoleResponse create_role(create_role_request)

Create a Role

Create a role for your organization.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.create_role_request import CreateRoleRequest
from rockset.model.error_model import ErrorModel
from rockset.model.role_response import RoleResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Create a Role
    api_response = rs.CustomRolesBetaApi.create_role(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CustomRolesBetaApi->create_role: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # Create a Role
    api_response = await rs.CustomRolesBetaApi.create_role(
        description="Role with read and write privileges to all collections.",
        privileges=[
        Privilege(
            action="Create collection",
            cluster="*ALL*",
            resource_name="commons",
        ),
    ],
        role_name="read_write",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CustomRolesBetaApi->create_role: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str** | Description for the role. | [optional]
 **privileges** | [**[Privilege]**](Privilege.md) | List of privileges that will be associated with the role. | [optional]
 **role_name** | **str** | Unique identifier for the role. | [optional]

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | role created successfully |  -  |
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

# **delete_role**
> RoleResponse delete_role(role_name)

Delete a Role

Delete a role for your organization.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.error_model import ErrorModel
from rockset.model.role_response import RoleResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Delete a Role
    api_response = rs.CustomRolesBetaApi.delete_role(
        role_name="roleName_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CustomRolesBetaApi->delete_role: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # Delete a Role
    api_response = await rs.CustomRolesBetaApi.delete_role(
        role_name="roleName_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CustomRolesBetaApi->delete_role: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str** |  |

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | role deleted successfully |  -  |
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

# **list_roles**
> ListRolesResponse list_roles()

List Roles

List all roles for your organization.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.list_roles_response import ListRolesResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # List Roles
    api_response = rs.CustomRolesBetaApi.list_roles(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CustomRolesBetaApi->list_roles: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # List Roles
    api_response = await rs.CustomRolesBetaApi.list_roles(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CustomRolesBetaApi->list_roles: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListRolesResponse**](ListRolesResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | roles retrived successfully |  -  |
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

# **update_role**
> RoleResponse update_role(role_name, update_role_request)

Update a Role

Update a role for your organization.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.error_model import ErrorModel
from rockset.model.role_response import RoleResponse
from rockset.model.update_role_request import UpdateRoleRequest
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Update a Role
    api_response = rs.CustomRolesBetaApi.update_role(
        role_name="roleName_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CustomRolesBetaApi->update_role: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # Update a Role
    api_response = await rs.CustomRolesBetaApi.update_role(
        role_name="roleName_example",
        description="Role with read and write privileges to all collections.",
        privileges=[
        Privilege(
            action="Create collection",
            cluster="*ALL*",
            resource_name="commons",
        ),
    ],
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CustomRolesBetaApi->update_role: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str** |  |
 **description** | **str** | Description for the role. | [optional]
 **privileges** | [**[Privilege]**](Privilege.md) | List of privileges that will be associated with the role. | [optional]

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | role updated successfully |  -  |
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

