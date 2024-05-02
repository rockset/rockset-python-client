# rockset.ScheduledLambdas

All URIs are relative to *https://api.use1a1.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ScheduledLambdasApi.md#create) | **POST** /v1/orgs/self/ws/{workspace}/scheduled_lambdas | Create a Scheduled Lambda mapping
[**delete**](ScheduledLambdasApi.md#delete) | **DELETE** /v1/orgs/self/ws/{workspace}/scheduled_lambdas/{scheduledLambdaId} | Delete a Scheduled Lambda mapping
[**get**](ScheduledLambdasApi.md#get) | **GET** /v1/orgs/self/ws/{workspace}/scheduled_lambdas/{scheduledLambdaId} | Retrieve a Scheduled Lambda mapping
[**list_org_scheduled_lambdas**](ScheduledLambdasApi.md#list_org_scheduled_lambdas) | **GET** /v1/orgs/self/lambdas/scheduled_lambdas | List Scheduled Lambdas
[**update**](ScheduledLambdasApi.md#update) | **POST** /v1/orgs/self/ws/{workspace}/scheduled_lambdas/{scheduledLambdaId} | Update a Scheduled Lambda mapping


# **create**
> ScheduledLambdaResponse create(create_scheduled_lambda_request)

Create a Scheduled Lambda mapping

Create a scheduled lambda mapping for your organization.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Create a Scheduled Lambda mapping
api_response = rs.ScheduledLambdas.create(
    apikey="qoiwkjndksd",
    cron_string="* * * * *",
    ql_name="ql_name",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling ScheduledLambdas->create: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Create a Scheduled Lambda mapping
api_response = await rs.ScheduledLambdas.create(
    apikey="qoiwkjndksd",
    cron_string="* * * * *",
    ql_name="ql_name",
    tag="production",
    total_times_to_execute=1,
    version="abcdef1234",
    webhook_auth_header="bearer qiowjkjkdskdskldio",
    webhook_payload="string_example",
    webhook_url="https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling ScheduledLambdas->create: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str** | The apikey to use when triggering execution of the associated query lambda. | [optional]
 **cron_string** | **str** | The UNIX-formatted cron string for this scheduled query lambda. | 
 **ql_name** | **str** | The name of the QL to use for scheduled execution. | 
 **tag** | **str** | The QL tag to use for scheduled execution. One of either the QL tag or version must be specified | [optional]
 **total_times_to_execute** | **int** | The number of times to execute this scheduled query lambda. Once this scheduled query lambda has been executed this many times, it will no longer be executed. | [optional]
 **version** | **str** | The version of the QL to use for scheduled execution. One of either the QL version or tag must be specified. | [optional]
 **webhook_auth_header** | **str** | The value to use as the authorization header when hitting the webhook. | [optional]
 **webhook_payload** | **str** | The payload that should be sent to the webhook. JSON format. | [optional]
 **webhook_url** | **str** | The URL of the webhook that should be triggered after this scheduled query lambda completes. | [optional]
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**ScheduledLambdaResponse**](ScheduledLambdaResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | scheduled lambda mapping created successfully |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> ScheduledLambdaResponse delete(scheduled_lambda_id)

Delete a Scheduled Lambda mapping

Delete a scheduled lambda mapping for your organization.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Delete a Scheduled Lambda mapping
api_response = rs.ScheduledLambdas.delete(
    scheduled_lambda_id="scheduledLambdaId_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling ScheduledLambdas->delete: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Delete a Scheduled Lambda mapping
api_response = await rs.ScheduledLambdas.delete(
    scheduled_lambda_id="scheduledLambdaId_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling ScheduledLambdas->delete: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_lambda_id** | **str** | Scheduled Lambda RRN |
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**ScheduledLambdaResponse**](ScheduledLambdaResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | scheduled lambda mapping deleted successfully |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ScheduledLambdaResponse get(scheduled_lambda_id)

Retrieve a Scheduled Lambda mapping

Retrieve a scheduled lambda mapping for your organization.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Retrieve a Scheduled Lambda mapping
api_response = rs.ScheduledLambdas.get(
    scheduled_lambda_id="scheduledLambdaId_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling ScheduledLambdas->get: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Retrieve a Scheduled Lambda mapping
api_response = await rs.ScheduledLambdas.get(
    scheduled_lambda_id="scheduledLambdaId_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling ScheduledLambdas->get: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_lambda_id** | **str** | Scheduled Lambda RRN |
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**ScheduledLambdaResponse**](ScheduledLambdaResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | scheduled lambda mapping retrieved successfully |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_org_scheduled_lambdas**
> ListScheduledLambdasResponse list_org_scheduled_lambdas()

List Scheduled Lambdas

List all Scheduled Lambdas in an organization.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# List Scheduled Lambdas
api_response = rs.ScheduledLambdas.list_org_scheduled_lambdas(
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling ScheduledLambdas->list_org_scheduled_lambdas: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# List Scheduled Lambdas
api_response = await rs.ScheduledLambdas.list_org_scheduled_lambdas(
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling ScheduledLambdas->list_org_scheduled_lambdas: %s\n" % e)
    return
pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListScheduledLambdasResponse**](ListScheduledLambdasResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | scheduled lambdas listed successfully |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ScheduledLambdaResponse update(scheduled_lambda_id, update_scheduled_lambda_request)

Update a Scheduled Lambda mapping

Update a scheduled lambda mapping for your organization.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Update a Scheduled Lambda mapping
api_response = rs.ScheduledLambdas.update(
    scheduled_lambda_id="scheduledLambdaId_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling ScheduledLambdas->update: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Update a Scheduled Lambda mapping
api_response = await rs.ScheduledLambdas.update(
    scheduled_lambda_id="scheduledLambdaId_example",
    apikey="qoiwkjndksd",
    resume_permanent_error=True,
    total_times_to_execute=1,
    webhook_auth_header="bearer qiowjkjkdskdskldio",
    webhook_payload="string_example",
    webhook_url="https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling ScheduledLambdas->update: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_lambda_id** | **str** | Scheduled Lambda RRN |
 **apikey** | **str** | The apikey to use when triggering execution of the associated query lambda. | [optional]
 **resume_permanent_error** | **bool** | Boolean flag to allow a scheduled query lambda to resume execution after being suspended due to execution failure. This flag will be unset after scheduled lambda execution. | [optional]
 **total_times_to_execute** | **int** | The number of times to execute this scheduled query lambda. | [optional]
 **webhook_auth_header** | **str** | The value to use as the authorization header when hitting the webhook. | [optional]
 **webhook_payload** | **str** | The payload that should be sent to the webhook. JSON format. | [optional]
 **webhook_url** | **str** | The URL of the webhook that should be triggered after this scheduled query lambda completes. | [optional]
 **workspace** | **str** | name of the workspace | defaults to "commons"

### Return type

[**ScheduledLambdaResponse**](ScheduledLambdaResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | scheduled lambda mapping updated successfully |  -  |
**400** | bad request |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**405** | not allowed |  -  |
**406** | not acceptable |  -  |
**408** | request timeout |  -  |
**409** | conflict |  -  |
**415** | not supported |  -  |
**429** | resource exceeded |  -  |
**500** | internal error |  -  |
**501** | not implemented |  -  |
**502** | bad gateway |  -  |
**503** | not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

