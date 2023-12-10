# VirtualInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Virtual instance name. | 
**auto_scaling_policy** | [**AutoScalingPolicy**](AutoScalingPolicy.md) |  | [optional] 
**auto_suspend_seconds** | **int** | Number of seconds without queries after which the VI is suspended | [optional] 
**created_at** | **str** | ISO-8601 date of when virtual instance was created. | [optional] 
**created_by** | **str** | Creator of requested virtual instance. | [optional] 
**current_size** | **str** | Virtual instance current size. | [optional] [readonly] 
**default_pod_count** | **int** |  | [optional] 
**default_vi** | **bool** |  | [optional] 
**description** | **str** | Virtual instance description. | [optional] 
**desired_size** | **str** | Virtual instance desired size. | [optional] [readonly] 
**enable_remount_on_resume** | **bool** | When a Virtual Instance is resumed, it will remount all collections that were mounted when the Virtual Instance was suspended. | [optional] 
**id** | **str** | Unique identifier for virtual instance. | [optional] 
**monitoring_enabled** | **bool** |  | [optional] 
**mount_refresh_interval_seconds** | **int** | DEPRECATED. Number of seconds between data refreshes for mounts on this Virtual Instance | [optional] 
**mount_type** | **str** | The mount type of collections that this Virtual Instance will query. Live mounted collections stay up-to-date with the underlying collection in real-time. Static mounted collections do not stay up-to-date. See https://docs.rockset.com/documentation/docs/virtual-instances#virtual-instance-configuration | [optional] 
**resumed_at** | **str** | ISO-8601 date of when virtual instance was created. | [optional] 
**rrn** | **str** | Virtual Instance RRN. | [optional] 
**scaled_pod_count** | **int** |  | [optional] 
**state** | **str** | Virtual instance state. | [optional] 
**stats** | [**VirtualInstanceStats**](VirtualInstanceStats.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


