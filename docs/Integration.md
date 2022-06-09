# Integration

Integrations that can be associated with data sources to create collections. Only one type of integration may be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | email of user who created the integration | 
**name** | **str** | descriptive label and unique identifier | 
**azure_blob_storage** | [**AzureBlobStorageIntegration**](AzureBlobStorageIntegration.md) |  | [optional] 
**azure_event_hubs** | [**AzureEventHubsIntegration**](AzureEventHubsIntegration.md) |  | [optional] 
**azure_service_bus** | [**AzureServiceBusIntegration**](AzureServiceBusIntegration.md) |  | [optional] 
**collections** | [**[Collection]**](Collection.md) | list of collections that use the integration | [optional] 
**created_at** | **str** | ISO-8601 date | [optional] 
**description** | **str** | longer explanation for the integration | [optional] 
**dynamodb** | [**DynamodbIntegration**](DynamodbIntegration.md) |  | [optional] 
**gcs** | [**GcsIntegration**](GcsIntegration.md) |  | [optional] 
**kafka** | [**KafkaIntegration**](KafkaIntegration.md) |  | [optional] 
**kinesis** | [**KinesisIntegration**](KinesisIntegration.md) |  | [optional] 
**mongodb** | [**MongoDbIntegration**](MongoDbIntegration.md) |  | [optional] 
**s3** | [**S3Integration**](S3Integration.md) |  | [optional] 
**segment** | [**SegmentIntegration**](SegmentIntegration.md) |  | [optional] 
**snowflake** | [**SnowflakeIntegration**](SnowflakeIntegration.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


