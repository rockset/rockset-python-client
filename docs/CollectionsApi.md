# rockset.Collections

All URIs are relative to *https://api.use1a1.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_azure_blob_storage_collection**](CollectionsApi.md#create_azure_blob_storage_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create azure blob storage collection
[**create_azure_event_hubs_collection**](CollectionsApi.md#create_azure_event_hubs_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create azure event hubs collection
[**create_dynamodb_collection**](CollectionsApi.md#create_dynamodb_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create dynamodb collection
[**create_gcs_collection**](CollectionsApi.md#create_gcs_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create gcs collection
[**create_kafka_collection**](CollectionsApi.md#create_kafka_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create kafka collection
[**create_kinesis_collection**](CollectionsApi.md#create_kinesis_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create kinesis collection
[**create_mongodb_collection**](CollectionsApi.md#create_mongodb_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create mongodb collection
[**create_s3_collection**](CollectionsApi.md#create_s3_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create s3 collection
[**create_snowflake_collection**](CollectionsApi.md#create_snowflake_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections | Create snowflake collection
[**delete**](CollectionsApi.md#delete) | **DELETE** /v1/orgs/self/ws/{workspace}/collections/{collection} | Delete Collection
[**get**](CollectionsApi.md#get) | **GET** /v1/orgs/self/ws/{workspace}/collections/{collection} | Retrieve Collection
[**get_collection_offsets**](CollectionsApi.md#get_collection_offsets) | **POST** /v1/orgs/self/ws/{workspace}/collections/{collection}/offsets/commit | Get Collection Commit
[**list**](CollectionsApi.md#list) | **GET** /v1/orgs/self/collections | List Collections
[**update**](CollectionsApi.md#update) | **PUT** /v1/orgs/self/ws/{workspace}/collections/{collection} | Update Collection
[**workspace_collections**](CollectionsApi.md#workspace_collections) | **GET** /v1/orgs/self/ws/{workspace}/collections | List Collections in Workspace


# **create_azure_blob_storage_collection**
> CreateCollectionResponse create_azure_blob_storage_collection(azure_blob_storage_collection_creation_request)

Create azure blob storage collection

Create new collection in a workspace.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create azure blob storage collection
api_response = rs.Collections.create_azure_blob_storage_collection(
    name="global-transactions",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Collections->create_azure_blob_storage_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create azure blob storage collection
api_response = await rs.Collections.create_azure_blob_storage_collection(
    clustering_key=[
        FieldPartition(
            field_name="address.city.zipcode",
            keys=["value1","value2"],
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
    name="global-transactions",
    retention_secs=1000000,
    source_download_soft_limit_bytes=1,
    sources=[
        AzureBlobStorageSourceWrapper(
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
            container="server-logs",
            pattern="prefix/to/**/keys/*.format",
            prefix="prefix/to/blobs",
        ),
    ],
    storage_compression_type="LZ4",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Collections->create_azure_blob_storage_collection: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | Deprecated. List of clustering fields. Use CLUSTER BY clause in &#x60;field_mapping_query&#x60; instead. | [optional]
 **description** | **str** | Text describing the collection. | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **name** | **str** | Unique identifier for collection, can contain alphanumeric or dash characters. | 
 **retention_secs** | **int** | Number of seconds after which data is purged, based on event time. | [optional]
 **source_download_soft_limit_bytes** | **int** | Soft ingest limit for this collection. | [optional]
 **sources** | [**[AzureBlobStorageSourceWrapper]**](AzureBlobStorageSourceWrapper.md) | List of sources from which to ingest data | [optional]
 **storage_compression_type** | **str** | RocksDB storage compression type. | [optional]
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
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create azure event hubs collection
api_response = rs.Collections.create_azure_event_hubs_collection(
    name="global-transactions",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Collections->create_azure_event_hubs_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create azure event hubs collection
api_response = await rs.Collections.create_azure_event_hubs_collection(
    clustering_key=[
        FieldPartition(
            field_name="address.city.zipcode",
            keys=["value1","value2"],
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
    name="global-transactions",
    retention_secs=1000000,
    source_download_soft_limit_bytes=1,
    sources=[
        AzureEventHubsSourceWrapper(
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
            hub_id="event-hub-1",
            offset_reset_policy="EARLIEST",
        ),
    ],
    storage_compression_type="LZ4",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Collections->create_azure_event_hubs_collection: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | Deprecated. List of clustering fields. Use CLUSTER BY clause in &#x60;field_mapping_query&#x60; instead. | [optional]
 **description** | **str** | Text describing the collection. | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **name** | **str** | Unique identifier for collection, can contain alphanumeric or dash characters. | 
 **retention_secs** | **int** | Number of seconds after which data is purged, based on event time. | [optional]
 **source_download_soft_limit_bytes** | **int** | Soft ingest limit for this collection. | [optional]
 **sources** | [**[AzureEventHubsSourceWrapper]**](AzureEventHubsSourceWrapper.md) | List of sources from which to ingest data | [optional]
 **storage_compression_type** | **str** | RocksDB storage compression type. | [optional]
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
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create dynamodb collection
api_response = rs.Collections.create_dynamodb_collection(
    name="global-transactions",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Collections->create_dynamodb_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create dynamodb collection
api_response = await rs.Collections.create_dynamodb_collection(
    clustering_key=[
        FieldPartition(
            field_name="address.city.zipcode",
            keys=["value1","value2"],
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
    name="global-transactions",
    retention_secs=1000000,
    source_download_soft_limit_bytes=1,
    sources=[
        DynamodbSourceWrapper(
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
            aws_region="us-east-2",
            rcu=1000,
            table_name="dynamodb_table_name",
            use_scan_api=True,
        ),
    ],
    storage_compression_type="LZ4",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Collections->create_dynamodb_collection: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | Deprecated. List of clustering fields. Use CLUSTER BY clause in &#x60;field_mapping_query&#x60; instead. | [optional]
 **description** | **str** | Text describing the collection. | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **name** | **str** | Unique identifier for collection, can contain alphanumeric or dash characters. | 
 **retention_secs** | **int** | Number of seconds after which data is purged, based on event time. | [optional]
 **source_download_soft_limit_bytes** | **int** | Soft ingest limit for this collection. | [optional]
 **sources** | [**[DynamodbSourceWrapper]**](DynamodbSourceWrapper.md) | List of sources from which to ingest data | [optional]
 **storage_compression_type** | **str** | RocksDB storage compression type. | [optional]
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
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create gcs collection
api_response = rs.Collections.create_gcs_collection(
    name="global-transactions",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Collections->create_gcs_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create gcs collection
api_response = await rs.Collections.create_gcs_collection(
    clustering_key=[
        FieldPartition(
            field_name="address.city.zipcode",
            keys=["value1","value2"],
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
    name="global-transactions",
    retention_secs=1000000,
    source_download_soft_limit_bytes=1,
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
            integration_name="aws-integration",
            bucket="server-logs",
            pattern="prefix/to/**/keys/*.format",
            prefix="prefix/to/keys",
        ),
    ],
    storage_compression_type="LZ4",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Collections->create_gcs_collection: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | Deprecated. List of clustering fields. Use CLUSTER BY clause in &#x60;field_mapping_query&#x60; instead. | [optional]
 **description** | **str** | Text describing the collection. | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **name** | **str** | Unique identifier for collection, can contain alphanumeric or dash characters. | 
 **retention_secs** | **int** | Number of seconds after which data is purged, based on event time. | [optional]
 **source_download_soft_limit_bytes** | **int** | Soft ingest limit for this collection. | [optional]
 **sources** | [**[GcsSourceWrapper]**](GcsSourceWrapper.md) | List of sources from which to ingest data | [optional]
 **storage_compression_type** | **str** | RocksDB storage compression type. | [optional]
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
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create kafka collection
api_response = rs.Collections.create_kafka_collection(
    name="global-transactions",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Collections->create_kafka_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create kafka collection
api_response = await rs.Collections.create_kafka_collection(
    clustering_key=[
        FieldPartition(
            field_name="address.city.zipcode",
            keys=["value1","value2"],
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
    name="global-transactions",
    retention_secs=1000000,
    source_download_soft_limit_bytes=1,
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
            consumer_group_id="org-collection",
            kafka_topic_name="example-topic",
            offset_reset_policy="EARLIEST",
            use_v3=True,
        ),
    ],
    storage_compression_type="LZ4",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Collections->create_kafka_collection: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | Deprecated. List of clustering fields. Use CLUSTER BY clause in &#x60;field_mapping_query&#x60; instead. | [optional]
 **description** | **str** | Text describing the collection. | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **name** | **str** | Unique identifier for collection, can contain alphanumeric or dash characters. | 
 **retention_secs** | **int** | Number of seconds after which data is purged, based on event time. | [optional]
 **source_download_soft_limit_bytes** | **int** | Soft ingest limit for this collection. | [optional]
 **sources** | [**[KafkaSourceWrapper]**](KafkaSourceWrapper.md) | List of sources from which to ingest data | [optional]
 **storage_compression_type** | **str** | RocksDB storage compression type. | [optional]
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
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create kinesis collection
api_response = rs.Collections.create_kinesis_collection(
    name="global-transactions",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Collections->create_kinesis_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create kinesis collection
api_response = await rs.Collections.create_kinesis_collection(
    clustering_key=[
        FieldPartition(
            field_name="address.city.zipcode",
            keys=["value1","value2"],
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
    name="global-transactions",
    retention_secs=1000000,
    source_download_soft_limit_bytes=1,
    sources=[
        KinesisSourceWrapper(
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
            aws_region="us-east-2",
            dms_primary_key=[
                "dms_primary_key_example",
            ],
            offset_reset_policy="EARLIEST",
            stream_name="click_stream",
        ),
    ],
    storage_compression_type="LZ4",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Collections->create_kinesis_collection: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | Deprecated. List of clustering fields. Use CLUSTER BY clause in &#x60;field_mapping_query&#x60; instead. | [optional]
 **description** | **str** | Text describing the collection. | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **name** | **str** | Unique identifier for collection, can contain alphanumeric or dash characters. | 
 **retention_secs** | **int** | Number of seconds after which data is purged, based on event time. | [optional]
 **source_download_soft_limit_bytes** | **int** | Soft ingest limit for this collection. | [optional]
 **sources** | [**[KinesisSourceWrapper]**](KinesisSourceWrapper.md) | List of sources from which to ingest data | [optional]
 **storage_compression_type** | **str** | RocksDB storage compression type. | [optional]
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
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create mongodb collection
api_response = rs.Collections.create_mongodb_collection(
    name="global-transactions",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Collections->create_mongodb_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create mongodb collection
api_response = await rs.Collections.create_mongodb_collection(
    clustering_key=[
        FieldPartition(
            field_name="address.city.zipcode",
            keys=["value1","value2"],
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
    name="global-transactions",
    retention_secs=1000000,
    source_download_soft_limit_bytes=1,
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
            collection_name="my_collection",
            database_name="my_database",
            retrieve_full_document=True,
        ),
    ],
    storage_compression_type="LZ4",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Collections->create_mongodb_collection: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | Deprecated. List of clustering fields. Use CLUSTER BY clause in &#x60;field_mapping_query&#x60; instead. | [optional]
 **description** | **str** | Text describing the collection. | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **name** | **str** | Unique identifier for collection, can contain alphanumeric or dash characters. | 
 **retention_secs** | **int** | Number of seconds after which data is purged, based on event time. | [optional]
 **source_download_soft_limit_bytes** | **int** | Soft ingest limit for this collection. | [optional]
 **sources** | [**[MongodbSourceWrapper]**](MongodbSourceWrapper.md) | List of sources from which to ingest data | [optional]
 **storage_compression_type** | **str** | RocksDB storage compression type. | [optional]
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
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create s3 collection
api_response = rs.Collections.create_s3_collection(
    name="global-transactions",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Collections->create_s3_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create s3 collection
api_response = await rs.Collections.create_s3_collection(
    clustering_key=[
        FieldPartition(
            field_name="address.city.zipcode",
            keys=["value1","value2"],
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
    name="global-transactions",
    retention_secs=1000000,
    source_download_soft_limit_bytes=1,
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
            bucket="s3://customer-account-info",
            pattern="prefix/to/**/keys/*.format",
            prefix="prefix/to/keys",
            region="us-west-2",
        ),
    ],
    storage_compression_type="LZ4",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Collections->create_s3_collection: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | Deprecated. List of clustering fields. Use CLUSTER BY clause in &#x60;field_mapping_query&#x60; instead. | [optional]
 **description** | **str** | Text describing the collection. | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **name** | **str** | Unique identifier for collection, can contain alphanumeric or dash characters. | 
 **retention_secs** | **int** | Number of seconds after which data is purged, based on event time. | [optional]
 **source_download_soft_limit_bytes** | **int** | Soft ingest limit for this collection. | [optional]
 **sources** | [**[S3SourceWrapper]**](S3SourceWrapper.md) | List of sources from which to ingest data | [optional]
 **storage_compression_type** | **str** | RocksDB storage compression type. | [optional]
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

# **create_snowflake_collection**
> CreateCollectionResponse create_snowflake_collection(snowflake_collection_creation_request)

Create snowflake collection

Create new collection in a workspace.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create snowflake collection
api_response = rs.Collections.create_snowflake_collection(
    name="global-transactions",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Collections->create_snowflake_collection: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create snowflake collection
api_response = await rs.Collections.create_snowflake_collection(
    clustering_key=[
        FieldPartition(
            field_name="address.city.zipcode",
            keys=["value1","value2"],
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
    name="global-transactions",
    retention_secs=1000000,
    source_download_soft_limit_bytes=1,
    sources=[
        SnowflakeSourceWrapper(
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
            database="NASDAQ",
            schema="PUBLIC",
            table_name="COMPANIES",
            warehouse="COMPUTE_XL",
        ),
    ],
    storage_compression_type="LZ4",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Collections->create_snowflake_collection: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clustering_key** | [**[FieldPartition]**](FieldPartition.md) | Deprecated. List of clustering fields. Use CLUSTER BY clause in &#x60;field_mapping_query&#x60; instead. | [optional]
 **description** | **str** | Text describing the collection. | [optional]
 **event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **name** | **str** | Unique identifier for collection, can contain alphanumeric or dash characters. | 
 **retention_secs** | **int** | Number of seconds after which data is purged, based on event time. | [optional]
 **source_download_soft_limit_bytes** | **int** | Soft ingest limit for this collection. | [optional]
 **sources** | [**[SnowflakeSourceWrapper]**](SnowflakeSourceWrapper.md) | List of sources from which to ingest data | [optional]
 **storage_compression_type** | **str** | RocksDB storage compression type. | [optional]
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

# **delete**
> DeleteCollectionResponse delete(collection)

Delete Collection

Delete a collection and all its documents from Rockset.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Delete Collection
api_response = rs.Collections.delete(
    collection="collection_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Collections->delete: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Delete Collection
api_response = await rs.Collections.delete(
    collection="collection_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Collections->delete: %s\n" % e)
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

# **get**
> GetCollectionResponse get(collection)

Retrieve Collection

Get details about a collection.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Retrieve Collection
api_response = rs.Collections.get(
    collection="collection_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Collections->get: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Retrieve Collection
api_response = await rs.Collections.get(
    collection="collection_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Collections->get: %s\n" % e)
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

# **get_collection_offsets**
> GetCollectionCommit get_collection_offsets(collection, get_collection_commit_request)

Get Collection Commit

Determines if the collection includes data at or after the specified fence(s) for close read-after-write semantics.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Get Collection Commit
api_response = rs.Collections.get_collection_offsets(
    collection="collection_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Collections->get_collection_offsets: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Get Collection Commit
api_response = await rs.Collections.get_collection_offsets(
    collection="collection_example",
    name=["f1:0:14:9:7092","f1:0:14:9:7093"],
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Collections->get_collection_offsets: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **name** | **[str]** | a list of zero or more collection offset fences | [optional]
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**GetCollectionCommit**](GetCollectionCommit.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned collection commit |  -  |
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
> ListCollectionsResponse list()

List Collections

Retrieve all collections in an organization.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# List Collections
api_response = rs.Collections.list(
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Collections->list: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# List Collections
api_response = await rs.Collections.list(
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Collections->list: %s\n" % e)
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

# **update**
> GetCollectionResponse update(collection, update_collection_request)

Update Collection

Update details about a collection.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Update Collection
api_response = rs.Collections.update(
    collection="collection_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Collections->update: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Update Collection
api_response = await rs.Collections.update(
    collection="collection_example",
    description="transactions from stores worldwide",
    field_mapping_query=FieldMappingQuery(
        sql="sql",
    ),
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Collections->update: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **description** | **str** | Updated text describing the collection. | [optional]
 **field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional]
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**GetCollectionResponse**](GetCollectionResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | collection updated successfully |  -  |
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
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# List Collections in Workspace
api_response = rs.Collections.workspace_collections(
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Collections->workspace_collections: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# List Collections in Workspace
api_response = await rs.Collections.workspace_collections(
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Collections->workspace_collections: %s\n" % e)
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

