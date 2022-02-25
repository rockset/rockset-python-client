# SourceS3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** | AWS credential with ListObjects and GetObject access | [optional] 
**secret_access** | **str** | AWS credential with ListObjects and GetObject access | [optional] 
**prefix** | **str** | Prefix that selects keys to ingest. | [optional] 
**pattern** | **str** | Glob-style pattern that selects keys to ingest. Only either prefix or pattern can be specified. | [optional] 
**region** | **str** | AWS region containing source bucket | [optional] 
**bucket** | **str** | address of S3 bucket containing data | 
**prefixes** | **list[str]** | list of prefixes to paths from which data should be ingested | 
**format** | **str** | do not use | [optional] 
**mappings** | [**list[FieldMask]**](FieldMask.md) | custom transformation on data field | [optional] 
**object_count_downloaded** | **int** |  | [optional] 
**object_count_total** | **int** |  | [optional] 
**object_bytes_total** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


