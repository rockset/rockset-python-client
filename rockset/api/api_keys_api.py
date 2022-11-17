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
from rockset.model.create_api_key_request import CreateApiKeyRequest
from rockset.model.create_api_key_response import CreateApiKeyResponse
from rockset.model.delete_api_key_response import DeleteApiKeyResponse
from rockset.model.error_model import ErrorModel
from rockset.model.get_api_key_response import GetApiKeyResponse
from rockset.model.list_api_keys_response import ListApiKeysResponse
from rockset.model.update_api_key_request import UpdateApiKeyRequest
from rockset.model.update_api_key_response import UpdateApiKeyResponse
from rockset.models import *


class APIKeys(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_endpoint = _Endpoint(
            settings={
                'response_type': (CreateApiKeyResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/users/self/apikeys',
                'operation_id': 'create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'create_api_key_request',
                ],
                'required': [
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
                    'create_api_key_request':
                        (CreateApiKeyRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'create_api_key_request': 'body',
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
        self.delete_endpoint = _Endpoint(
            settings={
                'response_type': (DeleteApiKeyResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/users/{user}/apikeys/{name}',
                'operation_id': 'delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'name',
                    'user',
                ],
                'required': [
                    'name',
                    'user',
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
                    'name':
                        (str,),
                    'user':
                        (str,),
                },
                'attribute_map': {
                    'name': 'name',
                    'user': 'user',
                },
                'location_map': {
                    'name': 'path',
                    'user': 'path',
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
        self.get_endpoint = _Endpoint(
            settings={
                'response_type': (GetApiKeyResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/users/{user}/apikeys/{name}',
                'operation_id': 'get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'user',
                    'name',
                    'reveal',
                ],
                'required': [
                    'user',
                    'name',
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
                    'user':
                        (str,),
                    'name':
                        (str,),
                    'reveal':
                        (bool,),
                },
                'attribute_map': {
                    'user': 'user',
                    'name': 'name',
                    'reveal': 'reveal',
                },
                'location_map': {
                    'user': 'path',
                    'name': 'path',
                    'reveal': 'query',
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
        self.list_endpoint = _Endpoint(
            settings={
                'response_type': (ListApiKeysResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/users/{user}/apikeys',
                'operation_id': 'list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'user',
                ],
                'required': [
                    'user',
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
                    'user':
                        (str,),
                },
                'attribute_map': {
                    'user': 'user',
                },
                'location_map': {
                    'user': 'path',
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
        self.update_endpoint = _Endpoint(
            settings={
                'response_type': (UpdateApiKeyResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/users/{user}/apikeys/{name}',
                'operation_id': 'update',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'name',
                    'user',
                    'update_api_key_request',
                ],
                'required': [
                    'name',
                    'user',
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
                    'name':
                        (str,),
                    'user':
                        (str,),
                    'update_api_key_request':
                        (UpdateApiKeyRequest,),
                },
                'attribute_map': {
                    'name': 'name',
                    'user': 'user',
                },
                'location_map': {
                    'name': 'path',
                    'user': 'path',
                    'update_api_key_request': 'body',
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

    def create(
        self,
        *,
        name: str,
        created_by: str = None,
        role: str = None,
        **kwargs
    ) -> typing.Union[CreateApiKeyResponse, asyncio.Future]:
        """Create API Key  # noqa: E501

        Create a new API key for the authenticated user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.APIKeys.create(
            created_by="string_example",
            name="my-app",
            role="string_example",
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            created_by (str): [optional]
            name (str): Name for this API key.. [required]
            role (str): [optional]
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
            CreateApiKeyResponse
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
        kwargs['create_api_key_request'] = \
            kwargs['create_api_key_request']
        return self.create_endpoint.call_with_http_info(**kwargs)

    def delete(
        self,
        *,
        name: str,
        user: str,
        **kwargs
    ) -> typing.Union[DeleteApiKeyResponse, asyncio.Future]:
        """Delete API Key  # noqa: E501

        Delete an API key for any user in your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.APIKeys.delete(
            name="my-key",
            user="admin@me.com",
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            name (str): Name of the API key.. [required]
            user (str): Email of the API key owner. Use `self` to specify the currently authenticated user.. [required]
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
            DeleteApiKeyResponse
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
        kwargs['name'] = \
            name
        kwargs['user'] = \
            user
        return self.delete_endpoint.call_with_http_info(**kwargs)

    def get(
        self,
        *,
        user: str,
        name: str,
        reveal: bool = None,
        **kwargs
    ) -> typing.Union[GetApiKeyResponse, asyncio.Future]:
        """Retrieve API Key  # noqa: E501

        Retrieve a particular API key for any user in your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.APIKeys.get(
            user="admin@me.com",
            name="my-key",
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            user (str): Email of the API key owner. Use `self` to specify the currently authenticated user.. [required]
            name (str): Name of the API key.. [required]
            reveal (bool): Reveal full key.. [optional]
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
            GetApiKeyResponse
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
        kwargs['user'] = \
            user
        kwargs['name'] = \
            name
        if reveal is not None:
            kwargs['reveal'] = \
                reveal
        return self.get_endpoint.call_with_http_info(**kwargs)

    def list(
        self,
        *,
        user: str,
        **kwargs
    ) -> typing.Union[ListApiKeysResponse, asyncio.Future]:
        """List API Keys  # noqa: E501

        List API key metadata for any user in your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.APIKeys.list(
            user="admin@me.com",
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            user (str): Email of the API key owner. Use `self` to specify the currently authenticated user.. [required]
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
            ListApiKeysResponse
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
        kwargs['user'] = \
            user
        return self.list_endpoint.call_with_http_info(**kwargs)

    def update(
        self,
        *,
        name: str,
        user: str,
        state: str = None,
        **kwargs
    ) -> typing.Union[UpdateApiKeyResponse, asyncio.Future]:
        """Update API Key State  # noqa: E501

        Update the state of an API key for any user in your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.APIKeys.update(
            name="my-key",
            user="admin@me.com",
            state="ACTIVE",
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            name (str): Name of the API key.. [required]
            user (str): Email of the API key owner. Use `self` to specify the currently authenticated user.. [required]
            state (str): State that the api key should be set to.. [optional]
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
            UpdateApiKeyResponse
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
        kwargs['name'] = \
            name
        kwargs['user'] = \
            user
        kwargs['update_api_key_request'] = \
            kwargs['update_api_key_request']
        return self.update_endpoint.call_with_http_info(**kwargs)


    body_params_dict = dict()
    return_types_dict = dict()
    body_params_dict['create'] = 'create_api_key_request'
    return_types_dict['create'] = CreateApiKeyRequest
    body_params_dict['update'] = 'update_api_key_request'
    return_types_dict['update'] = UpdateApiKeyRequest
