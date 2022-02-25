# ExecuteQueryLambdaRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**list[QueryParameter]**](QueryParameter.md) | list of named parameters | [optional] 
**default_row_limit** | **int** | Row limit to use if no limit specified in the SQL query text | [optional] 
**generate_warnings** | **bool** | Whether to generate warnings | [optional] 
**paginate** | **bool** | Flag to paginate and store the results of this query for later / sequential retrieval. | [optional] 
**initial_paginate_response_doc_count** | **int** | Number of documents to return in addition to paginating for this query call. Only relevant if &#x60;paginate&#x60; flag is also set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


