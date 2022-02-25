# swagger_client.QueryLambdasApi

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
> QueryLambdaVersionResponse create_query_lambda(workspace, body)

Create Query Lambda

Create a Query Lambda in given workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryLambdasApi()
workspace = 'workspace_example' # str | name of the workspace
body = swagger_client.CreateQueryLambdaRequest() # CreateQueryLambdaRequest | JSON object

try:
    # Create Query Lambda
    api_response = api_instance.create_query_lambda(workspace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryLambdasApi->create_query_lambda: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **body** | [**CreateQueryLambdaRequest**](CreateQueryLambdaRequest.md)| JSON object | 

### Return type

[**QueryLambdaVersionResponse**](QueryLambdaVersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_query_lambda_tag**
> QueryLambdaTagResponse create_query_lambda_tag(workspace, query_lambda, body)

Create Query Lambda Tag

Create a tag for a specific Query Lambda version, or update that tag if it already exists.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryLambdasApi()
workspace = 'workspace_example' # str | name of the workspace
query_lambda = 'query_lambda_example' # str | name of the Query Lambda
body = swagger_client.CreateQueryLambdaTagRequest() # CreateQueryLambdaTagRequest | JSON object

try:
    # Create Query Lambda Tag
    api_response = api_instance.create_query_lambda_tag(workspace, query_lambda, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryLambdasApi->create_query_lambda_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **query_lambda** | **str**| name of the Query Lambda | 
 **body** | [**CreateQueryLambdaTagRequest**](CreateQueryLambdaTagRequest.md)| JSON object | 

### Return type

[**QueryLambdaTagResponse**](QueryLambdaTagResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_query_lambda**
> DeleteQueryLambdaResponse delete_query_lambda(workspace, query_lambda)

Delete Query Lambda

Delete a Query Lambda.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryLambdasApi()
workspace = 'workspace_example' # str | name of the workspace
query_lambda = 'query_lambda_example' # str | name of the Query Lambda

try:
    # Delete Query Lambda
    api_response = api_instance.delete_query_lambda(workspace, query_lambda)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryLambdasApi->delete_query_lambda: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **query_lambda** | **str**| name of the Query Lambda | 

### Return type

[**DeleteQueryLambdaResponse**](DeleteQueryLambdaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_query_lambda_tag**
> QueryLambdaTagResponse delete_query_lambda_tag(workspace, query_lambda, tag)

Delete Query Lambda Tag Version

Delete a tag for a specific Query Lambda

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryLambdasApi()
workspace = 'workspace_example' # str | name of the workspace
query_lambda = 'query_lambda_example' # str | name of the Query Lambda
tag = 'tag_example' # str | name of the tag

try:
    # Delete Query Lambda Tag Version
    api_response = api_instance.delete_query_lambda_tag(workspace, query_lambda, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryLambdasApi->delete_query_lambda_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **query_lambda** | **str**| name of the Query Lambda | 
 **tag** | **str**| name of the tag | 

### Return type

[**QueryLambdaTagResponse**](QueryLambdaTagResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_query_lambda_version**
> QueryLambdaVersionResponse delete_query_lambda_version(workspace, query_lambda, version)

Delete Query Lambda Version

Delete a Query Lambda version.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryLambdasApi()
workspace = 'workspace_example' # str | name of the workspace
query_lambda = 'query_lambda_example' # str | name of the Query Lambda
version = 'version_example' # str | version

try:
    # Delete Query Lambda Version
    api_response = api_instance.delete_query_lambda_version(workspace, query_lambda, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryLambdasApi->delete_query_lambda_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **query_lambda** | **str**| name of the Query Lambda | 
 **version** | **str**| version | 

### Return type

[**QueryLambdaVersionResponse**](QueryLambdaVersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_query_lambda**
> QueryResponse execute_query_lambda(workspace, query_lambda, version, body=body)

Execute Query Lambda By Version

Execute a particular version of a Query Lambda.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryLambdasApi()
workspace = 'workspace_example' # str | name of the workspace
query_lambda = 'query_lambda_example' # str | name of the Query Lambda
version = 'version_example' # str | version
body = swagger_client.ExecuteQueryLambdaRequest() # ExecuteQueryLambdaRequest | JSON object (optional)

try:
    # Execute Query Lambda By Version
    api_response = api_instance.execute_query_lambda(workspace, query_lambda, version, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryLambdasApi->execute_query_lambda: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **query_lambda** | **str**| name of the Query Lambda | 
 **version** | **str**| version | 
 **body** | [**ExecuteQueryLambdaRequest**](ExecuteQueryLambdaRequest.md)| JSON object | [optional] 

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_query_lambda_by_tag**
> QueryResponse execute_query_lambda_by_tag(workspace, query_lambda, tag, body=body)

Execute Query Lambda By Tag

Execute the Query Lambda version associated with a given tag.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryLambdasApi()
workspace = 'workspace_example' # str | name of the workspace
query_lambda = 'query_lambda_example' # str | name of the Query Lambda
tag = 'tag_example' # str | tag
body = swagger_client.ExecuteQueryLambdaRequest() # ExecuteQueryLambdaRequest | JSON object (optional)

try:
    # Execute Query Lambda By Tag
    api_response = api_instance.execute_query_lambda_by_tag(workspace, query_lambda, tag, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryLambdasApi->execute_query_lambda_by_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **query_lambda** | **str**| name of the Query Lambda | 
 **tag** | **str**| tag | 
 **body** | [**ExecuteQueryLambdaRequest**](ExecuteQueryLambdaRequest.md)| JSON object | [optional] 

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_query_lambda_tag_version**
> QueryLambdaTagResponse get_query_lambda_tag_version(workspace, query_lambda, tag)

Retrieve Query Lambda Tag

Retrieve the Query Lambda version associated with a given tag.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryLambdasApi()
workspace = 'workspace_example' # str | name of the workspace
query_lambda = 'query_lambda_example' # str | name of the Query Lambda
tag = 'tag_example' # str | name of the tag

try:
    # Retrieve Query Lambda Tag
    api_response = api_instance.get_query_lambda_tag_version(workspace, query_lambda, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryLambdasApi->get_query_lambda_tag_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **query_lambda** | **str**| name of the Query Lambda | 
 **tag** | **str**| name of the tag | 

### Return type

[**QueryLambdaTagResponse**](QueryLambdaTagResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_query_lambda_version**
> QueryLambdaVersionResponse get_query_lambda_version(workspace, query_lambda, version)

Retrieve Query Lambda Version

Retrieve details for a specified version of a Query Lambda.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryLambdasApi()
workspace = 'workspace_example' # str | name of the workspace
query_lambda = 'query_lambda_example' # str | name of the Query Lambda
version = 'version_example' # str | version

try:
    # Retrieve Query Lambda Version
    api_response = api_instance.get_query_lambda_version(workspace, query_lambda, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryLambdasApi->get_query_lambda_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **query_lambda** | **str**| name of the Query Lambda | 
 **version** | **str**| version | 

### Return type

[**QueryLambdaVersionResponse**](QueryLambdaVersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_query_lambdas**
> ListQueryLambdasResponse list_all_query_lambdas()

List Query Lambdas

List all Query Lambdas in an organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryLambdasApi()

try:
    # List Query Lambdas
    api_response = api_instance.list_all_query_lambdas()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryLambdasApi->list_all_query_lambdas: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListQueryLambdasResponse**](ListQueryLambdasResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_query_lambda_tags**
> ListQueryLambdaTagsResponse list_query_lambda_tags(workspace, query_lambda)

List Query Lambda Tags

List all tags associated with a Query Lambda

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryLambdasApi()
workspace = 'workspace_example' # str | name of the workspace
query_lambda = 'query_lambda_example' # str | name of the Query Lambda

try:
    # List Query Lambda Tags
    api_response = api_instance.list_query_lambda_tags(workspace, query_lambda)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryLambdasApi->list_query_lambda_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **query_lambda** | **str**| name of the Query Lambda | 

### Return type

[**ListQueryLambdaTagsResponse**](ListQueryLambdaTagsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_query_lambda_versions**
> ListQueryLambdaVersionsResponse list_query_lambda_versions(workspace, query_lambda)

List Query Lambda Versions

List all versions of a Query Lambda.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryLambdasApi()
workspace = 'workspace_example' # str | name of the workspace
query_lambda = 'query_lambda_example' # str | name of the Query Lambda

try:
    # List Query Lambda Versions
    api_response = api_instance.list_query_lambda_versions(workspace, query_lambda)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryLambdasApi->list_query_lambda_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **query_lambda** | **str**| name of the Query Lambda | 

### Return type

[**ListQueryLambdaVersionsResponse**](ListQueryLambdaVersionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_query_lambdas_in_workspace**
> ListQueryLambdasResponse list_query_lambdas_in_workspace(workspace)

List Query Lambdas in Workspace

List all Query Lambdas under given workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryLambdasApi()
workspace = 'workspace_example' # str | name of the workspace

try:
    # List Query Lambdas in Workspace
    api_response = api_instance.list_query_lambdas_in_workspace(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryLambdasApi->list_query_lambdas_in_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 

### Return type

[**ListQueryLambdasResponse**](ListQueryLambdasResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_query_lambda**
> QueryLambdaVersionResponse update_query_lambda(workspace, query_lambda, body, create=create)

Update Query Lambda

Create a new version of a Query Lambda in given workspace.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QueryLambdasApi()
workspace = 'workspace_example' # str | name of the workspace
query_lambda = 'query_lambda_example' # str | name of the Query Lambda
body = swagger_client.UpdateQueryLambdaRequest() # UpdateQueryLambdaRequest | JSON object
create = true # bool |  (optional)

try:
    # Update Query Lambda
    api_response = api_instance.update_query_lambda(workspace, query_lambda, body, create=create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryLambdasApi->update_query_lambda: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| name of the workspace | 
 **query_lambda** | **str**| name of the Query Lambda | 
 **body** | [**UpdateQueryLambdaRequest**](UpdateQueryLambdaRequest.md)| JSON object | 
 **create** | **bool**|  | [optional] 

### Return type

[**QueryLambdaVersionResponse**](QueryLambdaVersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

