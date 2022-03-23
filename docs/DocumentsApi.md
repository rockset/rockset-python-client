# rockset.DocumentsApi

All URIs are relative to *https://api.rs2.usw2.rockset.com* or the apiserver provided when initializing RocksetClient

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
import time
import rockset
from rockset import RocksetClient
from rockset.model.add_documents_request import AddDocumentsRequest
from rockset.model.add_documents_response import AddDocumentsResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Add Documents
    api_response = rs.DocumentsApi.add_documents(
        collection="collection_example",
        data=[{"field":"value"}],
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling DocumentsApi->add_documents: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Add Documents
    api_response = await rs.DocumentsApi.add_documents(
        collection="collection_example",
        data=[{"field":"value"}],
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling DocumentsApi->add_documents: %s\n" % e)
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
import time
import rockset
from rockset import RocksetClient
from rockset.model.delete_documents_request import DeleteDocumentsRequest
from rockset.model.error_model import ErrorModel
from rockset.model.delete_documents_response import DeleteDocumentsResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Delete Documents
    api_response = rs.DocumentsApi.delete_documents(
        collection="collection_example",
        data=[
        DeleteDocumentsRequestData(
            id="2cd61e3b",
        ),
    ],
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling DocumentsApi->delete_documents: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Delete Documents
    api_response = await rs.DocumentsApi.delete_documents(
        collection="collection_example",
        data=[
        DeleteDocumentsRequestData(
            id="2cd61e3b",
        ),
    ],
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling DocumentsApi->delete_documents: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | Name of the collection. |
 **data** | [**[DeleteDocumentsRequestData]**](DeleteDocumentsRequestData.md) | Array of IDs of documents to be deleted | 
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
import time
import rockset
from rockset import RocksetClient
from rockset.model.patch_documents_request import PatchDocumentsRequest
from rockset.model.error_model import ErrorModel
from rockset.model.patch_documents_response import PatchDocumentsResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Patch Documents
    api_response = rs.DocumentsApi.patch_documents(
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
except rockset.ApiException as e:
    print("Exception when calling DocumentsApi->patch_documents: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Patch Documents
    api_response = await rs.DocumentsApi.patch_documents(
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
        print("Exception when calling DocumentsApi->patch_documents: %s\n" % e)
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
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

