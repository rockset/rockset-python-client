# ApiKey

API keys are used to authenticate requests to Rockset's API. An API key is tied to the user who creates it.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | This field will only be populated with the full key when creating an API key. Otherwise, it will be an API key identifier of 6 characters. | 
**name** | **str** | Name of the API key. | 
**created_at** | **str** | Date that API key was created (ISO-8601 format). | [optional] 
**created_by** | **str** | Email of API key owner. | [optional] 
**created_by_apikey_name** | **str** | Name of the API key that was used to create this object if one was used. | [optional] 
**expiry_time** | **str** | The expiration date of this API key. | [optional] 
**last_access_time** | **str** | Date that API key was most recently used (ISO-8601 format). | [optional] 
**role** | **str** | Role specifying access control. If not specified, API key will have access to all of the associated user&#39;s roles. | [optional] 
**state** | **str** | Current state of this key. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


