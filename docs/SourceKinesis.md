# SourceKinesis


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stream_name** | **str** | name of kinesis stream | 
**aws_region** | **str** | AWS region name of Kinesis stream, by default us-west-2 is used | [optional] 
**dms_primary_key** | **[str]** | set of fields that correspond to a DMS primary key | [optional] 
**offset_reset_policy** | **str** | For non-DMS streams, Rockset can tail from the earliest end or latest end of kinesis source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


