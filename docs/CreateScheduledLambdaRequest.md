# CreateScheduledLambdaRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apikey** | **str** | The apikey to use when triggering execution of the associated query lambda. | 
**cron_string** | **str** | The UNIX-formatted cron string for this scheduled query lambda. | 
**ql_name** | **str** | The name of the QL to use for scheduled execution. | 
**tag** | **str** | The QL tag to use for scheduled execution. One of either the QL tag or version must be specified | [optional] 
**total_times_to_execute** | **int** | The number of times to execute this scheduled query lambda. Once this scheduled query lambda has been executed this many times, it will no longer be executed. | [optional] 
**version** | **str** | The version of the QL to use for scheduled execution. One of either the QL version or tag must be specified. | [optional] 
**webhook_auth_header** | **str** | The value to use as the authorization header when hitting the webhook. | [optional] 
**webhook_payload** | **str** | The payload that should be sent to the webhook. JSON format. | [optional] 
**webhook_url** | **str** | The URL of the webhook that should be triggered after this scheduled query lambda completes. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


