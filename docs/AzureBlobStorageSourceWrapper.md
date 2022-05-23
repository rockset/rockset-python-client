# AzureBlobStorageSourceWrapper

Details about the data source for the given collection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format_params** | [**FormatParams**](FormatParams.md) |  | [optional] 
**integration_name** | **str** | name of integration to use | [optional] 
**status** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**blob_bytes_total** | **int** |  | [optional] [readonly] 
**blob_count_downloaded** | **int** |  | [optional] [readonly] 
**blob_count_total** | **int** |  | [optional] [readonly] 
**container** | **str** | name of Azure blob Storage container you want to ingest from | [optional] 
**pattern** | **str** | Glob-style pattern that selects keys to ingest. Only either prefix or pattern can be specified. | [optional] 
**prefix** | **str** | Prefix that selects blobs to ingest. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


