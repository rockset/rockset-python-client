# QueryInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executed_by** | **str** | User ID who executed the query. | [optional] 
**expires_at** | **str** | Time (UTC) that query results expire. Only populated if &#x60;status&#x60; is &#x60;COMPLETE&#x60;. | [optional] 
**last_offset** | **str** | The log offset that query results were written to in the destination collection. Only populated for INSERT INTO queries. | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**query_errors** | [**[QueryError]**](QueryError.md) | Errors encountered while executing the query. | [optional] 
**query_id** | **str** | Unique Query ID. | [optional] 
**stats** | [**Stats**](Stats.md) |  | [optional] 
**status** | **str** | Status of the query. | [optional] 
**submitted_at** | **str** | Time (UTC) the query request was first received and queued for execution. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


