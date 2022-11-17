# CreateIntegrationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Descriptive label. | 
**azure_blob_storage** | [**AzureBlobStorageIntegration**](AzureBlobStorageIntegration.md) |  | [optional] 
**azure_event_hubs** | [**AzureEventHubsIntegration**](AzureEventHubsIntegration.md) |  | [optional] 
**azure_service_bus** | [**AzureServiceBusIntegration**](AzureServiceBusIntegration.md) |  | [optional] 
**description** | **str** | Longer explanation for the integration. | [optional] 
**dynamodb** | [**DynamodbIntegration**](DynamodbIntegration.md) |  | [optional] 
**gcs** | [**GcsIntegration**](GcsIntegration.md) |  | [optional] 
**kafka** | [**KafkaIntegration**](KafkaIntegration.md) |  | [optional] 
**kinesis** | [**KinesisIntegration**](KinesisIntegration.md) |  | [optional] 
**mongodb** | [**MongoDbIntegration**](MongoDbIntegration.md) |  | [optional] 
**s3** | [**S3Integration**](S3Integration.md) |  | [optional] 
**snowflake** | [**SnowflakeIntegration**](SnowflakeIntegration.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


