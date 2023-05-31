# CreateVirtualInstanceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique identifier for virtual instance, can contain alphanumeric or dash characters. | 
**auto_suspend_seconds** | **int** | Number of seconds without queries after which the VI is suspended | [optional] 
**description** | **str** | Description of requested virtual instance. | [optional] 
**enable_remount_on_resume** | **bool** | When a Virtual Instance is resumed, it will remount all collections that were mounted when the Virtual Instance was suspended. | [optional] 
**mount_refresh_interval_seconds** | **int** | Number of seconds between data refreshes for mounts on this Virtual Instance. A value of 0 means continuous refresh and a value of null means never refresh. | [optional] 
**type** | **str** | Requested virtual instance type. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


