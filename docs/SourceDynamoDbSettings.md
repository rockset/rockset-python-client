# SourceDynamoDbSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamodb_stream_poll_frequency** | **str** | Each DynamoDB stream can have one to many shards, and Rockset polls each DynamoDB shard at a fixed rate. Decreasing the duration between polls helps reduce ingest latency, while increasing the duration can prevent  Rockset from keeping up with the updates. If the latency exceeds 24 hours (DynamoDB stream retention duration), Rockset will not be able to process all of the streaming updates. Each request also has a fixed price associated with it. Duration value is of type ISO 8601 (e.g. PT5H, PT4M, PT3S). It doesn&#39;t account for DST, leap seconds and leap years. Minimum value: PT0.25S. Maximum value: PT5M. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


