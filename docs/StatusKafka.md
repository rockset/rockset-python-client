# StatusKafka


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kafka_partitions** | [**[StatusKafkaPartition]**](StatusKafkaPartition.md) | Status info per partition. | [optional] 
**last_consumed_time** | **str** | Time at which the last document was consumed from Kafka. | [optional] 
**num_documents_processed** | **int** | Number of documents consumed by this Kafka topic. | [optional] 
**state** | **str** | State of the Kafka source. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


