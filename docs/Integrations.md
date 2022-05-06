# rockset.Integrations

All URIs are relative to *https://api.rs2.usw2.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_azure_blob_storage_integration**](Integrations.md#create_azure_blob_storage_integration) | **POST** /v1/orgs/self/integrations#AzureBlobStorage | Create azure blob storage integration
[**create_azure_event_hubs_integration**](Integrations.md#create_azure_event_hubs_integration) | **POST** /v1/orgs/self/integrations#AzureEventHubs | Create azure event hubs integration
[**create_dynamodb_integration**](Integrations.md#create_dynamodb_integration) | **POST** /v1/orgs/self/integrations#Dynamodb | Create dynamodb integration
[**create_gcs_integration**](Integrations.md#create_gcs_integration) | **POST** /v1/orgs/self/integrations#Gcs | Create gcs integration
[**create_kafka_integration**](Integrations.md#create_kafka_integration) | **POST** /v1/orgs/self/integrations#Kafka | Create kafka integration
[**create_kinesis_integration**](Integrations.md#create_kinesis_integration) | **POST** /v1/orgs/self/integrations#Kinesis | Create kinesis integration
[**create_mongodb_integration**](Integrations.md#create_mongodb_integration) | **POST** /v1/orgs/self/integrations#Mongodb | Create mongodb integration
[**create_s3_integration**](Integrations.md#create_s3_integration) | **POST** /v1/orgs/self/integrations#S3 | Create s3 integration
[**create_segment_integration**](Integrations.md#create_segment_integration) | **POST** /v1/orgs/self/integrations#Segment | Create segment integration
[**delete_integration**](Integrations.md#delete_integration) | **DELETE** /v1/orgs/self/integrations/{integration} | Delete Integration
[**get_integration**](Integrations.md#get_integration) | **GET** /v1/orgs/self/integrations/{integration} | Retrieve Integration
[**list_integrations**](Integrations.md#list_integrations) | **GET** /v1/orgs/self/integrations | List Integrations


# **create_azure_blob_storage_integration**
> CreateIntegrationResponse create_azure_blob_storage_integration(azure_blob_storage_integration_creation_request)

Create azure blob storage integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Create azure blob storage integration
    api_response = rs.Integrations.create_azure_blob_storage_integration(
        name="event-logs",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling Integrations->create_azure_blob_storage_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create azure blob storage integration
    api_response = await rs.Integrations.create_azure_blob_storage_integration(
        azure_blob_storage=AzureBlobStorageIntegration(
        connection_string="connection_string_example",
    ),
        description="AWS account with event data for the data science team.",
        name="event-logs",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling Integrations->create_azure_blob_storage_integration: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_blob_storage** | [**AzureBlobStorageIntegration**](AzureBlobStorageIntegration.md) |  | [optional]
 **description** | **str** | longer explanation for the integration | [optional]
 **name** | **str** | descriptive label | 

### Return type

[**CreateIntegrationResponse**](CreateIntegrationResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | integration created successfully |  -  |
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

# **create_azure_event_hubs_integration**
> CreateIntegrationResponse create_azure_event_hubs_integration(azure_event_hubs_integration_creation_request)

Create azure event hubs integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Create azure event hubs integration
    api_response = rs.Integrations.create_azure_event_hubs_integration(
        name="event-logs",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling Integrations->create_azure_event_hubs_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create azure event hubs integration
    api_response = await rs.Integrations.create_azure_event_hubs_integration(
        azure_event_hubs=AzureEventHubsIntegration(
    ),
        description="AWS account with event data for the data science team.",
        name="event-logs",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling Integrations->create_azure_event_hubs_integration: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_event_hubs** | [**AzureEventHubsIntegration**](AzureEventHubsIntegration.md) |  | [optional]
 **description** | **str** | longer explanation for the integration | [optional]
 **name** | **str** | descriptive label | 

### Return type

[**CreateIntegrationResponse**](CreateIntegrationResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | integration created successfully |  -  |
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

# **create_dynamodb_integration**
> CreateIntegrationResponse create_dynamodb_integration(dynamodb_integration_creation_request)

Create dynamodb integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Create dynamodb integration
    api_response = rs.Integrations.create_dynamodb_integration(
        name="event-logs",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling Integrations->create_dynamodb_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create dynamodb integration
    api_response = await rs.Integrations.create_dynamodb_integration(
        description="AWS account with event data for the data science team.",
        dynamodb=DynamodbIntegration(
        aws_access_key=AwsAccessKey(
            aws_access_key_id="AKIAIOSFODNN7EXAMPLE",
            aws_secret_access_key="wJal....",
        ),
        aws_role=AwsRole(
            aws_role_arn="arn:aws:iam::2378964092:role/rockset-role",
        ),
        s3_export_bucket_name="s3_export_bucket_name_example",
    ),
        name="event-logs",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling Integrations->create_dynamodb_integration: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str** | longer explanation for the integration | [optional]
 **dynamodb** | [**DynamodbIntegration**](DynamodbIntegration.md) |  | [optional]
 **name** | **str** | descriptive label | 

### Return type

[**CreateIntegrationResponse**](CreateIntegrationResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | integration created successfully |  -  |
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

# **create_gcs_integration**
> CreateIntegrationResponse create_gcs_integration(gcs_integration_creation_request)

Create gcs integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Create gcs integration
    api_response = rs.Integrations.create_gcs_integration(
        name="event-logs",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling Integrations->create_gcs_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create gcs integration
    api_response = await rs.Integrations.create_gcs_integration(
        description="AWS account with event data for the data science team.",
        gcs=GcsIntegration(
        gcp_service_account=GcpServiceAccount(
            service_account_key_file_json="service_account_key_file_json_example",
        ),
    ),
        name="event-logs",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling Integrations->create_gcs_integration: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str** | longer explanation for the integration | [optional]
 **gcs** | [**GcsIntegration**](GcsIntegration.md) |  | [optional]
 **name** | **str** | descriptive label | 

### Return type

[**CreateIntegrationResponse**](CreateIntegrationResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | integration created successfully |  -  |
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

# **create_kafka_integration**
> CreateIntegrationResponse create_kafka_integration(kafka_integration_creation_request)

Create kafka integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Create kafka integration
    api_response = rs.Integrations.create_kafka_integration(
        name="event-logs",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling Integrations->create_kafka_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create kafka integration
    api_response = await rs.Integrations.create_kafka_integration(
        description="AWS account with event data for the data science team.",
        kafka=KafkaIntegration(
        bootstrap_servers="bootstrap_servers_example",
        kafka_data_format="json",
        kafka_topic_names=[
            "kafka_topic_names_example",
        ],
        schema_registry_config=SchemaRegistryConfig(
            key="key_example",
            secret="secret_example",
            url="url_example",
        ),
        security_config=KafkaV3SecurityConfig(
            api_key="api_key_example",
            secret="secret_example",
        ),
        use_v3=True,
    ),
        name="event-logs",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling Integrations->create_kafka_integration: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str** | longer explanation for the integration | [optional]
 **kafka** | [**KafkaIntegration**](KafkaIntegration.md) |  | [optional]
 **name** | **str** | descriptive label | 

### Return type

[**CreateIntegrationResponse**](CreateIntegrationResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | integration created successfully |  -  |
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

# **create_kinesis_integration**
> CreateIntegrationResponse create_kinesis_integration(kinesis_integration_creation_request)

Create kinesis integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Create kinesis integration
    api_response = rs.Integrations.create_kinesis_integration(
        name="event-logs",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling Integrations->create_kinesis_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create kinesis integration
    api_response = await rs.Integrations.create_kinesis_integration(
        description="AWS account with event data for the data science team.",
        kinesis=KinesisIntegration(
        aws_access_key=AwsAccessKey(
            aws_access_key_id="AKIAIOSFODNN7EXAMPLE",
            aws_secret_access_key="wJal....",
        ),
        aws_role=AwsRole(
            aws_role_arn="arn:aws:iam::2378964092:role/rockset-role",
        ),
    ),
        name="event-logs",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling Integrations->create_kinesis_integration: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str** | longer explanation for the integration | [optional]
 **kinesis** | [**KinesisIntegration**](KinesisIntegration.md) |  | [optional]
 **name** | **str** | descriptive label | 

### Return type

[**CreateIntegrationResponse**](CreateIntegrationResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | integration created successfully |  -  |
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

# **create_mongodb_integration**
> CreateIntegrationResponse create_mongodb_integration(mongodb_integration_creation_request)

Create mongodb integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Create mongodb integration
    api_response = rs.Integrations.create_mongodb_integration(
        name="event-logs",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling Integrations->create_mongodb_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create mongodb integration
    api_response = await rs.Integrations.create_mongodb_integration(
        description="AWS account with event data for the data science team.",
        mongodb=MongoDbIntegration(
        connection_uri="mongodb+srv://<username>:<password>@server.example.com/",
    ),
        name="event-logs",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling Integrations->create_mongodb_integration: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str** | longer explanation for the integration | [optional]
 **mongodb** | [**MongoDbIntegration**](MongoDbIntegration.md) |  | [optional]
 **name** | **str** | descriptive label | 

### Return type

[**CreateIntegrationResponse**](CreateIntegrationResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | integration created successfully |  -  |
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

# **create_s3_integration**
> CreateIntegrationResponse create_s3_integration(s3_integration_creation_request)

Create s3 integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Create s3 integration
    api_response = rs.Integrations.create_s3_integration(
        name="event-logs",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling Integrations->create_s3_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create s3 integration
    api_response = await rs.Integrations.create_s3_integration(
        description="AWS account with event data for the data science team.",
        name="event-logs",
        s3=S3Integration(
        aws_access_key=AwsAccessKey(
            aws_access_key_id="AKIAIOSFODNN7EXAMPLE",
            aws_secret_access_key="wJal....",
        ),
        aws_role=AwsRole(
            aws_role_arn="arn:aws:iam::2378964092:role/rockset-role",
        ),
    ),
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling Integrations->create_s3_integration: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str** | longer explanation for the integration | [optional]
 **name** | **str** | descriptive label | 
 **s3** | [**S3Integration**](S3Integration.md) |  | [optional]

### Return type

[**CreateIntegrationResponse**](CreateIntegrationResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | integration created successfully |  -  |
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

# **create_segment_integration**
> CreateIntegrationResponse create_segment_integration(segment_integration_creation_request)

Create segment integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Create segment integration
    api_response = rs.Integrations.create_segment_integration(
        name="event-logs",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling Integrations->create_segment_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create segment integration
    api_response = await rs.Integrations.create_segment_integration(
        description="AWS account with event data for the data science team.",
        name="event-logs",
        segment=SegmentIntegration(
    ),
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling Integrations->create_segment_integration: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str** | longer explanation for the integration | [optional]
 **name** | **str** | descriptive label | 
 **segment** | [**SegmentIntegration**](SegmentIntegration.md) |  | [optional]

### Return type

[**CreateIntegrationResponse**](CreateIntegrationResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | integration created successfully |  -  |
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

# **delete_integration**
> DeleteIntegrationResponse delete_integration(integration)

Delete Integration

Remove an integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Delete Integration
    api_response = rs.Integrations.delete_integration(
        integration="integration_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling Integrations->delete_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Delete Integration
    api_response = await rs.Integrations.delete_integration(
        integration="integration_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling Integrations->delete_integration: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str** | name of the integration |

### Return type

[**DeleteIntegrationResponse**](DeleteIntegrationResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | integration deleted successfully |  -  |
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

# **get_integration**
> GetIntegrationResponse get_integration(integration)

Retrieve Integration

Retrieve information about a single integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Retrieve Integration
    api_response = rs.Integrations.get_integration(
        integration="integration_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling Integrations->get_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Retrieve Integration
    api_response = await rs.Integrations.get_integration(
        integration="integration_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling Integrations->get_integration: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str** | name of the integration |

### Return type

[**GetIntegrationResponse**](GetIntegrationResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | integration retrieved successfully |  -  |
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

# **list_integrations**
> ListIntegrationsResponse list_integrations()

List Integrations

List all integrations in an organization.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # List Integrations
    api_response = rs.Integrations.list_integrations(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling Integrations->list_integrations: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # List Integrations
    api_response = await rs.Integrations.list_integrations(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling Integrations->list_integrations: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListIntegrationsResponse**](ListIntegrationsResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | integrations retrieved successfully |  -  |
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
