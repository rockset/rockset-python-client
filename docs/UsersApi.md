# rockset.UsersApi

All URIs are relative to *https://api.rs2.usw2.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /v1/orgs/self/users | Create User
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /v1/orgs/self/users/{user} | Delete User
[**get_current_user**](UsersApi.md#get_current_user) | **GET** /v1/orgs/self/users/self | Retrieve Current User
[**get_user**](UsersApi.md#get_user) | **GET** /v1/orgs/self/users/{user} | Retrieve User
[**list_unsubscribe_preferences**](UsersApi.md#list_unsubscribe_preferences) | **GET** /v1/orgs/self/users/self/preferences | Retrieve Notification Preferences
[**list_users**](UsersApi.md#list_users) | **GET** /v1/orgs/self/users | List Users
[**update_unsubscribe_preferences**](UsersApi.md#update_unsubscribe_preferences) | **POST** /v1/orgs/self/users/self/preferences | Update Notification Preferences


# **create_user**
> CreateUserResponse create_user(create_user_request)

Create User

Create a new user for an organization.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Create User
    api_response = rs.UsersApi.create_user(
        email="hello@rockset.com",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create User
    api_response = await rs.UsersApi.create_user(
        email="hello@rockset.com",
        roles=["admin","member","read-only"],
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling UsersApi->create_user: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str** | user email, must be unique | 
 **roles** | **[str]** | List of roles for a given user | [optional]

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | user created successfully |  -  |
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

# **delete_user**
> DeleteUserResponse delete_user(user)

Delete User

Delete a user from an organization.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Delete User
    api_response = rs.UsersApi.delete_user(
        user="user_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Delete User
    api_response = await rs.UsersApi.delete_user(
        user="user_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str** | user email |

### Return type

[**DeleteUserResponse**](DeleteUserResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | user deleted successfully |  -  |
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

# **get_current_user**
> User get_current_user()

Retrieve Current User

Retrieve currently authenticated user.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Retrieve Current User
    api_response = rs.UsersApi.get_current_user(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling UsersApi->get_current_user: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Retrieve Current User
    api_response = await rs.UsersApi.get_current_user(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling UsersApi->get_current_user: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | user retrieved successfully |  -  |
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

# **get_user**
> User get_user(user)

Retrieve User

Retrieve user by email.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Retrieve User
    api_response = rs.UsersApi.get_user(
        user="user_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Retrieve User
    api_response = await rs.UsersApi.get_user(
        user="user_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling UsersApi->get_user: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str** | user email |

### Return type

[**User**](User.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | user found |  -  |
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

# **list_unsubscribe_preferences**
> ListUnsubscribePreferencesResponse list_unsubscribe_preferences()

Retrieve Notification Preferences

Get all notification preferences.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Retrieve Notification Preferences
    api_response = rs.UsersApi.list_unsubscribe_preferences(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling UsersApi->list_unsubscribe_preferences: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Retrieve Notification Preferences
    api_response = await rs.UsersApi.list_unsubscribe_preferences(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling UsersApi->list_unsubscribe_preferences: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListUnsubscribePreferencesResponse**](ListUnsubscribePreferencesResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Notification preferences retrieved successfully |  -  |
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

# **list_users**
> ListUsersResponse list_users()

List Users

Retrieve all users for an organization.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # List Users
    api_response = rs.UsersApi.list_users(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling UsersApi->list_users: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # List Users
    api_response = await rs.UsersApi.list_users(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling UsersApi->list_users: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | users retrieved successfully |  -  |
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

# **update_unsubscribe_preferences**
> UpdateUnsubscribePreferencesResponse update_unsubscribe_preferences(update_unsubscribe_preferences_request)

Update Notification Preferences

Update notification preference.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Update Notification Preferences
    api_response = rs.UsersApi.update_unsubscribe_preferences(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling UsersApi->update_unsubscribe_preferences: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Update Notification Preferences
    api_response = await rs.UsersApi.update_unsubscribe_preferences(
        data=[
        UnsubscribePreference(
            notification_type="create_apikey",
        ),
    ],
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling UsersApi->update_unsubscribe_preferences: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**[UnsubscribePreference]**](UnsubscribePreference.md) | List of notification preferences | [optional]

### Return type

[**UpdateUnsubscribePreferencesResponse**](UpdateUnsubscribePreferencesResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Notification preference created successfully |  -  |
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

