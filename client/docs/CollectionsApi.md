# swagger_client.CollectionsApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_collection**](CollectionsApi.md#create_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create Collection
[**delete_collection**](CollectionsApi.md#delete_collection) | **DELETE** /v1/orgs/self/ws/{workspace}/collections/{collection} | Delete Collection
[**get_collection**](CollectionsApi.md#get_collection) | **GET** /v1/orgs/self/ws/{workspace}/collections/{collection} | Retrieve Collection
[**list_collections**](CollectionsApi.md#list_collections) | **GET** /v1/orgs/self/collections | List Collections
[**workspace_collections**](CollectionsApi.md#workspace_collections) | **GET** /v1/orgs/self/ws/{workspace}/collections | List Collections in Workspace


# **create_collection**
> CreateCollectionResponse create_collection(workspace, body)

Create Collection

Create new collection in a workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollectionsApi()
workspace = 'workspace_example' # str | name of the workspace
body = swagger_client.CreateCollectionRequest() # CreateCollectionRequest | JSON object

try:
    # Create Collection
    api_response = api_instance.create_collection(workspace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->create_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **body** | [**CreateCollectionRequest**](CreateCollectionRequest.md)| JSON object | 

### Return type

[**CreateCollectionResponse**](CreateCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection**
> DeleteCollectionResponse delete_collection(workspace, collection)

Delete Collection

Delete a collection and all its documents from Rockset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollectionsApi()
workspace = 'workspace_example' # str | name of the workspace
collection = 'collection_example' # str | name of the collection

try:
    # Delete Collection
    api_response = api_instance.delete_collection(workspace, collection)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->delete_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **collection** | **str**| name of the collection | 

### Return type

[**DeleteCollectionResponse**](DeleteCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection**
> GetCollectionResponse get_collection(workspace, collection)

Retrieve Collection

Get details about a collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollectionsApi()
workspace = 'workspace_example' # str | name of the workspace
collection = 'collection_example' # str | name of the collection

try:
    # Retrieve Collection
    api_response = api_instance.get_collection(workspace, collection)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->get_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **collection** | **str**| name of the collection | 

### Return type

[**GetCollectionResponse**](GetCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_collections**
> ListCollectionsResponse list_collections()

List Collections

Retrieve all collections in an organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollectionsApi()

try:
    # List Collections
    api_response = api_instance.list_collections()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->list_collections: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListCollectionsResponse**](ListCollectionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workspace_collections**
> ListCollectionsResponse workspace_collections(workspace)

List Collections in Workspace

Retrieve all collections in a workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollectionsApi()
workspace = 'workspace_example' # str | name of the workspace

try:
    # List Collections in Workspace
    api_response = api_instance.workspace_collections(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->workspace_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 

### Return type

[**ListCollectionsResponse**](ListCollectionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

