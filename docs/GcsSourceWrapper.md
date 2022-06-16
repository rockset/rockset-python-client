# GcsSourceWrapper

Details about the data source for the given collection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format_params** | [**FormatParams**](FormatParams.md) |  | [optional] 
**integration_name** | **str** | name of integration to use | [optional] 
**status** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**bucket** | **str** | name of GCS bucket you want to ingest from | [optional] 
**object_bytes_total** | **int** |  | [optional] [readonly] 
**object_count_downloaded** | **int** |  | [optional] [readonly] 
**object_count_total** | **int** |  | [optional] [readonly] 
**pattern** | **str** | Glob-style pattern that selects keys to ingest. Only either prefix or pattern can be specified. | [optional] 
**prefix** | **str** | Prefix that selects keys to ingest. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


