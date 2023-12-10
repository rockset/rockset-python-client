# SourceGcs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** | Name of GCS bucket you want to ingest from. | [optional] 
**object_bytes_downloaded** | **int** |  | [optional] [readonly] 
**object_bytes_total** | **int** |  | [optional] [readonly] 
**object_count_downloaded** | **int** |  | [optional] [readonly] 
**object_count_total** | **int** |  | [optional] [readonly] 
**pattern** | **str** | Glob-style pattern that selects keys to ingest. Only either prefix or pattern can be specified. | [optional] 
**prefix** | **str** | Prefix that selects keys to ingest. | [optional] 
**settings** | [**SourceGcsSettings**](SourceGcsSettings.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


