# KinesisCollectionCreationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | unique identifier for collection, can contain alphanumeric or dash characters | 
**clustering_key** | [**[FieldPartition]**](FieldPartition.md) | list of clustering fields | [optional] 
**description** | **str** | text describing the collection | [optional] 
**event_time_info** | [**EventTimeInfo**](EventTimeInfo.md) |  | [optional] 
**field_mapping_query** | [**FieldMappingQuery**](FieldMappingQuery.md) |  | [optional] 
**field_mappings** | [**[FieldMappingV2]**](FieldMappingV2.md) | list of mappings | [optional] 
**insert_only** | **bool** | If true disallows updates and deletes, but makes indexing more efficient | [optional] 
**retention_secs** | **int** | number of seconds after which data is purged, based on event time | [optional] 
**sources** | [**[KinesisSourceWrapper]**](KinesisSourceWrapper.md) | List of sources from which to ingest data | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


