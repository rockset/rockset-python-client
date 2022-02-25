# swagger_client.VirtualInstancesApi

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
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VirtualInstancesApi()
virtual_instance_id = 'virtual_instance_id_example' # str | uuid of the virtual instance

try:
    # Retrieve Virtual Instance
    api_response = api_instance.get_virtual_instance(virtual_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualInstancesApi->get_virtual_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_instance_id** | **str**| uuid of the virtual instance | 

### Return type

[**GetVirtualInstanceResponse**](GetVirtualInstanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_instances**
> ListVirtualInstancesResponse list_virtual_instances()

List Virtual Instances

Retrieve all virtual instances in an organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VirtualInstancesApi()

try:
    # List Virtual Instances
    api_response = api_instance.list_virtual_instances()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualInstancesApi->list_virtual_instances: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListVirtualInstancesResponse**](ListVirtualInstancesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_virtual_instance**
> UpdateVirtualInstanceResponse set_virtual_instance(virtual_instance_id, body)

Update Virtual Instance

Update the properties of a virtual instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VirtualInstancesApi()
virtual_instance_id = 'virtual_instance_id_example' # str | uuid of the virtual instance
body = swagger_client.UpdateVirtualInstanceRequest() # UpdateVirtualInstanceRequest | JSON object

try:
    # Update Virtual Instance
    api_response = api_instance.set_virtual_instance(virtual_instance_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualInstancesApi->set_virtual_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_instance_id** | **str**| uuid of the virtual instance | 
 **body** | [**UpdateVirtualInstanceRequest**](UpdateVirtualInstanceRequest.md)| JSON object | 

### Return type

[**UpdateVirtualInstanceResponse**](UpdateVirtualInstanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

