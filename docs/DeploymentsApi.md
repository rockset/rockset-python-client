# rockset.Deployments

All URIs are relative to *https://api.use1a1.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_deployment**](DeploymentsApi.md#delete_deployment) | **DELETE** /v1/deployments/{rrn} | Delete deployment
[**get_deployment**](DeploymentsApi.md#get_deployment) | **GET** /v1/deployments/{rrn} | Get info about a deployment
[**get_self_deployment**](DeploymentsApi.md#get_self_deployment) | **GET** /v1/deployments/self | Get info about your own deployment
[**list_deployments**](DeploymentsApi.md#list_deployments) | **GET** /v1/deployments | List all deployments
[**provision_deployment**](DeploymentsApi.md#provision_deployment) | **POST** /v1/deployments | Provision a deployment


# **delete_deployment**
> DeleteDeploymentResponse delete_deployment(rrn)

Delete deployment

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Delete deployment
api_response = rs.Deployments.delete_deployment(
    rrn="rrn_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Deployments->delete_deployment: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Delete deployment
api_response = await rs.Deployments.delete_deployment(
    rrn="rrn_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Deployments->delete_deployment: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rrn** | **str** | The deployment RRN |

### Return type

[**DeleteDeploymentResponse**](DeleteDeploymentResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deployment deletion initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment**
> GetDeploymentResponse get_deployment(rrn)

Get info about a deployment

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Get info about a deployment
api_response = rs.Deployments.get_deployment(
    rrn="rrn_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Deployments->get_deployment: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Get info about a deployment
api_response = await rs.Deployments.get_deployment(
    rrn="rrn_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Deployments->get_deployment: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rrn** | **str** | The deployment RRN |

### Return type

[**GetDeploymentResponse**](GetDeploymentResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deployment info |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_deployment**
> GetDeploymentResponse get_self_deployment()

Get info about your own deployment

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Get info about your own deployment
api_response = rs.Deployments.get_self_deployment(
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Deployments->get_self_deployment: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Get info about your own deployment
api_response = await rs.Deployments.get_self_deployment(
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Deployments->get_self_deployment: %s\n" % e)
    return
pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetDeploymentResponse**](GetDeploymentResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deployment info |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deployments**
> ListDeploymentsResponse list_deployments()

List all deployments

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# List all deployments
api_response = rs.Deployments.list_deployments(
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Deployments->list_deployments: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# List all deployments
api_response = await rs.Deployments.list_deployments(
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Deployments->list_deployments: %s\n" % e)
    return
pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListDeploymentsResponse**](ListDeploymentsResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deployment list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provision_deployment**
> CreateDeploymentResponse provision_deployment(create_deployment_request)

Provision a deployment

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Provision a deployment
api_response = rs.Deployments.provision_deployment(
    display_name="string_example",
    email="string_example",
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Deployments->provision_deployment: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Provision a deployment
api_response = await rs.Deployments.provision_deployment(
    display_name="string_example",
    email="string_example",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Deployments->provision_deployment: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_name** | **str** | The display name of the deployment | 
 **email** | **str** | The email of the user creating the deployment | 

### Return type

[**CreateDeploymentResponse**](CreateDeploymentResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | deployment provisioned successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

