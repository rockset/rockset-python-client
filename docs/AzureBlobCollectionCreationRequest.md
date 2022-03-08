# AzureBlobCollectionCreationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | unique identifier for collection, can contain alphanumeric or dash characters | 
**clustering_key** | [**[FieldPartition]**](FieldPartition.md) | list of clustering fields | [optional] 
**description** | **str** | text describing the collection | [optional] 
**event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional] 
**field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional] 
**field_mappings** | [**[FieldMappingV2]**](FieldMappingV2.md) | list of mappings | [optional] 
**field_schemas** | [**[FieldSchema]**](FieldSchema.md) | list of field schemas | [optional] 
**insert_only** | **bool** | If true disallows updates and deletes, but makes indexing more efficient | [optional] 
**inverted_index_group_encoding_options** | [**InvertedIndexGroupEncodingOptions**](InvertedIndexGroupEncodingOptions.md) |  | [optional] 
**retention_secs** | **int** | number of seconds after which data is purged, based on event time | [optional] 
**sources** | [**[AzureBlobStorageSourceWrapper]**](AzureBlobStorageSourceWrapper.md) | List of sources from which to ingest data | [optional] 
**time_partition_resolution_secs** | **int** | If non-null, the collection will be time partitioned and each partition will be time_partition_resolution_secs wide. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


