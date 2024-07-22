# UpdateVirtualInstanceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_scaling_policy** | [**AutoScalingPolicy**](AutoScalingPolicy.md) |  | [optional] 
**auto_suspend_enabled** | **bool** | Whether Query VI auto-suspend should be enabled for this Virtual Instance. | [optional] 
**auto_suspend_seconds** | **int** | Number of seconds without queries after which the Query VI is suspended | [optional] 
**description** | **str** | New virtual instance description. | [optional] 
**enable_remount_on_resume** | **bool** | When a Virtual Instance is resumed, it will remount all collections that were mounted when the Virtual Instance was suspended. | [optional] 
**instance_class** | **str** | Virtual Instance Class. Use &#x60;MO_IL&#x60; for Memory Optimized and &#x60;GP_IL&#x60; for General Purpose instance class. | [optional] 
**microbatch_policy** | [**MicrobatchPolicy**](MicrobatchPolicy.md) |  | [optional] 
**name** | **str** | New virtual instance name. | [optional] 
**new_size** | **str** | Requested virtual instance size. | [optional] 
**settings** | [**UpdateVirtualInstanceSettingsRequest**](UpdateVirtualInstanceSettingsRequest.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


