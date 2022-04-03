# rockset.CollectionsApi

All URIs are relative to *https://api.rs2.usw2.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_azure_blob_storage_collection**](CollectionsApi.md#create_azure_blob_storage_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create azure blob storage collection
[**create_azure_event_hubs_collection**](CollectionsApi.md#create_azure_event_hubs_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create azure event hubs collection
[**create_azure_service_bus_collection**](CollectionsApi.md#create_azure_service_bus_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create azure service bus collection
[**create_dynamodb_collection**](CollectionsApi.md#create_dynamodb_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create dynamodb collection
[**create_file_upload_collection**](CollectionsApi.md#create_file_upload_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create file upload collection
[**create_gcs_collection**](CollectionsApi.md#create_gcs_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create gcs collection
[**create_kafka_collection**](CollectionsApi.md#create_kafka_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create kafka collection
[**create_kinesis_collection**](CollectionsApi.md#create_kinesis_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create kinesis collection
[**create_mongodb_collection**](CollectionsApi.md#create_mongodb_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create mongodb collection
[**create_s3_collection**](CollectionsApi.md#create_s3_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create s3 collection
[**delete_collection**](CollectionsApi.md#delete_collection) | **DELETE** /v1/orgs/self/ws/{workspace}/collections/{collection} | Delete Collection
[**get_collection**](CollectionsApi.md#get_collection) | **GET** /v1/orgs/self/ws/{workspace}/collections/{collection} | Retrieve Collection
[**list_collections**](CollectionsApi.md#list_collections) | **GET** /v1/orgs/self/collections | List Collections
[**workspace_collections**](CollectionsApi.md#workspace_collections) | **GET** /v1/orgs/self/ws/{workspace}/collections | List Collections in Workspace


# **create_azure_blob_storage_collection**
> CreateCollectionResponse create_azure_blob_storage_collection(azure_blob_storage_collection_creation_request)

Create azure blob storage collection

Create new collection in a workspace.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.create_collection_response import CreateCollectionResponse
from rockset.model.error_model import ErrorModel
from rockset.model.azure_blob_storage_collection_creation_request import AzureBlobStorageCollectionCreationRequest
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Create azure blob storage collection
    api_response = rs.CollectionsApi.create_azure_blob_storage_collection(
        name="global-transactions",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CollectionsApi->create_azure_blob_storage_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create azure blob storage collection
    api_response = await rs.CollectionsApi.create_azure_blob_storage_collection(
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
        AzureBlobStorageSourceWrapper(
            azure_blob_storage=SourceAzureBlobStorage(
                container="server-logs",
                pattern="prefix/to/**/keys/*.format",
                prefix="prefix/to/blobs",
            ),
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
        ),
    ],
        time_partition_resolution_secs=1,
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CollectionsApi->create_azure_blob_storage_collection: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | list of clustering fields | [optional]
 **description** | **str** | text describing the collection | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **field_mappings** | [**[FieldMappingV2]**](FieldMappingV2.md) | list of mappings | [optional]
 **field_schemas** | [**[FieldSchema]**](FieldSchema.md) | list of field schemas | [optional]
 **insert_only** | **bool** | If true disallows updates and deletes, but makes indexing more efficient | [optional]
 **inverted_index_group_encoding_options** | [**InvertedIndexGroupEncodingOptions**](InvertedIndexGroupEncodingOptions.md) |  | [optional]
 **name** | **str** | unique identifier for collection, can contain alphanumeric or dash characters | 
 **retention_secs** | **int** | number of seconds after which data is purged, based on event time | [optional]
 **sources** | [**[AzureBlobStorageSourceWrapper]**](AzureBlobStorageSourceWrapper.md) | List of sources from which to ingest data | [optional]
 **time_partition_resolution_secs** | **int** | If non-null, the collection will be time partitioned and each partition will be time_partition_resolution_secs wide. | [optional]
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**CreateCollectionResponse**](CreateCollectionResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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

# **create_azure_event_hubs_collection**
> CreateCollectionResponse create_azure_event_hubs_collection(azure_event_hubs_collection_creation_request)

Create azure event hubs collection

Create new collection in a workspace.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.create_collection_response import CreateCollectionResponse
from rockset.model.error_model import ErrorModel
from rockset.model.azure_event_hubs_collection_creation_request import AzureEventHubsCollectionCreationRequest
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Create azure event hubs collection
    api_response = rs.CollectionsApi.create_azure_event_hubs_collection(
        name="global-transactions",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CollectionsApi->create_azure_event_hubs_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create azure event hubs collection
    api_response = await rs.CollectionsApi.create_azure_event_hubs_collection(
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
        AzureEventHubsSourceWrapper(
            azure_event_hubs=SourceAzureEventHubs(
                hub_id="event-hub-1",
                offset_reset_policy="EARLIEST",
            ),
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
        ),
    ],
        time_partition_resolution_secs=1,
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CollectionsApi->create_azure_event_hubs_collection: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | list of clustering fields | [optional]
 **description** | **str** | text describing the collection | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **field_mappings** | [**[FieldMappingV2]**](FieldMappingV2.md) | list of mappings | [optional]
 **field_schemas** | [**[FieldSchema]**](FieldSchema.md) | list of field schemas | [optional]
 **insert_only** | **bool** | If true disallows updates and deletes, but makes indexing more efficient | [optional]
 **inverted_index_group_encoding_options** | [**InvertedIndexGroupEncodingOptions**](InvertedIndexGroupEncodingOptions.md) |  | [optional]
 **name** | **str** | unique identifier for collection, can contain alphanumeric or dash characters | 
 **retention_secs** | **int** | number of seconds after which data is purged, based on event time | [optional]
 **sources** | [**[AzureEventHubsSourceWrapper]**](AzureEventHubsSourceWrapper.md) | List of sources from which to ingest data | [optional]
 **time_partition_resolution_secs** | **int** | If non-null, the collection will be time partitioned and each partition will be time_partition_resolution_secs wide. | [optional]
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**CreateCollectionResponse**](CreateCollectionResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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

# **create_azure_service_bus_collection**
> CreateCollectionResponse create_azure_service_bus_collection(azure_service_bus_collection_creation_request)

Create azure service bus collection

Create new collection in a workspace.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.create_collection_response import CreateCollectionResponse
from rockset.model.error_model import ErrorModel
from rockset.model.azure_service_bus_collection_creation_request import AzureServiceBusCollectionCreationRequest
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Create azure service bus collection
    api_response = rs.CollectionsApi.create_azure_service_bus_collection(
        name="global-transactions",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CollectionsApi->create_azure_service_bus_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create azure service bus collection
    api_response = await rs.CollectionsApi.create_azure_service_bus_collection(
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
        AzureServiceBusSourceWrapper(
            azure_service_bus=SourceAzureServiceBus(
                subscription="rockset-subscription",
                topic="rockset-topic",
            ),
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
        ),
    ],
        time_partition_resolution_secs=1,
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CollectionsApi->create_azure_service_bus_collection: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | list of clustering fields | [optional]
 **description** | **str** | text describing the collection | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **field_mappings** | [**[FieldMappingV2]**](FieldMappingV2.md) | list of mappings | [optional]
 **field_schemas** | [**[FieldSchema]**](FieldSchema.md) | list of field schemas | [optional]
 **insert_only** | **bool** | If true disallows updates and deletes, but makes indexing more efficient | [optional]
 **inverted_index_group_encoding_options** | [**InvertedIndexGroupEncodingOptions**](InvertedIndexGroupEncodingOptions.md) |  | [optional]
 **name** | **str** | unique identifier for collection, can contain alphanumeric or dash characters | 
 **retention_secs** | **int** | number of seconds after which data is purged, based on event time | [optional]
 **sources** | [**[AzureServiceBusSourceWrapper]**](AzureServiceBusSourceWrapper.md) | List of sources from which to ingest data | [optional]
 **time_partition_resolution_secs** | **int** | If non-null, the collection will be time partitioned and each partition will be time_partition_resolution_secs wide. | [optional]
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**CreateCollectionResponse**](CreateCollectionResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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

# **create_dynamodb_collection**
> CreateCollectionResponse create_dynamodb_collection(dynamodb_collection_creation_request)

Create dynamodb collection

Create new collection in a workspace.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.create_collection_response import CreateCollectionResponse
from rockset.model.error_model import ErrorModel
from rockset.model.dynamodb_collection_creation_request import DynamodbCollectionCreationRequest
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Create dynamodb collection
    api_response = rs.CollectionsApi.create_dynamodb_collection(
        name="global-transactions",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CollectionsApi->create_dynamodb_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create dynamodb collection
    api_response = await rs.CollectionsApi.create_dynamodb_collection(
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
        DynamodbSourceWrapper(
            dynamodb=SourceDynamoDb(
                aws_region="us-east-2",
                rcu=1000,
                table_name="dynamodb_table_name",
                use_scan_api=True,
            ),
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
        ),
    ],
        time_partition_resolution_secs=1,
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CollectionsApi->create_dynamodb_collection: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | list of clustering fields | [optional]
 **description** | **str** | text describing the collection | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **field_mappings** | [**[FieldMappingV2]**](FieldMappingV2.md) | list of mappings | [optional]
 **field_schemas** | [**[FieldSchema]**](FieldSchema.md) | list of field schemas | [optional]
 **insert_only** | **bool** | If true disallows updates and deletes, but makes indexing more efficient | [optional]
 **inverted_index_group_encoding_options** | [**InvertedIndexGroupEncodingOptions**](InvertedIndexGroupEncodingOptions.md) |  | [optional]
 **name** | **str** | unique identifier for collection, can contain alphanumeric or dash characters | 
 **retention_secs** | **int** | number of seconds after which data is purged, based on event time | [optional]
 **sources** | [**[DynamodbSourceWrapper]**](DynamodbSourceWrapper.md) | List of sources from which to ingest data | [optional]
 **time_partition_resolution_secs** | **int** | If non-null, the collection will be time partitioned and each partition will be time_partition_resolution_secs wide. | [optional]
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**CreateCollectionResponse**](CreateCollectionResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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

# **create_file_upload_collection**
> CreateCollectionResponse create_file_upload_collection(file_upload_collection_creation_request)

Create file upload collection

Create new collection in a workspace.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.create_collection_response import CreateCollectionResponse
from rockset.model.error_model import ErrorModel
from rockset.model.file_upload_collection_creation_request import FileUploadCollectionCreationRequest
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Create file upload collection
    api_response = rs.CollectionsApi.create_file_upload_collection(
        name="global-transactions",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CollectionsApi->create_file_upload_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create file upload collection
    api_response = await rs.CollectionsApi.create_file_upload_collection(
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
        FileUploadSourceWrapper(
            file_upload=SourceFileUpload(
                file_name="file1.json",
                file_size=12345,
                file_upload_time="2019-01-15T21:48:23Z",
            ),
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
        ),
    ],
        time_partition_resolution_secs=1,
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CollectionsApi->create_file_upload_collection: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | list of clustering fields | [optional]
 **description** | **str** | text describing the collection | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **field_mappings** | [**[FieldMappingV2]**](FieldMappingV2.md) | list of mappings | [optional]
 **field_schemas** | [**[FieldSchema]**](FieldSchema.md) | list of field schemas | [optional]
 **insert_only** | **bool** | If true disallows updates and deletes, but makes indexing more efficient | [optional]
 **inverted_index_group_encoding_options** | [**InvertedIndexGroupEncodingOptions**](InvertedIndexGroupEncodingOptions.md) |  | [optional]
 **name** | **str** | unique identifier for collection, can contain alphanumeric or dash characters | 
 **retention_secs** | **int** | number of seconds after which data is purged, based on event time | [optional]
 **sources** | [**[FileUploadSourceWrapper]**](FileUploadSourceWrapper.md) | List of sources from which to ingest data | [optional]
 **time_partition_resolution_secs** | **int** | If non-null, the collection will be time partitioned and each partition will be time_partition_resolution_secs wide. | [optional]
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**CreateCollectionResponse**](CreateCollectionResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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
from rockset import RocksetClient
from rockset.model.create_collection_response import CreateCollectionResponse
from rockset.model.error_model import ErrorModel
from rockset.model.gcs_collection_creation_request import GcsCollectionCreationRequest
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Create gcs collection
    api_response = rs.CollectionsApi.create_gcs_collection(
        name="global-transactions",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CollectionsApi->create_gcs_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create gcs collection
    api_response = await rs.CollectionsApi.create_gcs_collection(
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
        GcsSourceWrapper(
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
            gcs=SourceGcs(
                bucket="server-logs",
                pattern="prefix/to/**/keys/*.format",
                prefix="prefix/to/keys",
            ),
            integration_name="aws-integration",
        ),
    ],
        time_partition_resolution_secs=1,
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CollectionsApi->create_gcs_collection: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | list of clustering fields | [optional]
 **description** | **str** | text describing the collection | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **field_mappings** | [**[FieldMappingV2]**](FieldMappingV2.md) | list of mappings | [optional]
 **field_schemas** | [**[FieldSchema]**](FieldSchema.md) | list of field schemas | [optional]
 **insert_only** | **bool** | If true disallows updates and deletes, but makes indexing more efficient | [optional]
 **inverted_index_group_encoding_options** | [**InvertedIndexGroupEncodingOptions**](InvertedIndexGroupEncodingOptions.md) |  | [optional]
 **name** | **str** | unique identifier for collection, can contain alphanumeric or dash characters | 
 **retention_secs** | **int** | number of seconds after which data is purged, based on event time | [optional]
 **sources** | [**[GcsSourceWrapper]**](GcsSourceWrapper.md) | List of sources from which to ingest data | [optional]
 **time_partition_resolution_secs** | **int** | If non-null, the collection will be time partitioned and each partition will be time_partition_resolution_secs wide. | [optional]
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**CreateCollectionResponse**](CreateCollectionResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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

# **create_kafka_collection**
> CreateCollectionResponse create_kafka_collection(kafka_collection_creation_request)

Create kafka collection

Create new collection in a workspace.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.create_collection_response import CreateCollectionResponse
from rockset.model.kafka_collection_creation_request import KafkaCollectionCreationRequest
from rockset.model.error_model import ErrorModel
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Create kafka collection
    api_response = rs.CollectionsApi.create_kafka_collection(
        name="global-transactions",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CollectionsApi->create_kafka_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create kafka collection
    api_response = await rs.CollectionsApi.create_kafka_collection(
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
        KafkaSourceWrapper(
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
            kafka=SourceKafka(
                kafka_topic_name="example-topic",
                offset_reset_policy="LATEST",
                use_v3=True,
            ),
        ),
    ],
        time_partition_resolution_secs=1,
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CollectionsApi->create_kafka_collection: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | list of clustering fields | [optional]
 **description** | **str** | text describing the collection | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **field_mappings** | [**[FieldMappingV2]**](FieldMappingV2.md) | list of mappings | [optional]
 **field_schemas** | [**[FieldSchema]**](FieldSchema.md) | list of field schemas | [optional]
 **insert_only** | **bool** | If true disallows updates and deletes, but makes indexing more efficient | [optional]
 **inverted_index_group_encoding_options** | [**InvertedIndexGroupEncodingOptions**](InvertedIndexGroupEncodingOptions.md) |  | [optional]
 **name** | **str** | unique identifier for collection, can contain alphanumeric or dash characters | 
 **retention_secs** | **int** | number of seconds after which data is purged, based on event time | [optional]
 **sources** | [**[KafkaSourceWrapper]**](KafkaSourceWrapper.md) | List of sources from which to ingest data | [optional]
 **time_partition_resolution_secs** | **int** | If non-null, the collection will be time partitioned and each partition will be time_partition_resolution_secs wide. | [optional]
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**CreateCollectionResponse**](CreateCollectionResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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

# **create_kinesis_collection**
> CreateCollectionResponse create_kinesis_collection(kinesis_collection_creation_request)

Create kinesis collection

Create new collection in a workspace.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.create_collection_response import CreateCollectionResponse
from rockset.model.error_model import ErrorModel
from rockset.model.kinesis_collection_creation_request import KinesisCollectionCreationRequest
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Create kinesis collection
    api_response = rs.CollectionsApi.create_kinesis_collection(
        name="global-transactions",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CollectionsApi->create_kinesis_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create kinesis collection
    api_response = await rs.CollectionsApi.create_kinesis_collection(
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
        KinesisStorageSourceWrapper(
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
            kinesis=SourceKinesis(
                aws_region="us-east-2",
                dms_primary_key=[
                    "dms_primary_key_example",
                ],
                offset_reset_policy="EARLIEST",
                stream_name="click_stream",
            ),
        ),
    ],
        time_partition_resolution_secs=1,
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CollectionsApi->create_kinesis_collection: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | list of clustering fields | [optional]
 **description** | **str** | text describing the collection | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **field_mappings** | [**[FieldMappingV2]**](FieldMappingV2.md) | list of mappings | [optional]
 **field_schemas** | [**[FieldSchema]**](FieldSchema.md) | list of field schemas | [optional]
 **insert_only** | **bool** | If true disallows updates and deletes, but makes indexing more efficient | [optional]
 **inverted_index_group_encoding_options** | [**InvertedIndexGroupEncodingOptions**](InvertedIndexGroupEncodingOptions.md) |  | [optional]
 **name** | **str** | unique identifier for collection, can contain alphanumeric or dash characters | 
 **retention_secs** | **int** | number of seconds after which data is purged, based on event time | [optional]
 **sources** | [**[KinesisStorageSourceWrapper]**](KinesisStorageSourceWrapper.md) | List of sources from which to ingest data | [optional]
 **time_partition_resolution_secs** | **int** | If non-null, the collection will be time partitioned and each partition will be time_partition_resolution_secs wide. | [optional]
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**CreateCollectionResponse**](CreateCollectionResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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

# **create_mongodb_collection**
> CreateCollectionResponse create_mongodb_collection(mongodb_collection_creation_request)

Create mongodb collection

Create new collection in a workspace.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.create_collection_response import CreateCollectionResponse
from rockset.model.error_model import ErrorModel
from rockset.model.mongodb_collection_creation_request import MongodbCollectionCreationRequest
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Create mongodb collection
    api_response = rs.CollectionsApi.create_mongodb_collection(
        name="global-transactions",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CollectionsApi->create_mongodb_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create mongodb collection
    api_response = await rs.CollectionsApi.create_mongodb_collection(
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
        MongodbSourceWrapper(
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
            mongodb=SourceMongoDb(
                collection_name="my_collection",
                database_name="my_database",
            ),
        ),
    ],
        time_partition_resolution_secs=1,
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CollectionsApi->create_mongodb_collection: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | list of clustering fields | [optional]
 **description** | **str** | text describing the collection | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **field_mappings** | [**[FieldMappingV2]**](FieldMappingV2.md) | list of mappings | [optional]
 **field_schemas** | [**[FieldSchema]**](FieldSchema.md) | list of field schemas | [optional]
 **insert_only** | **bool** | If true disallows updates and deletes, but makes indexing more efficient | [optional]
 **inverted_index_group_encoding_options** | [**InvertedIndexGroupEncodingOptions**](InvertedIndexGroupEncodingOptions.md) |  | [optional]
 **name** | **str** | unique identifier for collection, can contain alphanumeric or dash characters | 
 **retention_secs** | **int** | number of seconds after which data is purged, based on event time | [optional]
 **sources** | [**[MongodbSourceWrapper]**](MongodbSourceWrapper.md) | List of sources from which to ingest data | [optional]
 **time_partition_resolution_secs** | **int** | If non-null, the collection will be time partitioned and each partition will be time_partition_resolution_secs wide. | [optional]
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**CreateCollectionResponse**](CreateCollectionResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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

# **create_s3_collection**
> CreateCollectionResponse create_s3_collection(s3_collection_creation_request)

Create s3 collection

Create new collection in a workspace.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.create_collection_response import CreateCollectionResponse
from rockset.model.error_model import ErrorModel
from rockset.model.s3_collection_creation_request import S3CollectionCreationRequest
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Create s3 collection
    api_response = rs.CollectionsApi.create_s3_collection(
        name="global-transactions",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CollectionsApi->create_s3_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create s3 collection
    api_response = await rs.CollectionsApi.create_s3_collection(
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
        S3SourceWrapper(
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
            s3=SourceS3(
                bucket="s3://customer-account-info",
                format="none",
                mappings=[
                    FieldMask(
                        input_path=[
                            "input_path_example",
                        ],
                        mask=FieldMaskMask(
                            args={},
                            name="name_example",
                        ),
                    ),
                ],
                pattern="prefix/to/**/keys/*.format",
                prefix="prefix/to/keys",
                region="us-west-2",
            ),
        ),
    ],
        time_partition_resolution_secs=1,
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CollectionsApi->create_s3_collection: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | list of clustering fields | [optional]
 **description** | **str** | text describing the collection | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **field_mappings** | [**[FieldMappingV2]**](FieldMappingV2.md) | list of mappings | [optional]
 **field_schemas** | [**[FieldSchema]**](FieldSchema.md) | list of field schemas | [optional]
 **insert_only** | **bool** | If true disallows updates and deletes, but makes indexing more efficient | [optional]
 **inverted_index_group_encoding_options** | [**InvertedIndexGroupEncodingOptions**](InvertedIndexGroupEncodingOptions.md) |  | [optional]
 **name** | **str** | unique identifier for collection, can contain alphanumeric or dash characters | 
 **retention_secs** | **int** | number of seconds after which data is purged, based on event time | [optional]
 **sources** | [**[S3SourceWrapper]**](S3SourceWrapper.md) | List of sources from which to ingest data | [optional]
 **time_partition_resolution_secs** | **int** | If non-null, the collection will be time partitioned and each partition will be time_partition_resolution_secs wide. | [optional]
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**CreateCollectionResponse**](CreateCollectionResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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
from rockset import RocksetClient
from rockset.model.delete_collection_response import DeleteCollectionResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Delete Collection
    api_response = rs.CollectionsApi.delete_collection(
        collection="collection_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CollectionsApi->delete_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Delete Collection
    api_response = await rs.CollectionsApi.delete_collection(
        collection="collection_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CollectionsApi->delete_collection: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**DeleteCollectionResponse**](DeleteCollectionResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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
from rockset import RocksetClient
from rockset.model.error_model import ErrorModel
from rockset.model.get_collection_response import GetCollectionResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Retrieve Collection
    api_response = rs.CollectionsApi.get_collection(
        collection="collection_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CollectionsApi->get_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Retrieve Collection
    api_response = await rs.CollectionsApi.get_collection(
        collection="collection_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CollectionsApi->get_collection: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**GetCollectionResponse**](GetCollectionResponse.md)

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

# **list_collections**
> ListCollectionsResponse list_collections()

List Collections

Retrieve all collections in an organization.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.error_model import ErrorModel
from rockset.model.list_collections_response import ListCollectionsResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # List Collections
    api_response = rs.CollectionsApi.list_collections(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CollectionsApi->list_collections: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # List Collections
    api_response = await rs.CollectionsApi.list_collections(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CollectionsApi->list_collections: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListCollectionsResponse**](ListCollectionsResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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
from rockset import RocksetClient
from rockset.model.error_model import ErrorModel
from rockset.model.list_collections_response import ListCollectionsResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # List Collections in Workspace
    api_response = rs.CollectionsApi.workspace_collections(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling CollectionsApi->workspace_collections: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # List Collections in Workspace
    api_response = await rs.CollectionsApi.workspace_collections(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling CollectionsApi->workspace_collections: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**ListCollectionsResponse**](ListCollectionsResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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

