# rockset.VirtualInstances

All URIs are relative to *https://api.use1a1.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](VirtualInstancesApi.md#create) | **POST** /v1/orgs/self/virtualinstances | Create Virtual Instance
[**delete**](VirtualInstancesApi.md#delete) | **DELETE** /v1/orgs/self/virtualinstances/{virtualInstanceId} | Delete Virtual Instance
[**get**](VirtualInstancesApi.md#get) | **GET** /v1/orgs/self/virtualinstances/{virtualInstanceId} | Retrieve Virtual Instance
[**get_collection_mount**](VirtualInstancesApi.md#get_collection_mount) | **GET** /v1/orgs/self/virtualinstances/{virtualInstanceId}/mounts/{collectionPath} | Get Collection Mount
[**get_virtual_instance_queries**](VirtualInstancesApi.md#get_virtual_instance_queries) | **GET** /v1/orgs/self/virtualinstances/{virtualInstanceId}/queries | List Queries
[**list**](VirtualInstancesApi.md#list) | **GET** /v1/orgs/self/virtualinstances | List Virtual Instances
[**list_collection_mounts**](VirtualInstancesApi.md#list_collection_mounts) | **GET** /v1/orgs/self/virtualinstances/{virtualInstanceId}/mounts | List Collection Mounts
[**mount_collection**](VirtualInstancesApi.md#mount_collection) | **POST** /v1/orgs/self/virtualinstances/{virtualInstanceId}/mounts | Mount Collections
[**query_virtual_instance**](VirtualInstancesApi.md#query_virtual_instance) | **POST** /v1/orgs/self/virtualinstances/{virtualInstanceId}/queries | Execute SQL Query
[**resume_virtual_instance**](VirtualInstancesApi.md#resume_virtual_instance) | **POST** /v1/orgs/self/virtualinstances/{virtualInstanceId}/resume | Resume Virtual Instance
[**suspend_virtual_instance**](VirtualInstancesApi.md#suspend_virtual_instance) | **POST** /v1/orgs/self/virtualinstances/{virtualInstanceId}/suspend | Suspend Virtual Instance
[**unmount_collection**](VirtualInstancesApi.md#unmount_collection) | **DELETE** /v1/orgs/self/virtualinstances/{virtualInstanceId}/mounts/{collectionPath} | Unmount Collection
[**update**](VirtualInstancesApi.md#update) | **POST** /v1/orgs/self/virtualinstances/{virtualInstanceId} | Update Virtual Instance


# **create**
> CreateVirtualInstanceResponse create(create_virtual_instance_request)

Create Virtual Instance

[beta] Create virtual instance

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create Virtual Instance
api_response = rs.VirtualInstances.create(
    name="prod_vi",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling VirtualInstances->create: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create Virtual Instance
api_response = await rs.VirtualInstances.create(
    auto_suspend_seconds=3600,
    description="VI serving prod traffic",
    enable_remount_on_resume=True,
    mount_refresh_interval_seconds=3600,
    name="prod_vi",
    type="LARGE",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling VirtualInstances->create: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_suspend_seconds** | **int** | Number of seconds without queries after which the VI is suspended | [optional]
 **description** | **str** | Description of requested virtual instance. | [optional]
 **enable_remount_on_resume** | **bool** | When a Virtual Instance is resumed, it will remount all collections that were mounted when the Virtual Instance was suspended. | [optional]
 **mount_refresh_interval_seconds** | **int** | Number of seconds between data refreshes for mounts on this Virtual Instance. A value of 0 means continuous refresh and a value of null means never refresh. | [optional]
 **name** | **str** | Unique identifier for virtual instance, can contain alphanumeric or dash characters. | 
 **type** | **str** | Requested virtual instance type. | [optional]

### Return type

[**CreateVirtualInstanceResponse**](CreateVirtualInstanceResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | virtual instance created successfully |  -  |
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

# **delete**
> DeleteVirtualInstanceResponse delete(virtual_instance_id)

Delete Virtual Instance

[beta] Delete a virtual instance.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Delete Virtual Instance
api_response = rs.VirtualInstances.delete(
    virtual_instance_id="virtualInstanceId_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling VirtualInstances->delete: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Delete Virtual Instance
api_response = await rs.VirtualInstances.delete(
    virtual_instance_id="virtualInstanceId_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling VirtualInstances->delete: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_instance_id** | **str** | Virtual Instance RRN |

### Return type

[**DeleteVirtualInstanceResponse**](DeleteVirtualInstanceResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | virtual instance deleted successfully |  -  |
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

# **get**
> GetVirtualInstanceResponse get(virtual_instance_id)

Retrieve Virtual Instance

Get details about a virtual instance.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Retrieve Virtual Instance
api_response = rs.VirtualInstances.get(
    virtual_instance_id="virtualInstanceId_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling VirtualInstances->get: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Retrieve Virtual Instance
api_response = await rs.VirtualInstances.get(
    virtual_instance_id="virtualInstanceId_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling VirtualInstances->get: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_instance_id** | **str** | Virtual Instance RRN |

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

# **get_collection_mount**
> CollectionMountResponse get_collection_mount(virtual_instance_id, collection_path)

Get Collection Mount

[beta] Retrieve a mount on this virtual instance.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Get Collection Mount
api_response = rs.VirtualInstances.get_collection_mount(
    virtual_instance_id="virtualInstanceId_example",
    collection_path="collectionPath_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling VirtualInstances->get_collection_mount: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Get Collection Mount
api_response = await rs.VirtualInstances.get_collection_mount(
    virtual_instance_id="virtualInstanceId_example",
    collection_path="collectionPath_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling VirtualInstances->get_collection_mount: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_instance_id** | **str** | Virtual Instance RRN |
 **collection_path** | **str** |  |

### Return type

[**CollectionMountResponse**](CollectionMountResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | collection unmounted |  -  |
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

# **get_virtual_instance_queries**
> ListQueriesResponse get_virtual_instance_queries(virtual_instance_id)

List Queries

[beta] Lists actively queued and running queries for a particular Virtual Instance.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# List Queries
api_response = rs.VirtualInstances.get_virtual_instance_queries(
    virtual_instance_id="virtualInstanceId_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling VirtualInstances->get_virtual_instance_queries: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# List Queries
api_response = await rs.VirtualInstances.get_virtual_instance_queries(
    virtual_instance_id="virtualInstanceId_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling VirtualInstances->get_virtual_instance_queries: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_instance_id** | **str** | Virtual Instance RRN |

### Return type

[**ListQueriesResponse**](ListQueriesResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully fetched queries |  -  |
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

# **list**
> ListVirtualInstancesResponse list()

List Virtual Instances

Retrieve all virtual instances in an organization.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# List Virtual Instances
api_response = rs.VirtualInstances.list(
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling VirtualInstances->list: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# List Virtual Instances
api_response = await rs.VirtualInstances.list(
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling VirtualInstances->list: %s\n" % e)
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

# **list_collection_mounts**
> ListCollectionMountsResponse list_collection_mounts(virtual_instance_id)

List Collection Mounts

[beta] List collection mounts for a particular VI.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# List Collection Mounts
api_response = rs.VirtualInstances.list_collection_mounts(
    virtual_instance_id="virtualInstanceId_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling VirtualInstances->list_collection_mounts: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# List Collection Mounts
api_response = await rs.VirtualInstances.list_collection_mounts(
    virtual_instance_id="virtualInstanceId_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling VirtualInstances->list_collection_mounts: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_instance_id** | **str** | Virtual Instance RRN |

### Return type

[**ListCollectionMountsResponse**](ListCollectionMountsResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | resource mounted |  -  |
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

# **mount_collection**
> CreateCollectionMountsResponse mount_collection(virtual_instance_id, create_collection_mount_request)

Mount Collections

[beta] Mount a collection to this virtual instance.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Mount Collections
api_response = rs.VirtualInstances.mount_collection(
    virtual_instance_id="virtualInstanceId_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling VirtualInstances->mount_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Mount Collections
api_response = await rs.VirtualInstances.mount_collection(
    virtual_instance_id="virtualInstanceId_example",
    collection_paths=["commons.foo","commons.bar"],
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling VirtualInstances->mount_collection: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_instance_id** | **str** | Virtual Instance RRN |
 **collection_paths** | **[str]** | Collections to mount. | [optional]

### Return type

[**CreateCollectionMountsResponse**](CreateCollectionMountsResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | collection mounted |  -  |
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

# **query_virtual_instance**
> QueryResponse query_virtual_instance(virtual_instance_id, query_request)

Execute SQL Query

[beta] Make a SQL query to Rockset.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Execute SQL Query
api_response = rs.VirtualInstances.query_virtual_instance(
    virtual_instance_id="virtualInstanceId_example",
    sql=QueryRequestSql(
        default_row_limit=1,
        initial_paginate_response_doc_count=1,
        parameters=[
            QueryParameter(
                name="_id",
                type="string",
                value="85beb391",
            ),
        ],
        query="SELECT * FROM foo where _id = :_id",
    ),
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling VirtualInstances->query_virtual_instance: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Execute SQL Query
api_response = await rs.VirtualInstances.query_virtual_instance(
    virtual_instance_id="virtualInstanceId_example",
    _async=True,
    async_options=AsyncQueryOptions(
        client_timeout_ms=1,
        max_initial_results=1,
        timeout_ms=1,
    ),
    debug_threshold_ms=1,
    max_initial_results=1,
    sql=QueryRequestSql(
        default_row_limit=1,
        initial_paginate_response_doc_count=1,
        parameters=[
            QueryParameter(
                name="_id",
                type="string",
                value="85beb391",
            ),
        ],
        query="SELECT * FROM foo where _id = :_id",
    ),
    timeout_ms=1,
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling VirtualInstances->query_virtual_instance: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_instance_id** | **str** | Virtual Instance RRN |
 **_async** | **bool** | If true, the query will run asynchronously for up to 30 minutes. The query request will immediately return with a query id that can be used to retrieve the query status and results. If false or not specified, the query will return with results once completed or timeout after 2 minutes. (To return results directly for shorter queries while still allowing a timeout of up to 30 minutes, set &#x60;async_options.client_timeout_ms&#x60;.)  | [optional]
 **async_options** | [**AsyncQueryOptions**](AsyncQueryOptions.md) |  | [optional]
 **debug_threshold_ms** | **int** | If query execution takes longer than this value, debug information will be logged. If the query text includes the DEBUG hint and this parameter is also provided, only this value will be used and the DEBUG hint will be ignored. | [optional]
 **max_initial_results** | **int** | This limits the maximum number of results in the initial response. A pagination cursor is returned if the number of results exceeds &#x60;max_initial_results&#x60;. If &#x60;max_initial_results&#x60; is not set, all results will be returned in the initial response up to 4 million. If &#x60;max_initial_results&#x60; is set, the value must be between 0 and 100,000. If the query is async and &#x60;client_timeout_ms&#x60; is exceeded, &#x60;max_initial_results&#x60; does not apply since none of the results will be returned with the initial response. | [optional]
 **sql** | [**QueryRequestSql**](QueryRequestSql.md) |  | 
 **timeout_ms** | **int** | If a query exceeds the specified timeout, the query will automatically stop and return an error. The query timeout defaults to a maximum of 2 minutes. If &#x60;async&#x60; is true, the query timeout defaults to a maximum of 30 minutes. | [optional]

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query executed successfully |  -  |
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

# **resume_virtual_instance**
> ResumeVirtualInstanceResponse resume_virtual_instance(virtual_instance_id)

Resume Virtual Instance

[beta] Resume a virtual instance.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Resume Virtual Instance
api_response = rs.VirtualInstances.resume_virtual_instance(
    virtual_instance_id="virtualInstanceId_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling VirtualInstances->resume_virtual_instance: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Resume Virtual Instance
api_response = await rs.VirtualInstances.resume_virtual_instance(
    virtual_instance_id="virtualInstanceId_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling VirtualInstances->resume_virtual_instance: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_instance_id** | **str** | Virtual Instance RRN |

### Return type

[**ResumeVirtualInstanceResponse**](ResumeVirtualInstanceResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | virtual instance resumed successfully |  -  |
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

# **suspend_virtual_instance**
> SuspendVirtualInstanceResponse suspend_virtual_instance(virtual_instance_id)

Suspend Virtual Instance

[beta] Suspend a virtual instance.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Suspend Virtual Instance
api_response = rs.VirtualInstances.suspend_virtual_instance(
    virtual_instance_id="virtualInstanceId_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling VirtualInstances->suspend_virtual_instance: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Suspend Virtual Instance
api_response = await rs.VirtualInstances.suspend_virtual_instance(
    virtual_instance_id="virtualInstanceId_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling VirtualInstances->suspend_virtual_instance: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_instance_id** | **str** | Virtual Instance RRN |

### Return type

[**SuspendVirtualInstanceResponse**](SuspendVirtualInstanceResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | virtual instance suspended successfully |  -  |
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

# **unmount_collection**
> CollectionMountResponse unmount_collection(virtual_instance_id, collection_path)

Unmount Collection

[beta] Unmount a collection from this virtual instance.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Unmount Collection
api_response = rs.VirtualInstances.unmount_collection(
    virtual_instance_id="virtualInstanceId_example",
    collection_path="collectionPath_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling VirtualInstances->unmount_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Unmount Collection
api_response = await rs.VirtualInstances.unmount_collection(
    virtual_instance_id="virtualInstanceId_example",
    collection_path="collectionPath_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling VirtualInstances->unmount_collection: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_instance_id** | **str** | Virtual Instance RRN |
 **collection_path** | **str** |  |

### Return type

[**CollectionMountResponse**](CollectionMountResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | collection unmounted |  -  |
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

# **update**
> UpdateVirtualInstanceResponse update(virtual_instance_id, update_virtual_instance_request)

Update Virtual Instance

Update the properties of a virtual instance.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Update Virtual Instance
api_response = rs.VirtualInstances.update(
    virtual_instance_id="virtualInstanceId_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling VirtualInstances->update: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Update Virtual Instance
api_response = await rs.VirtualInstances.update(
    virtual_instance_id="virtualInstanceId_example",
    auto_scaling_policy=AutoScalingPolicy(
        enabled=True,
        max_size="XLARGE2",
        min_size="LARGE",
    ),
    auto_suspend_enabled=True,
    auto_suspend_seconds=3600,
    description="VI for prod traffic",
    enable_remount_on_resume=True,
    mount_refresh_interval_seconds=3600,
    name="prod_vi",
    new_size="LARGE",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling VirtualInstances->update: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtual_instance_id** | **str** | Virtual Instance RRN |
 **auto_scaling_policy** | [**AutoScalingPolicy**](AutoScalingPolicy.md) |  | [optional]
 **auto_suspend_enabled** | **bool** | Whether auto-suspend should be enabled for this Virtual Instance. | [optional]
 **auto_suspend_seconds** | **int** | Number of seconds without queries after which the VI is suspended | [optional]
 **description** | **str** | New virtual instance description. | [optional]
 **enable_remount_on_resume** | **bool** | When a Virtual Instance is resumed, it will remount all collections that were mounted when the Virtual Instance was suspended. | [optional]
 **mount_refresh_interval_seconds** | **int** | Number of seconds between data refreshes for mounts on this Virtual Instance. A value of 0 means continuous refresh and a value of null means never refresh. | [optional]
 **name** | **str** | New virtual instance name. | [optional]
 **new_size** | **str** | Requested virtual instance size. | [optional]

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

