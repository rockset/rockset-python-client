# PatchOperation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | [JSON Patch operation](https://datatracker.ietf.org/doc/html/rfc6902#page-4) to be performed in this patch. Case insensitive. | 
**path** | **str** | [JSON Pointer](https://datatracker.ietf.org/doc/html/rfc6901) referencing a location in the target document where the operation is performed | 
**_from** | **str** | [JSON Pointer](https://datatracker.ietf.org/doc/html/rfc6901) referencing a location in the target document. Required for &#x60;COPY&#x60; and &#x60;MOVE&#x60; operations. | [optional] 
**value** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Value used in the patch operation. Required for &#x60;ADD&#x60;, &#x60;REPLACE&#x60;, &#x60;TEST&#x60;, and &#x60;INCREMENT&#x60; operations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


