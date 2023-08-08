# S3CollectionCreationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique identifier for collection, can contain alphanumeric or dash characters. | 
**clustering_key** | [**[FieldPartition]**](FieldPartition.md) | Deprecated. List of clustering fields. Use CLUSTER BY clause in &#x60;field_mapping_query&#x60; instead. | [optional] 
**description** | **str** | Text describing the collection. | [optional] 
**event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional] 
**field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional] 
**retention_secs** | **int** | Number of seconds after which data is purged, based on event time. | [optional] 
**source_download_soft_limit_bytes** | **int** | Soft ingest limit for this collection. | [optional] 
**sources** | [**[S3SourceWrapper]**](S3SourceWrapper.md) | List of sources from which to ingest data | [optional] 
**storage_compression_type** | **str** | RocksDB storage compression type. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


