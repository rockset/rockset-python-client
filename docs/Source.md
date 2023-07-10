# Source

Details about the data source for the given collection. Only one of the following fields are allowed to be defined. Only collections can act as data sources for views. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azure_blob_storage** | [**SourceAzureBlobStorage**](SourceAzureBlobStorage.md) |  | [optional] 
**azure_event_hubs** | [**SourceAzureEventHubs**](SourceAzureEventHubs.md) |  | [optional] 
**azure_service_bus** | [**SourceAzureServiceBus**](SourceAzureServiceBus.md) |  | [optional] 
**dynamodb** | [**SourceDynamoDb**](SourceDynamoDb.md) |  | [optional] 
**file_upload** | [**SourceFileUpload**](SourceFileUpload.md) |  | [optional] 
**format_params** | [**FormatParams**](FormatParams.md) |  | [optional] 
**gcs** | [**SourceGcs**](SourceGcs.md) |  | [optional] 
**id** | **str** | Unique source identifier. | [optional] 
**integration_name** | **str** | Name of integration to use. | [optional] 
**kafka** | [**SourceKafka**](SourceKafka.md) |  | [optional] 
**kinesis** | [**SourceKinesis**](SourceKinesis.md) |  | [optional] 
**mongodb** | [**SourceMongoDb**](SourceMongoDb.md) |  | [optional] 
**s3** | [**SourceS3**](SourceS3.md) |  | [optional] 
**snowflake** | [**SourceSnowflake**](SourceSnowflake.md) |  | [optional] 
**status** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**system** | [**SourceSystem**](SourceSystem.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


