Things that are currently being worked on:
- Docs
- Polishing
- QA
# rockset
Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.

All endpoints are only accessible via https.

Build something awesome!

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

Until the library is actually published in Pypi, you can install this client by running:
```sh
pip install ./dist/rockset-1.0.0-py3-none-any.whl
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import rockset
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import rockset
from pprint import pprint
from rockset.api import api_keys_api
from rockset.model.create_api_key_request import CreateApiKeyRequest
from rockset.model.create_api_key_response import CreateApiKeyResponse
from rockset.model.delete_api_key_response import DeleteApiKeyResponse
from rockset.model.error_model import ErrorModel
from rockset.model.get_api_key_response import GetApiKeyResponse
from rockset.model.list_api_keys_response import ListApiKeysResponse
from rockset.model.update_api_key_request import UpdateApiKeyRequest
from rockset.model.update_api_key_response import UpdateApiKeyResponse

# Enter a context with an instance of the API client
# Defining the host is optional and defaults to https://api.rs2.usw2.rockset.com
with rockset.RocksetClient(host="https://api.rs2.usw2.rockset.com", apikey="APIKEY") as rs:
    try:
        rs.ApiKey.create_api_key(name="api-key-name", role="member")
    except rockset.ApiException as e:
        print("Exception when calling ApiKey->create_api_key: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.rs2.usw2.rockset.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APIKeysApi* | [**create_api_key**](docs/APIKeysApi.md#create_api_key) | **POST** /v1/orgs/self/users/self/apikeys | Create API Key
*APIKeysApi* | [**delete_api_key**](docs/APIKeysApi.md#delete_api_key) | **DELETE** /v1/orgs/self/users/{user}/apikeys/{name} | Delete API Key
*APIKeysApi* | [**get_api_key**](docs/APIKeysApi.md#get_api_key) | **GET** /v1/orgs/self/users/{user}/apikeys/{name} | Retrieve API Key
*APIKeysApi* | [**list_api_keys**](docs/APIKeysApi.md#list_api_keys) | **GET** /v1/orgs/self/users/{user}/apikeys | List API Keys.
*APIKeysApi* | [**update_api_key**](docs/APIKeysApi.md#update_api_key) | **POST** /v1/orgs/self/users/{user}/apikeys/{name} | Update an API key&#39;s state
*AliasesApi* | [**create_alias**](docs/AliasesApi.md#create_alias) | **POST** /v1/orgs/self/ws/{workspace}/aliases | Create Alias
*AliasesApi* | [**delete_alias**](docs/AliasesApi.md#delete_alias) | **DELETE** /v1/orgs/self/ws/{workspace}/aliases/{alias} | Delete Alias
*AliasesApi* | [**get_alias**](docs/AliasesApi.md#get_alias) | **GET** /v1/orgs/self/ws/{workspace}/aliases/{alias} | Retrieve Alias
*AliasesApi* | [**list_aliases**](docs/AliasesApi.md#list_aliases) | **GET** /v1/orgs/self/aliases | List Aliases
*AliasesApi* | [**update_alias**](docs/AliasesApi.md#update_alias) | **POST** /v1/orgs/self/ws/{workspace}/aliases/{alias} | Update Alias
*AliasesApi* | [**workspace_aliases**](docs/AliasesApi.md#workspace_aliases) | **GET** /v1/orgs/self/ws/{workspace}/aliases | List Aliases in Workspace
*CollectionsApi* | [**create_azure_blob_collection**](docs/CollectionsApi.md#create_azure_blob_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections#AzureBlob | Create azure blob collection
*CollectionsApi* | [**create_gcs_collection**](docs/CollectionsApi.md#create_gcs_collection) | **POST** /v1/orgs/self/ws/{workspace}/collections#Gcs | Create gcs collection
*CollectionsApi* | [**delete_collection**](docs/CollectionsApi.md#delete_collection) | **DELETE** /v1/orgs/self/ws/{workspace}/collections/{collection} | Delete Collection
*CollectionsApi* | [**get_collection**](docs/CollectionsApi.md#get_collection) | **GET** /v1/orgs/self/ws/{workspace}/collections/{collection} | Retrieve Collection
*CollectionsApi* | [**list_collections**](docs/CollectionsApi.md#list_collections) | **GET** /v1/orgs/self/collections | List Collections
*CollectionsApi* | [**workspace_collections**](docs/CollectionsApi.md#workspace_collections) | **GET** /v1/orgs/self/ws/{workspace}/collections | List Collections in Workspace
*CustomRolesBetaApi* | [**create_role**](docs/CustomRolesBetaApi.md#create_role) | **POST** /v1/orgs/self/roles | Create a Role
*CustomRolesBetaApi* | [**delete_role**](docs/CustomRolesBetaApi.md#delete_role) | **DELETE** /v1/orgs/self/roles/{roleName} | Delete a Role
*CustomRolesBetaApi* | [**list_roles**](docs/CustomRolesBetaApi.md#list_roles) | **GET** /v1/orgs/self/roles | List Roles
*CustomRolesBetaApi* | [**update_role**](docs/CustomRolesBetaApi.md#update_role) | **POST** /v1/orgs/self/roles/{roleName} | Update a Role
*DocumentsApi* | [**add_documents**](docs/DocumentsApi.md#add_documents) | **POST** /v1/orgs/self/ws/{workspace}/collections/{collection}/docs | Add Documents
*DocumentsApi* | [**delete_documents**](docs/DocumentsApi.md#delete_documents) | **DELETE** /v1/orgs/self/ws/{workspace}/collections/{collection}/docs | Delete Documents
*DocumentsApi* | [**patch_documents**](docs/DocumentsApi.md#patch_documents) | **PATCH** /v1/orgs/self/ws/{workspace}/collections/{collection}/docs | Patch Documents
*IntegrationsApi* | [**create_azure_blob_integration**](docs/IntegrationsApi.md#create_azure_blob_integration) | **POST** /v1/orgs/self/integrations#AzureBlob | Create azure blob integration
*IntegrationsApi* | [**create_gcs_integration**](docs/IntegrationsApi.md#create_gcs_integration) | **POST** /v1/orgs/self/integrations#Gcs | Create gcs integration
*IntegrationsApi* | [**delete_integration**](docs/IntegrationsApi.md#delete_integration) | **DELETE** /v1/orgs/self/integrations/{integration} | Delete Integration
*IntegrationsApi* | [**get_integration**](docs/IntegrationsApi.md#get_integration) | **GET** /v1/orgs/self/integrations/{integration} | Retrieve Integration
*IntegrationsApi* | [**list_integrations**](docs/IntegrationsApi.md#list_integrations) | **GET** /v1/orgs/self/integrations | List Integrations
*OrganizationsApi* | [**get_organization**](docs/OrganizationsApi.md#get_organization) | **GET** /v1/orgs/self | Get Organization
*QueriesApi* | [**query**](docs/QueriesApi.md#query) | **POST** /v1/orgs/self/queries | Query
*QueriesApi* | [**validate**](docs/QueriesApi.md#validate) | **POST** /v1/orgs/self/queries/validations | Validate Query
*QueryLambdasApi* | [**create_query_lambda**](docs/QueryLambdasApi.md#create_query_lambda) | **POST** /v1/orgs/self/ws/{workspace}/lambdas | Create Query Lambda
*QueryLambdasApi* | [**create_query_lambda_tag**](docs/QueryLambdasApi.md#create_query_lambda_tag) | **POST** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/tags | Create Query Lambda Tag
*QueryLambdasApi* | [**delete_query_lambda**](docs/QueryLambdasApi.md#delete_query_lambda) | **DELETE** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda} | Delete Query Lambda
*QueryLambdasApi* | [**delete_query_lambda_tag**](docs/QueryLambdasApi.md#delete_query_lambda_tag) | **DELETE** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/tags/{tag} | Delete Query Lambda Tag Version
*QueryLambdasApi* | [**delete_query_lambda_version**](docs/QueryLambdasApi.md#delete_query_lambda_version) | **DELETE** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/version/{version} | Delete Query Lambda Version
*QueryLambdasApi* | [**execute_query_lambda**](docs/QueryLambdasApi.md#execute_query_lambda) | **POST** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/versions/{version} | Execute Query Lambda By Version
*QueryLambdasApi* | [**execute_query_lambda_by_tag**](docs/QueryLambdasApi.md#execute_query_lambda_by_tag) | **POST** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/tags/{tag} | Execute Query Lambda By Tag
*QueryLambdasApi* | [**get_query_lambda_tag_version**](docs/QueryLambdasApi.md#get_query_lambda_tag_version) | **GET** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/tags/{tag} | Retrieve Query Lambda Tag
*QueryLambdasApi* | [**get_query_lambda_version**](docs/QueryLambdasApi.md#get_query_lambda_version) | **GET** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/versions/{version} | Retrieve Query Lambda Version
*QueryLambdasApi* | [**list_all_query_lambdas**](docs/QueryLambdasApi.md#list_all_query_lambdas) | **GET** /v1/orgs/self/lambdas | List Query Lambdas
*QueryLambdasApi* | [**list_query_lambda_tags**](docs/QueryLambdasApi.md#list_query_lambda_tags) | **GET** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/tags | List Query Lambda Tags
*QueryLambdasApi* | [**list_query_lambda_versions**](docs/QueryLambdasApi.md#list_query_lambda_versions) | **GET** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/versions | List Query Lambda Versions
*QueryLambdasApi* | [**list_query_lambdas_in_workspace**](docs/QueryLambdasApi.md#list_query_lambdas_in_workspace) | **GET** /v1/orgs/self/ws/{workspace}/lambdas | List Query Lambdas in Workspace
*QueryLambdasApi* | [**update_query_lambda**](docs/QueryLambdasApi.md#update_query_lambda) | **POST** /v1/orgs/self/ws/{workspace}/lambdas/{queryLambda}/versions | Update Query Lambda
*UsersApi* | [**create_user**](docs/UsersApi.md#create_user) | **POST** /v1/orgs/self/users | Create User
*UsersApi* | [**delete_user**](docs/UsersApi.md#delete_user) | **DELETE** /v1/orgs/self/users/{user} | Delete User
*UsersApi* | [**get_current_user**](docs/UsersApi.md#get_current_user) | **GET** /v1/orgs/self/users/self | Retrieve Current User
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /v1/orgs/self/users/{user} | Retrieve User
*UsersApi* | [**list_unsubscribe_preferences**](docs/UsersApi.md#list_unsubscribe_preferences) | **GET** /v1/orgs/self/users/self/preferences | Get all notification preferences
*UsersApi* | [**list_users**](docs/UsersApi.md#list_users) | **GET** /v1/orgs/self/users | List Users
*UsersApi* | [**update_unsubscribe_preferences**](docs/UsersApi.md#update_unsubscribe_preferences) | **POST** /v1/orgs/self/users/self/preferences | Update notification preferences
*ViewsApi* | [**create_view**](docs/ViewsApi.md#create_view) | **POST** /v1/orgs/self/ws/{workspace}/views | Create View
*ViewsApi* | [**delete_view**](docs/ViewsApi.md#delete_view) | **DELETE** /v1/orgs/self/ws/{workspace}/views/{view} | Delete View
*ViewsApi* | [**get_view**](docs/ViewsApi.md#get_view) | **GET** /v1/orgs/self/ws/{workspace}/views/{view} | Retrieve View
*ViewsApi* | [**list_views**](docs/ViewsApi.md#list_views) | **GET** /v1/orgs/self/views | List Views
*ViewsApi* | [**update_view**](docs/ViewsApi.md#update_view) | **POST** /v1/orgs/self/ws/{workspace}/views/{view} | Update View
*ViewsApi* | [**workspace_views**](docs/ViewsApi.md#workspace_views) | **GET** /v1/orgs/self/ws/{workspace}/views | List Views in Workspace
*VirtualInstancesApi* | [**get_virtual_instance**](docs/VirtualInstancesApi.md#get_virtual_instance) | **GET** /v1/orgs/self/virtualinstances/{virtualInstanceId} | Retrieve Virtual Instance
*VirtualInstancesApi* | [**list_virtual_instances**](docs/VirtualInstancesApi.md#list_virtual_instances) | **GET** /v1/orgs/self/virtualinstances | List Virtual Instances
*VirtualInstancesApi* | [**set_virtual_instance**](docs/VirtualInstancesApi.md#set_virtual_instance) | **POST** /v1/orgs/self/virtualinstances/{virtualInstanceId} | Update Virtual Instance
*WorkspacesApi* | [**child_workspaces**](docs/WorkspacesApi.md#child_workspaces) | **GET** /v1/orgs/self/ws/{workspace}/ws | List Workspaces in Workspace
*WorkspacesApi* | [**create_workspace**](docs/WorkspacesApi.md#create_workspace) | **POST** /v1/orgs/self/ws | Create Workspace
*WorkspacesApi* | [**delete_workspace**](docs/WorkspacesApi.md#delete_workspace) | **DELETE** /v1/orgs/self/ws/{workspace} | Delete Workspace
*WorkspacesApi* | [**get_workspace**](docs/WorkspacesApi.md#get_workspace) | **GET** /v1/orgs/self/ws/{workspace} | Retrieve Workspace
*WorkspacesApi* | [**list_workspaces**](docs/WorkspacesApi.md#list_workspaces) | **GET** /v1/orgs/self/ws | List Workspaces


## Documentation For Models

 - [AddDocumentsRequest](docs/AddDocumentsRequest.md)
 - [AddDocumentsResponse](docs/AddDocumentsResponse.md)
 - [Alias](docs/Alias.md)
 - [ApiKey](docs/ApiKey.md)
 - [AwsAccessKey](docs/AwsAccessKey.md)
 - [AwsRole](docs/AwsRole.md)
 - [AzEventHubIntegration](docs/AzEventHubIntegration.md)
 - [AzServiceBusIntegration](docs/AzServiceBusIntegration.md)
 - [AzureBlobCollectionCreationRequest](docs/AzureBlobCollectionCreationRequest.md)
 - [AzureBlobIntegrationCreationRequest](docs/AzureBlobIntegrationCreationRequest.md)
 - [AzureBlobStorageIntegration](docs/AzureBlobStorageIntegration.md)
 - [AzureBlobStorageSourceWrapper](docs/AzureBlobStorageSourceWrapper.md)
 - [Cluster](docs/Cluster.md)
 - [Collection](docs/Collection.md)
 - [CollectionStats](docs/CollectionStats.md)
 - [CreateAliasRequest](docs/CreateAliasRequest.md)
 - [CreateAliasResponse](docs/CreateAliasResponse.md)
 - [CreateApiKeyRequest](docs/CreateApiKeyRequest.md)
 - [CreateApiKeyResponse](docs/CreateApiKeyResponse.md)
 - [CreateCollectionRequest](docs/CreateCollectionRequest.md)
 - [CreateCollectionResponse](docs/CreateCollectionResponse.md)
 - [CreateIntegrationRequest](docs/CreateIntegrationRequest.md)
 - [CreateIntegrationResponse](docs/CreateIntegrationResponse.md)
 - [CreateQueryLambdaRequest](docs/CreateQueryLambdaRequest.md)
 - [CreateQueryLambdaTagRequest](docs/CreateQueryLambdaTagRequest.md)
 - [CreateRoleRequest](docs/CreateRoleRequest.md)
 - [CreateUserRequest](docs/CreateUserRequest.md)
 - [CreateUserResponse](docs/CreateUserResponse.md)
 - [CreateViewRequest](docs/CreateViewRequest.md)
 - [CreateViewResponse](docs/CreateViewResponse.md)
 - [CreateWorkspaceRequest](docs/CreateWorkspaceRequest.md)
 - [CreateWorkspaceResponse](docs/CreateWorkspaceResponse.md)
 - [CsvParams](docs/CsvParams.md)
 - [DeleteAliasResponse](docs/DeleteAliasResponse.md)
 - [DeleteApiKeyResponse](docs/DeleteApiKeyResponse.md)
 - [DeleteCollectionResponse](docs/DeleteCollectionResponse.md)
 - [DeleteDocumentsRequest](docs/DeleteDocumentsRequest.md)
 - [DeleteDocumentsRequestData](docs/DeleteDocumentsRequestData.md)
 - [DeleteDocumentsResponse](docs/DeleteDocumentsResponse.md)
 - [DeleteIntegrationResponse](docs/DeleteIntegrationResponse.md)
 - [DeleteQueryLambdaResponse](docs/DeleteQueryLambdaResponse.md)
 - [DeleteUserResponse](docs/DeleteUserResponse.md)
 - [DeleteViewResponse](docs/DeleteViewResponse.md)
 - [DeleteWorkspaceResponse](docs/DeleteWorkspaceResponse.md)
 - [DocumentStatus](docs/DocumentStatus.md)
 - [DynamodbIntegration](docs/DynamodbIntegration.md)
 - [ErrorModel](docs/ErrorModel.md)
 - [EventTimeInfo](docs/EventTimeInfo.md)
 - [ExecuteQueryLambdaRequest](docs/ExecuteQueryLambdaRequest.md)
 - [FieldMappingQuery](docs/FieldMappingQuery.md)
 - [FieldMappingV2](docs/FieldMappingV2.md)
 - [FieldMask](docs/FieldMask.md)
 - [FieldMaskMask](docs/FieldMaskMask.md)
 - [FieldOptions](docs/FieldOptions.md)
 - [FieldPartition](docs/FieldPartition.md)
 - [FieldSchema](docs/FieldSchema.md)
 - [FormatParams](docs/FormatParams.md)
 - [GcpServiceAccount](docs/GcpServiceAccount.md)
 - [GcsCollectionCreationRequest](docs/GcsCollectionCreationRequest.md)
 - [GcsIntegration](docs/GcsIntegration.md)
 - [GcsIntegrationCreationRequest](docs/GcsIntegrationCreationRequest.md)
 - [GcsSourceWrapper](docs/GcsSourceWrapper.md)
 - [GetAliasResponse](docs/GetAliasResponse.md)
 - [GetApiKeyResponse](docs/GetApiKeyResponse.md)
 - [GetCollectionResponse](docs/GetCollectionResponse.md)
 - [GetIntegrationResponse](docs/GetIntegrationResponse.md)
 - [GetViewResponse](docs/GetViewResponse.md)
 - [GetVirtualInstanceResponse](docs/GetVirtualInstanceResponse.md)
 - [GetWorkspaceResponse](docs/GetWorkspaceResponse.md)
 - [InputField](docs/InputField.md)
 - [Integration](docs/Integration.md)
 - [InvertedIndexGroupEncodingOptions](docs/InvertedIndexGroupEncodingOptions.md)
 - [KafkaIntegration](docs/KafkaIntegration.md)
 - [KafkaV3SecurityConfig](docs/KafkaV3SecurityConfig.md)
 - [KinesisIntegration](docs/KinesisIntegration.md)
 - [ListAliasesResponse](docs/ListAliasesResponse.md)
 - [ListApiKeysResponse](docs/ListApiKeysResponse.md)
 - [ListCollectionsResponse](docs/ListCollectionsResponse.md)
 - [ListIntegrationsResponse](docs/ListIntegrationsResponse.md)
 - [ListQueryLambdaTagsResponse](docs/ListQueryLambdaTagsResponse.md)
 - [ListQueryLambdaVersionsResponse](docs/ListQueryLambdaVersionsResponse.md)
 - [ListQueryLambdasResponse](docs/ListQueryLambdasResponse.md)
 - [ListRolesResponse](docs/ListRolesResponse.md)
 - [ListUnsubscribePreferencesResponse](docs/ListUnsubscribePreferencesResponse.md)
 - [ListUsersResponse](docs/ListUsersResponse.md)
 - [ListViewsResponse](docs/ListViewsResponse.md)
 - [ListVirtualInstancesResponse](docs/ListVirtualInstancesResponse.md)
 - [ListWorkspacesResponse](docs/ListWorkspacesResponse.md)
 - [MongoDbIntegration](docs/MongoDbIntegration.md)
 - [Organization](docs/Organization.md)
 - [OrganizationResponse](docs/OrganizationResponse.md)
 - [OutputField](docs/OutputField.md)
 - [PaginationInfo](docs/PaginationInfo.md)
 - [PatchDocument](docs/PatchDocument.md)
 - [PatchDocumentsRequest](docs/PatchDocumentsRequest.md)
 - [PatchDocumentsResponse](docs/PatchDocumentsResponse.md)
 - [PatchOperation](docs/PatchOperation.md)
 - [Privilege](docs/Privilege.md)
 - [QueryError](docs/QueryError.md)
 - [QueryFieldType](docs/QueryFieldType.md)
 - [QueryLambda](docs/QueryLambda.md)
 - [QueryLambdaSql](docs/QueryLambdaSql.md)
 - [QueryLambdaStats](docs/QueryLambdaStats.md)
 - [QueryLambdaTag](docs/QueryLambdaTag.md)
 - [QueryLambdaTagResponse](docs/QueryLambdaTagResponse.md)
 - [QueryLambdaVersion](docs/QueryLambdaVersion.md)
 - [QueryLambdaVersionResponse](docs/QueryLambdaVersionResponse.md)
 - [QueryParameter](docs/QueryParameter.md)
 - [QueryRequest](docs/QueryRequest.md)
 - [QueryRequestSql](docs/QueryRequestSql.md)
 - [QueryResponse](docs/QueryResponse.md)
 - [QueryResponseStats](docs/QueryResponseStats.md)
 - [RedshiftIntegration](docs/RedshiftIntegration.md)
 - [Role](docs/Role.md)
 - [RoleResponse](docs/RoleResponse.md)
 - [S3Integration](docs/S3Integration.md)
 - [SegmentIntegration](docs/SegmentIntegration.md)
 - [Source](docs/Source.md)
 - [SourceAzEventHub](docs/SourceAzEventHub.md)
 - [SourceAzServiceBus](docs/SourceAzServiceBus.md)
 - [SourceAzureBlobStorage](docs/SourceAzureBlobStorage.md)
 - [SourceDynamoDb](docs/SourceDynamoDb.md)
 - [SourceFileUpload](docs/SourceFileUpload.md)
 - [SourceGcs](docs/SourceGcs.md)
 - [SourceKafka](docs/SourceKafka.md)
 - [SourceKinesis](docs/SourceKinesis.md)
 - [SourceMongoDb](docs/SourceMongoDb.md)
 - [SourceRedshift](docs/SourceRedshift.md)
 - [SourceS3](docs/SourceS3.md)
 - [SqlExpression](docs/SqlExpression.md)
 - [Status](docs/Status.md)
 - [StatusAzEventHub](docs/StatusAzEventHub.md)
 - [StatusAzEventHubPartition](docs/StatusAzEventHubPartition.md)
 - [StatusAzServiceBus](docs/StatusAzServiceBus.md)
 - [StatusDynamoDb](docs/StatusDynamoDb.md)
 - [StatusDynamoDbV2](docs/StatusDynamoDbV2.md)
 - [StatusKafka](docs/StatusKafka.md)
 - [StatusKafkaPartition](docs/StatusKafkaPartition.md)
 - [StatusMongoDb](docs/StatusMongoDb.md)
 - [UnsubscribePreference](docs/UnsubscribePreference.md)
 - [UpdateAliasRequest](docs/UpdateAliasRequest.md)
 - [UpdateApiKeyRequest](docs/UpdateApiKeyRequest.md)
 - [UpdateApiKeyResponse](docs/UpdateApiKeyResponse.md)
 - [UpdateQueryLambdaRequest](docs/UpdateQueryLambdaRequest.md)
 - [UpdateRoleRequest](docs/UpdateRoleRequest.md)
 - [UpdateUnsubscribePreferencesRequest](docs/UpdateUnsubscribePreferencesRequest.md)
 - [UpdateUnsubscribePreferencesResponse](docs/UpdateUnsubscribePreferencesResponse.md)
 - [UpdateViewRequest](docs/UpdateViewRequest.md)
 - [UpdateViewResponse](docs/UpdateViewResponse.md)
 - [UpdateVirtualInstanceRequest](docs/UpdateVirtualInstanceRequest.md)
 - [UpdateVirtualInstanceResponse](docs/UpdateVirtualInstanceResponse.md)
 - [User](docs/User.md)
 - [ValidateQueryResponse](docs/ValidateQueryResponse.md)
 - [View](docs/View.md)
 - [VirtualInstance](docs/VirtualInstance.md)
 - [Workspace](docs/Workspace.md)
 - [XmlParams](docs/XmlParams.md)


## Documentation For Authorization

The RocksetClient object must be instantiated with an apikey. You can create your first apikey in the [Rockset console](https://console.rockset.com/apikeys). The provided apikey will be used for all requests that are made using the instance of the client.

```python
rs = RocksetClient(apikey="aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT")
```

The client will automatically include the provided apikey within the authorization header of every request.

```
Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT
```

## Author

Rockset

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in rockset.apis and rockset.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from rockset.api.default_api import DefaultApi`
- `from rockset.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import rockset
from rockset.apis import *
from rockset.models import *
```

