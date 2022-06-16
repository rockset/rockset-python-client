# KafkaIntegration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootstrap_servers** | **str** |  | [optional] 
**connection_string** | **str** | kafka connection string | [optional] [readonly] 
**kafka_data_format** | **str** | The format of the Kafka topics being tailed | [optional] 
**kafka_topic_names** | **[str]** | Kafka topics to tail | [optional] 
**schema_registry_config** | [**SchemaRegistryConfig**](SchemaRegistryConfig.md) |  | [optional] 
**security_config** | [**KafkaV3SecurityConfig**](KafkaV3SecurityConfig.md) |  | [optional] 
**source_status_by_topic** | [**{str: (StatusKafka,)}**](StatusKafka.md) | The status of the Kafka source by topic | [optional] [readonly] 
**use_v3** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


