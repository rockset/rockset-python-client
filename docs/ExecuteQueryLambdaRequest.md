# ExecuteQueryLambdaRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_async** | **bool** | If true, the query will run asynchronously for up to 30 minutes. The query request will immediately return with a query id that can be used to retrieve the query status and results. If false or not specified, the query will return with results once completed or timeout after 2 minutes. (To return results directly for shorter queries while still allowing a timeout of up to 30 minutes, set &#x60;async_options.client_timeout_ms&#x60;.)  | [optional] 
**async_options** | [**AsyncQueryOptions**](AsyncQueryOptions.md) |  | [optional] 
**debug_threshold_ms** | **int** | If query execution takes longer than this value, debug information will be logged. If the query text includes the DEBUG hint and this parameter is also provided, only this value will be used and the DEBUG hint will be ignored. | [optional] 
**default_row_limit** | **int** | Row limit to use if no limit specified in the SQL query text. | [optional] 
**generate_warnings** | **bool** | Whether to generate warnings. | [optional] 
**initial_paginate_response_doc_count** | **int** | [DEPRECATED] Use &#x60;max_initial_results&#x60; instead. Number of documents to return in addition to paginating for this query call. Only relevant if &#x60;paginate&#x60; flag is also set. | [optional] 
**max_initial_results** | **int** | This limits the maximum number of results in the initial response. A pagination cursor is returned if the number of results exceeds &#x60;max_initial_results&#x60;. If &#x60;max_initial_results&#x60; is not set, all results will be returned in the initial response up to 4 million. If &#x60;max_initial_results&#x60; is set, the value must be between 0 and 100,000. If the query is async and &#x60;client_timeout_ms&#x60; is exceeded, &#x60;max_initial_results&#x60; does not apply since none of the results will be returned with the initial response. | [optional] 
**paginate** | **bool** | Flag to paginate and store the results of this query for later / sequential retrieval. | [optional] 
**parameters** | [**[QueryParameter]**](QueryParameter.md) | List of named parameters. | [optional] 
**timeout_ms** | **int** | If a query exceeds the specified timeout, the query will automatically stop and return an error. The query timeout defaults to a maximum of 2 minutes. If &#x60;async&#x60; is true, the query timeout defaults to a maximum of 30 minutes. | [optional] 
**virtual_instance_id** | **str** | Virtual instance on which to run the query. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


