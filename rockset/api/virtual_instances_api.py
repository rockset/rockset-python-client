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
from rockset.model.error_model import ErrorModel
from rockset.model.get_virtual_instance_response import GetVirtualInstanceResponse
from rockset.model.list_virtual_instances_response import ListVirtualInstancesResponse
from rockset.model.update_virtual_instance_request import UpdateVirtualInstanceRequest
from rockset.model.update_virtual_instance_response import UpdateVirtualInstanceResponse
from rockset.models import *


class VirtualInstances(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_endpoint = _Endpoint(
            settings={
                'response_type': (GetVirtualInstanceResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/virtualinstances/{virtualInstanceId}',
                'operation_id': 'get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'virtual_instance_id',
                ],
                'required': [
                    'virtual_instance_id',
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
                    'virtual_instance_id':
                        (str,),
                },
                'attribute_map': {
                    'virtual_instance_id': 'virtualInstanceId',
                },
                'location_map': {
                    'virtual_instance_id': 'path',
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
                'response_type': (ListVirtualInstancesResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/virtualinstances',
                'operation_id': 'list',
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
        self.set_virtual_instance_endpoint = _Endpoint(
            settings={
                'response_type': (UpdateVirtualInstanceResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/virtualinstances/{virtualInstanceId}',
                'operation_id': 'set_virtual_instance',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'virtual_instance_id',
                    'update_virtual_instance_request',
                ],
                'required': [
                    'virtual_instance_id',
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
                    'virtual_instance_id':
                        (str,),
                    'update_virtual_instance_request':
                        (UpdateVirtualInstanceRequest,),
                },
                'attribute_map': {
                    'virtual_instance_id': 'virtualInstanceId',
                },
                'location_map': {
                    'virtual_instance_id': 'path',
                    'update_virtual_instance_request': 'body',
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

    def get(
        self,
        *,
        virtual_instance_id: str,
        **kwargs
    ) -> typing.Union[GetVirtualInstanceResponse, asyncio.Future]:
        """Retrieve Virtual Instance  # noqa: E501

        Get details about a virtual instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.VirtualInstances.get(
            virtual_instance_id="virtualInstanceId_example",
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            virtual_instance_id (str): uuid of the virtual instance. [required]
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
            GetVirtualInstanceResponse
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
        kwargs['virtual_instance_id'] = \
            virtual_instance_id
        return self.get_endpoint.call_with_http_info(**kwargs)

    def list(
        self,
        **kwargs
    ) -> typing.Union[ListVirtualInstancesResponse, asyncio.Future]:
        """List Virtual Instances  # noqa: E501

        Retrieve all virtual instances in an organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.VirtualInstances.list(
            async_req=True,
        )
        result = await future
        ```

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
            ListVirtualInstancesResponse
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
        return self.list_endpoint.call_with_http_info(**kwargs)

    def set_virtual_instance(
        self,
        *,
        virtual_instance_id: str,
        monitoring_enabled: bool = None,
        new_size: str = None,
        new_type: str = None,
        **kwargs
    ) -> typing.Union[UpdateVirtualInstanceResponse, asyncio.Future]:
        """Update Virtual Instance  # noqa: E501

        Update the properties of a virtual instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.VirtualInstances.set_virtual_instance(
            virtual_instance_id="virtualInstanceId_example",
            monitoring_enabled=True,
            new_size="LARGE",
            new_type="FREE",
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            virtual_instance_id (str): uuid of the virtual instance. [required]
            monitoring_enabled (bool): [optional]
            new_size (str): requested virtual instance size. [optional]
            new_type (str): [optional]
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
            UpdateVirtualInstanceResponse
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
        kwargs['virtual_instance_id'] = \
            virtual_instance_id
        kwargs['update_virtual_instance_request'] = \
            kwargs['update_virtual_instance_request']
        return self.set_virtual_instance_endpoint.call_with_http_info(**kwargs)


    body_params_dict = dict()
    return_types_dict = dict()
    body_params_dict['set_virtual_instance'] = 'update_virtual_instance_request'
    return_types_dict['set_virtual_instance'] = UpdateVirtualInstanceRequest
