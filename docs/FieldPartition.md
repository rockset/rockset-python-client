# FieldPartition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | The name of a field, parsed as a SQL qualified name. | [optional] 
**keys** | **[str]** | The values for partitioning of a field. Unneeded if the partition type is AUTO. | [optional] 
**type** | **str** | The type of partitions on a field. | [optional]  if omitted the server will use the default value of "AUTO"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


