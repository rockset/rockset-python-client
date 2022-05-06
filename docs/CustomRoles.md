# rockset.CustomRoles

All URIs are relative to *https://api.rs2.usw2.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](CustomRoles.md#create_role) | **POST** /v1/orgs/self/roles | Create a Role
[**delete_role**](CustomRoles.md#delete_role) | **DELETE** /v1/orgs/self/roles/{roleName} | Delete a Role
[**get_role**](CustomRoles.md#get_role) | **GET** /v1/orgs/self/roles/{roleName} | Retrieve role
[**list_roles**](CustomRoles.md#list_roles) | **GET** /v1/orgs/self/roles | List Roles
[**update_role**](CustomRoles.md#update_role) | **POST** /v1/orgs/self/roles/{roleName} | Update a Role


# **create_role**
> RoleResponse create_role(create_role_request)

Create a Role

Create a role for your organization.

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
    # Create a Role
    api_response = rs.CustomRoles.create_role(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CustomRoles->create_role: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create a Role
    api_response = await rs.CustomRoles.create_role(
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
        print("Exception when calling CustomRoles->create_role: %s\n" % e)
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
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Delete a Role
    api_response = rs.CustomRoles.delete_role(
        role_name="roleName_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CustomRoles->delete_role: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Delete a Role
    api_response = await rs.CustomRoles.delete_role(
        role_name="roleName_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CustomRoles->delete_role: %s\n" % e)
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

# **get_role**
> RoleResponse get_role(role_name)

Retrieve role

Retrieve a role by name for your organization.

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
    # Retrieve role
    api_response = rs.CustomRoles.get_role(
        role_name="roleName_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CustomRoles->get_role: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Retrieve role
    api_response = await rs.CustomRoles.get_role(
        role_name="roleName_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CustomRoles->get_role: %s\n" % e)
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
**200** | role retrieved successfully |  -  |
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
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # List Roles
    api_response = rs.CustomRoles.list_roles(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CustomRoles->list_roles: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # List Roles
    api_response = await rs.CustomRoles.list_roles(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CustomRoles->list_roles: %s\n" % e)
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
**200** | roles retrieved successfully |  -  |
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
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Update a Role
    api_response = rs.CustomRoles.update_role(
        role_name="roleName_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CustomRoles->update_role: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Update a Role
    api_response = await rs.CustomRoles.update_role(
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
        print("Exception when calling CustomRoles->update_role: %s\n" % e)
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
