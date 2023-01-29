# rockset.Queries

All URIs are relative to *https://api.use1a1.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_query**](QueriesApi.md#cancel_query) | **DELETE** /v1/orgs/self/queries/{queryId} | Cancel Query
[**get_query**](QueriesApi.md#get_query) | **GET** /v1/orgs/self/queries/{queryId} | Retrieve Query
[**get_query_results**](QueriesApi.md#get_query_results) | **GET** /v1/orgs/self/queries/{queryId}/pages | Retrieve Query Results Page
[**list_active_queries**](QueriesApi.md#list_active_queries) | **GET** /v1/orgs/self/queries | List Queries
[**query**](QueriesApi.md#query) | **POST** /v1/orgs/self/queries | Execute SQL Query
[**validate**](QueriesApi.md#validate) | **POST** /v1/orgs/self/queries/validations | Validate Query


# **cancel_query**
> CancelQueryResponse cancel_query(query_id)

Cancel Query

Attempts to cancel an actively-running query.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Cancel Query
api_response = rs.Queries.cancel_query(
    query_id="queryId_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Queries->cancel_query: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Cancel Query
api_response = await rs.Queries.cancel_query(
    query_id="queryId_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Queries->cancel_query: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str** |  |

### Return type

[**CancelQueryResponse**](CancelQueryResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully canceled query |  -  |
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

# **get_query**
> GetQueryResponse get_query(query_id)

Retrieve Query

Returns information about a query.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Retrieve Query
api_response = rs.Queries.get_query(
    query_id="queryId_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Queries->get_query: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Retrieve Query
api_response = await rs.Queries.get_query(
    query_id="queryId_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Queries->get_query: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str** |  |

### Return type

[**GetQueryResponse**](GetQueryResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched query info |  -  |
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

# **get_query_results**
> QueryPaginationResponse get_query_results(query_id)

Retrieve Query Results Page

Returns a page of query results.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Retrieve Query Results Page
api_response = rs.Queries.get_query_results(
    query_id="queryId_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Queries->get_query_results: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Retrieve Query Results Page
api_response = await rs.Queries.get_query_results(
    query_id="queryId_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Queries->get_query_results: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str** |  |
 **cursor** | **str** | Cursor to current page. If unset, will default to the first page. | [optional]
 **docs** | **int** | Number of documents to fetch. | [optional]

### Return type

[**QueryPaginationResponse**](QueryPaginationResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully fetched query results |  -  |
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

# **list_active_queries**
> ListQueriesResponse list_active_queries()

List Queries

Lists actively queued and running queries.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# List Queries
api_response = rs.Queries.list_active_queries(
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Queries->list_active_queries: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# List Queries
api_response = await rs.Queries.list_active_queries(
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Queries->list_active_queries: %s\n" % e)
    return
pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListQueriesResponse**](ListQueriesResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully fetched queries |  -  |
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

# **query**
> QueryResponse query(query_request)

Execute SQL Query

Make a SQL query to Rockset.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Execute SQL Query
api_response = rs.Queries.query(
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
        query="SELECT * FROM foo where _id = :_id",
    ),
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Queries->query: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Execute SQL Query
api_response = await rs.Queries.query(
    async_options=AsyncQueryOptions(
        client_timeout_ms=1,
        max_initial_results=1,
        timeout_ms=1,
    ),
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
        query="SELECT * FROM foo where _id = :_id",
    ),
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Queries->query: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_options** | [**AsyncQueryOptions**](AsyncQueryOptions.md) |  | [optional]
 **sql** | [**QueryRequestSql**](QueryRequestSql.md) |  | 

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Validate Query
api_response = rs.Queries.validate(
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
        query="SELECT * FROM foo where _id = :_id",
    ),
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Queries->validate: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Validate Query
api_response = await rs.Queries.validate(
    async_options=AsyncQueryOptions(
        client_timeout_ms=1,
        max_initial_results=1,
        timeout_ms=1,
    ),
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
        query="SELECT * FROM foo where _id = :_id",
    ),
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Queries->validate: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_options** | [**AsyncQueryOptions**](AsyncQueryOptions.md) |  | [optional]
 **sql** | [**QueryRequestSql**](QueryRequestSql.md) |  | 

### Return type

[**ValidateQueryResponse**](ValidateQueryResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


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

