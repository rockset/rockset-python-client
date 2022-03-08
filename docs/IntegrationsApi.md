# rockset.IntegrationsApi

All URIs are relative to *https://api.rs2.usw2.rockset.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_azure_blob_integration**](IntegrationsApi.md#create_azure_blob_integration) | **POST** /v1/orgs/self/integrations#AzureBlob | Create azure blob integration
[**create_gcs_integration**](IntegrationsApi.md#create_gcs_integration) | **POST** /v1/orgs/self/integrations#Gcs | Create gcs integration
[**delete_integration**](IntegrationsApi.md#delete_integration) | **DELETE** /v1/orgs/self/integrations/{integration} | Delete Integration
[**get_integration**](IntegrationsApi.md#get_integration) | **GET** /v1/orgs/self/integrations/{integration} | Retrieve Integration
[**list_integrations**](IntegrationsApi.md#list_integrations) | **GET** /v1/orgs/self/integrations | List Integrations


# **create_azure_blob_integration**
> CreateIntegrationResponse create_azure_blob_integration(azure_blob_integration_creation_request)

Create azure blob integration

Create a new integration.

### Example


```python
import time
import rockset
from rockset.api import integrations_api
from rockset.model.create_integration_response import CreateIntegrationResponse
from rockset.model.error_model import ErrorModel
from rockset.model.azure_blob_integration_creation_request import AzureBlobIntegrationCreationRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    azure_blob_integration_creation_request = AzureBlobIntegrationCreationRequest(
        azure_blob_storage=AzureBlobStorageIntegration(
            connection_string="connection_string_example",
        ),
        description="AWS account with event data for the data science team.",
        name="event-logs",
    ) # AzureBlobIntegrationCreationRequest | integration credentials

    # example passing only required values which don't have defaults set
    try:
        # Create azure blob integration
        api_response = api_instance.create_azure_blob_integration(azure_blob_integration_creation_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling IntegrationsApi->create_azure_blob_integration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_blob_integration_creation_request** | [**AzureBlobIntegrationCreationRequest**](AzureBlobIntegrationCreationRequest.md)| integration credentials |

### Return type

[**CreateIntegrationResponse**](CreateIntegrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | integration created successfully |  -  |
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

# **create_gcs_integration**
> CreateIntegrationResponse create_gcs_integration(gcs_integration_creation_request)

Create gcs integration

Create a new integration.

### Example


```python
import time
import rockset
from rockset.api import integrations_api
from rockset.model.create_integration_response import CreateIntegrationResponse
from rockset.model.error_model import ErrorModel
from rockset.model.gcs_integration_creation_request import GcsIntegrationCreationRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    gcs_integration_creation_request = GcsIntegrationCreationRequest(
        description="AWS account with event data for the data science team.",
        gcs=GcsIntegration(
            gcp_service_account=GcpServiceAccount(
                service_account_key_file_json="service_account_key_file_json_example",
            ),
        ),
        name="event-logs",
    ) # GcsIntegrationCreationRequest | integration credentials

    # example passing only required values which don't have defaults set
    try:
        # Create gcs integration
        api_response = api_instance.create_gcs_integration(gcs_integration_creation_request)
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling IntegrationsApi->create_gcs_integration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcs_integration_creation_request** | [**GcsIntegrationCreationRequest**](GcsIntegrationCreationRequest.md)| integration credentials |

### Return type

[**CreateIntegrationResponse**](CreateIntegrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | integration created successfully |  -  |
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

# **delete_integration**
> DeleteIntegrationResponse delete_integration(integration)

Delete Integration

Remove an integration.

### Example


```python
import time
import rockset
from rockset.api import integrations_api
from rockset.model.delete_integration_response import DeleteIntegrationResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    integration = "integration_example" # str | name of the integration

    # example passing only required values which don't have defaults set
    try:
        # Delete Integration
        api_response = api_instance.delete_integration(integration)
        pprint(api_response)
    except rockset.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | integration deleted successfully |  -  |
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

# **get_integration**
> GetIntegrationResponse get_integration(integration)

Retrieve Integration

Retrieve information about a single integration.

### Example


```python
import time
import rockset
from rockset.api import integrations_api
from rockset.model.error_model import ErrorModel
from rockset.model.get_integration_response import GetIntegrationResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)
    integration = "integration_example" # str | name of the integration

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Integration
        api_response = api_instance.get_integration(integration)
        pprint(api_response)
    except rockset.ApiException as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | integration retrieved successfully |  -  |
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

# **list_integrations**
> ListIntegrationsResponse list_integrations()

List Integrations

List all integrations in an organization.

### Example


```python
import time
import rockset
from rockset.api import integrations_api
from rockset.model.list_integrations_response import ListIntegrationsResponse
from rockset.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rockset.Configuration(
    host = "https://api.rs2.usw2.rockset.com"
)


# Enter a context with an instance of the API client
with rockset.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = integrations_api.IntegrationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Integrations
        api_response = api_instance.list_integrations()
        pprint(api_response)
    except rockset.ApiException as e:
        print("Exception when calling IntegrationsApi->list_integrations: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListIntegrationsResponse**](ListIntegrationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | integrations retrieved successfully |  -  |
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

