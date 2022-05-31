# rockset.Integrations

All URIs are relative to *https://api.use1a1.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](IntegrationsApi.md#create) | **POST** /v1/orgs/self/integrations | Create azure blob storage integration
[**create_0**](IntegrationsApi.md#create_0) | **POST** /v1/orgs/self/integrations | Create azure event hubs integration
[**create_1**](IntegrationsApi.md#create_1) | **POST** /v1/orgs/self/integrations | Create dynamodb integration
[**create_2**](IntegrationsApi.md#create_2) | **POST** /v1/orgs/self/integrations | Create gcs integration
[**create_3**](IntegrationsApi.md#create_3) | **POST** /v1/orgs/self/integrations | Create kafka integration
[**create_4**](IntegrationsApi.md#create_4) | **POST** /v1/orgs/self/integrations | Create kinesis integration
[**create_5**](IntegrationsApi.md#create_5) | **POST** /v1/orgs/self/integrations | Create mongodb integration
[**create_6**](IntegrationsApi.md#create_6) | **POST** /v1/orgs/self/integrations | Create s3 integration
[**create_7**](IntegrationsApi.md#create_7) | **POST** /v1/orgs/self/integrations | Create segment integration
[**delete**](IntegrationsApi.md#delete) | **DELETE** /v1/orgs/self/integrations/{integration} | Delete Integration
[**get**](IntegrationsApi.md#get) | **GET** /v1/orgs/self/integrations/{integration} | Retrieve Integration
[**list**](IntegrationsApi.md#list) | **GET** /v1/orgs/self/integrations | List Integrations


# **create**
> CreateIntegrationResponse create(azure_blob_storage_integration_creation_request)

Create azure blob storage integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create azure blob storage integration
api_response = rs.Integrations.create(
    name="event-logs",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->create: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create azure blob storage integration
api_response = await rs.Integrations.create(
    azure_blob_storage=AzureBlobStorageIntegration(
        connection_string="connection_string_example",
    ),
    description="AWS account with event data for the data science team.",
    name="event-logs",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Integrations->create: %s\n" % e)
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

# **create_0**
> CreateIntegrationResponse create_0(azure_event_hubs_integration_creation_request)

Create azure event hubs integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create azure event hubs integration
api_response = rs.Integrations.create_0(
    name="event-logs",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->create_0: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create azure event hubs integration
api_response = await rs.Integrations.create_0(
    azure_event_hubs=AzureEventHubsIntegration(
    ),
    description="AWS account with event data for the data science team.",
    name="event-logs",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Integrations->create_0: %s\n" % e)
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

# **create_1**
> CreateIntegrationResponse create_1(dynamodb_integration_creation_request)

Create dynamodb integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create dynamodb integration
api_response = rs.Integrations.create_1(
    name="event-logs",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->create_1: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create dynamodb integration
api_response = await rs.Integrations.create_1(
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
    print("Exception when calling Integrations->create_1: %s\n" % e)
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

# **create_2**
> CreateIntegrationResponse create_2(gcs_integration_creation_request)

Create gcs integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create gcs integration
api_response = rs.Integrations.create_2(
    name="event-logs",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->create_2: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create gcs integration
api_response = await rs.Integrations.create_2(
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
    print("Exception when calling Integrations->create_2: %s\n" % e)
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

# **create_3**
> CreateIntegrationResponse create_3(kafka_integration_creation_request)

Create kafka integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create kafka integration
api_response = rs.Integrations.create_3(
    name="event-logs",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->create_3: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create kafka integration
api_response = await rs.Integrations.create_3(
    description="AWS account with event data for the data science team.",
    kafka=KafkaIntegration(
        bootstrap_servers="bootstrap_servers_example",
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
    print("Exception when calling Integrations->create_3: %s\n" % e)
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

# **create_4**
> CreateIntegrationResponse create_4(kinesis_integration_creation_request)

Create kinesis integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create kinesis integration
api_response = rs.Integrations.create_4(
    name="event-logs",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->create_4: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create kinesis integration
api_response = await rs.Integrations.create_4(
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
    print("Exception when calling Integrations->create_4: %s\n" % e)
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

# **create_5**
> CreateIntegrationResponse create_5(mongodb_integration_creation_request)

Create mongodb integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create mongodb integration
api_response = rs.Integrations.create_5(
    name="event-logs",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->create_5: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create mongodb integration
api_response = await rs.Integrations.create_5(
    description="AWS account with event data for the data science team.",
    mongodb=MongoDbIntegration(
        connection_uri="mongodb+srv://<username>:<password>@server.example.com/",
    ),
    name="event-logs",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Integrations->create_5: %s\n" % e)
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

# **create_6**
> CreateIntegrationResponse create_6(s3_integration_creation_request)

Create s3 integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create s3 integration
api_response = rs.Integrations.create_6(
    name="event-logs",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->create_6: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create s3 integration
api_response = await rs.Integrations.create_6(
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
    print("Exception when calling Integrations->create_6: %s\n" % e)
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

# **create_7**
> CreateIntegrationResponse create_7(segment_integration_creation_request)

Create segment integration

Create a new integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create segment integration
api_response = rs.Integrations.create_7(
    name="event-logs",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Integrations->create_7: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create segment integration
api_response = await rs.Integrations.create_7(
    description="AWS account with event data for the data science team.",
    name="event-logs",
    segment=SegmentIntegration(
    ),
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Integrations->create_7: %s\n" % e)
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

# **delete**
> DeleteIntegrationResponse delete(integration)

Delete Integration

Remove an integration.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
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

