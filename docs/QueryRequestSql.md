# QueryRequestSql


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | SQL query string. | 
**default_row_limit** | **int** | Row limit to use. Limits specified in the query text will override this default. | [optional] 
**generate_warnings** | **bool** | Flag to enable warnings. Warnings can help debug query issues but negatively affect performance. | [optional] 
**initial_paginate_response_doc_count** | **int** | [DEPRECATED] Use &#x60;max_initial_results&#x60; instead. Number of documents to return in addition to paginating for this query call. Only relevant if &#x60;paginate&#x60; flag is also set. | [optional] 
**parameters** | [**[QueryParameter]**](QueryParameter.md) | List of named parameters. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


