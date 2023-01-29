# rockset.Documents

All URIs are relative to *https://api.use1a1.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_documents**](DocumentsApi.md#add_documents) | **POST** /v1/orgs/self/ws/{workspace}/collections/{collection}/docs | Add Documents
[**delete_documents**](DocumentsApi.md#delete_documents) | **DELETE** /v1/orgs/self/ws/{workspace}/collections/{collection}/docs | Delete Documents
[**patch_documents**](DocumentsApi.md#patch_documents) | **PATCH** /v1/orgs/self/ws/{workspace}/collections/{collection}/docs | Patch Documents


# **add_documents**
> AddDocumentsResponse add_documents(collection, add_documents_request)

Add Documents

Add documents to a collection.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Add Documents
api_response = rs.Documents.add_documents(
    collection="collection_example",
    data=[{"field":"value"}],
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Documents->add_documents: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Add Documents
api_response = await rs.Documents.add_documents(
    collection="collection_example",
    data=[{"field":"value"}],
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Documents->add_documents: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | Name of the collection. |
 **data** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** | Array of documents to be added to the collection. | 
 **workspace** | **str** | Name of the workspace. | defaults to "commons"

### Return type

[**AddDocumentsResponse**](AddDocumentsResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | documents added successfully |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**413** | content too large |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_documents**
> DeleteDocumentsResponse delete_documents(collection, delete_documents_request)

Delete Documents

Delete documents from a collection.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Delete Documents
api_response = rs.Documents.delete_documents(
    collection="collection_example",
    data=[
        DeleteDocumentsRequestData(
            id="2cd61e3b",
        ),
    ],
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Documents->delete_documents: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Delete Documents
api_response = await rs.Documents.delete_documents(
    collection="collection_example",
    data=[
        DeleteDocumentsRequestData(
            id="2cd61e3b",
        ),
    ],
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Documents->delete_documents: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | Name of the collection. |
 **data** | [**[DeleteDocumentsRequestData]**](DeleteDocumentsRequestData.md) | Array of IDs of documents to be deleted. | 
 **workspace** | **str** | Name of the workspace. | defaults to "commons"

### Return type

[**DeleteDocumentsResponse**](DeleteDocumentsResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | documents deleted successfully |  -  |
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

# **patch_documents**
> PatchDocumentsResponse patch_documents(collection, patch_documents_request)

Patch Documents

Update existing documents in a collection.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Patch Documents
api_response = rs.Documents.patch_documents(
    collection="collection_example",
    data=[
        PatchDocument(
            id="ca2d6832-1bfd-f88f-0620-d2aa27a5d86c",
            patch=[
                PatchOperation(
                    _from="_from_example",
                    op="ADD",
                    path="/foo/bar",
                    value={},
                ),
            ],
        ),
    ],
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Documents->patch_documents: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Patch Documents
api_response = await rs.Documents.patch_documents(
    collection="collection_example",
    data=[
        PatchDocument(
            id="ca2d6832-1bfd-f88f-0620-d2aa27a5d86c",
            patch=[
                PatchOperation(
                    _from="_from_example",
                    op="ADD",
                    path="/foo/bar",
                    value={},
                ),
            ],
        ),
    ],
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Documents->patch_documents: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | Name of the collection. |
 **data** | [**[PatchDocument]**](PatchDocument.md) | List of patches to be applied. | 
 **workspace** | **str** | Name of the workspace. | defaults to "commons"

### Return type

[**PatchDocumentsResponse**](PatchDocumentsResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Documents patched successfully |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**413** | content too large |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

