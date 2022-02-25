# SourceDynamoDb

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_region** | **str** | AWS region name of DynamoDB table, by default us-west-2 is used | [optional] 
**table_name** | **str** | name of DynamoDB table containing data | 
**current_status** | [**StatusDynamoDbV2**](StatusDynamoDbV2.md) | DynamoDB source status v2 | [optional] 
**rcu** | **int** | Max RCU usage for scan | [optional] 
**status** | [**StatusDynamoDb**](StatusDynamoDb.md) | DynamoDB source status | [optional] 
**use_scan_api** | **bool** | Whether to use DynamoDB Scan API for the initial scan | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


