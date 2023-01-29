# rockset.Integrations

All URIs are relative to *https://api.use1a1.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_azure_blob_storage_integration**](IntegrationsApi.md#create_azure_blob_storage_integration) | **POST** /v1/orgs/self/integrations | Create azure blob storage integration
[**create_azure_event_hubs_integration**](IntegrationsApi.md#create_azure_event_hubs_integration) | **POST** /v1/orgs/self/integrations | Create azure event hubs integration
[**create_dynamodb_integration**](IntegrationsApi.md#create_dynamodb_integration) | **POST** /v1/orgs/self/integrations | Create dynamodb integration
[**create_gcs_integration**](IntegrationsApi.md#create_gcs_integration) | **POST** /v1/orgs/self/integrations | Create gcs integration
[**create_kafka_integration**](IntegrationsApi.md#create_kafka_integration) | **POST** /v1/orgs/self/integrations | Create kafka integration
[**create_kinesis_integration**](IntegrationsApi.md#create_kinesis_integration) | **POST** /v1/orgs/self/integrations | Create kinesis integration
[**create_mongodb_integration**](IntegrationsApi.md#create_mongodb_integration) | **POST** /v1/orgs/self/integrations | Create mongodb integration
[**create_s3_integration**](IntegrationsApi.md#create_s3_integration) | **POST** /v1/orgs/self/integrations | Create s3 integration
[**create_snowflake_integration**](IntegrationsApi.md#create_snowflake_integration) | **POST** /v1/orgs/self/integrations | Create snowflake integration
[**delete**](IntegrationsApi.md#delete) | **DELETE** /v1/orgs/self/integrations/{integration} | Delete Integration
[**get**](IntegrationsApi.md#get) | **GET** /v1/orgs/self/integrations/{integration} | Retrieve Integration
[**list**](IntegrationsApi.md#list) | **GET** /v1/orgs/self/integrations | List Integrations


# **create_azure_blob_storage_integration**
> CreateIntegrationResponse create_azure_blob_storage_integration(azure_blob_storage_integration_creation_request)

Create azure blob storage integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create azure blob storage integration
api_response = rs.Integrations.create_azure_blob_storage_integration(
    name="event-logs",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->create_azure_blob_storage_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create azure blob storage integration
api_response = await rs.Integrations.create_azure_blob_storage_integration(
    azure_blob_storage=AzureBlobStorageIntegration(
        connection_string='''BlobEndpoint=https://<NamespaceName>.blob.core.windows.net;
SharedAccessSignature=<KeyValue>''',
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
 **description** | **str** | Longer explanation for the integration. | [optional]
 **name** | **str** | Descriptive label. | 

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
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create azure event hubs integration
api_response = rs.Integrations.create_azure_event_hubs_integration(
    name="event-logs",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->create_azure_event_hubs_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create azure event hubs integration
api_response = await rs.Integrations.create_azure_event_hubs_integration(
    azure_event_hubs=AzureEventHubsIntegration(
        connection_string="Endpoint=sb://<NamespaceName>.servicebus.windows.net/;SharedAccessKeyName=<KeyName>;SharedAccessKey=<KeyValue>",
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
 **description** | **str** | Longer explanation for the integration. | [optional]
 **name** | **str** | Descriptive label. | 

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
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create dynamodb integration
api_response = rs.Integrations.create_dynamodb_integration(
    name="event-logs",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->create_dynamodb_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create dynamodb integration
api_response = await rs.Integrations.create_dynamodb_integration(
    description="AWS account with event data for the data science team.",
    dynamodb=DynamodbIntegration(
        aws_access_key=AwsAccessKey(
            aws_access_key_id="AKIAIOSFODNN7EXAMPLE",
            aws_secret_access_key="wJal....",
        ),
        aws_role=AwsRole(
            aws_external_id="external id of aws",
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
 **description** | **str** | Longer explanation for the integration. | [optional]
 **dynamodb** | [**DynamodbIntegration**](DynamodbIntegration.md) |  | [optional]
 **name** | **str** | Descriptive label. | 

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
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create gcs integration
api_response = rs.Integrations.create_gcs_integration(
    name="event-logs",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->create_gcs_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
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
 **description** | **str** | Longer explanation for the integration. | [optional]
 **gcs** | [**GcsIntegration**](GcsIntegration.md) |  | [optional]
 **name** | **str** | Descriptive label. | 

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
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create kafka integration
api_response = rs.Integrations.create_kafka_integration(
    name="event-logs",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->create_kafka_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create kafka integration
api_response = await rs.Integrations.create_kafka_integration(
    description="AWS account with event data for the data science team.",
    kafka=KafkaIntegration(
        aws_role=AwsRole(
            aws_external_id="external id of aws",
            aws_role_arn="arn:aws:iam::2378964092:role/rockset-role",
        ),
        bootstrap_servers="localhost:9092",
        connection_string="connection_string_example",
        kafka_data_format="JSON",
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
 **description** | **str** | Longer explanation for the integration. | [optional]
 **kafka** | [**KafkaIntegration**](KafkaIntegration.md) |  | [optional]
 **name** | **str** | Descriptive label. | 

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
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create kinesis integration
api_response = rs.Integrations.create_kinesis_integration(
    name="event-logs",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->create_kinesis_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create kinesis integration
api_response = await rs.Integrations.create_kinesis_integration(
    description="AWS account with event data for the data science team.",
    kinesis=KinesisIntegration(
        aws_access_key=AwsAccessKey(
            aws_access_key_id="AKIAIOSFODNN7EXAMPLE",
            aws_secret_access_key="wJal....",
        ),
        aws_role=AwsRole(
            aws_external_id="external id of aws",
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
 **description** | **str** | Longer explanation for the integration. | [optional]
 **kinesis** | [**KinesisIntegration**](KinesisIntegration.md) |  | [optional]
 **name** | **str** | Descriptive label. | 

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
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create mongodb integration
api_response = rs.Integrations.create_mongodb_integration(
    name="event-logs",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->create_mongodb_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
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
 **description** | **str** | Longer explanation for the integration. | [optional]
 **mongodb** | [**MongoDbIntegration**](MongoDbIntegration.md) |  | [optional]
 **name** | **str** | Descriptive label. | 

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
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create s3 integration
api_response = rs.Integrations.create_s3_integration(
    name="event-logs",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->create_s3_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
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
            aws_external_id="external id of aws",
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
 **description** | **str** | Longer explanation for the integration. | [optional]
 **name** | **str** | Descriptive label. | 
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

# **create_snowflake_integration**
> CreateIntegrationResponse create_snowflake_integration(snowflake_integration_creation_request)

Create snowflake integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create snowflake integration
api_response = rs.Integrations.create_snowflake_integration(
    name="event-logs",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->create_snowflake_integration: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create snowflake integration
api_response = await rs.Integrations.create_snowflake_integration(
    description="AWS account with event data for the data science team.",
    name="event-logs",
    snowflake=SnowflakeIntegration(
        aws_access_key=AwsAccessKey(
            aws_access_key_id="AKIAIOSFODNN7EXAMPLE",
            aws_secret_access_key="wJal....",
        ),
        aws_role=AwsRole(
            aws_external_id="external id of aws",
            aws_role_arn="arn:aws:iam::2378964092:role/rockset-role",
        ),
        default_warehouse="default_warehouse_example",
        password="password_example",
        s3_export_path="s3://bucket/prefix",
        snowflake_url="acme-marketing-test-account.snowflakecomputing.com",
        user_role="user_role_example",
        username="username_example",
    ),
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Integrations->create_snowflake_integration: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str** | Longer explanation for the integration. | [optional]
 **name** | **str** | Descriptive label. | 
 **snowflake** | [**SnowflakeIntegration**](SnowflakeIntegration.md) |  | [optional]

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

# **delete**
> DeleteIntegrationResponse delete(integration)

Delete Integration

Remove an integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Delete Integration
api_response = rs.Integrations.delete(
    integration="integration_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->delete: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Delete Integration
api_response = await rs.Integrations.delete(
    integration="integration_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Integrations->delete: %s\n" % e)
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

# **get**
> GetIntegrationResponse get(integration)

Retrieve Integration

Retrieve information about a single integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Retrieve Integration
api_response = rs.Integrations.get(
    integration="integration_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->get: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Retrieve Integration
api_response = await rs.Integrations.get(
    integration="integration_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Integrations->get: %s\n" % e)
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

# **list**
> ListIntegrationsResponse list()

List Integrations

List all integrations in an organization.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# List Integrations
api_response = rs.Integrations.list(
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->list: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# List Integrations
api_response = await rs.Integrations.list(
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Integrations->list: %s\n" % e)
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

