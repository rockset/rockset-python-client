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
from rockset.model.create_scheduled_lambda_request import CreateScheduledLambdaRequest
from rockset.model.error_model import ErrorModel
from rockset.model.scheduled_lambda_response import ScheduledLambdaResponse
from rockset.model.update_scheduled_lambda_request import UpdateScheduledLambdaRequest
from rockset.models import *


class ScheduledLambdas(object):
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
                'response_type': (ScheduledLambdaResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/ws/{workspace}/scheduled_lambdas',
                'operation_id': 'create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace',
                    'create_scheduled_lambda_request',
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
                    'create_scheduled_lambda_request':
                        (CreateScheduledLambdaRequest,),
                },
                'attribute_map': {
                    'workspace': 'workspace',
                },
                'location_map': {
                    'workspace': 'path',
                    'create_scheduled_lambda_request': 'body',
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
                'response_type': (ScheduledLambdaResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/ws/{workspace}/scheduled_lambdas/{scheduledLambdaId}',
                'operation_id': 'delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace',
                    'scheduled_lambda_id',
                ],
                'required': [
                    'workspace',
                    'scheduled_lambda_id',
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
                    'scheduled_lambda_id':
                        (str,),
                },
                'attribute_map': {
                    'workspace': 'workspace',
                    'scheduled_lambda_id': 'scheduledLambdaId',
                },
                'location_map': {
                    'workspace': 'path',
                    'scheduled_lambda_id': 'path',
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
                'response_type': (ScheduledLambdaResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/ws/{workspace}/scheduled_lambdas/{scheduledLambdaId}',
                'operation_id': 'update',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace',
                    'scheduled_lambda_id',
                    'update_scheduled_lambda_request',
                ],
                'required': [
                    'workspace',
                    'scheduled_lambda_id',
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
                    'scheduled_lambda_id':
                        (str,),
                    'update_scheduled_lambda_request':
                        (UpdateScheduledLambdaRequest,),
                },
                'attribute_map': {
                    'workspace': 'workspace',
                    'scheduled_lambda_id': 'scheduledLambdaId',
                },
                'location_map': {
                    'workspace': 'path',
                    'scheduled_lambda_id': 'path',
                    'update_scheduled_lambda_request': 'body',
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
        cron_string: str,
        ql_name: str,
        apikey: str = None,
        tag: str = None,
        total_times_to_execute: int = None,
        version: str = None,
        webhook_auth_header: str = None,
        webhook_payload: str = None,
        webhook_url: str = None,
        workspace = "commons",
        **kwargs
    ) -> typing.Union[ScheduledLambdaResponse, asyncio.Future]:
        """Create a Scheduled Lambda mapping  # noqa: E501

        Create a scheduled lambda mapping for your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.ScheduledLambdas.create(
            apikey="qoiwkjndksd",
            cron_string="* * * * *",
            ql_name="ql_name",
            tag="production",
            total_times_to_execute=1,
            version="abcdef1234",
            webhook_auth_header="bearer qiowjkjkdskdskldio",
            webhook_payload="string_example",
            webhook_url="https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX",
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            workspace (str): name of the workspace. [required] if omitted the server will use the default value of "commons"
            apikey (str): The apikey to use when triggering execution of the associated query lambda.. [optional]
            cron_string (str): The UNIX-formatted cron string for this scheduled query lambda.. [required]
            ql_name (str): The name of the QL to use for scheduled execution.. [required]
            tag (str): The QL tag to use for scheduled execution.. [optional]
            total_times_to_execute (int): The number of times to execute this scheduled query lambda. Once this scheduled query lambda has been executed this many times, it will no longer be executed.. [optional]
            version (str): The version of the QL to use for scheduled execution.. [optional]
            webhook_auth_header (str): The value to use as the authorization header when hitting the webhook.. [optional]
            webhook_payload (str): The payload that should be sent to the webhook. JSON format.. [optional]
            webhook_url (str): The URL of the webhook that should be triggered after this scheduled query lambda completes.. [optional]
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
            ScheduledLambdaResponse
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
        kwargs['create_scheduled_lambda_request'] = \
            kwargs['create_scheduled_lambda_request']
        return self.create_endpoint.call_with_http_info(**kwargs)

    def delete(
        self,
        *,
        scheduled_lambda_id: str,
        workspace = "commons",
        **kwargs
    ) -> typing.Union[ScheduledLambdaResponse, asyncio.Future]:
        """Delete a Scheduled Lambda mapping  # noqa: E501

        Delete a scheduled lambda mapping for your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.ScheduledLambdas.delete(
            scheduled_lambda_id="scheduledLambdaId_example",
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            workspace (str): name of the workspace. [required] if omitted the server will use the default value of "commons"
            scheduled_lambda_id (str): Scheduled Lambda RRN. [required]
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
            ScheduledLambdaResponse
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
        kwargs['scheduled_lambda_id'] = \
            scheduled_lambda_id
        return self.delete_endpoint.call_with_http_info(**kwargs)

    def update(
        self,
        *,
        scheduled_lambda_id: str,
        apikey: str = None,
        resume_permanent_error: bool = None,
        total_times_to_execute: int = None,
        webhook_auth_header: str = None,
        webhook_payload: str = None,
        webhook_url: str = None,
        workspace = "commons",
        **kwargs
    ) -> typing.Union[ScheduledLambdaResponse, asyncio.Future]:
        """Update a Scheduled Lambda mapping  # noqa: E501

        Update a scheduled lambda mapping for your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.ScheduledLambdas.update(
            scheduled_lambda_id="scheduledLambdaId_example",
            apikey="qoiwkjndksd",
            resume_permanent_error=True,
            total_times_to_execute=1,
            webhook_auth_header="bearer qiowjkjkdskdskldio",
            webhook_payload="string_example",
            webhook_url="https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX",
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            workspace (str): name of the workspace. [required] if omitted the server will use the default value of "commons"
            scheduled_lambda_id (str): Scheduled Lambda RRN. [required]
            apikey (str): The apikey to use when triggering execution of the associated query lambda.. [optional]
            resume_permanent_error (bool): Boolean flag to allow a scheduled query lambda to resume execution after being suspended due to execution failure. This flag will be unset after scheduled lambda execution.. [optional]
            total_times_to_execute (int): The number of times to execute this scheduled query lambda.. [optional]
            webhook_auth_header (str): The value to use as the authorization header when hitting the webhook.. [optional]
            webhook_payload (str): The payload that should be sent to the webhook. JSON format.. [optional]
            webhook_url (str): The URL of the webhook that should be triggered after this scheduled query lambda completes.. [optional]
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
            ScheduledLambdaResponse
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
        kwargs['scheduled_lambda_id'] = \
            scheduled_lambda_id
        kwargs['update_scheduled_lambda_request'] = \
            kwargs['update_scheduled_lambda_request']
        return self.update_endpoint.call_with_http_info(**kwargs)


    body_params_dict = dict()
    return_types_dict = dict()
    body_params_dict['create'] = 'create_scheduled_lambda_request'
    return_types_dict['create'] = CreateScheduledLambdaRequest
    body_params_dict['update'] = 'update_scheduled_lambda_request'
    return_types_dict['update'] = UpdateScheduledLambdaRequest
