# AsyncQueryOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_timeout_ms** | **int** | If the query completes before the client timeout, the results are returned. Otherwise if the client timeout is exceeded, the query id will be returned, and the query will continue to run in the background for up to 30 minutes. (The 30 minute timeout can be configured lower with timeout_ms.) &#x60;async_options.client_timeout_ms&#x60; only applies when &#x60;async&#x60; is true. The default value of &#x60;client_timeout_ms&#x60; is 0, so async query requests will immediately return with a query id by default.  | [optional] 
**max_initial_results** | **int** | [DEPRECATED] Use the query request &#x60;max_initial_results&#x60; instead. The maximum number of results you will receive as a client. If the query exceeds this limit, the remaining results can be requested using a returned pagination cursor. In addition, there is a maximum response size of 100MiB so fewer than &#x60;max_results&#x60; may be returned. | [optional] 
**timeout_ms** | **int** | [DEPRECATED] Use the query request &#x60;timeout_ms&#x60; instead. The maximum amount of time that the system will attempt to complete query execution before aborting the query and returning an error. This must be set to a value that is greater than or equal to the client timeout, and the maximum value of this timeout is 30 minutes. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


