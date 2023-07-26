# SourceS3


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** | Address of S3 bucket containing data. | 
**object_bytes_downloaded** | **int** |  | [optional] [readonly] 
**object_bytes_total** | **int** |  | [optional] [readonly] 
**object_count_downloaded** | **int** |  | [optional] [readonly] 
**object_count_total** | **int** |  | [optional] [readonly] 
**pattern** | **str** | Glob-style pattern that selects keys to ingest. Only either prefix or pattern can be specified. | [optional] 
**prefix** | **str** | Prefix that selects keys to ingest. | [optional] 
**prefixes** | **[str]** | List of prefixes to paths from which data should be ingested. | [optional] [readonly] 
**region** | **str** | AWS region containing source bucket. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


