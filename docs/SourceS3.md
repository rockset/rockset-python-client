# SourceS3


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** | address of S3 bucket containing data | 
**prefixes** | **[str]** | list of prefixes to paths from which data should be ingested | [readonly] 
**access_key** | **str** | AWS credential with ListObjects and GetObject access | [optional] [readonly] 
**format** | **str** | do not use | [optional]  if omitted the server will use the default value of "JSON"
**mappings** | [**[FieldMask]**](FieldMask.md) | custom transformation on data field | [optional] 
**object_bytes_total** | **int** |  | [optional] 
**object_count_downloaded** | **int** |  | [optional] 
**object_count_total** | **int** |  | [optional] 
**pattern** | **str** | Glob-style pattern that selects keys to ingest. Only either prefix or pattern can be specified. | [optional] 
**prefix** | **str** | Prefix that selects keys to ingest. | [optional] 
**region** | **str** | AWS region containing source bucket | [optional] 
**secret_access** | **str** | AWS credential with ListObjects and GetObject access | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


