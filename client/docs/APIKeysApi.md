# swagger_client.APIKeysApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](APIKeysApi.md#create_api_key) | **POST** /v1/orgs/self/users/self/apikeys | Create API Key
[**delete_api_key**](APIKeysApi.md#delete_api_key) | **DELETE** /v1/orgs/self/users/{user}/apikeys/{name} | Delete API Key
[**get_api_key**](APIKeysApi.md#get_api_key) | **GET** /v1/orgs/self/users/{user}/apikeys/{name} | Retrieve API Key
[**list_api_keys**](APIKeysApi.md#list_api_keys) | **GET** /v1/orgs/self/users/{user}/apikeys | List API Keys.
[**update_api_key**](APIKeysApi.md#update_api_key) | **POST** /v1/orgs/self/users/{user}/apikeys/{name} | Update an API key&#39;s state


# **create_api_key**
> CreateApiKeyResponse create_api_key(body)

Create API Key

Create a new API key for the authenticated user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIKeysApi()
body = swagger_client.CreateApiKeyRequest() # CreateApiKeyRequest | JSON object

try:
    # Create API Key
    api_response = api_instance.create_api_key(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->create_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateApiKeyRequest**](CreateApiKeyRequest.md)| JSON object | 

### Return type

[**CreateApiKeyResponse**](CreateApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> DeleteApiKeyResponse delete_api_key(name, user)

Delete API Key

Delete an API key for any user in your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIKeysApi()
name = 'name_example' # str | Name of the API key.
user = 'user_example' # str | Email of the API key owner. Use `self` to specify the currently authenticated user.

try:
    # Delete API Key
    api_response = api_instance.delete_api_key(name, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->delete_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the API key. | 
 **user** | **str**| Email of the API key owner. Use &#x60;self&#x60; to specify the currently authenticated user. | 

### Return type

[**DeleteApiKeyResponse**](DeleteApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key**
> GetApiKeyResponse get_api_key(user, name)

Retrieve API Key

Retrieve a particular API key for any user in your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIKeysApi()
user = 'user_example' # str | Email of the API key owner. Use `self` to specify the currently authenticated user.
name = 'name_example' # str | Name of the API key.

try:
    # Retrieve API Key
    api_response = api_instance.get_api_key(user, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->get_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Email of the API key owner. Use &#x60;self&#x60; to specify the currently authenticated user. | 
 **name** | **str**| Name of the API key. | 

### Return type

[**GetApiKeyResponse**](GetApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_keys**
> ListApiKeysResponse list_api_keys(user)

List API Keys.

List API key metadata for any user in your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIKeysApi()
user = 'user_example' # str | Email of the API key owner. Use `self` to specify the currently authenticated user.

try:
    # List API Keys.
    api_response = api_instance.list_api_keys(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->list_api_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Email of the API key owner. Use &#x60;self&#x60; to specify the currently authenticated user. | 

### Return type

[**ListApiKeysResponse**](ListApiKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key**
> UpdateApiKeyResponse update_api_key(name, user, body)

Update an API key's state

Update the state of an API key for any user in your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIKeysApi()
name = 'name_example' # str | Name of the API key.
user = 'user_example' # str | Email of the API key owner. Use `self` to specify the currently authenticated user.
body = swagger_client.UpdateApiKeyRequest() # UpdateApiKeyRequest | JSON object

try:
    # Update an API key's state
    api_response = api_instance.update_api_key(name, user, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIKeysApi->update_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the API key. | 
 **user** | **str**| Email of the API key owner. Use &#x60;self&#x60; to specify the currently authenticated user. | 
 **body** | [**UpdateApiKeyRequest**](UpdateApiKeyRequest.md)| JSON object | 

### Return type

[**UpdateApiKeyResponse**](UpdateApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

