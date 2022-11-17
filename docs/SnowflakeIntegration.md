# SnowflakeIntegration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_warehouse** | **str** | default snowflake data warehouse name for query execution. Warehouse name can be overridden in the collection. | 
**password** | **str** | Snowflake database password. | 
**s3_export_path** | **str** | S3 path used for running &#39;COPY INTO&#39; command on snowflake table. | 
**snowflake_url** | **str** | Snowflake browser url. | 
**username** | **str** | Snowflake database username. | 
**aws_access_key** | [**AwsAccessKey**](AwsAccessKey.md) |  | [optional] 
**aws_role** | [**AwsRole**](AwsRole.md) |  | [optional] 
**user_role** | **str** | Snowflake user role. If unspecified, will use the default user role. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


