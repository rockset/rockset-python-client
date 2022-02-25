# KafkaIntegration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kafka_topic_names** | **list[str]** | Kafka topics to tail | [optional] 
**source_status_by_topic** | [**dict(str, StatusKafka)**](StatusKafka.md) | The status of the Kafka source by topic | [optional] 
**kafka_data_format** | **str** | The format of the Kafka topics being tailed | [optional] 
**connection_string** | **str** | kafka connection string | [optional] 
**use_v3** | **bool** |  | [optional] 
**bootstrap_servers** | **str** |  | [optional] 
**security_config** | [**KafkaV3SecurityConfig**](KafkaV3SecurityConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


