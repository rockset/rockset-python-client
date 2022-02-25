# StatusKafka

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | State of the Kafka source | [optional] 
**last_consumed_time** | **str** | Time at which the last document was consumed from Kafka | [optional] 
**num_documents_processed** | **int** | Number of documents consumed by this Kafka topic | [optional] 
**kafka_partitions** | [**list[StatusKafkaPartition]**](StatusKafkaPartition.md) | Status info per partition | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


