# rockset.DocumentsApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

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
from rockset.api import documents_api
from rockset.model.add_documents_request import AddDocumentsRequest
from rockset.model.add_documents_response import AddDocumentsResponse
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
    api_instance = documents_api.DocumentsApi(api_client)
    collection = "collection_example" # str | Name of the collection.
    add_documents_request = AddDocumentsRequest(
        data=[
            {},
        ],
    ) # AddDocumentsRequest | JSON object

    # example passing only required values which don't have defaults set
    try:
        # Add Documents
        api_response = api_instance.add_documents(collection, add_documents_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling DocumentsApi->add_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Name of the collection. |
 **add_documents_request** | [**AddDocumentsRequest**](AddDocumentsRequest.md)| JSON object |
 **workspace** | **str**| Name of the workspace. | defaults to "commons"

### Return type

[**AddDocumentsResponse**](AddDocumentsResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
from rockset.api import documents_api
from rockset.model.delete_documents_request import DeleteDocumentsRequest
from rockset.model.error_model import ErrorModel
from rockset.model.delete_documents_response import DeleteDocumentsResponse
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
    api_instance = documents_api.DocumentsApi(api_client)
    collection = "collection_example" # str | Name of the collection.
    delete_documents_request = DeleteDocumentsRequest(
        data=[
            DeleteDocumentsRequestData(
                id="2cd61e3b",
            ),
        ],
    ) # DeleteDocumentsRequest | JSON object

    # example passing only required values which don't have defaults set
    try:
        # Delete Documents
        api_response = api_instance.delete_documents(collection, delete_documents_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling DocumentsApi->delete_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Name of the collection. |
 **delete_documents_request** | [**DeleteDocumentsRequest**](DeleteDocumentsRequest.md)| JSON object |
 **workspace** | **str**| Name of the workspace. | defaults to "commons"

### Return type

[**DeleteDocumentsResponse**](DeleteDocumentsResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
from rockset.api import documents_api
from rockset.model.patch_documents_request import PatchDocumentsRequest
from rockset.model.error_model import ErrorModel
from rockset.model.patch_documents_response import PatchDocumentsResponse
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
    api_instance = documents_api.DocumentsApi(api_client)
    collection = "collection_example" # str | Name of the collection.
    patch_documents_request = PatchDocumentsRequest(
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
    ) # PatchDocumentsRequest | JSON Patch objects

    # example passing only required values which don't have defaults set
    try:
        # Patch Documents
        api_response = api_instance.patch_documents(collection, patch_documents_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling DocumentsApi->patch_documents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Name of the collection. |
 **patch_documents_request** | [**PatchDocumentsRequest**](PatchDocumentsRequest.md)| JSON Patch objects |
 **workspace** | **str**| Name of the workspace. | defaults to "commons"

### Return type

[**PatchDocumentsResponse**](PatchDocumentsResponse.md)

### Authorization

[apikey](../README.md#apikey)

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

