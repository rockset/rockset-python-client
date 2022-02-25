# QueryLambdaVersion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace** | **str** | workspace of this Query Lambda | [optional] 
**created_by** | **str** | user that created this Query Lambda | [optional] 
**created_at** | **str** | ISO-8601 date of when Query Lambda was created | [optional] 
**name** | **str** | Query Lambda name | [optional] 
**version** | **str** | Query Lambda version | [optional] 
**description** | **str** | optional description | [optional] 
**sql** | [**QueryLambdaSql**](QueryLambdaSql.md) | Query Lambda SQL query | [optional] 
**collections** | **list[str]** | collections queried by underlying SQL query | [optional] 
**state** | **str** | status of this Query Lambda | [optional] 
**stats** | [**QueryLambdaStats**](QueryLambdaStats.md) | stats related to this Query Lambda | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


