# Stats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed_time_ms** | **int** | Total execution time (including time queued) of the query, in milliseconds. | [optional] 
**result_set_bytes_size** | **int** | Number of bytes in the query result set. Only populated if &#x60;status&#x60; is &#x60;COMPLETE&#x60;. Not populated for INSERT INTO queries. | [optional] 
**result_set_document_count** | **int** | Number of documents returned by the query. Only populated if &#x60;status&#x60; is &#x60;COMPLETE&#x60;. | [optional] 
**result_set_file_count** | **int** | Number of files written by by the query. Only populated if &#x60;status&#x60; is &#x60;COMPLETE&#x60; and the query is an export query. | [optional] 
**throttled_time_ms** | **int** | Time query spent queued, in milliseconds. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


