# S3SourceWrapper

Details about the data source for the given collection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** | address of S3 bucket containing data | 
**prefixes** | **[str]** | list of prefixes to paths from which data should be ingested | [readonly] 
**format_params** | [**FormatParams**](FormatParams.md) |  | [optional] 
**integration_name** | **str** | name of integration to use | [optional] 
**status** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**object_bytes_total** | **int** |  | [optional] [readonly] 
**object_count_downloaded** | **int** |  | [optional] [readonly] 
**object_count_total** | **int** |  | [optional] [readonly] 
**pattern** | **str** | Glob-style pattern that selects keys to ingest. Only either prefix or pattern can be specified. | [optional] 
**prefix** | **str** | Prefix that selects keys to ingest. | [optional] 
**region** | **str** | AWS region containing source bucket | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


