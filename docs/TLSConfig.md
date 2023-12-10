# TLSConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_cert** | **str** | PEM-formatted certificate chain to use for client authentication | 
**client_key** | **str** | PEM-formatted private key to be used for client authentication | 
**ca_cert** | **str** | PEM-formatted certificate chain of the Certificate Authority used to verify remote server. If empty, Rockset, will use publicly trusted CAs | [optional] 
**client_cert_expiry** | **int** | Expiration date of the client certificate (represented as number of ms since epoch) | [optional] [readonly] 
**client_cert_subject** | **str** | Subject of the client certificate, containing common name and other attributes | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


