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
**mount_refresh_interval_seconds** | **int** | DEPRECATED. Use &#x60;mount_type&#x60; instead. Number of seconds between data refreshes for mounts on this Virtual Instance. The only valid values are 0 and null. 0 means the data will be refreshed continuously and null means the data will never refresh. | [optional] 
**mount_type** | **str** | The mount type of collections that this Virtual Instance will query. Live mounted collections stay up-to-date with the underlying collection in real-time. Static mounted collections do not stay up-to-date. See https://docs.rockset.com/documentation/docs/virtual-instances#virtual-instance-configuration | [optional] 
**name** | **str** | New virtual instance name. | [optional] 
**new_size** | **str** | Requested virtual instance size. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


