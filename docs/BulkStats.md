# BulkStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_downloaded_bytes** | **int** | Size in bytes of documents downloaded from source during an ongoing or completed bulk ingest. This includes documents that are dropped and reingested. | [optional] 
**data_indexed_bytes** | **int** | Size in bytes of documents indexed. This is the total size of documents after transformations and dropping before indexes are built. | [optional] 
**documents_downloaded** | **int** | Number of documents downloaded from source during an ongoing or completed bulk ingest. This includes documents that are dropped and reingested. | [optional] 
**download_compute_ms** | **int** | Bulk ingest compute units in milliseconds used for downloading documents. | [optional] 
**downloading_stage_done_at** | **str** | ISO-8601 date of when the downloading stage was completed. | [optional] 
**finalizing_stage_done_at** | **str** | ISO-8601 date of when the finalizing stage was completed. | [optional] 
**index_compute_ms** | **int** | Bulk ingest compute units in milliseconds used for indexing documents. | [optional] 
**indexing_stage_done_at** | **str** | ISO-8601 date of when the indexing stage was completed. | [optional] 
**initializing_stage_done_at** | **str** | ISO-8601 date of when the initializing stage was completed. | [optional] 
**provisioning_stage_done_at** | **str** | ISO-8601 date of when the provisioning stage was completed. | [optional] 
**started_at** | **str** | ISO-8601 date of when the bulk ingest was started. | [optional] 
**total_index_size_bytes** | **int** | Total size of indexes after the completed bulk ingest. This is the same as collection size. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


