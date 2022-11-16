# KinesisSourceWrapper

Details about the data source for the given collection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stream_name** | **str** | Name of kinesis stream. | 
**format_params** | [**FormatParams**](FormatParams.md) |  | [optional] 
**integration_name** | **str** | Name of integration to use. | [optional] 
**status** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] [readonly] 
**aws_region** | **str** | AWS region name of Kinesis stream, by default us-west-2 is used. | [optional] 
**dms_primary_key** | **[str]** | Set of fields that correspond to a DMS primary key. | [optional] 
**offset_reset_policy** | **str** | For non-DMS streams, Rockset can tail from the earliest end or latest end of kinesis source. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


