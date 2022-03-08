# rockset.QueriesApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query**](QueriesApi.md#query) | **POST** /v1/orgs/self/queries | Query
[**validate**](QueriesApi.md#validate) | **POST** /v1/orgs/self/queries/validations | Validate Query


# **query**
> QueryResponse query(query_request)

Query

Make a SQL query to Rockset.

### Example


```python
import time
import rockset
from rockset.api import queries_api
from rockset.model.error_model import ErrorModel
from rockset.model.query_request import QueryRequest
from rockset.model.query_response import QueryResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = queries_api.QueriesApi(api_client)
    query_request = QueryRequest(
        sql=QueryRequestSql(
            default_row_limit=1,
            generate_warnings=True,
            initial_paginate_response_doc_count=1,
            paginate=True,
            parameters=[
                QueryParameter(
                    name="_id",
                    type="string",
                    value="85beb391",
                ),
            ],
            profiling_enabled=True,
            query="SELECT * FROM foo where _id = :_id",
        ),
    ) # QueryRequest | JSON object

    # example passing only required values which don't have defaults set
    try:
        # Query
        api_response = api_instance.query(query_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling QueriesApi->query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_request** | [**QueryRequest**](QueryRequest.md)| JSON object |

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query executed successfully |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate**
> ValidateQueryResponse validate(query_request)

Validate Query

Validate a SQL query with Rockset's parser and planner.

### Example


```python
import time
import rockset
from rockset.api import queries_api
from rockset.model.validate_query_response import ValidateQueryResponse
from rockset.model.error_model import ErrorModel
from rockset.model.query_request import QueryRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = queries_api.QueriesApi(api_client)
    query_request = QueryRequest(
        sql=QueryRequestSql(
            default_row_limit=1,
            generate_warnings=True,
            initial_paginate_response_doc_count=1,
            paginate=True,
            parameters=[
                QueryParameter(
                    name="_id",
                    type="string",
                    value="85beb391",
                ),
            ],
            profiling_enabled=True,
            query="SELECT * FROM foo where _id = :_id",
        ),
    ) # QueryRequest | JSON object

    # example passing only required values which don't have defaults set
    try:
        # Validate Query
        api_response = api_instance.validate(query_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling QueriesApi->validate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_request** | [**QueryRequest**](QueryRequest.md)| JSON object |

### Return type

[**ValidateQueryResponse**](ValidateQueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | query validated successfully |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

