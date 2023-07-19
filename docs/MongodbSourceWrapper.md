# MongodbSourceWrapper

Details about the data source for the given collection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_name** | **str** | MongoDB collection name. | 
**database_name** | **str** | MongoDB database name containing this collection. | 
**format_params** | [**FormatParams**](FormatParams.md) |  | [optional] 
**integration_name** | **str** | Name of integration to use. | [optional] 
**retrieve_full_document** | **bool** | Whether to get the full document from the MongoDB change stream to enable multi-field expression transformations. Selecting this option will increase load on your upstream MongoDB database. | [optional] 
**status** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


