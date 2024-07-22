# BoxQueryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**box_rrn** | [**BoxRrn**](BoxRrn.md) |  | [optional] 
**column_fields** | [**[QueryFieldType]**](QueryFieldType.md) | Meta information about each column in the result set. Not populated in &#x60;SELECT *&#x60; queries. | [optional] 
**query_errors** | [**[QueryError]**](QueryError.md) | Errors encountered while executing the query. | [optional] 
**query_id** | **str** | Unique ID for this query. | [optional] 
**results** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** | Results from the query. | [optional] 
**stats** | [**QueryResponseStats**](QueryResponseStats.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


