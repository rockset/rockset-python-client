# Integration

Integrations that can be associated with data sources to create collections. Only one type of integration may be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | Email of user who created the integration. | 
**name** | **str** | Descriptive label and unique identifier. | 
**azure_blob_storage** | [**AzureBlobStorageIntegration**](AzureBlobStorageIntegration.md) |  | [optional] 
**azure_event_hubs** | [**AzureEventHubsIntegration**](AzureEventHubsIntegration.md) |  | [optional] 
**azure_service_bus** | [**AzureServiceBusIntegration**](AzureServiceBusIntegration.md) |  | [optional] 
**collections** | [**[Collection]**](Collection.md) | List of collections that use the integration. | [optional] 
**created_at** | **str** | ISO-8601 date. | [optional] 
**created_by_apikey_name** | **str** | Name of the API key that was used to create this object if one was used. | [optional] 
**description** | **str** | Longer explanation for the integration. | [optional] 
**dynamodb** | [**DynamodbIntegration**](DynamodbIntegration.md) |  | [optional] 
**gcs** | [**GcsIntegration**](GcsIntegration.md) |  | [optional] 
**is_write_enabled** | **bool** | is write access enabled for this integration | [optional] 
**kafka** | [**KafkaIntegration**](KafkaIntegration.md) |  | [optional] 
**kinesis** | [**KinesisIntegration**](KinesisIntegration.md) |  | [optional] 
**mongodb** | [**MongoDbIntegration**](MongoDbIntegration.md) |  | [optional] 
**owner_email** | **str** | User that owns this integration. | [optional] 
**s3** | [**S3Integration**](S3Integration.md) |  | [optional] 
**snowflake** | [**SnowflakeIntegration**](SnowflakeIntegration.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


