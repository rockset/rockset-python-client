# rockset.Search

All URIs are relative to *https://api.use1a1.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_box**](SearchApi.md#create_box) | **POST** /v1/search/boxes | Create a box
[**delete_box**](SearchApi.md#delete_box) | **DELETE** /v1/search/boxes/{box_rrn} | Delete a box
[**delete_pallet**](SearchApi.md#delete_pallet) | **DELETE** /v1/search/pallets/{pallet_id} | Delete a pallet
[**insert_docs**](SearchApi.md#insert_docs) | **POST** /v1/search/boxes/{box_rrn}/documents | Insert documents into a box
[**list_pallet_boxes**](SearchApi.md#list_pallet_boxes) | **GET** /v1/search/pallets/{pallet_id}/boxes | Get the boxes associated with a pallet ID within this cluster
[**query_box**](SearchApi.md#query_box) | **POST** /v1/search/boxes/{box_rrn}/query | Query a box
[**upgrade_box**](SearchApi.md#upgrade_box) | **POST** /v1/search/boxes/{box_rrn}/resize | Resize a box


# **create_box**
> BoxCreateResponse create_box()

Create a box

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create a box
api_response = rs.Search.create_box(
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Search->create_box: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create a box
api_response = await rs.Search.create_box(
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Search->create_box: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **initial_box_size** | **str** | The initial size of this box | [optional]
 **pallet_id** | **str** | optional opaque id of a pallet to associate this box with | [optional]
 **schema** | [**[BoxField]**](BoxField.md) | the set of fields that will be ingested. | [optional]
 **search_configuration** | [**BoxSearchConfiguration**](BoxSearchConfiguration.md) |  | [optional]


### Return type

[**BoxCreateResponse**](BoxCreateResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | box info |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_box**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} delete_box(box_rrn)

Delete a box

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Delete a box
api_response = rs.Search.delete_box(
    box_rrn="box_rrn_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Search->delete_box: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Delete a box
api_response = await rs.Search.delete_box(
    box_rrn="box_rrn_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Search->delete_box: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_rrn** | **str** | rrn of the box |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | box info |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pallet**
> delete_pallet(pallet_id)

Delete a pallet

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Delete a pallet
rs.Search.delete_pallet(
    pallet_id="pallet_id_example",
)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Search->delete_pallet: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Delete a pallet
rs.Search.delete_pallet(
    pallet_id="pallet_id_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Search->delete_pallet: %s\n" % e)
    return

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pallet_id** | **str** | opaque unique pallet id |

### Return type

void (empty response body)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | pallet deleted |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_docs**
> BoxInsertDocumentsResponse insert_docs(box_rrn)

Insert documents into a box

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Insert documents into a box
api_response = rs.Search.insert_docs(
    box_rrn="box_rrn_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Search->insert_docs: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Insert documents into a box
api_response = await rs.Search.insert_docs(
    box_rrn="box_rrn_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Search->insert_docs: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_rrn** | **str** | rrn of the box |

### Return type

[**BoxInsertDocumentsResponse**](BoxInsertDocumentsResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | insertion details |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pallet_boxes**
> PalletListBoxesResponse list_pallet_boxes(pallet_id)

Get the boxes associated with a pallet ID within this cluster

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Get the boxes associated with a pallet ID within this cluster
api_response = rs.Search.list_pallet_boxes(
    pallet_id="pallet_id_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Search->list_pallet_boxes: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Get the boxes associated with a pallet ID within this cluster
api_response = await rs.Search.list_pallet_boxes(
    pallet_id="pallet_id_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Search->list_pallet_boxes: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pallet_id** | **str** | opaque unique pallet id |

### Return type

[**PalletListBoxesResponse**](PalletListBoxesResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list of boxes on this pallet in this cluster |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_box**
> BoxQueryResponse query_box(box_rrn)

Query a box

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Query a box
api_response = rs.Search.query_box(
    box_rrn="box_rrn_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Search->query_box: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Query a box
api_response = await rs.Search.query_box(
    box_rrn="box_rrn_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Search->query_box: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_rrn** | **str** | rrn of the box |
 **count** | **bool** | Whether to return the total count of documents in the response | [optional]
 **limit** | **int** | The max results to return | [optional]
 **offset** | **int** | Skip over these many many top results | [optional]
 **select** | **[str]** | The fields to return from matched documents | [optional]
 **text_search** | [**BoxFullTextQuery**](BoxFullTextQuery.md) |  | [optional]
 **vector_queries** | [**[BoxVectorQuery]**](BoxVectorQuery.md) | The vector queries to make against this dataset | [optional]


### Return type

[**BoxQueryResponse**](BoxQueryResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query results |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_box**
> BoxResizeResponse upgrade_box(box_rrn)

Resize a box

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Resize a box
api_response = rs.Search.upgrade_box(
    box_rrn="box_rrn_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Search->upgrade_box: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Resize a box
api_response = await rs.Search.upgrade_box(
    box_rrn="box_rrn_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Search->upgrade_box: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_rrn** | **str** | rrn of the box |
 **new_size** | **str** | desired new size | [optional]


### Return type

[**BoxResizeResponse**](BoxResizeResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | box upgrade results |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

