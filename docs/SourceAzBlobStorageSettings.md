# SourceAzBlobStorageSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azblob_scan_frequency** | **str** | Rockset scans an Azure blob Storage container based on a defined time interval. The scan frequency determines the length of time between a new scan and the previous scan. If the previous scan finds new objects or updates to existing objects, Rockset immediately scans the bucket again after processing changes from the previous scan. Duration value is of type ISO 8601 (e.g. PT5H, PT4M, PT3S). It doesn&#39;t account for DST, leap seconds and leap years. Minimum value: PT1S. Maximum value: PT1H. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


