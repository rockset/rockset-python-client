# AutoScalingPolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether auto scaling policy is enabled. | [optional] 
**max_size** | **str** | Maximum size Rockset can auto scale the Virtual Instance to. This value should be one of the dedicated sizes greater than or same as the min_size and lower than or same as the current size. | [optional] 
**min_size** | **str** | Minimum size Rockset can auto scale the Virtual Instance to. This value should be one of the dedicated sizes lower than or same as the max_size and greater than or same as the current size. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


