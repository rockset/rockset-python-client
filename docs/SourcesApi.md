# rockset.Sources

All URIs are relative to *https://api.use1a1.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_source**](SourcesApi.md#create_source) | **POST** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources | Create a source
[**delete**](SourcesApi.md#delete) | **DELETE** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources/{source} | Delete Collection source
[**get**](SourcesApi.md#get) | **GET** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources/{source} | Retrieve source
[**list_collection_sources**](SourcesApi.md#list_collection_sources) | **GET** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources | List sources in collection


# **create_source**
> GetSourceResponse create_source(collection, source)

Create a source

Create new source in a collection.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create a source
api_response = rs.Sources.create_source(
    collection="collection_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Sources->create_source: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create a source
api_response = await rs.Sources.create_source(
    collection="collection_example",
    format_params=FormatParams(
        csv=CsvParams(
            column_names=["c1","c2","c3"],
            column_types=["BOOLEAN","INTEGER","FLOAT","STRING"],
            encoding="UTF-8",
            escape_char="\\",
            first_line_as_column_names=True,
            quote_char="\"",
            separator=",",
        ),
        json=True,
        mssql_dms=True,
        mysql_dms=True,
        oracle_dms=True,
        postgres_dms=True,
        xml=XmlParams(
            attribute_prefix="_attr",
            doc_tag="row",
            encoding="UTF-8",
            root_tag="root",
            value_tag="value",
        ),
    ),
    integration_name="aws-integration",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Sources->create_source: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **format_params** | [**FormatParams**](FormatParams.md) |  | [optional]
 **integration_name** | **str** | Name of integration to use. | [optional]
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**GetSourceResponse**](GetSourceResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | source created successfully |  -  |
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
> DeleteSourceResponse delete(collection, source)

Delete Collection source

Delete a collection source

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Delete Collection source
api_response = rs.Sources.delete(
    collection="collection_example",
    source="source_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Sources->delete: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Delete Collection source
api_response = await rs.Sources.delete(
    collection="collection_example",
    source="source_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Sources->delete: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **source** | **str** | id of source |
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**DeleteSourceResponse**](DeleteSourceResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | source deleted successfully |  -  |
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
> GetSourceResponse get(collection, source)

Retrieve source

Get details about a collection source.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Retrieve source
api_response = rs.Sources.get(
    collection="collection_example",
    source="source_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Sources->get: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Retrieve source
api_response = await rs.Sources.get(
    collection="collection_example",
    source="source_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Sources->get: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **source** | **str** | id of source |
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**GetSourceResponse**](GetSourceResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | collection retrieved successfully |  -  |
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

# **list_collection_sources**
> ListSourcesResponse list_collection_sources(collection)

List sources in collection

Retrieve all sources in a collection.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# List sources in collection
api_response = rs.Sources.list_collection_sources(
    collection="collection_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Sources->list_collection_sources: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# List sources in collection
api_response = await rs.Sources.list_collection_sources(
    collection="collection_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Sources->list_collection_sources: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**ListSourcesResponse**](ListSourcesResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | collection sources retrieved successfully |  -  |
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

