# rockset.DeploymentSettings

All URIs are relative to *https://api.use1a1.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_deployment_settings**](DeploymentSettingsApi.md#get_deployment_settings) | **GET** /v1/orgs/self/deploymentsettings | Retrieve Deployment Settings
[**update_deployment_settings**](DeploymentSettingsApi.md#update_deployment_settings) | **PUT** /v1/orgs/self/deploymentsettings | Update Deployment Settings


# **get_deployment_settings**
> DeploymentSettingsResponse get_deployment_settings()

Retrieve Deployment Settings

Retrieve settings for the current deployment.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Retrieve Deployment Settings
api_response = rs.DeploymentSettings.get_deployment_settings(
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling DeploymentSettings->get_deployment_settings: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Retrieve Deployment Settings
api_response = await rs.DeploymentSettings.get_deployment_settings(
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling DeploymentSettings->get_deployment_settings: %s\n" % e)
    return
pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DeploymentSettingsResponse**](DeploymentSettingsResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deployment settings retrieved successfully |  -  |
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

# **update_deployment_settings**
> DeploymentSettingsResponse update_deployment_settings(update_deployment_settings_request)

Update Deployment Settings

Update settings for the current deployment.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from rockset.models import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Update Deployment Settings
api_response = rs.DeploymentSettings.update_deployment_settings(
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling DeploymentSettings->update_deployment_settings: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Update Deployment Settings
api_response = await rs.DeploymentSettings.update_deployment_settings(
    default_query_vi="rrn:vi:use1a1:123e4567-e89b-12d3-a456-556642440000",
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling DeploymentSettings->update_deployment_settings: %s\n" % e)
    return
pprint(api_response)

```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **default_query_vi** | **str** | RRN of the Virtual Instance that all queries will be routed to by default | [optional]

### Return type

[**DeploymentSettingsResponse**](DeploymentSettingsResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Deployment settings updated successfully. Settings may take up to 1 minute to take effect |  -  |
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

