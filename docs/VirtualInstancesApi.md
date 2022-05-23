# rockset.VirtualInstances

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
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Retrieve Virtual Instance
api_response = rs.VirtualInstances.get_virtual_instance(
    virtual_instance_id="virtualInstanceId_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling VirtualInstances->get_virtual_instance: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Retrieve Virtual Instance
api_response = await rs.VirtualInstances.get_virtual_instance(
    virtual_instance_id="virtualInstanceId_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling VirtualInstances->get_virtual_instance: %s\n" % e)
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
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# List Virtual Instances
api_response = rs.VirtualInstances.list_virtual_instances(
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling VirtualInstances->list_virtual_instances: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# List Virtual Instances
api_response = await rs.VirtualInstances.list_virtual_instances(
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling VirtualInstances->list_virtual_instances: %s\n" % e)
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
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Update Virtual Instance
api_response = rs.VirtualInstances.set_virtual_instance(
    virtual_instance_id="virtualInstanceId_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling VirtualInstances->set_virtual_instance: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Update Virtual Instance
api_response = await rs.VirtualInstances.set_virtual_instance(
    virtual_instance_id="virtualInstanceId_example",
    monitoring_enabled=True,
    new_size="LARGE",
    new_type="FREE",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling VirtualInstances->set_virtual_instance: %s\n" % e)
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

