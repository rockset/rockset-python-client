# rockset.QueryLambdas

All URIs are relative to *https://api.rs2.usw2.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_query_lambda**](QueryLambdas.md#create_query_lambda) | **POST** /v1/orgs/self/ws/{workspace}/lambdas | Create Query Lambda
[**create_query_lambda_tag**](QueryLambdas.md#create_query_lambda_tag) | **POST** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/tags | Create Query Lambda Tag
[**delete_query_lambda**](QueryLambdas.md#delete_query_lambda) | **DELETE** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda} | Delete Query Lambda
[**delete_query_lambda_tag**](QueryLambdas.md#delete_query_lambda_tag) | **DELETE** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/tags/{tag} | Delete Query Lambda Tag Version
[**delete_query_lambda_version**](QueryLambdas.md#delete_query_lambda_version) | **DELETE** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/version/{version} | Delete Query Lambda Version
[**execute_query_lambda**](QueryLambdas.md#execute_query_lambda) | **POST** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/versions/{version} | Execute Query Lambda By Version
[**execute_query_lambda_by_tag**](QueryLambdas.md#execute_query_lambda_by_tag) | **POST** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/tags/{tag} | Execute Query Lambda By Tag
[**get_query_lambda_tag_version**](QueryLambdas.md#get_query_lambda_tag_version) | **GET** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/tags/{tag} | Retrieve Query Lambda Tag
[**get_query_lambda_version**](QueryLambdas.md#get_query_lambda_version) | **GET** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/versions/{version} | Retrieve Query Lambda Version
[**list_all_query_lambdas**](QueryLambdas.md#list_all_query_lambdas) | **GET** /v1/orgs/self/lambdas | List Query Lambdas
[**list_query_lambda_tags**](QueryLambdas.md#list_query_lambda_tags) | **GET** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/tags | List Query Lambda Tags
[**list_query_lambda_versions**](QueryLambdas.md#list_query_lambda_versions) | **GET** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/versions | List Query Lambda Versions
[**list_query_lambdas_in_workspace**](QueryLambdas.md#list_query_lambdas_in_workspace) | **GET** /v1/orgs/self/ws/{workspace}/lambdas | List Query Lambdas in Workspace
[**update_query_lambda**](QueryLambdas.md#update_query_lambda) | **POST** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/versions | Update Query Lambda


# **create_query_lambda**
> QueryLambdaVersionResponse create_query_lambda(create_query_lambda_request)

Create Query Lambda

Create a Query Lambda in given workspace.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Create Query Lambda
    api_response = rs.QueryLambdas.create_query_lambda(
        name="myQueryLambda",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdas->create_query_lambda: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create Query Lambda
    api_response = await rs.QueryLambdas.create_query_lambda(
        description="production version foo",
        name="myQueryLambda",
        sql=QueryLambdaSql(
        default_parameters=[
            QueryParameter(
                name="_id",
                type="string",
                value="85beb391",
            ),
        ],
        query="SELECT 'Foo'",
    ),
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdas->create_query_lambda: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str** | optional description | [optional]
 **name** | **str** | Query Lambda name | 
 **sql** | [**QueryLambdaSql**](QueryLambdaSql.md) |  | [optional]
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**QueryLambdaVersionResponse**](QueryLambdaVersionResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query Lambda created successfully |  -  |
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

# **create_query_lambda_tag**
> QueryLambdaTagResponse create_query_lambda_tag(query_lambda, create_query_lambda_tag_request)

Create Query Lambda Tag

Create a tag for a specific Query Lambda version, or update that tag if it already exists.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Create Query Lambda Tag
    api_response = rs.QueryLambdas.create_query_lambda_tag(
        query_lambda="queryLambda_example",
        tag_name="production",
        version="123ABC",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdas->create_query_lambda_tag: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Create Query Lambda Tag
    api_response = await rs.QueryLambdas.create_query_lambda_tag(
        query_lambda="queryLambda_example",
        tag_name="production",
        version="123ABC",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdas->create_query_lambda_tag: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str** | name of the Query Lambda |
 **tag_name** | **str** | name of Query Lambda tag | 
 **version** | **str** | hash identifying a Query Lambda tag | 
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**QueryLambdaTagResponse**](QueryLambdaTagResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tag created successfully |  -  |
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

# **delete_query_lambda**
> DeleteQueryLambdaResponse delete_query_lambda(query_lambda)

Delete Query Lambda

Delete a Query Lambda.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Delete Query Lambda
    api_response = rs.QueryLambdas.delete_query_lambda(
        query_lambda="queryLambda_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdas->delete_query_lambda: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Delete Query Lambda
    api_response = await rs.QueryLambdas.delete_query_lambda(
        query_lambda="queryLambda_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdas->delete_query_lambda: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str** | name of the Query Lambda |
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**DeleteQueryLambdaResponse**](DeleteQueryLambdaResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query Lambda deleted successfully |  -  |
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

# **delete_query_lambda_tag**
> QueryLambdaTagResponse delete_query_lambda_tag(query_lambda, tag)

Delete Query Lambda Tag Version

Delete a tag for a specific Query Lambda

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Delete Query Lambda Tag Version
    api_response = rs.QueryLambdas.delete_query_lambda_tag(
        query_lambda="queryLambda_example",
        tag="tag_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdas->delete_query_lambda_tag: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Delete Query Lambda Tag Version
    api_response = await rs.QueryLambdas.delete_query_lambda_tag(
        query_lambda="queryLambda_example",
        tag="tag_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdas->delete_query_lambda_tag: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str** | name of the Query Lambda |
 **tag** | **str** | name of the tag |
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**QueryLambdaTagResponse**](QueryLambdaTagResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tag deleted successfully |  -  |
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

# **delete_query_lambda_version**
> QueryLambdaVersionResponse delete_query_lambda_version(query_lambda, version)

Delete Query Lambda Version

Delete a Query Lambda version.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Delete Query Lambda Version
    api_response = rs.QueryLambdas.delete_query_lambda_version(
        query_lambda="queryLambda_example",
        version="version_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdas->delete_query_lambda_version: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Delete Query Lambda Version
    api_response = await rs.QueryLambdas.delete_query_lambda_version(
        query_lambda="queryLambda_example",
        version="version_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdas->delete_query_lambda_version: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str** | name of the Query Lambda |
 **version** | **str** | version |
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**QueryLambdaVersionResponse**](QueryLambdaVersionResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query Lambda version deleted successfully |  -  |
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

# **execute_query_lambda**
> QueryResponse execute_query_lambda(query_lambda, version)

Execute Query Lambda By Version

Execute a particular version of a Query Lambda.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Execute Query Lambda By Version
    api_response = rs.QueryLambdas.execute_query_lambda(
        query_lambda="queryLambda_example",
        version="version_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdas->execute_query_lambda: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Execute Query Lambda By Version
    api_response = await rs.QueryLambdas.execute_query_lambda(
        query_lambda="queryLambda_example",
        version="version_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdas->execute_query_lambda: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str** | name of the Query Lambda |
 **version** | **str** | version |
 **workspace** | **str** | name of the workspace | defaults to "commons"
 **execute_query_lambda_request** | [**ExecuteQueryLambdaRequest**](ExecuteQueryLambdaRequest.md) | JSON object | [optional]

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
**200** | Query Lambda executed successfully |  -  |
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

# **execute_query_lambda_by_tag**
> QueryResponse execute_query_lambda_by_tag(query_lambda, tag)

Execute Query Lambda By Tag

Execute the Query Lambda version associated with a given tag.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Execute Query Lambda By Tag
    api_response = rs.QueryLambdas.execute_query_lambda_by_tag(
        query_lambda="queryLambda_example",
        tag="tag_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdas->execute_query_lambda_by_tag: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Execute Query Lambda By Tag
    api_response = await rs.QueryLambdas.execute_query_lambda_by_tag(
        query_lambda="queryLambda_example",
        tag="tag_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdas->execute_query_lambda_by_tag: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str** | name of the Query Lambda |
 **tag** | **str** | tag |
 **workspace** | **str** | name of the workspace | defaults to "commons"
 **execute_query_lambda_request** | [**ExecuteQueryLambdaRequest**](ExecuteQueryLambdaRequest.md) | JSON object | [optional]

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
**200** | Query Lambda executed successfully |  -  |
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

# **get_query_lambda_tag_version**
> QueryLambdaTagResponse get_query_lambda_tag_version(query_lambda, tag)

Retrieve Query Lambda Tag

Retrieve the Query Lambda version associated with a given tag.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Retrieve Query Lambda Tag
    api_response = rs.QueryLambdas.get_query_lambda_tag_version(
        query_lambda="queryLambda_example",
        tag="tag_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdas->get_query_lambda_tag_version: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Retrieve Query Lambda Tag
    api_response = await rs.QueryLambdas.get_query_lambda_tag_version(
        query_lambda="queryLambda_example",
        tag="tag_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdas->get_query_lambda_tag_version: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str** | name of the Query Lambda |
 **tag** | **str** | name of the tag |
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**QueryLambdaTagResponse**](QueryLambdaTagResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | version retrieved successfully |  -  |
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

# **get_query_lambda_version**
> QueryLambdaVersionResponse get_query_lambda_version(query_lambda, version)

Retrieve Query Lambda Version

Retrieve details for a specified version of a Query Lambda.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Retrieve Query Lambda Version
    api_response = rs.QueryLambdas.get_query_lambda_version(
        query_lambda="queryLambda_example",
        version="version_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdas->get_query_lambda_version: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Retrieve Query Lambda Version
    api_response = await rs.QueryLambdas.get_query_lambda_version(
        query_lambda="queryLambda_example",
        version="version_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdas->get_query_lambda_version: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str** | name of the Query Lambda |
 **version** | **str** | version |
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**QueryLambdaVersionResponse**](QueryLambdaVersionResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query Lambda retrieved successfully |  -  |
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

# **list_all_query_lambdas**
> ListQueryLambdasResponse list_all_query_lambdas()

List Query Lambdas

List all Query Lambdas in an organization.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # List Query Lambdas
    api_response = rs.QueryLambdas.list_all_query_lambdas(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdas->list_all_query_lambdas: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # List Query Lambdas
    api_response = await rs.QueryLambdas.list_all_query_lambdas(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdas->list_all_query_lambdas: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListQueryLambdasResponse**](ListQueryLambdasResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query Lambdas listed successfully |  -  |
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

# **list_query_lambda_tags**
> ListQueryLambdaTagsResponse list_query_lambda_tags(query_lambda)

List Query Lambda Tags

List all tags associated with a Query Lambda

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # List Query Lambda Tags
    api_response = rs.QueryLambdas.list_query_lambda_tags(
        query_lambda="queryLambda_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdas->list_query_lambda_tags: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # List Query Lambda Tags
    api_response = await rs.QueryLambdas.list_query_lambda_tags(
        query_lambda="queryLambda_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdas->list_query_lambda_tags: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str** | name of the Query Lambda |
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**ListQueryLambdaTagsResponse**](ListQueryLambdaTagsResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tags listed successfully |  -  |
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

# **list_query_lambda_versions**
> ListQueryLambdaVersionsResponse list_query_lambda_versions(query_lambda)

List Query Lambda Versions

List all versions of a Query Lambda.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # List Query Lambda Versions
    api_response = rs.QueryLambdas.list_query_lambda_versions(
        query_lambda="queryLambda_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdas->list_query_lambda_versions: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # List Query Lambda Versions
    api_response = await rs.QueryLambdas.list_query_lambda_versions(
        query_lambda="queryLambda_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdas->list_query_lambda_versions: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str** | name of the Query Lambda |
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**ListQueryLambdaVersionsResponse**](ListQueryLambdaVersionsResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | versions listed successfully |  -  |
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

# **list_query_lambdas_in_workspace**
> ListQueryLambdasResponse list_query_lambdas_in_workspace()

List Query Lambdas in Workspace

List all Query Lambdas under given workspace.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # List Query Lambdas in Workspace
    api_response = rs.QueryLambdas.list_query_lambdas_in_workspace(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdas->list_query_lambdas_in_workspace: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # List Query Lambdas in Workspace
    api_response = await rs.QueryLambdas.list_query_lambdas_in_workspace(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdas->list_query_lambdas_in_workspace: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**ListQueryLambdasResponse**](ListQueryLambdasResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query Lambdas listed successfully |  -  |
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

# **update_query_lambda**
> QueryLambdaVersionResponse update_query_lambda(query_lambda, update_query_lambda_request)

Update Query Lambda

Create a new version of a Query Lambda in given workspace.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(api_key="abc123", host=rockset.Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
try:
    # Update Query Lambda
    api_response = rs.QueryLambdas.update_query_lambda(
        query_lambda="queryLambda_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdas->update_query_lambda: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
async def call_api():
    # Update Query Lambda
    api_response = await rs.QueryLambdas.update_query_lambda(
        query_lambda="queryLambda_example",
        description="production version foo",
        sql=QueryLambdaSql(
        default_parameters=[
            QueryParameter(
                name="_id",
                type="string",
                value="85beb391",
            ),
        ],
        query="SELECT 'Foo'",
    ),
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdas->update_query_lambda: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str** | name of the Query Lambda |
 **description** | **str** | optional description | [optional]
 **sql** | [**QueryLambdaSql**](QueryLambdaSql.md) |  | [optional]
 **workspace** | **str** | name of the workspace | defaults to "commons"
 **create** | **bool** |  | [optional]

### Return type

[**QueryLambdaVersionResponse**](QueryLambdaVersionResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query Lambda updated successfully |  -  |
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

