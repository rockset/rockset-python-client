# StatusMongoDb

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scan_start_time** | **str** | MongoDB scan start time | [optional] 
**scan_end_time** | **str** | MongoDB scan end time | [optional] 
**scan_records_processed** | **int** | Number of records inserted using scan | [optional] 
**scan_total_records** | **int** | Number of records in MongoDB table at time of scan | [optional] 
**state** | **str** | state of current ingest for this table | [optional] 
**stream_last_insert_processed_at** | **str** | ISO-8601 date when new insert from source was last processed | [optional] 
**stream_last_update_processed_at** | **str** | ISO-8601 date when update from source was last processed | [optional] 
**stream_last_delete_processed_at** | **str** | ISO-8601 date when delete from source was last processed | [optional] 
**stream_records_inserted** | **int** | Number of new records inserted using stream | [optional] 
**stream_records_updated** | **int** | Number of new records updated using stream | [optional] 
**stream_records_deleted** | **int** | Number of new records deleted using stream | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


