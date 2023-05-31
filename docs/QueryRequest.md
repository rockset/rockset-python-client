# QueryRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sql** | [**QueryRequestSql**](QueryRequestSql.md) |  | 
**async_options** | [**AsyncQueryOptions**](AsyncQueryOptions.md) |  | [optional] 
**timeout_ms** | **int** | The maximum amount of time that the system will attempt to complete query execution before aborting the query and returning an error. The maximum value for this timeout is 2 minutes. async_options.timeout_ms will override this timeout. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


