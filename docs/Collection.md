# Collection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**[Alias]**](Alias.md) | List of aliases for a collection. | [optional] 
**bulk_stats** | [**[BulkStats]**](BulkStats.md) |  | [optional] 
**clustering_key** | [**[FieldPartition]**](FieldPartition.md) | List of clustering fields for a collection. | [optional] 
**created_at** | **str** | ISO-8601 date. | [optional] 
**created_by** | **str** | Email of user who created the collection. | [optional] 
**description** | **str** | Text describing the collection. | [optional] 
**field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional] 
**field_mappings** | [**[FieldMappingV2]**](FieldMappingV2.md) | List of mappings applied on all documents in a collection. | [optional] 
**insert_only** | **bool** | Whether the collection is insert only or not. | [optional] 
**name** | **str** | Unique identifer for collection, can contain alphanumeric or dash characters. | [optional] 
**read_only** | **bool** | Whether the collection is read-only or not. | [optional] 
**retention_secs** | **int** | Number of seconds after which data is purged based on event time. | [optional] 
**sources** | [**[Source]**](Source.md) | List of sources from which collection ingests. | [optional] 
**stats** | [**CollectionStats**](CollectionStats.md) |  | [optional] 
**status** | **str** | Current status of collection. | [optional] 
**workspace** | **str** | Name of the workspace that the collection is in. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


