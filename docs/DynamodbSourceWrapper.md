# DynamodbSourceWrapper

Details about the data source for the given collection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_name** | **str** | Name of DynamoDB table containing data. | 
**format_params** | [**FormatParams**](FormatParams.md) |  | [optional] 
**integration_name** | **str** | Name of integration to use. | [optional] 
**status** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**aws_region** | **str** | AWS region name of DynamoDB table, by default us-west-2 is used. | [optional] 
**current_status** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**rcu** | **int** | Max RCU usage for scan. | [optional] 
**use_scan_api** | **bool** | Whether to use DynamoDB Scan API for the initial scan. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


