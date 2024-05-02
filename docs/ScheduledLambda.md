# ScheduledLambda


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron_string** | **str** | The UNIX-formatted cron string for this scheduled query lambda. | [optional] 
**execution_count** | **int** | The number of times this scheduled QL has been executed. | [optional] 
**last_completion_date** | **str** | The last time this scheduled query lambda completed successfully. | [optional] 
**last_query_id** | **str** | The ID of the query that was triggered by this scheduled lambda&#39;s last run. | [optional] 
**next_execution_date** | **str** | The next time this scheduled query lambda will be executed. | [optional] 
**ql_name** | **str** | The name of the associated query lambda. | [optional] 
**query_execution_status** | [**ExecutionStatus**](ExecutionStatus.md) |  | [optional] 
**resume_permanent_error** | **bool** | Boolean flag to allow a scheduled query lambda to resume execution after being suspended due to execution failure. This flag will be unset after scheduled lambda execution. | [optional] 
**rrn** | **str** | Scheduled Lambda mapping RRN. | [optional] 
**tag** | **str** | The query lambda tag. | [optional] 
**total_times_to_execute** | **int** | The number of times to execute this scheduled query lambda. Once this scheduled query lambda has been executed this many times, it will no longer be executed. | [optional] 
**version** | **str** | The version of the associated query lambda. | [optional] 
**webhook_execution_status** | [**ExecutionStatus**](ExecutionStatus.md) |  | [optional] 
**webhook_payload** | **str** | The payload that should be sent to the webhook. | [optional] 
**webhook_url** | **str** | The URL of the webhook that should be triggered after this scheduled query lambda completes. | [optional] 
**workspace** | **str** | Workspace of the associated query lambda. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


