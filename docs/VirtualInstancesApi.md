# rockset.VirtualInstancesApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_virtual_instance**](VirtualInstancesApi.md#get_virtual_instance) | **GET** /v1/orgs/self/virtualinstances/{virtualInstanceId} | Retrieve Virtual Instance
[**list_virtual_instances**](VirtualInstancesApi.md#list_virtual_instances) | **GET** /v1/orgs/self/virtualinstances | List Virtual Instances
[**set_virtual_instance**](VirtualInstancesApi.md#set_virtual_instance) | **POST** /v1/orgs/self/virtualinstances/{virtualInstanceId} | Update Virtual Instance


# **get_virtual_instance**
> GetVirtualInstanceResponse get_virtual_instance(virtual_instance_id)

Retrieve Virtual Instance

Get details about a virtual instance.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset.api import virtual_instances_api
from rockset.model.error_model import ErrorModel
from rockset.model.get_virtual_instance_response import GetVirtualInstanceResponse
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
    api_instance = virtual_instances_api.VirtualInstancesApi(api_client)
    virtual_instance_id = "virtualInstanceId_example" # str | uuid of the virtual instance

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Virtual Instance
        api_response = api_instance.get_virtual_instance(virtual_instance_id)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling VirtualInstancesApi->get_virtual_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_instance_id** | **str**| uuid of the virtual instance |

### Return type

[**GetVirtualInstanceResponse**](GetVirtualInstanceResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | virtual instance retrieved successfully |  -  |
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

# **list_virtual_instances**
> ListVirtualInstancesResponse list_virtual_instances()

List Virtual Instances

Retrieve all virtual instances in an organization.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset.api import virtual_instances_api
from rockset.model.error_model import ErrorModel
from rockset.model.list_virtual_instances_response import ListVirtualInstancesResponse
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
    api_instance = virtual_instances_api.VirtualInstancesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Virtual Instances
        api_response = api_instance.list_virtual_instances()
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling VirtualInstancesApi->list_virtual_instances: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListVirtualInstancesResponse**](ListVirtualInstancesResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | virtual instances retrieved successfully |  -  |
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

# **set_virtual_instance**
> UpdateVirtualInstanceResponse set_virtual_instance(virtual_instance_id, update_virtual_instance_request)

Update Virtual Instance

Update the properties of a virtual instance.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset.api import virtual_instances_api
from rockset.model.update_virtual_instance_response import UpdateVirtualInstanceResponse
from rockset.model.update_virtual_instance_request import UpdateVirtualInstanceRequest
from rockset.model.error_model import ErrorModel
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
    api_instance = virtual_instances_api.VirtualInstancesApi(api_client)
    virtual_instance_id = "virtualInstanceId_example" # str | uuid of the virtual instance
    update_virtual_instance_request = UpdateVirtualInstanceRequest(
        monitoring_enabled=True,
        new_size="LARGE",
        new_type="FREE",
    ) # UpdateVirtualInstanceRequest | JSON object

    # example passing only required values which don't have defaults set
    try:
        # Update Virtual Instance
        api_response = api_instance.set_virtual_instance(virtual_instance_id, update_virtual_instance_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling VirtualInstancesApi->set_virtual_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_instance_id** | **str**| uuid of the virtual instance |
 **update_virtual_instance_request** | [**UpdateVirtualInstanceRequest**](UpdateVirtualInstanceRequest.md)| JSON object |

### Return type

[**UpdateVirtualInstanceResponse**](UpdateVirtualInstanceResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | virtual instance updated successfully |  -  |
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

