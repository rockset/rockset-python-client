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


```python
import time
import rockset
from rockset.api import custom_roles__beta_api
from rockset.model.create_role_request import CreateRoleRequest
from rockset.model.error_model import ErrorModel
from rockset.model.role_response import RoleResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = custom_roles__beta_api.CustomRolesBetaApi(api_client)
    create_role_request = CreateRoleRequest(
        description="Role with read and write privileges to all collections.",
        privileges=[
            Privilege(
                action="Create collection",
                cluster="*ALL*",
                resource_name="commons",
            ),
        ],
        role_name="read_write",
    ) # CreateRoleRequest | JSON Object

    # example passing only required values which don't have defaults set
    try:
        # Create a Role
        api_response = api_instance.create_role(create_role_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling CustomRolesBetaApi->create_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_role_request** | [**CreateRoleRequest**](CreateRoleRequest.md)| JSON Object |

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

No authorization required

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


```python
import time
import rockset
from rockset.api import custom_roles__beta_api
from rockset.model.error_model import ErrorModel
from rockset.model.role_response import RoleResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = custom_roles__beta_api.CustomRolesBetaApi(api_client)
    role_name = "roleName_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a Role
        api_response = api_instance.delete_role(role_name)
        pprint(api_response)
    except rockset.ApiException as e:
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


```python
import time
import rockset
from rockset.api import custom_roles__beta_api
from rockset.model.list_roles_response import ListRolesResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = custom_roles__beta_api.CustomRolesBetaApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Roles
        api_response = api_instance.list_roles()
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling CustomRolesBetaApi->list_roles: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListRolesResponse**](ListRolesResponse.md)

### Authorization

No authorization required

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


```python
import time
import rockset
from rockset.api import custom_roles__beta_api
from rockset.model.error_model import ErrorModel
from rockset.model.role_response import RoleResponse
from rockset.model.update_role_request import UpdateRoleRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = custom_roles__beta_api.CustomRolesBetaApi(api_client)
    role_name = "roleName_example" # str | 
    update_role_request = UpdateRoleRequest(
        description="Role with read and write privileges to all collections.",
        privileges=[
            Privilege(
                action="Create collection",
                cluster="*ALL*",
                resource_name="commons",
            ),
        ],
    ) # UpdateRoleRequest | JSON Object

    # example passing only required values which don't have defaults set
    try:
        # Update a Role
        api_response = api_instance.update_role(role_name, update_role_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling CustomRolesBetaApi->update_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**|  |
 **update_role_request** | [**UpdateRoleRequest**](UpdateRoleRequest.md)| JSON Object |

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

No authorization required

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

