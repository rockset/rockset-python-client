# CreateIntegrationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | descriptive label | 
**description** | **str** | longer explanation for the integration | [optional] 
**s3** | [**S3Integration**](S3Integration.md) | Amazon S3 details, must have one of aws_access_key or aws_role | [optional] 
**kinesis** | [**KinesisIntegration**](KinesisIntegration.md) | Amazon Kinesis details, must have one of aws_access_key or aws_role | [optional] 
**dynamodb** | [**DynamodbIntegration**](DynamodbIntegration.md) | Amazon DynamoDB details, must have one of aws_access_key or aws_role | [optional] 
**redshift** | [**RedshiftIntegration**](RedshiftIntegration.md) | Amazon Redshift details | [optional] 
**gcs** | [**GcsIntegration**](GcsIntegration.md) | GCS details | [optional] 
**azure_blob_storage** | [**AzureBlobStorageIntegration**](AzureBlobStorageIntegration.md) | Azure Blob Storage details | [optional] 
**azure_event_hub** | [**AzEventHubIntegration**](AzEventHubIntegration.md) |  | [optional] 
**segment** | [**SegmentIntegration**](SegmentIntegration.md) |  | [optional] 
**kafka** | [**KafkaIntegration**](KafkaIntegration.md) |  | [optional] 
**mongodb** | [**MongoDbIntegration**](MongoDbIntegration.md) | MongoDb details | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


