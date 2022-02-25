# Source

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_name** | **str** | name of integration to use | 
**s3** | [**SourceS3**](SourceS3.md) | configuration for ingestion from S3 | [optional] 
**kinesis** | [**SourceKinesis**](SourceKinesis.md) | configuration for ingestion from kinesis stream | [optional] 
**gcs** | [**SourceGcs**](SourceGcs.md) | configuration for ingestion from GCS | [optional] 
**azure_blob_storage** | [**SourceAzureBlobStorage**](SourceAzureBlobStorage.md) |  | [optional] 
**azure_service_bus** | [**SourceAzServiceBus**](SourceAzServiceBus.md) |  | [optional] 
**azure_event_hub** | [**SourceAzEventHub**](SourceAzEventHub.md) |  | [optional] 
**redshift** | [**SourceRedshift**](SourceRedshift.md) | configuration for ingestion from Redshift | [optional] 
**dynamodb** | [**SourceDynamoDb**](SourceDynamoDb.md) | configuration for ingestion from  a dynamodb table | [optional] 
**file_upload** | [**SourceFileUpload**](SourceFileUpload.md) | file upload details | [optional] 
**kafka** | [**SourceKafka**](SourceKafka.md) | kafka collection identifier | [optional] 
**mongodb** | [**SourceMongoDb**](SourceMongoDb.md) | MongoDB collection details | [optional] 
**status** | [**Status**](Status.md) | the ingest status of this source | [optional] 
**format_params** | [**FormatParams**](FormatParams.md) | format parameters for data from this source | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


