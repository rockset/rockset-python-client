# Status


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detected_size_bytes** | **int** | Size in bytes detected for the source at collection initialization. This size can be 0 or null for event stream sources. | [optional] 
**last_processed_at** | **str** | ISO-8601 date when source was last processed. | [optional] 
**last_processed_item** | **str** | Last source item processed by ingester. | [optional] 
**message** | **str** | State message. | [optional] 
**state** | **str** | Status of the Source&#39;s ingestion. | [optional] 
**total_processed_items** | **int** | Total items processed of source. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


