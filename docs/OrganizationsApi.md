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
from rockset.api import organizations_api
from rockset.model.organization_response import OrganizationResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with rockset.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Organization
        api_response = api_instance.get_organization()
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling OrganizationsApi->get_organization: %s\n" % e)
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

