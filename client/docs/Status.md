# Status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Status of the Source&#39;s ingestion, one of: INITIALIZING, WATCHING, PROCESSING, COMPLETED, ERROR | [optional] 
**message** | **str** | state message | [optional] 
**last_processed_at** | **str** | ISO-8601 date when source was last processed | [optional] 
**last_processed_item** | **str** | last source item processed by ingester | [optional] 
**total_processed_items** | **int** | Total items processed of source | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


