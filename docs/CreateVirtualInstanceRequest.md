# CreateVirtualInstanceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique identifier for virtual instance, can contain alphanumeric or dash characters. | 
**auto_suspend_seconds** | **int** | Number of seconds without queries after which the VI is suspended | [optional] 
**description** | **str** | Description of requested virtual instance. | [optional] 
**enable_remount_on_resume** | **bool** | When a Virtual Instance is resumed, it will remount all collections that were mounted when the Virtual Instance was suspended. Defaults to true. | [optional] 
**instance_class** | **str** | Virtual Instance Class. Use &#x60;MO_IL&#x60; for Memory Optimized and &#x60;GP_IL&#x60; for General Purpose instance class. | [optional] 
**type** | **str** | Requested virtual instance type. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


