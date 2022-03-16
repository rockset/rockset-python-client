# rockset.QueryLambdasApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_query_lambda**](QueryLambdasApi.md#create_query_lambda) | **POST** /v1/orgs/self/ws/{workspace}/lambdas | Create Query Lambda
[**create_query_lambda_tag**](QueryLambdasApi.md#create_query_lambda_tag) | **POST** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/tags | Create Query Lambda Tag
[**delete_query_lambda**](QueryLambdasApi.md#delete_query_lambda) | **DELETE** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda} | Delete Query Lambda
[**delete_query_lambda_tag**](QueryLambdasApi.md#delete_query_lambda_tag) | **DELETE** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/tags/{tag} | Delete Query Lambda Tag Version
[**delete_query_lambda_version**](QueryLambdasApi.md#delete_query_lambda_version) | **DELETE** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/version/{version} | Delete Query Lambda Version
[**execute_query_lambda**](QueryLambdasApi.md#execute_query_lambda) | **POST** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/versions/{version} | Execute Query Lambda By Version
[**execute_query_lambda_by_tag**](QueryLambdasApi.md#execute_query_lambda_by_tag) | **POST** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/tags/{tag} | Execute Query Lambda By Tag
[**get_query_lambda_tag_version**](QueryLambdasApi.md#get_query_lambda_tag_version) | **GET** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/tags/{tag} | Retrieve Query Lambda Tag
[**get_query_lambda_version**](QueryLambdasApi.md#get_query_lambda_version) | **GET** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/versions/{version} | Retrieve Query Lambda Version
[**list_all_query_lambdas**](QueryLambdasApi.md#list_all_query_lambdas) | **GET** /v1/orgs/self/lambdas | List Query Lambdas
[**list_query_lambda_tags**](QueryLambdasApi.md#list_query_lambda_tags) | **GET** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/tags | List Query Lambda Tags
[**list_query_lambda_versions**](QueryLambdasApi.md#list_query_lambda_versions) | **GET** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/versions | List Query Lambda Versions
[**list_query_lambdas_in_workspace**](QueryLambdasApi.md#list_query_lambdas_in_workspace) | **GET** /v1/orgs/self/ws/{workspace}/lambdas | List Query Lambdas in Workspace
[**update_query_lambda**](QueryLambdasApi.md#update_query_lambda) | **POST** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/versions | Update Query Lambda


# **create_query_lambda**
> QueryLambdaVersionResponse create_query_lambda(create_query_lambda_request)

Create Query Lambda

Create a Query Lambda in given workspace.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.query_lambda_version_response import QueryLambdaVersionResponse
from rockset.model.create_query_lambda_request import CreateQueryLambdaRequest
from rockset.model.error_model import ErrorModel
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Create Query Lambda
    api_response = rs.QueryLambdasApi.create_query_lambda(
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
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdasApi->create_query_lambda: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # Create Query Lambda
    api_response = await rs.QueryLambdasApi.create_query_lambda(
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
        print("Exception when calling QueryLambdasApi->create_query_lambda: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_query_lambda_request** | [**CreateQueryLambdaRequest**](CreateQueryLambdaRequest.md)| JSON object |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**QueryLambdaVersionResponse**](QueryLambdaVersionResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
import time
import rockset
from rockset import RocksetClient
from rockset.model.error_model import ErrorModel
from rockset.model.create_query_lambda_tag_request import CreateQueryLambdaTagRequest
from rockset.model.query_lambda_tag_response import QueryLambdaTagResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Create Query Lambda Tag
    api_response = rs.QueryLambdasApi.create_query_lambda_tag(
        query_lambda="queryLambda_example",
        tag_name="production",
        version="123ABC",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdasApi->create_query_lambda_tag: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # Create Query Lambda Tag
    api_response = await rs.QueryLambdasApi.create_query_lambda_tag(
        query_lambda="queryLambda_example",
        tag_name="production",
        version="123ABC",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdasApi->create_query_lambda_tag: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str**| name of the Query Lambda |
 **create_query_lambda_tag_request** | [**CreateQueryLambdaTagRequest**](CreateQueryLambdaTagRequest.md)| JSON object |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**QueryLambdaTagResponse**](QueryLambdaTagResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
import time
import rockset
from rockset import RocksetClient
from rockset.model.error_model import ErrorModel
from rockset.model.delete_query_lambda_response import DeleteQueryLambdaResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Delete Query Lambda
    api_response = rs.QueryLambdasApi.delete_query_lambda(
        query_lambda="queryLambda_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdasApi->delete_query_lambda: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # Delete Query Lambda
    api_response = await rs.QueryLambdasApi.delete_query_lambda(
        query_lambda="queryLambda_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdasApi->delete_query_lambda: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str**| name of the Query Lambda |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**DeleteQueryLambdaResponse**](DeleteQueryLambdaResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
import time
import rockset
from rockset import RocksetClient
from rockset.model.error_model import ErrorModel
from rockset.model.query_lambda_tag_response import QueryLambdaTagResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Delete Query Lambda Tag Version
    api_response = rs.QueryLambdasApi.delete_query_lambda_tag(
        query_lambda="queryLambda_example",
        tag="tag_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdasApi->delete_query_lambda_tag: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # Delete Query Lambda Tag Version
    api_response = await rs.QueryLambdasApi.delete_query_lambda_tag(
        query_lambda="queryLambda_example",
        tag="tag_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdasApi->delete_query_lambda_tag: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str**| name of the Query Lambda |
 **tag** | **str**| name of the tag |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**QueryLambdaTagResponse**](QueryLambdaTagResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
import time
import rockset
from rockset import RocksetClient
from rockset.model.query_lambda_version_response import QueryLambdaVersionResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Delete Query Lambda Version
    api_response = rs.QueryLambdasApi.delete_query_lambda_version(
        query_lambda="queryLambda_example",
        version="version_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdasApi->delete_query_lambda_version: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # Delete Query Lambda Version
    api_response = await rs.QueryLambdasApi.delete_query_lambda_version(
        query_lambda="queryLambda_example",
        version="version_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdasApi->delete_query_lambda_version: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str**| name of the Query Lambda |
 **version** | **str**| version |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**QueryLambdaVersionResponse**](QueryLambdaVersionResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
import time
import rockset
from rockset import RocksetClient
from rockset.model.execute_query_lambda_request import ExecuteQueryLambdaRequest
from rockset.model.error_model import ErrorModel
from rockset.model.query_response import QueryResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Execute Query Lambda By Version
    api_response = rs.QueryLambdasApi.execute_query_lambda(
        query_lambda="queryLambda_example",
        version="version_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdasApi->execute_query_lambda: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # Execute Query Lambda By Version
    api_response = await rs.QueryLambdasApi.execute_query_lambda(
        query_lambda="queryLambda_example",
        version="version_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdasApi->execute_query_lambda: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str**| name of the Query Lambda |
 **version** | **str**| version |
 **workspace** | **str**| name of the workspace | defaults to "commons"
 **execute_query_lambda_request** | [**ExecuteQueryLambdaRequest**](ExecuteQueryLambdaRequest.md)| JSON object | [optional]

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
import time
import rockset
from rockset import RocksetClient
from rockset.model.execute_query_lambda_request import ExecuteQueryLambdaRequest
from rockset.model.error_model import ErrorModel
from rockset.model.query_response import QueryResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Execute Query Lambda By Tag
    api_response = rs.QueryLambdasApi.execute_query_lambda_by_tag(
        query_lambda="queryLambda_example",
        tag="tag_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdasApi->execute_query_lambda_by_tag: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # Execute Query Lambda By Tag
    api_response = await rs.QueryLambdasApi.execute_query_lambda_by_tag(
        query_lambda="queryLambda_example",
        tag="tag_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdasApi->execute_query_lambda_by_tag: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str**| name of the Query Lambda |
 **tag** | **str**| tag |
 **workspace** | **str**| name of the workspace | defaults to "commons"
 **execute_query_lambda_request** | [**ExecuteQueryLambdaRequest**](ExecuteQueryLambdaRequest.md)| JSON object | [optional]

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
import time
import rockset
from rockset import RocksetClient
from rockset.model.error_model import ErrorModel
from rockset.model.query_lambda_tag_response import QueryLambdaTagResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Retrieve Query Lambda Tag
    api_response = rs.QueryLambdasApi.get_query_lambda_tag_version(
        query_lambda="queryLambda_example",
        tag="tag_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdasApi->get_query_lambda_tag_version: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # Retrieve Query Lambda Tag
    api_response = await rs.QueryLambdasApi.get_query_lambda_tag_version(
        query_lambda="queryLambda_example",
        tag="tag_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdasApi->get_query_lambda_tag_version: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str**| name of the Query Lambda |
 **tag** | **str**| name of the tag |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**QueryLambdaTagResponse**](QueryLambdaTagResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
import time
import rockset
from rockset import RocksetClient
from rockset.model.query_lambda_version_response import QueryLambdaVersionResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Retrieve Query Lambda Version
    api_response = rs.QueryLambdasApi.get_query_lambda_version(
        query_lambda="queryLambda_example",
        version="version_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdasApi->get_query_lambda_version: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # Retrieve Query Lambda Version
    api_response = await rs.QueryLambdasApi.get_query_lambda_version(
        query_lambda="queryLambda_example",
        version="version_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdasApi->get_query_lambda_version: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str**| name of the Query Lambda |
 **version** | **str**| version |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**QueryLambdaVersionResponse**](QueryLambdaVersionResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
import time
import rockset
from rockset import RocksetClient
from rockset.model.list_query_lambdas_response import ListQueryLambdasResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # List Query Lambdas
    api_response = rs.QueryLambdasApi.list_all_query_lambdas(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdasApi->list_all_query_lambdas: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # List Query Lambdas
    api_response = await rs.QueryLambdasApi.list_all_query_lambdas(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdasApi->list_all_query_lambdas: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListQueryLambdasResponse**](ListQueryLambdasResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
import time
import rockset
from rockset import RocksetClient
from rockset.model.error_model import ErrorModel
from rockset.model.list_query_lambda_tags_response import ListQueryLambdaTagsResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # List Query Lambda Tags
    api_response = rs.QueryLambdasApi.list_query_lambda_tags(
        query_lambda="queryLambda_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdasApi->list_query_lambda_tags: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # List Query Lambda Tags
    api_response = await rs.QueryLambdasApi.list_query_lambda_tags(
        query_lambda="queryLambda_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdasApi->list_query_lambda_tags: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str**| name of the Query Lambda |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**ListQueryLambdaTagsResponse**](ListQueryLambdaTagsResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
import time
import rockset
from rockset import RocksetClient
from rockset.model.error_model import ErrorModel
from rockset.model.list_query_lambda_versions_response import ListQueryLambdaVersionsResponse
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # List Query Lambda Versions
    api_response = rs.QueryLambdasApi.list_query_lambda_versions(
        query_lambda="queryLambda_example",
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdasApi->list_query_lambda_versions: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # List Query Lambda Versions
    api_response = await rs.QueryLambdasApi.list_query_lambda_versions(
        query_lambda="queryLambda_example",
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdasApi->list_query_lambda_versions: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str**| name of the Query Lambda |
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**ListQueryLambdaVersionsResponse**](ListQueryLambdaVersionsResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
import time
import rockset
from rockset import RocksetClient
from rockset.model.list_query_lambdas_response import ListQueryLambdasResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # List Query Lambdas in Workspace
    api_response = rs.QueryLambdasApi.list_query_lambdas_in_workspace(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdasApi->list_query_lambdas_in_workspace: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # List Query Lambdas in Workspace
    api_response = await rs.QueryLambdasApi.list_query_lambdas_in_workspace(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling QueryLambdasApi->list_query_lambdas_in_workspace: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | defaults to "commons"

### Return type

[**ListQueryLambdasResponse**](ListQueryLambdasResponse.md)

### Authorization

[apikey](../README.md#apikey)

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
import time
import rockset
from rockset import RocksetClient
from rockset.model.query_lambda_version_response import QueryLambdaVersionResponse
from rockset.model.update_query_lambda_request import UpdateQueryLambdaRequest
from rockset.model.error_model import ErrorModel
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Update Query Lambda
    api_response = rs.QueryLambdasApi.update_query_lambda(
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
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling QueryLambdasApi->update_query_lambda: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # Update Query Lambda
    api_response = await rs.QueryLambdasApi.update_query_lambda(
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
        print("Exception when calling QueryLambdasApi->update_query_lambda: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_lambda** | **str**| name of the Query Lambda |
 **update_query_lambda_request** | [**UpdateQueryLambdaRequest**](UpdateQueryLambdaRequest.md)| JSON object |
 **workspace** | **str**| name of the workspace | defaults to "commons"
 **create** | **bool**|  | [optional]

### Return type

[**QueryLambdaVersionResponse**](QueryLambdaVersionResponse.md)

### Authorization

[apikey](../README.md#apikey)

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

