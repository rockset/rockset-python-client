# rockset.UsersApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /v1/orgs/self/users | Create User
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /v1/orgs/self/users/{user} | Delete User
[**get_current_user**](UsersApi.md#get_current_user) | **GET** /v1/orgs/self/users/self | Retrieve Current User
[**get_user**](UsersApi.md#get_user) | **GET** /v1/orgs/self/users/{user} | Retrieve User
[**list_unsubscribe_preferences**](UsersApi.md#list_unsubscribe_preferences) | **GET** /v1/orgs/self/users/self/preferences | Get all notification preferences
[**list_users**](UsersApi.md#list_users) | **GET** /v1/orgs/self/users | List Users
[**update_unsubscribe_preferences**](UsersApi.md#update_unsubscribe_preferences) | **POST** /v1/orgs/self/users/self/preferences | Update notification preferences


# **create_user**
> CreateUserResponse create_user(create_user_request)

Create User

Create a new user for an organization.

### Example


```python
import time
import rockset
from rockset.api import users_api
from rockset.model.create_user_response import CreateUserResponse
from rockset.model.error_model import ErrorModel
from rockset.model.create_user_request import CreateUserRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    create_user_request = CreateUserRequest(
        email="hello@rockset.com",
        roles=[
            "["admin", "member", "read-only"]",
        ],
    ) # CreateUserRequest | JSON object

    # example passing only required values which don't have defaults set
    try:
        # Create User
        api_response = api_instance.create_user(create_user_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_request** | [**CreateUserRequest**](CreateUserRequest.md)| JSON object |

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

No authorization required

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


```python
import time
import rockset
from rockset.api import users_api
from rockset.model.error_model import ErrorModel
from rockset.model.delete_user_response import DeleteUserResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user = "user_example" # str | user email

    # example passing only required values which don't have defaults set
    try:
        # Delete User
        api_response = api_instance.delete_user(user)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| user email |

### Return type

[**DeleteUserResponse**](DeleteUserResponse.md)

### Authorization

No authorization required

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


```python
import time
import rockset
from rockset.api import users_api
from rockset.model.error_model import ErrorModel
from rockset.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve Current User
        api_response = api_instance.get_current_user()
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling UsersApi->get_current_user: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

No authorization required

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


```python
import time
import rockset
from rockset.api import users_api
from rockset.model.error_model import ErrorModel
from rockset.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user = "user_example" # str | user email

    # example passing only required values which don't have defaults set
    try:
        # Retrieve User
        api_response = api_instance.get_user(user)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| user email |

### Return type

[**User**](User.md)

### Authorization

No authorization required

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

Get all notification preferences

Get all notification preferences.

### Example


```python
import time
import rockset
from rockset.api import users_api
from rockset.model.list_unsubscribe_preferences_response import ListUnsubscribePreferencesResponse
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
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all notification preferences
        api_response = api_instance.list_unsubscribe_preferences()
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling UsersApi->list_unsubscribe_preferences: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListUnsubscribePreferencesResponse**](ListUnsubscribePreferencesResponse.md)

### Authorization

No authorization required

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


```python
import time
import rockset
from rockset.api import users_api
from rockset.model.error_model import ErrorModel
from rockset.model.list_users_response import ListUsersResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Users
        api_response = api_instance.list_users()
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling UsersApi->list_users: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### Authorization

No authorization required

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

Update notification preferences

Update notification preference.

### Example


```python
import time
import rockset
from rockset.api import users_api
from rockset.model.error_model import ErrorModel
from rockset.model.update_unsubscribe_preferences_request import UpdateUnsubscribePreferencesRequest
from rockset.model.update_unsubscribe_preferences_response import UpdateUnsubscribePreferencesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    update_unsubscribe_preferences_request = UpdateUnsubscribePreferencesRequest(
        data=[
            UnsubscribePreference(
                notification_type="create_apikey",
            ),
        ],
    ) # UpdateUnsubscribePreferencesRequest | JSON Object

    # example passing only required values which don't have defaults set
    try:
        # Update notification preferences
        api_response = api_instance.update_unsubscribe_preferences(update_unsubscribe_preferences_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling UsersApi->update_unsubscribe_preferences: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_unsubscribe_preferences_request** | [**UpdateUnsubscribePreferencesRequest**](UpdateUnsubscribePreferencesRequest.md)| JSON Object |

### Return type

[**UpdateUnsubscribePreferencesResponse**](UpdateUnsubscribePreferencesResponse.md)

### Authorization

No authorization required

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

