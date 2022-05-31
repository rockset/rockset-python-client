# rockset.Organizations

All URIs are relative to *https://api.use1a1.rockset.com* or the apiserver provided when initializing RocksetClient

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](OrganizationsApi.md#get) | **GET** /v1/orgs/self | Get Organization


# **get**
> OrganizationResponse get()

Get Organization

Retrieve information about current organization.

### Example

* Api Key Authentication (apikey):

```python
from rockset import *
from pprint import pprint

# Create an instance of the Rockset client
rs = RocksetClient(api_key="abc123", host=Regions.use1a1)

# synchronous example passing only required values which don't have defaults set
# Get Organization
api_response = rs.Organizations.get(
)
pprint(api_response)
# Error responses from the server will cause the client to throw an ApiException
# except ApiException as e:
#     print("Exception when calling Organizations->get: %s\n" % e)

# asynchronous example passing optional values and required values which don't have defaults set
# assumes that execution takes place within an asynchronous context
# Get Organization
api_response = await rs.Organizations.get(
    async_req=True,
)
if isinstance(api_response, rockset.ApiException):
    print("Exception when calling Organizations->get: %s\n" % e)
    return
pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

All requests must use apikeys for [authorization](../README.md#Documentation-For-Authorization).


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | organization retrieved successfully |  -  |
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

