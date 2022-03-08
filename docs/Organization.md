# Organization

An organization in Rockset is a container for users and collections.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**[Cluster]**](Cluster.md) | list of clusters associated with this org | [optional] 
**created_at** | **str** | ISO-8601 date | [optional] 
**deletion_scheduled_at** | **str** |  | [optional] 
**display_name** | **str** | name of the organization | [optional] 
**external_id** | **str** | organization&#39;s unique external ID within Rockset | [optional] 
**id** | **str** | unique identifier for the organization | [optional] 
**rockset_user** | **str** | Rockset&#39;s global AWS user | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


