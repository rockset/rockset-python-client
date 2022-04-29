"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401

import asyncio

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
from rockset.model.add_documents_request import AddDocumentsRequest
from rockset.model.add_documents_response import AddDocumentsResponse
from rockset.model.delete_documents_request import DeleteDocumentsRequest
from rockset.model.delete_documents_response import DeleteDocumentsResponse
from rockset.model.error_model import ErrorModel
from rockset.model.patch_documents_request import PatchDocumentsRequest
from rockset.model.patch_documents_response import PatchDocumentsResponse
from rockset.models import *


class Documents(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.add_documents_endpoint = _Endpoint(
            settings={
                'response_type': (AddDocumentsResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/ws/{workspace}/collections/{collection}/docs'.split('#')[0],
                'operation_id': 'add_documents',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace',
                    'collection',
                    'add_documents_request',
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
                    'add_documents_request':
                        (AddDocumentsRequest,),
                },
                'attribute_map': {
                    'workspace': 'workspace',
                    'collection': 'collection',
                },
                'location_map': {
                    'workspace': 'path',
                    'collection': 'path',
                    'add_documents_request': 'body',
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
        self.delete_documents_endpoint = _Endpoint(
            settings={
                'response_type': (DeleteDocumentsResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/ws/{workspace}/collections/{collection}/docs'.split('#')[0],
                'operation_id': 'delete_documents',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace',
                    'collection',
                    'delete_documents_request',
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
                    'delete_documents_request':
                        (DeleteDocumentsRequest,),
                },
                'attribute_map': {
                    'workspace': 'workspace',
                    'collection': 'collection',
                },
                'location_map': {
                    'workspace': 'path',
                    'collection': 'path',
                    'delete_documents_request': 'body',
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
        self.patch_documents_endpoint = _Endpoint(
            settings={
                'response_type': (PatchDocumentsResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/ws/{workspace}/collections/{collection}/docs'.split('#')[0],
                'operation_id': 'patch_documents',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace',
                    'collection',
                    'patch_documents_request',
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
                    'patch_documents_request':
                        (PatchDocumentsRequest,),
                },
                'attribute_map': {
                    'workspace': 'workspace',
                    'collection': 'collection',
                },
                'location_map': {
                    'workspace': 'path',
                    'collection': 'path',
                    'patch_documents_request': 'body',
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

    def add_documents(
        self,
        *,
        collection: str,
        data: typing.Sequence,
        workspace = "commons",
        **kwargs
    ) -> typing.Union[AddDocumentsResponse, asyncio.Future]:
        """Add Documents  # noqa: E501

        Add documents to a collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.Documents.add_documents(
            collection="collection_example",
            data=[{"field":"value"}],
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            workspace (str): Name of the workspace.. [required] if omitted the server will use the default value of "commons"
            collection (str): Name of the collection.. [required]
            data ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]): Array of documents to be added to the collection.. [required]
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
                should be done on the data received from the server.
                If False, the client will also not convert nested inner objects
                into the respective model types (the outermost object
                is still converted to the model).
                Default is True.
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
            AddDocumentsResponse
                If the method is called asynchronously, returns an asyncio.Future which resolves to the response.
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
            '_check_return_type', True
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
        kwargs['add_documents_request'] = \
            kwargs['add_documents_request']
        return self.add_documents_endpoint.call_with_http_info(**kwargs)

    def delete_documents(
        self,
        *,
        collection: str,
        data: typing.Sequence[DeleteDocumentsRequestData],
        workspace = "commons",
        **kwargs
    ) -> typing.Union[DeleteDocumentsResponse, asyncio.Future]:
        """Delete Documents  # noqa: E501

        Delete documents from a collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.Documents.delete_documents(
            collection="collection_example",
            data=[
                DeleteDocumentsRequestData(
                    id="2cd61e3b",
                ),
            ],
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            workspace (str): Name of the workspace.. [required] if omitted the server will use the default value of "commons"
            collection (str): Name of the collection.. [required]
            data ([DeleteDocumentsRequestData]): Array of IDs of documents to be deleted. [required]
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
                should be done on the data received from the server.
                If False, the client will also not convert nested inner objects
                into the respective model types (the outermost object
                is still converted to the model).
                Default is True.
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
            DeleteDocumentsResponse
                If the method is called asynchronously, returns an asyncio.Future which resolves to the response.
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
            '_check_return_type', True
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
        kwargs['delete_documents_request'] = \
            kwargs['delete_documents_request']
        return self.delete_documents_endpoint.call_with_http_info(**kwargs)

    def patch_documents(
        self,
        *,
        collection: str,
        data: typing.Sequence[PatchDocument],
        workspace = "commons",
        **kwargs
    ) -> typing.Union[PatchDocumentsResponse, asyncio.Future]:
        """Patch Documents  # noqa: E501

        Update existing documents in a collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.Documents.patch_documents(
            collection="collection_example",
            data=[
                PatchDocument(
                    id="ca2d6832-1bfd-f88f-0620-d2aa27a5d86c",
                    patch=[
                        PatchOperation(
                            _from="_from_example",
                            op="ADD",
                            path="/foo/bar",
                            value={},
                        ),
                    ],
                ),
            ],
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            workspace (str): Name of the workspace.. [required] if omitted the server will use the default value of "commons"
            collection (str): Name of the collection.. [required]
            data ([PatchDocument]): List of patches to be applied.. [required]
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
                should be done on the data received from the server.
                If False, the client will also not convert nested inner objects
                into the respective model types (the outermost object
                is still converted to the model).
                Default is True.
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
            PatchDocumentsResponse
                If the method is called asynchronously, returns an asyncio.Future which resolves to the response.
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
            '_check_return_type', True
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
        kwargs['patch_documents_request'] = \
            kwargs['patch_documents_request']
        return self.patch_documents_endpoint.call_with_http_info(**kwargs)


    body_params_dict = dict()
    return_types_dict = dict()
    body_params_dict['add_documents'] = 'add_documents_request'
    return_types_dict['add_documents'] = AddDocumentsRequest
    body_params_dict['delete_documents'] = 'delete_documents_request'
    return_types_dict['delete_documents'] = DeleteDocumentsRequest
    body_params_dict['patch_documents'] = 'patch_documents_request'
    return_types_dict['patch_documents'] = PatchDocumentsRequest
