# BulkStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_downloaded_bytes** | **int** | Size in bytes of documents downloaded from source during an ongoing or completed bulk ingest. This includes documents that are dropped and reingested. | [optional] 
**data_indexed_bytes** | **int** | Size in bytes of documents indexed. This is the total size of documents after transformations and dropping before indexes are built. | [optional] 
**data_indexed_throughput_bytes** | **float** | Throughput of documents indexed in the last minute measured in bytes/s. This is based off the data_indexed_bytes size. Throughput during the download stage is shown on a per-source granularity in the sources field of the Collection response. | [optional] 
**documents_downloaded** | **int** | Number of documents downloaded from source during an ongoing or completed bulk ingest. This includes documents that are dropped and reingested. | [optional] 
**download_compute_ms** | **int** | Bulk ingest compute units in milliseconds used for downloading documents. | [optional] 
**downloading_stage_done_at** | **str** | ISO-8601 date of when the downloading stage was completed. | [optional] 
**finalizing_stage_done_at** | **str** | ISO-8601 date of when the finalizing stage was completed. | [optional] 
**index_compute_ms** | **int** | Bulk ingest compute units in milliseconds used for indexing documents. | [optional] 
**indexing_stage_done_at** | **str** | ISO-8601 date of when the indexing stage was completed. | [optional] 
**initializing_stage_done_at** | **str** | ISO-8601 date of when the initializing stage was completed. | [optional] 
**pre_index_size_bytes** | **int** | Size in bytes of documents before being indexed. This is the total size of documents after decompression, transformations, and dropping. This is equal to data_indexed_bytes after the indexing stage is done unless there are retries during indexing the data. | [optional] 
**provisioning_stage_done_at** | **str** | ISO-8601 date of when the provisioning stage was completed. | [optional] 
**started_at** | **str** | ISO-8601 date of when the bulk ingest was started. | [optional] 
**total_index_size_bytes** | **int** | Total size of indexes after the completed bulk ingest. This is the same as collection size. | [optional] 
**transformation_compute_ms** | **int** | Bulk ingest compute units in milliseconds used for ingest transformation. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


