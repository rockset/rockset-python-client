# rockset.Sources

All URIs are relative to *https://api.use1a1.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_azure_blob_storage_source**](SourcesApi.md#create_azure_blob_storage_source) | **POST** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources | Create a new azure blob storage source in a collection
[**create_azure_event_hubs_source**](SourcesApi.md#create_azure_event_hubs_source) | **POST** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources | Create a new azure event hubs source in a collection
[**create_dynamodb_source**](SourcesApi.md#create_dynamodb_source) | **POST** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources | Create a new dynamodb source in a collection
[**create_gcs_source**](SourcesApi.md#create_gcs_source) | **POST** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources | Create a new gcs source in a collection
[**create_kafka_source**](SourcesApi.md#create_kafka_source) | **POST** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources | Create a new kafka source in a collection
[**create_kinesis_source**](SourcesApi.md#create_kinesis_source) | **POST** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources | Create a new kinesis source in a collection
[**create_mongodb_source**](SourcesApi.md#create_mongodb_source) | **POST** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources | Create a new mongodb source in a collection
[**create_s3_source**](SourcesApi.md#create_s3_source) | **POST** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources | Create a new s3 source in a collection
[**create_snowflake_source**](SourcesApi.md#create_snowflake_source) | **POST** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources | Create a new snowflake source in a collection
[**delete**](SourcesApi.md#delete) | **DELETE** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources/{source} | Delete Collection source
[**get**](SourcesApi.md#get) | **GET** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources/{source} | Retrieve source
[**list**](SourcesApi.md#list) | **GET** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources | List sources in collection
[**resume**](SourcesApi.md#resume) | **POST** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources/{source}/resume | Resume source ingest
[**suspend**](SourcesApi.md#suspend) | **POST** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources/{source}/suspend | Suspend source ingest
[**update**](SourcesApi.md#update) | **PUT** /v1/orgs/self/ws/{workspace}/collections/{collection}/sources/{source} | Update a collection source


# **create_azure_blob_storage_source**
> GetSourceResponse create_azure_blob_storage_source(collection, azure_blob_storage_source_wrapper)

Create a new azure blob storage source in a collection

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
# Create a new azure blob storage source in a collection
api_response = rs.Sources.create_azure_blob_storage_source(
    collection="collection_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Sources->create_azure_blob_storage_source: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create a new azure blob storage source in a collection
api_response = await rs.Sources.create_azure_blob_storage_source(
    collection="collection_example",
    format_params=FormatParams(
        bson=True,
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
    settings=SourceAzBlobStorageSettings(
        azblob_scan_frequency="PT5M",
    ),
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Sources->create_azure_blob_storage_source: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **format_params** | [**FormatParams**](FormatParams.md) |  | [optional]
 **integration_name** | **str** | Name of integration to use. | [optional]
 **container** | **str** | Name of Azure blob Storage container you want to ingest from. | [optional]
 **pattern** | **str** | Glob-style pattern that selects keys to ingest. Only either prefix or pattern can be specified. | [optional]
 **prefix** | **str** | Prefix that selects blobs to ingest. | [optional]
 **settings** | [**SourceAzBlobStorageSettings**](SourceAzBlobStorageSettings.md) |  | [optional]
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
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_azure_event_hubs_source**
> GetSourceResponse create_azure_event_hubs_source(collection, azure_event_hubs_source_wrapper)

Create a new azure event hubs source in a collection

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
# Create a new azure event hubs source in a collection
api_response = rs.Sources.create_azure_event_hubs_source(
    collection="collection_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Sources->create_azure_event_hubs_source: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create a new azure event hubs source in a collection
api_response = await rs.Sources.create_azure_event_hubs_source(
    collection="collection_example",
    format_params=FormatParams(
        bson=True,
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
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Sources->create_azure_event_hubs_source: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **format_params** | [**FormatParams**](FormatParams.md) |  | [optional]
 **integration_name** | **str** | Name of integration to use. | [optional]
 **hub_id** | **str** | Name of the hub which rockset should ingest from. | [optional]
 **offset_reset_policy** | **str** | The offset reset policy. | [optional]
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
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dynamodb_source**
> GetSourceResponse create_dynamodb_source(collection, dynamodb_source_wrapper)

Create a new dynamodb source in a collection

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
# Create a new dynamodb source in a collection
api_response = rs.Sources.create_dynamodb_source(
    collection="collection_example",
    table_name="dynamodb_table_name",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Sources->create_dynamodb_source: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create a new dynamodb source in a collection
api_response = await rs.Sources.create_dynamodb_source(
    collection="collection_example",
    format_params=FormatParams(
        bson=True,
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
    settings=SourceDynamoDbSettings(
        dynamodb_stream_poll_frequency="PT1S",
    ),
    table_name="dynamodb_table_name",
    use_scan_api=True,
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Sources->create_dynamodb_source: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **format_params** | [**FormatParams**](FormatParams.md) |  | [optional]
 **integration_name** | **str** | Name of integration to use. | [optional]
 **aws_region** | **str** | AWS region name of DynamoDB table, by default us-west-2 is used. | [optional]
 **rcu** | **int** | Max RCU usage for scan. | [optional]
 **settings** | [**SourceDynamoDbSettings**](SourceDynamoDbSettings.md) |  | [optional]
 **table_name** | **str** | Name of DynamoDB table containing data. | 
 **use_scan_api** | **bool** | Whether to use DynamoDB Scan API for the initial scan. | [optional]
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
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_gcs_source**
> GetSourceResponse create_gcs_source(collection, gcs_source_wrapper)

Create a new gcs source in a collection

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
# Create a new gcs source in a collection
api_response = rs.Sources.create_gcs_source(
    collection="collection_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Sources->create_gcs_source: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create a new gcs source in a collection
api_response = await rs.Sources.create_gcs_source(
    collection="collection_example",
    format_params=FormatParams(
        bson=True,
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
    settings=SourceGcsSettings(
        gcs_scan_frequency="PT5M",
    ),
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Sources->create_gcs_source: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **format_params** | [**FormatParams**](FormatParams.md) |  | [optional]
 **integration_name** | **str** | Name of integration to use. | [optional]
 **bucket** | **str** | Name of GCS bucket you want to ingest from. | [optional]
 **pattern** | **str** | Glob-style pattern that selects keys to ingest. Only either prefix or pattern can be specified. | [optional]
 **prefix** | **str** | Prefix that selects keys to ingest. | [optional]
 **settings** | [**SourceGcsSettings**](SourceGcsSettings.md) |  | [optional]
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
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_kafka_source**
> GetSourceResponse create_kafka_source(collection, kafka_source_wrapper)

Create a new kafka source in a collection

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
# Create a new kafka source in a collection
api_response = rs.Sources.create_kafka_source(
    collection="collection_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Sources->create_kafka_source: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create a new kafka source in a collection
api_response = await rs.Sources.create_kafka_source(
    collection="collection_example",
    format_params=FormatParams(
        bson=True,
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
    client_id="cwc|0013a00001hSJ7oAAG|rockset-colln-consumer",
    consumer_group_id="org-collection",
    kafka_topic_name="example-topic",
    offset_reset_policy="EARLIEST",
    use_v3=True,
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Sources->create_kafka_source: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **format_params** | [**FormatParams**](FormatParams.md) |  | [optional]
 **integration_name** | **str** | Name of integration to use. | [optional]
 **client_id** | **str** | The kafka client id being used. | [optional]
 **consumer_group_id** | **str** | The Kafka consumer group Id being used. | [optional]
 **kafka_topic_name** | **str** | The Kafka topic to be tailed. | [optional]
 **offset_reset_policy** | **str** | The offset reset policy. | [optional]
 **use_v3** | **bool** | Whether to use v3 integration. | [optional]
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
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_kinesis_source**
> GetSourceResponse create_kinesis_source(collection, kinesis_source_wrapper)

Create a new kinesis source in a collection

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
# Create a new kinesis source in a collection
api_response = rs.Sources.create_kinesis_source(
    collection="collection_example",
    stream_name="click_stream",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Sources->create_kinesis_source: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create a new kinesis source in a collection
api_response = await rs.Sources.create_kinesis_source(
    collection="collection_example",
    format_params=FormatParams(
        bson=True,
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
        "string_example",
    ],
    offset_reset_policy="EARLIEST",
    stream_name="click_stream",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Sources->create_kinesis_source: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **format_params** | [**FormatParams**](FormatParams.md) |  | [optional]
 **integration_name** | **str** | Name of integration to use. | [optional]
 **aws_region** | **str** | AWS region name of Kinesis stream, by default us-west-2 is used. | [optional]
 **dms_primary_key** | **[str]** | Set of fields that correspond to a DMS primary key. | [optional]
 **offset_reset_policy** | **str** | For non-DMS streams, Rockset can tail from the earliest end or latest end of kinesis source. | [optional]
 **stream_name** | **str** | Name of kinesis stream. | 
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
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mongodb_source**
> GetSourceResponse create_mongodb_source(collection, mongodb_source_wrapper)

Create a new mongodb source in a collection

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
# Create a new mongodb source in a collection
api_response = rs.Sources.create_mongodb_source(
    collection="collection_example",
    collection_name="my_collection",
    database_name="my_database",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Sources->create_mongodb_source: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create a new mongodb source in a collection
api_response = await rs.Sources.create_mongodb_source(
    collection="collection_example",
    format_params=FormatParams(
        bson=True,
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
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Sources->create_mongodb_source: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **format_params** | [**FormatParams**](FormatParams.md) |  | [optional]
 **integration_name** | **str** | Name of integration to use. | [optional]
 **collection_name** | **str** | MongoDB collection name. | 
 **database_name** | **str** | MongoDB database name containing this collection. | 
 **retrieve_full_document** | **bool** | Whether to get the full document from the MongoDB change stream to enable multi-field expression transformations. Selecting this option will increase load on your upstream MongoDB database. | [optional]
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
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_s3_source**
> GetSourceResponse create_s3_source(collection, s3_source_wrapper)

Create a new s3 source in a collection

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
# Create a new s3 source in a collection
api_response = rs.Sources.create_s3_source(
    collection="collection_example",
    bucket="s3://customer-account-info",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Sources->create_s3_source: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create a new s3 source in a collection
api_response = await rs.Sources.create_s3_source(
    collection="collection_example",
    format_params=FormatParams(
        bson=True,
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
    settings=SourceS3Settings(
        s3_scan_frequency="PT5M",
    ),
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Sources->create_s3_source: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **format_params** | [**FormatParams**](FormatParams.md) |  | [optional]
 **integration_name** | **str** | Name of integration to use. | [optional]
 **bucket** | **str** | Address of S3 bucket containing data. | 
 **pattern** | **str** | Glob-style pattern that selects keys to ingest. Only either prefix or pattern can be specified. | [optional]
 **prefix** | **str** | Prefix that selects keys to ingest. | [optional]
 **region** | **str** | AWS region containing source bucket. | [optional]
 **settings** | [**SourceS3Settings**](SourceS3Settings.md) |  | [optional]
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
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snowflake_source**
> GetSourceResponse create_snowflake_source(collection, snowflake_source_wrapper)

Create a new snowflake source in a collection

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
# Create a new snowflake source in a collection
api_response = rs.Sources.create_snowflake_source(
    collection="collection_example",
    database="NASDAQ",
    schema="PUBLIC",
    table_name="COMPANIES",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Sources->create_snowflake_source: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create a new snowflake source in a collection
api_response = await rs.Sources.create_snowflake_source(
    collection="collection_example",
    format_params=FormatParams(
        bson=True,
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
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Sources->create_snowflake_source: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **format_params** | [**FormatParams**](FormatParams.md) |  | [optional]
 **integration_name** | **str** | Name of integration to use. | [optional]
 **database** | **str** | Name of the snowflake database. | 
 **schema** | **str** | Name of the snowflake database schema. | 
 **table_name** | **str** | Name of the snowflake table. | 
 **warehouse** | **str** | Name of the data warehouse to be used. | [optional]
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
**409** | conflict |  -  |
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
**409** | conflict |  -  |
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
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ListSourcesResponse list(collection)

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
api_response = rs.Sources.list(
    collection="collection_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Sources->list: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# List sources in collection
api_response = await rs.Sources.list(
    collection="collection_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Sources->list: %s\n" % e)
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
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume**
> GetSourceResponse resume(collection, source)

Resume source ingest

Resume source ingest

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Resume source ingest
api_response = rs.Sources.resume(
    collection="collection_example",
    source="source_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Sources->resume: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Resume source ingest
api_response = await rs.Sources.resume(
    collection="collection_example",
    source="source_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Sources->resume: %s\n" % e)
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
**200** | source was resumed |  -  |
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

# **suspend**
> GetSourceResponse suspend(collection, source)

Suspend source ingest

Suspend source ingest

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Suspend source ingest
api_response = rs.Sources.suspend(
    collection="collection_example",
    source="source_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Sources->suspend: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Suspend source ingest
api_response = await rs.Sources.suspend(
    collection="collection_example",
    source="source_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Sources->suspend: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **source** | **str** | id of source |
 **workspace** | **str** | name of the workspace | defaults to "commons"
 **resume_after_duration** | **str** | duration to suspend source; 1h is the default | [optional]


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
**200** | source was suspended |  -  |
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

# **update**
> GetSourceResponse update(collection, source, source_base)

Update a collection source

Update details about a collection source.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Update a collection source
api_response = rs.Sources.update(
    collection="collection_example",
    source="source_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Sources->update: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Update a collection source
api_response = await rs.Sources.update(
    collection="collection_example",
    source="source_example",
    azure_blob_storage=SourceAzBlobStorageBase(
        settings=SourceAzBlobStorageSettings(
            azblob_scan_frequency="PT5M",
        ),
    ),
    dynamodb=SourceDynamoDbBase(
        settings=SourceDynamoDbSettings(
            dynamodb_stream_poll_frequency="PT1S",
        ),
    ),
    gcs=SourceGcsBase(
        settings=SourceGcsSettings(
            gcs_scan_frequency="PT5M",
        ),
    ),
    s3=SourceS3Base(
        settings=SourceS3Settings(
            s3_scan_frequency="PT5M",
        ),
    ),
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Sources->update: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str** | name of the collection |
 **source** | **str** | id of source |
 **azure_blob_storage** | [**SourceAzBlobStorageBase**](SourceAzBlobStorageBase.md) |  | [optional]
 **dynamodb** | [**SourceDynamoDbBase**](SourceDynamoDbBase.md) |  | [optional]
 **gcs** | [**SourceGcsBase**](SourceGcsBase.md) |  | [optional]
 **s3** | [**SourceS3Base**](SourceS3Base.md) |  | [optional]
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
**200** | collection updated successfully |  -  |
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

