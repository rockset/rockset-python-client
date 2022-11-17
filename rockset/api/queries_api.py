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
from rockset.model.cancel_query_response import CancelQueryResponse
from rockset.model.error_model import ErrorModel
from rockset.model.get_query_response import GetQueryResponse
from rockset.model.list_queries_response import ListQueriesResponse
from rockset.model.query_pagination_response import QueryPaginationResponse
from rockset.model.query_request import QueryRequest
from rockset.model.query_response import QueryResponse
from rockset.model.validate_query_response import ValidateQueryResponse
from rockset.models import *


class Queries(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.cancel_query_endpoint = _Endpoint(
            settings={
                'response_type': (CancelQueryResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/queries/{queryId}',
                'operation_id': 'cancel_query',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'query_id',
                ],
                'required': [
                    'query_id',
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
                    'query_id':
                        (str,),
                },
                'attribute_map': {
                    'query_id': 'queryId',
                },
                'location_map': {
                    'query_id': 'path',
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
        self.get_query_endpoint = _Endpoint(
            settings={
                'response_type': (GetQueryResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/queries/{queryId}',
                'operation_id': 'get_query',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'query_id',
                ],
                'required': [
                    'query_id',
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
                    'query_id':
                        (str,),
                },
                'attribute_map': {
                    'query_id': 'queryId',
                },
                'location_map': {
                    'query_id': 'path',
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
        self.get_query_results_endpoint = _Endpoint(
            settings={
                'response_type': (QueryPaginationResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/queries/{queryId}/pages',
                'operation_id': 'get_query_results',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'query_id',
                    'cursor',
                    'docs',
                ],
                'required': [
                    'query_id',
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
                    'query_id':
                        (str,),
                    'cursor':
                        (str,),
                    'docs':
                        (int,),
                },
                'attribute_map': {
                    'query_id': 'queryId',
                    'cursor': 'cursor',
                    'docs': 'docs',
                },
                'location_map': {
                    'query_id': 'path',
                    'cursor': 'query',
                    'docs': 'query',
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
        self.list_active_queries_endpoint = _Endpoint(
            settings={
                'response_type': (ListQueriesResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/queries',
                'operation_id': 'list_active_queries',
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
        self.query_endpoint = _Endpoint(
            settings={
                'response_type': (QueryResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/queries',
                'operation_id': 'query',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'query_request',
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
                    'query_request':
                        (QueryRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'query_request': 'body',
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
        self.validate_endpoint = _Endpoint(
            settings={
                'response_type': (ValidateQueryResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/queries/validations',
                'operation_id': 'validate',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'query_request',
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
                    'query_request':
                        (QueryRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'query_request': 'body',
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

    def cancel_query(
        self,
        *,
        query_id: str,
        **kwargs
    ) -> typing.Union[CancelQueryResponse, asyncio.Future]:
        """Cancel Query  # noqa: E501

        Attempts to cancel an actively-running query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.Queries.cancel_query(
            query_id="queryId_example",
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            query_id (str): [required]
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
            CancelQueryResponse
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
        kwargs['query_id'] = \
            query_id
        return self.cancel_query_endpoint.call_with_http_info(**kwargs)

    def get_query(
        self,
        *,
        query_id: str,
        **kwargs
    ) -> typing.Union[GetQueryResponse, asyncio.Future]:
        """Retrieve Query  # noqa: E501

        Returns information about a query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.Queries.get_query(
            query_id="queryId_example",
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            query_id (str): [required]
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
            GetQueryResponse
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
        kwargs['query_id'] = \
            query_id
        return self.get_query_endpoint.call_with_http_info(**kwargs)

    def get_query_results(
        self,
        *,
        query_id: str,
        cursor: str = None,
        docs: int = None,
        **kwargs
    ) -> typing.Union[QueryPaginationResponse, asyncio.Future]:
        """Retrieve Query Results Page  # noqa: E501

        Returns a page of query results.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.Queries.get_query_results(
            query_id="queryId_example",
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            query_id (str): [required]
            cursor (str): Cursor to current page. If unset, will default to the first page.. [optional]
            docs (int): Number of documents to fetch.. [optional]
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
            QueryPaginationResponse
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
        kwargs['query_id'] = \
            query_id
        if cursor is not None:
            kwargs['cursor'] = \
                cursor
        if docs is not None:
            kwargs['docs'] = \
                docs
        return self.get_query_results_endpoint.call_with_http_info(**kwargs)

    def list_active_queries(
        self,
        **kwargs
    ) -> typing.Union[ListQueriesResponse, asyncio.Future]:
        """List Queries  # noqa: E501

        Lists actively queued and running queries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.Queries.list_active_queries(
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
            ListQueriesResponse
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
        return self.list_active_queries_endpoint.call_with_http_info(**kwargs)

    def query(
        self,
        *,
        sql: QueryRequestSql,
        async_options: AsyncQueryOptions = None,
        **kwargs
    ) -> typing.Union[QueryResponse, asyncio.Future]:
        """Execute SQL Query  # noqa: E501

        Make a SQL query to Rockset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.Queries.query(
            async_options=AsyncQueryOptions(
                client_timeout_ms=1,
                max_initial_results=1,
                timeout_ms=1,
            ),
            sql=QueryRequestSql(
                default_row_limit=1,
                generate_warnings=True,
                initial_paginate_response_doc_count=1,
                paginate=True,
                parameters=[
                    QueryParameter(
                        name="_id",
                        type="string",
                        value="85beb391",
                    ),
                ],
                query="SELECT * FROM foo where _id = :_id",
            ),
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            async_options (AsyncQueryOptions): [optional]
            sql (QueryRequestSql): [required]
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
            QueryResponse
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
        kwargs['query_request'] = \
            kwargs['query_request']
        return self.query_endpoint.call_with_http_info(**kwargs)

    def validate(
        self,
        *,
        sql: QueryRequestSql,
        async_options: AsyncQueryOptions = None,
        **kwargs
    ) -> typing.Union[ValidateQueryResponse, asyncio.Future]:
        """Validate Query  # noqa: E501

        Validate a SQL query with Rockset's parser and planner.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        ```python
        rs = RocksetClient(api_key=APIKEY)
        future = rs.Queries.validate(
            async_options=AsyncQueryOptions(
                client_timeout_ms=1,
                max_initial_results=1,
                timeout_ms=1,
            ),
            sql=QueryRequestSql(
                default_row_limit=1,
                generate_warnings=True,
                initial_paginate_response_doc_count=1,
                paginate=True,
                parameters=[
                    QueryParameter(
                        name="_id",
                        type="string",
                        value="85beb391",
                    ),
                ],
                query="SELECT * FROM foo where _id = :_id",
            ),
            async_req=True,
        )
        result = await future
        ```

        Keyword Args:
            async_options (AsyncQueryOptions): [optional]
            sql (QueryRequestSql): [required]
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
            ValidateQueryResponse
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
        kwargs['query_request'] = \
            kwargs['query_request']
        return self.validate_endpoint.call_with_http_info(**kwargs)


    body_params_dict = dict()
    return_types_dict = dict()
    body_params_dict['query'] = 'query_request'
    return_types_dict['query'] = QueryRequest
    body_params_dict['validate'] = 'query_request'
    return_types_dict['validate'] = QueryRequest
