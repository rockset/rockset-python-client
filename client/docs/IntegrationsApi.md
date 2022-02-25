# swagger_client.IntegrationsApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_integration**](IntegrationsApi.md#create_integration) | **POST** /v1/orgs/self/integrations | Create Integration
[**delete_integration**](IntegrationsApi.md#delete_integration) | **DELETE** /v1/orgs/self/integrations/{integration} | Delete Integration
[**get_integration**](IntegrationsApi.md#get_integration) | **GET** /v1/orgs/self/integrations/{integration} | Retrieve Integration
[**list_integrations**](IntegrationsApi.md#list_integrations) | **GET** /v1/orgs/self/integrations | List Integrations


# **create_integration**
> CreateIntegrationResponse create_integration(body)

Create Integration

Create a new integration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationsApi()
body = swagger_client.CreateIntegrationRequest() # CreateIntegrationRequest | integration credentials

try:
    # Create Integration
    api_response = api_instance.create_integration(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->create_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateIntegrationRequest**](CreateIntegrationRequest.md)| integration credentials | 

### Return type

[**CreateIntegrationResponse**](CreateIntegrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_integration**
> DeleteIntegrationResponse delete_integration(integration)

Delete Integration

Remove an integration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationsApi()
integration = 'integration_example' # str | name of the integration

try:
    # Delete Integration
    api_response = api_instance.delete_integration(integration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->delete_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**| name of the integration | 

### Return type

[**DeleteIntegrationResponse**](DeleteIntegrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration**
> GetIntegrationResponse get_integration(integration)

Retrieve Integration

Retrieve information about a single integration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationsApi()
integration = 'integration_example' # str | name of the integration

try:
    # Retrieve Integration
    api_response = api_instance.get_integration(integration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration** | **str**| name of the integration | 

### Return type

[**GetIntegrationResponse**](GetIntegrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integrations**
> ListIntegrationsResponse list_integrations()

List Integrations

List all integrations in an organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationsApi()

try:
    # List Integrations
    api_response = api_instance.list_integrations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->list_integrations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListIntegrationsResponse**](ListIntegrationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

