# Collection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | ISO-8601 date | [optional] 
**created_by** | **str** | email of user who created the collection | [optional] 
**name** | **str** | unique identifer for collection, can contain alphanumeric or dash characters | [optional] 
**description** | **str** | text describing the collection | [optional] 
**workspace** | **str** | name of the workspace that the collection is in | [optional] 
**status** | **str** | current status of collection, one of: CREATED, READY, DELETED | [optional] 
**sources** | [**list[Source]**](Source.md) | list of sources from which collection ingests | [optional] 
**stats** | [**CollectionStats**](CollectionStats.md) | metrics about the collection | [optional] 
**retention_secs** | **int** | number of seconds after which data is purged based on event time | [optional] 
**field_mappings** | [**list[FieldMappingV2]**](FieldMappingV2.md) | list of mappings applied on all documents in a collection | [optional] 
**field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) | Field mapping for a collection | [optional] 
**clustering_key** | [**list[FieldPartition]**](FieldPartition.md) | list of clustering fields for a collection | [optional] 
**aliases** | [**list[Alias]**](Alias.md) | list of aliases for a collection | [optional] 
**field_schemas** | [**list[FieldSchema]**](FieldSchema.md) | list of field schemas  | [optional] 
**inverted_index_group_encoding_options** | [**InvertedIndexGroupEncodingOptions**](InvertedIndexGroupEncodingOptions.md) | inverted index group encoding options | [optional] 
**field_partitions** | [**list[FieldPartition]**](FieldPartition.md) |  | [optional] 
**insert_only** | **bool** | Whether the collection is insert only or not | [optional] 
**enable_exactly_once_writes** | **bool** | If true, exactly-once write semantics is enabled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


