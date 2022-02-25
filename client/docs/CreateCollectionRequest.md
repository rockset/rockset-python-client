# CreateCollectionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | unique identifier for collection, can contain alphanumeric or dash characters | 
**description** | **str** | text describing the collection | [optional] 
**sources** | [**list[Source]**](Source.md) | list of sources from which to ingest data | [optional] 
**retention_secs** | **int** | number of seconds after which data is purged, based on event time | [optional] 
**time_partition_resolution_secs** | **int** | If non-null, the collection will be time partitioned and each partition will be time_partition_resolution_secs wide. | [optional] 
**insert_only** | **bool** | If true disallows updates and deletes, but makes indexing more efficient | [optional] 
**event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) | configuration for event data | [optional] 
**field_mappings** | [**list[FieldMappingV2]**](FieldMappingV2.md) | list of mappings | [optional] 
**field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) | Mapping of fields for a collection | [optional] 
**clustering_key** | [**list[FieldPartition]**](FieldPartition.md) | list of clustering fields | [optional] 
**field_schemas** | [**list[FieldSchema]**](FieldSchema.md) | list of field schemas | [optional] 
**inverted_index_group_encoding_options** | [**InvertedIndexGroupEncodingOptions**](InvertedIndexGroupEncodingOptions.md) | inverted index group encoding options | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


