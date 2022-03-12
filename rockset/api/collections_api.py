"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401

from rockset.api_client import ApiClient, Endpoint as _Endpoint
from rockset.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from rockset.model.azure_blob_collection_creation_request import AzureBlobCollectionCreationRequest
from rockset.model.create_collection_response import CreateCollectionResponse
from rockset.model.delete_collection_response import DeleteCollectionResponse
from rockset.model.error_model import ErrorModel
from rockset.model.gcs_collection_creation_request import GcsCollectionCreationRequest
from rockset.model.get_collection_response import GetCollectionResponse
from rockset.model.list_collections_response import ListCollectionsResponse
from rockset.models import *


class CollectionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_azure_blob_collection_endpoint = _Endpoint(
            settings={
                'response_type': (CreateCollectionResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/ws/{workspace}/collections#AzureBlob'.split('#')[0],
                'operation_id': 'create_azure_blob_collection',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace',
                    'azure_blob_collection_creation_request',
                ],
                'required': [
                    'workspace',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workspace':
                        (str,),
                    'azure_blob_collection_creation_request':
                        (AzureBlobCollectionCreationRequest,),
                },
                'attribute_map': {
                    'workspace': 'workspace',
                },
                'location_map': {
                    'workspace': 'path',
                    'azure_blob_collection_creation_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.create_gcs_collection_endpoint = _Endpoint(
            settings={
                'response_type': (CreateCollectionResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/ws/{workspace}/collections#Gcs'.split('#')[0],
                'operation_id': 'create_gcs_collection',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace',
                    'gcs_collection_creation_request',
                ],
                'required': [
                    'workspace',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workspace':
                        (str,),
                    'gcs_collection_creation_request':
                        (GcsCollectionCreationRequest,),
                },
                'attribute_map': {
                    'workspace': 'workspace',
                },
                'location_map': {
                    'workspace': 'path',
                    'gcs_collection_creation_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_collection_endpoint = _Endpoint(
            settings={
                'response_type': (DeleteCollectionResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/ws/{workspace}/collections/{collection}'.split('#')[0],
                'operation_id': 'delete_collection',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace',
                    'collection',
                ],
                'required': [
                    'workspace',
                    'collection',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workspace':
                        (str,),
                    'collection':
                        (str,),
                },
                'attribute_map': {
                    'workspace': 'workspace',
                    'collection': 'collection',
                },
                'location_map': {
                    'workspace': 'path',
                    'collection': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_collection_endpoint = _Endpoint(
            settings={
                'response_type': (GetCollectionResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/ws/{workspace}/collections/{collection}'.split('#')[0],
                'operation_id': 'get_collection',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace',
                    'collection',
                ],
                'required': [
                    'workspace',
                    'collection',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workspace':
                        (str,),
                    'collection':
                        (str,),
                },
                'attribute_map': {
                    'workspace': 'workspace',
                    'collection': 'collection',
                },
                'location_map': {
                    'workspace': 'path',
                    'collection': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_collections_endpoint = _Endpoint(
            settings={
                'response_type': (ListCollectionsResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/collections'.split('#')[0],
                'operation_id': 'list_collections',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.workspace_collections_endpoint = _Endpoint(
            settings={
                'response_type': (ListCollectionsResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/ws/{workspace}/collections'.split('#')[0],
                'operation_id': 'workspace_collections',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace',
                ],
                'required': [
                    'workspace',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'workspace':
                        (str,),
                },
                'attribute_map': {
                    'workspace': 'workspace',
                },
                'location_map': {
                    'workspace': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def create_azure_blob_collection(
        self,
        *,
        name: str,
        clustering_key: typing.List[FieldPartition]=None,
        description: str=None,
        event_time_info: EventTimeInfo=None,
        field_mapping_query: FieldMappingQuery=None,
        field_mappings: typing.List[FieldMappingV2]=None,
        field_schemas: typing.List[FieldSchema]=None,
        insert_only: bool=None,
        inverted_index_group_encoding_options: InvertedIndexGroupEncodingOptions=None,
        retention_secs: int=None,
        sources: typing.List[AzureBlobStorageSourceWrapper]=None,
        time_partition_resolution_secs: int=None,
        workspace="commons",
        **kwargs
    ):
        """Create azure blob collection  # noqa: E501

        Create new collection in a workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_azure_blob_collection(azure_blob_collection_creation_request, workspace="commons", async_req=True)
        >>> result = thread.get()

        Args:
            azure_blob_collection_creation_request (AzureBlobCollectionCreationRequest): JSON object
            workspace (str): name of the workspace. defaults to "commons", must be one of ["commons"]

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is False.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CreateCollectionResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', False
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['workspace'] = \
            workspace
        kwargs['azure_blob_collection_creation_request'] = \
            kwargs['azure_blob_collection_creation_request']
        return self.create_azure_blob_collection_endpoint.call_with_http_info(**kwargs)

    def create_gcs_collection(
        self,
        *,
        name: str,
        clustering_key: typing.List[FieldPartition]=None,
        description: str=None,
        event_time_info: EventTimeInfo=None,
        field_mapping_query: FieldMappingQuery=None,
        field_mappings: typing.List[FieldMappingV2]=None,
        field_schemas: typing.List[FieldSchema]=None,
        insert_only: bool=None,
        inverted_index_group_encoding_options: InvertedIndexGroupEncodingOptions=None,
        retention_secs: int=None,
        sources: typing.List[GcsSourceWrapper]=None,
        time_partition_resolution_secs: int=None,
        workspace="commons",
        **kwargs
    ):
        """Create gcs collection  # noqa: E501

        Create new collection in a workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_gcs_collection(gcs_collection_creation_request, workspace="commons", async_req=True)
        >>> result = thread.get()

        Args:
            gcs_collection_creation_request (GcsCollectionCreationRequest): JSON object
            workspace (str): name of the workspace. defaults to "commons", must be one of ["commons"]

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is False.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CreateCollectionResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', False
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['workspace'] = \
            workspace
        kwargs['gcs_collection_creation_request'] = \
            kwargs['gcs_collection_creation_request']
        return self.create_gcs_collection_endpoint.call_with_http_info(**kwargs)

    def delete_collection(
        self,
        *,
        collection: str,
        workspace="commons",
        **kwargs
    ):
        """Delete Collection  # noqa: E501

        Delete a collection and all its documents from Rockset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_collection(collection, workspace="commons", async_req=True)
        >>> result = thread.get()

        Args:
            collection (str): name of the collection
            workspace (str): name of the workspace. defaults to "commons", must be one of ["commons"]

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is False.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            DeleteCollectionResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', False
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['workspace'] = \
            workspace
        kwargs['collection'] = \
            collection
        return self.delete_collection_endpoint.call_with_http_info(**kwargs)

    def get_collection(
        self,
        *,
        collection: str,
        workspace="commons",
        **kwargs
    ):
        """Retrieve Collection  # noqa: E501

        Get details about a collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_collection(collection, workspace="commons", async_req=True)
        >>> result = thread.get()

        Args:
            collection (str): name of the collection
            workspace (str): name of the workspace. defaults to "commons", must be one of ["commons"]

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is False.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            GetCollectionResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', False
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['workspace'] = \
            workspace
        kwargs['collection'] = \
            collection
        return self.get_collection_endpoint.call_with_http_info(**kwargs)

    def list_collections(
        self,
        **kwargs
    ):
        """List Collections  # noqa: E501

        Retrieve all collections in an organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_collections(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is False.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ListCollectionsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', False
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_collections_endpoint.call_with_http_info(**kwargs)

    def workspace_collections(
        self,
        *,
        workspace="commons",
        **kwargs
    ):
        """List Collections in Workspace  # noqa: E501

        Retrieve all collections in a workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.workspace_collections(workspace="commons", async_req=True)
        >>> result = thread.get()

        Args:
            workspace (str): name of the workspace. defaults to "commons", must be one of ["commons"]

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is False.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ListCollectionsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', False
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['workspace'] = \
            workspace
        return self.workspace_collections_endpoint.call_with_http_info(**kwargs)


    body_params_dict = dict()
    return_types_dict = dict()
    body_params_dict['create_azure_blob_collection'] = 'azure_blob_collection_creation_request'
    return_types_dict['create_azure_blob_collection'] = AzureBlobCollectionCreationRequest
    body_params_dict['create_gcs_collection'] = 'gcs_collection_creation_request'
    return_types_dict['create_gcs_collection'] = GcsCollectionCreationRequest