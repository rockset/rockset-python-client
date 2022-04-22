# rockset.VirtualInstancesApi

All URIs are relative to *https://api.rs2.usw2.rockset.com* or the apiserver provided when initializing RocksetClient

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
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Retrieve Virtual Instance
    api_response = rs.VirtualInstancesApi.get_virtual_instance(
        virtual_instance_id="virtualInstanceId_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling VirtualInstancesApi->get_virtual_instance: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Retrieve Virtual Instance
    api_response = await rs.VirtualInstancesApi.get_virtual_instance(
        virtual_instance_id="virtualInstanceId_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling VirtualInstancesApi->get_virtual_instance: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_instance_id** | **str** | uuid of the virtual instance |

### Return type

[**GetVirtualInstanceResponse**](GetVirtualInstanceResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # List Virtual Instances
    api_response = rs.VirtualInstancesApi.list_virtual_instances(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling VirtualInstancesApi->list_virtual_instances: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # List Virtual Instances
    api_response = await rs.VirtualInstancesApi.list_virtual_instances(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling VirtualInstancesApi->list_virtual_instances: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListVirtualInstancesResponse**](ListVirtualInstancesResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Update Virtual Instance
    api_response = rs.VirtualInstancesApi.set_virtual_instance(
        virtual_instance_id="virtualInstanceId_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling VirtualInstancesApi->set_virtual_instance: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Update Virtual Instance
    api_response = await rs.VirtualInstancesApi.set_virtual_instance(
        virtual_instance_id="virtualInstanceId_example",
        monitoring_enabled=True,
        new_size="LARGE",
        new_type="FREE",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling VirtualInstancesApi->set_virtual_instance: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_instance_id** | **str** | uuid of the virtual instance |
 **monitoring_enabled** | **bool** |  | [optional]
 **new_size** | **str** | requested virtual instance size | [optional]
 **new_type** | **str** |  | [optional]

### Return type

[**UpdateVirtualInstanceResponse**](UpdateVirtualInstanceResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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

