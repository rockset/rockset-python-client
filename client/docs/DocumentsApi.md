# swagger_client.DocumentsApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_documents**](DocumentsApi.md#add_documents) | **POST** /v1/orgs/self/ws/{workspace}/collections/{collection}/docs | Add Documents
[**delete_documents**](DocumentsApi.md#delete_documents) | **DELETE** /v1/orgs/self/ws/{workspace}/collections/{collection}/docs | Delete Documents
[**patch_documents**](DocumentsApi.md#patch_documents) | **PATCH** /v1/orgs/self/ws/{workspace}/collections/{collection}/docs | Patch Documents


# **add_documents**
> AddDocumentsResponse add_documents(workspace, collection, body)

Add Documents

Add documents to a collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DocumentsApi()
workspace = 'workspace_example' # str | Name of the workspace.
collection = 'collection_example' # str | Name of the collection.
body = swagger_client.AddDocumentsRequest() # AddDocumentsRequest | JSON object

try:
    # Add Documents
    api_response = api_instance.add_documents(workspace, collection, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->add_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace. | 
 **collection** | **str**| Name of the collection. | 
 **body** | [**AddDocumentsRequest**](AddDocumentsRequest.md)| JSON object | 

### Return type

[**AddDocumentsResponse**](AddDocumentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_documents**
> DeleteDocumentsResponse delete_documents(workspace, collection, body)

Delete Documents

Delete documents from a collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DocumentsApi()
workspace = 'workspace_example' # str | Name of the workspace.
collection = 'collection_example' # str | Name of the collection.
body = swagger_client.DeleteDocumentsRequest() # DeleteDocumentsRequest | JSON object

try:
    # Delete Documents
    api_response = api_instance.delete_documents(workspace, collection, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->delete_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace. | 
 **collection** | **str**| Name of the collection. | 
 **body** | [**DeleteDocumentsRequest**](DeleteDocumentsRequest.md)| JSON object | 

### Return type

[**DeleteDocumentsResponse**](DeleteDocumentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_documents**
> PatchDocumentsResponse patch_documents(workspace, collection, body)

Patch Documents

Update existing documents in a collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DocumentsApi()
workspace = 'workspace_example' # str | Name of the workspace.
collection = 'collection_example' # str | Name of the collection.
body = swagger_client.PatchDocumentsRequest() # PatchDocumentsRequest | JSON Patch objects

try:
    # Patch Documents
    api_response = api_instance.patch_documents(workspace, collection, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->patch_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace. | 
 **collection** | **str**| Name of the collection. | 
 **body** | [**PatchDocumentsRequest**](PatchDocumentsRequest.md)| JSON Patch objects | 

### Return type

[**PatchDocumentsResponse**](PatchDocumentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

