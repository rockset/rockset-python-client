# QueryRequestSql

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | SQL query string. | 
**generate_warnings** | **bool** | Flag to enable warnings. Warnings can help debug query issues but negatively affect performance. | [optional] 
**profiling_enabled** | **bool** | Flag to generate a performance profile for this query. | [optional] 
**parameters** | [**list[QueryParameter]**](QueryParameter.md) | List of named parameters. | [optional] 
**default_row_limit** | **int** | Row limit to use. Limits specified in the query text will override this default. | [optional] 
**paginate** | **bool** | Flag to paginate and store the results of this query for later / sequential retrieval. | [optional] 
**initial_paginate_response_doc_count** | **int** | Number of documents to return in addition to paginating for this query call. Only relevant if &#x60;paginate&#x60; flag is also set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


