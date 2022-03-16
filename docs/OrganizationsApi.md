# rockset.OrganizationsApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization**](OrganizationsApi.md#get_organization) | **GET** /v1/orgs/self | Get Organization


# **get_organization**
> OrganizationResponse get_organization()

Get Organization

Retrieve information about current organization.

### Example

* Api Key Authentication (apikey):

```python
import time
import rockset
from rockset import RocksetClient
from rockset.model.organization_response import OrganizationResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint

# Create an instance of the Rockset client
# example passing only required values which don't have defaults set
rs = RocksetClient(apikey="abc123")

# synchronous example passing only required values which don't have defaults set
try:
    # Get Organization
    api_response = rs.OrganizationsApi.get_organization(
    )
    pprint(api_response)
except rockset.ApiException as e:
    print("Exception when calling OrganizationsApi->get_organization: %s\n" % e)

# asynchronous example passing required values which don't have defaults set and optional values
async def call_api():
    # Get Organization
    api_response = await rs.OrganizationsApi.get_organization(
        async_req=True,
    )
    if isinstance(api_response, rockset.ApiException):
        print("Exception when calling OrganizationsApi->get_organization: %s\n" % e)
        return
    pprint(api_response)

```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

[apikey](../README.md#apikey)

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

