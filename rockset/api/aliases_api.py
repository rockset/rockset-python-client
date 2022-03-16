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
from rockset.model.create_alias_request import CreateAliasRequest
from rockset.model.create_alias_response import CreateAliasResponse
from rockset.model.delete_alias_response import DeleteAliasResponse
from rockset.model.error_model import ErrorModel
from rockset.model.get_alias_response import GetAliasResponse
from rockset.model.list_aliases_response import ListAliasesResponse
from rockset.model.update_alias_request import UpdateAliasRequest
from rockset.models import *


class AliasesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_alias_endpoint = _Endpoint(
            settings={
                'response_type': (CreateAliasResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/ws/{workspace}/aliases'.split('#')[0],
                'operation_id': 'create_alias',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace',
                    'create_alias_request',
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
                    'create_alias_request':
                        (CreateAliasRequest,),
                },
                'attribute_map': {
                    'workspace': 'workspace',
                },
                'location_map': {
                    'workspace': 'path',
                    'create_alias_request': 'body',
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
        self.delete_alias_endpoint = _Endpoint(
            settings={
                'response_type': (DeleteAliasResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/ws/{workspace}/aliases/{alias}'.split('#')[0],
                'operation_id': 'delete_alias',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace',
                    'alias',
                ],
                'required': [
                    'workspace',
                    'alias',
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
                    'alias':
                        (str,),
                },
                'attribute_map': {
                    'workspace': 'workspace',
                    'alias': 'alias',
                },
                'location_map': {
                    'workspace': 'path',
                    'alias': 'path',
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
        self.get_alias_endpoint = _Endpoint(
            settings={
                'response_type': (GetAliasResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/ws/{workspace}/aliases/{alias}'.split('#')[0],
                'operation_id': 'get_alias',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace',
                    'alias',
                ],
                'required': [
                    'workspace',
                    'alias',
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
                    'alias':
                        (str,),
                },
                'attribute_map': {
                    'workspace': 'workspace',
                    'alias': 'alias',
                },
                'location_map': {
                    'workspace': 'path',
                    'alias': 'path',
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
        self.list_aliases_endpoint = _Endpoint(
            settings={
                'response_type': (ListAliasesResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/aliases'.split('#')[0],
                'operation_id': 'list_aliases',
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
        self.update_alias_endpoint = _Endpoint(
            settings={
                'response_type': (GetAliasResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/ws/{workspace}/aliases/{alias}'.split('#')[0],
                'operation_id': 'update_alias',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace',
                    'alias',
                    'update_alias_request',
                ],
                'required': [
                    'workspace',
                    'alias',
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
                    'alias':
                        (str,),
                    'update_alias_request':
                        (UpdateAliasRequest,),
                },
                'attribute_map': {
                    'workspace': 'workspace',
                    'alias': 'alias',
                },
                'location_map': {
                    'workspace': 'path',
                    'alias': 'path',
                    'update_alias_request': 'body',
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
        self.workspace_aliases_endpoint = _Endpoint(
            settings={
                'response_type': (ListAliasesResponse,),
                'auth': [
                    'apikey'
                ],
                'endpoint_path': '/v1/orgs/self/ws/{workspace}/aliases'.split('#')[0],
                'operation_id': 'workspace_aliases',
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

    def create_alias(
        self,
        *,
        collections: typing.Sequence[str],
        name: str,
        description: str = None,
        workspace = "commons",
        **kwargs
    ) -> typing.Union[CreateAliasResponse, asyncio.Future]:
        """Create Alias  # noqa: E501

        Create new alias in a workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

```python
rs = RocksetClient(apikey=APIKEY)
future = rs.AliasesApi.create_alias(
    collections=["commons.foo","prod.demo"],
    description="version alias",
    name="aliasName",
    async_req=True,
)
result = await future
```

        Keyword Args:
            workspace (str): name of the workspace. [required] if omitted the server will use the default value of "commons"
            collections ([str]): list of fully qualified collection names referenced by alias. [required]
            description (str): optional description. [optional]
            name (str): Alias name. [required]
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
            CreateAliasResponse
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
        kwargs['create_alias_request'] = \
            kwargs['create_alias_request']
        return self.create_alias_endpoint.call_with_http_info(**kwargs)

    def delete_alias(
        self,
        *,
        alias: str,
        workspace = "commons",
        **kwargs
    ) -> typing.Union[DeleteAliasResponse, asyncio.Future]:
        """Delete Alias  # noqa: E501

        Delete an alias.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

```python
rs = RocksetClient(apikey=APIKEY)
future = rs.AliasesApi.delete_alias(
    alias="alias_example",
    async_req=True,
)
result = await future
```

        Keyword Args:
            workspace (str): name of the workspace. [required] if omitted the server will use the default value of "commons"
            alias (str): name of the alias. [required]
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
            DeleteAliasResponse
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
        kwargs['alias'] = \
            alias
        return self.delete_alias_endpoint.call_with_http_info(**kwargs)

    def get_alias(
        self,
        *,
        alias: str,
        workspace = "commons",
        **kwargs
    ) -> typing.Union[GetAliasResponse, asyncio.Future]:
        """Retrieve Alias  # noqa: E501

        Get details about an alias  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

```python
rs = RocksetClient(apikey=APIKEY)
future = rs.AliasesApi.get_alias(
    alias="alias_example",
    async_req=True,
)
result = await future
```

        Keyword Args:
            workspace (str): name of the workspace. [required] if omitted the server will use the default value of "commons"
            alias (str): name of the alias. [required]
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
            GetAliasResponse
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
        kwargs['alias'] = \
            alias
        return self.get_alias_endpoint.call_with_http_info(**kwargs)

    def list_aliases(
        self,
        **kwargs
    ) -> typing.Union[ListAliasesResponse, asyncio.Future]:
        """List Aliases  # noqa: E501

        Retrieve all aliases in an organization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

```python
rs = RocksetClient(apikey=APIKEY)
future = rs.AliasesApi.list_aliases(
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
            ListAliasesResponse
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
            '_check_return_type', False
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_aliases_endpoint.call_with_http_info(**kwargs)

    def update_alias(
        self,
        *,
        alias: str,
        collections: typing.Sequence[str],
        description: str = None,
        workspace = "commons",
        **kwargs
    ) -> typing.Union[GetAliasResponse, asyncio.Future]:
        """Update Alias  # noqa: E501

        Update alias in a workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

```python
rs = RocksetClient(apikey=APIKEY)
future = rs.AliasesApi.update_alias(
    alias="alias_example",
    collections=["commons.foo","prod.demo"],
    description="version alias",
    async_req=True,
)
result = await future
```

        Keyword Args:
            workspace (str): name of the workspace. [required] if omitted the server will use the default value of "commons"
            alias (str): name of the alias. [required]
            collections ([str]): list of fully qualified collection names referenced by alias. [required]
            description (str): optional description. [optional]
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
            GetAliasResponse
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
        kwargs['alias'] = \
            alias
        kwargs['update_alias_request'] = \
            kwargs['update_alias_request']
        return self.update_alias_endpoint.call_with_http_info(**kwargs)

    def workspace_aliases(
        self,
        *,
        workspace = "commons",
        **kwargs
    ) -> typing.Union[ListAliasesResponse, asyncio.Future]:
        """List Aliases in Workspace  # noqa: E501

        Retrieve all aliases in a workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

```python
rs = RocksetClient(apikey=APIKEY)
future = rs.AliasesApi.workspace_aliases(
    async_req=True,
)
result = await future
```

        Keyword Args:
            workspace (str): name of the workspace. [required] if omitted the server will use the default value of "commons"
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
            ListAliasesResponse
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
        return self.workspace_aliases_endpoint.call_with_http_info(**kwargs)


    body_params_dict = dict()
    return_types_dict = dict()
    body_params_dict['create_alias'] = 'create_alias_request'
    return_types_dict['create_alias'] = CreateAliasRequest
    body_params_dict['update_alias'] = 'update_alias_request'
    return_types_dict['update_alias'] = UpdateAliasRequest
