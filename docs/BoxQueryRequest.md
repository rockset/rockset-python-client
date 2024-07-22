# BoxQueryRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **bool** | Whether to return the total count of documents in the response | [optional] 
**limit** | **int** | The max results to return | [optional] 
**offset** | **int** | Skip over these many many top results | [optional] 
**select** | **[str]** | The fields to return from matched documents | [optional] 
**text_search** | [**BoxFullTextQuery**](BoxFullTextQuery.md) |  | [optional] 
**vector_queries** | [**[BoxVectorQuery]**](BoxVectorQuery.md) | The vector queries to make against this dataset | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


