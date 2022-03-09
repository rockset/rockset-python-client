# rockset.CollectionsApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_azure_blob_collection**](CollectionsApi.md#create_azure_blob_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections#AzureBlob | Create azure blob collection
[**create_gcs_collection**](CollectionsApi.md#create_gcs_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections#Gcs | Create gcs collection
[**delete_collection**](CollectionsApi.md#delete_collection) | **DELETE** /v1/orgs/self/ws/{workspace}/collections/{collection} | Delete Collection
[**get_collection**](CollectionsApi.md#get_collection) | **GET** /v1/orgs/self/ws/{workspace}/collections/{collection} | Retrieve Collection
[**list_collections**](CollectionsApi.md#list_collections) | **GET** /v1/orgs/self/collections | List Collections
[**workspace_collections**](CollectionsApi.md#workspace_collections) | **GET** /v1/orgs/self/ws/{workspace}/collections | List Collections in Workspace


# **create_azure_blob_collection**
> CreateCollectionResponse create_azure_blob_collection(azure_blob_collection_creation_request)

Create azure blob collection

Create new collection in a workspace.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset.api import collections_api
from rockset.model.create_collection_response import CreateCollectionResponse
from rockset.model.error_model import ErrorModel
from rockset.model.azure_blob_collection_creation_request import AzureBlobCollectionCreationRequest
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
    api_instance = collections_api.CollectionsApi(api_client)
    azure_blob_collection_creation_request = AzureBlobCollectionCreationRequest(
        clustering_key=[
            FieldPartition(
                field_name="address.city.zipcode",
                keys=[
                    "Values of a record to partition on. This is not needed if the partition type is AUTO",
                ],
                type="AUTO",
            ),
        ],
        description="transactions from stores worldwide",
        event_time_info=EventTimeInfo(
            field="timestamp",
            format="seconds_since_epoch",
            time_zone="UTC",
        ),
        field_mapping_query=FieldMappingQuery(
            sql="sql",
        ),
        field_mappings=[
            FieldMappingV2(
                input_fields=[
                    InputField(
                        field_name="address.city.zipcode",
                        if_missing="['SKIP', 'PASS']",
                        is_drop=True,
                        param="zip",
                    ),
                ],
                is_drop_all_fields=True,
                name="myTestMapping",
                output_field=OutputField(
                    field_name="zip_hash",
                    on_error="['SKIP', 'FAIL']",
                    value=SqlExpression(
                        sql="SHA256()",
                    ),
                ),
            ),
        ],
        field_schemas=[
            FieldSchema(
                field_name="address.city.zipcode",
                field_options=FieldOptions(
                    column_index_mode="store",
                    index_mode="index",
                    range_index_mode="v1_index",
                    type_index_mode="index",
                ),
            ),
        ],
        insert_only=True,
        inverted_index_group_encoding_options=InvertedIndexGroupEncodingOptions(
            doc_id_codec="doc_id_codec_example",
            event_time_codec="event_time_codec_example",
            format_version=1,
            group_size=1,
            restart_length=1,
        ),
        name="global-transactions",
        retention_secs=1000000,
        sources=[
            AzureBlobStorageSourceWrapper(None),
        ],
        time_partition_resolution_secs=1,
    ) # AzureBlobCollectionCreationRequest | JSON object

    # example passing only required values which don't have defaults set
    try:
        # Create azure blob collection
        api_response = api_instance.create_azure_blob_collection(azure_blob_collection_creation_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling CollectionsApi->create_azure_blob_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_blob_collection_creation_request** | [**AzureBlobCollectionCreationRequest**](AzureBlobCollectionCreationRequest.md)| JSON object |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**CreateCollectionResponse**](CreateCollectionResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | collection created successfully |  -  |
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

# **create_gcs_collection**
> CreateCollectionResponse create_gcs_collection(gcs_collection_creation_request)

Create gcs collection

Create new collection in a workspace.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset.api import collections_api
from rockset.model.create_collection_response import CreateCollectionResponse
from rockset.model.error_model import ErrorModel
from rockset.model.gcs_collection_creation_request import GcsCollectionCreationRequest
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
    api_instance = collections_api.CollectionsApi(api_client)
    gcs_collection_creation_request = GcsCollectionCreationRequest(
        clustering_key=[
            FieldPartition(
                field_name="address.city.zipcode",
                keys=[
                    "Values of a record to partition on. This is not needed if the partition type is AUTO",
                ],
                type="AUTO",
            ),
        ],
        description="transactions from stores worldwide",
        event_time_info=EventTimeInfo(
            field="timestamp",
            format="seconds_since_epoch",
            time_zone="UTC",
        ),
        field_mapping_query=FieldMappingQuery(
            sql="sql",
        ),
        field_mappings=[
            FieldMappingV2(
                input_fields=[
                    InputField(
                        field_name="address.city.zipcode",
                        if_missing="['SKIP', 'PASS']",
                        is_drop=True,
                        param="zip",
                    ),
                ],
                is_drop_all_fields=True,
                name="myTestMapping",
                output_field=OutputField(
                    field_name="zip_hash",
                    on_error="['SKIP', 'FAIL']",
                    value=SqlExpression(
                        sql="SHA256()",
                    ),
                ),
            ),
        ],
        field_schemas=[
            FieldSchema(
                field_name="address.city.zipcode",
                field_options=FieldOptions(
                    column_index_mode="store",
                    index_mode="index",
                    range_index_mode="v1_index",
                    type_index_mode="index",
                ),
            ),
        ],
        insert_only=True,
        inverted_index_group_encoding_options=InvertedIndexGroupEncodingOptions(
            doc_id_codec="doc_id_codec_example",
            event_time_codec="event_time_codec_example",
            format_version=1,
            group_size=1,
            restart_length=1,
        ),
        name="global-transactions",
        retention_secs=1000000,
        sources=[
            GcsSourceWrapper(None),
        ],
        time_partition_resolution_secs=1,
    ) # GcsCollectionCreationRequest | JSON object

    # example passing only required values which don't have defaults set
    try:
        # Create gcs collection
        api_response = api_instance.create_gcs_collection(gcs_collection_creation_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling CollectionsApi->create_gcs_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcs_collection_creation_request** | [**GcsCollectionCreationRequest**](GcsCollectionCreationRequest.md)| JSON object |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**CreateCollectionResponse**](CreateCollectionResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | collection created successfully |  -  |
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

# **delete_collection**
> DeleteCollectionResponse delete_collection(collection)

Delete Collection

Delete a collection and all its documents from Rockset.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset.api import collections_api
from rockset.model.delete_collection_response import DeleteCollectionResponse
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
    api_instance = collections_api.CollectionsApi(api_client)
    collection = "collection_example" # str | name of the collection

    # example passing only required values which don't have defaults set
    try:
        # Delete Collection
        api_response = api_instance.delete_collection(collection)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling CollectionsApi->delete_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| name of the collection |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**DeleteCollectionResponse**](DeleteCollectionResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | collection deleted successfully |  -  |
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

# **get_collection**
> GetCollectionResponse get_collection(collection)

Retrieve Collection

Get details about a collection.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset.api import collections_api
from rockset.model.error_model import ErrorModel
from rockset.model.get_collection_response import GetCollectionResponse
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
    api_instance = collections_api.CollectionsApi(api_client)
    collection = "collection_example" # str | name of the collection

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Collection
        api_response = api_instance.get_collection(collection)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling CollectionsApi->get_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| name of the collection |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**GetCollectionResponse**](GetCollectionResponse.md)

### Authorization

[apikey](../README.md#apikey)

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

# **list_collections**
> ListCollectionsResponse list_collections()

List Collections

Retrieve all collections in an organization.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset.api import collections_api
from rockset.model.error_model import ErrorModel
from rockset.model.list_collections_response import ListCollectionsResponse
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
    api_instance = collections_api.CollectionsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Collections
        api_response = api_instance.list_collections()
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling CollectionsApi->list_collections: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListCollectionsResponse**](ListCollectionsResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | collections retrieved successfully |  -  |
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

# **workspace_collections**
> ListCollectionsResponse workspace_collections()

List Collections in Workspace

Retrieve all collections in a workspace.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset.api import collections_api
from rockset.model.error_model import ErrorModel
from rockset.model.list_collections_response import ListCollectionsResponse
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
    api_instance = collections_api.CollectionsApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # List Collections in Workspace
        api_response = api_instance.workspace_collections()
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling CollectionsApi->workspace_collections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**ListCollectionsResponse**](ListCollectionsResponse.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | collections retrieved successfully |  -  |
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

