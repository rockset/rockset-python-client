# UpdateScheduledLambdaRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apikey** | **str** | The apikey to use when triggering execution of the associated query lambda. | [optional] 
**resume_permanent_error** | **bool** | Boolean flag to allow a scheduled query lambda to resume execution after being suspended due to execution failure. This flag will be unset after scheduled lambda execution. | [optional] 
**total_times_to_execute** | **int** | The number of times to execute this scheduled query lambda. | [optional] 
**webhook_auth_header** | **str** | The value to use as the authorization header when hitting the webhook. | [optional] 
**webhook_payload** | **str** | The payload that should be sent to the webhook. JSON format. | [optional] 
**webhook_url** | **str** | The URL of the webhook that should be triggered after this scheduled query lambda completes. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


