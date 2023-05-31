# AsyncQueryOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_timeout_ms** | **int** | The maximum amount of time that the client is willing to wait for the query to complete. If the query is not complete by this timeout, a response will be returned with a &#x60;query_id&#x60; that can be used to check the status of the query and retrieve results once the query has completed. | [optional] 
**max_initial_results** | **int** | The maximum number of results you will receive as a client. If the query exceeds this limit, the remaining results can be requested using a returned pagination cursor. In addition, there is a maximum response size of 100MiB so fewer than &#x60;max_results&#x60; may be returned. | [optional] 
**timeout_ms** | **int** | The maximum amount of time that the system will attempt to complete query execution before aborting the query and returning an error. This must be set to a value that is greater than or equal to the client timeout, and the maximum value of this timeout is 30 minutes. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


