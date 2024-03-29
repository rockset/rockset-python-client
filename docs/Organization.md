# Organization

An organization in Rockset is a container for users and collections.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**[Cluster]**](Cluster.md) | List of clusters associated with this org. | [optional] 
**created_at** | **str** | ISO-8601 date. | [optional] 
**display_name** | **str** | Name of the organization. | [optional] 
**external_id** | **str** | Organization&#39;s unique external ID within Rockset. | [optional] 
**id** | **str** | Unique identifier for the organization. | [optional] 
**rockset_user** | **str** | Rockset&#39;s global AWS user. | [optional] 
**sso_connection** | **str** | Connection name of SSO connection. | [optional] 
**sso_only** | **bool** | Whether or not SSO is the only permitted form of auth. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


