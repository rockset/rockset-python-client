"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from unittest import mock

from rockset.models import *
from test.conftest import EarlyExit, validate_call


def test_create_query_lambda(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.QueryLambdas.create_query_lambda(
                description="production version foo",
                is_public=True,
                name="myQueryLambda",
                sql=QueryLambdaSql(
                    default_parameters=[
                        QueryParameter(
                            name="_id",
                            type="string",
                            value="85beb391",
                        ),
                    ],
                    query="SELECT 'Foo'",
                ),
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_query_lambda_tag(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.QueryLambdas.create_query_lambda_tag(
                query_lambda="queryLambda_example",
                tag_name="production",
                version="123ABC",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_delete_query_lambda(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.QueryLambdas.delete_query_lambda(
                query_lambda="queryLambda_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_delete_query_lambda_tag(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.QueryLambdas.delete_query_lambda_tag(
                query_lambda="queryLambda_example",
                tag="tag_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_delete_query_lambda_version(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.QueryLambdas.delete_query_lambda_version(
                query_lambda="queryLambda_example",
                version="version_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_execute_query_lambda(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.QueryLambdas.execute_query_lambda(
                query_lambda="queryLambda_example",
                version="version_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_execute_query_lambda_by_tag(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.QueryLambdas.execute_query_lambda_by_tag(
                query_lambda="queryLambda_example",
                tag="tag_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_get_query_lambda_tag_version(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.QueryLambdas.get_query_lambda_tag_version(
                query_lambda="queryLambda_example",
                tag="tag_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_get_query_lambda_version(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.QueryLambdas.get_query_lambda_version(
                query_lambda="queryLambda_example",
                version="version_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_list_all_query_lambdas(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.QueryLambdas.list_all_query_lambdas()
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_list_query_lambda_tags(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.QueryLambdas.list_query_lambda_tags(
                query_lambda="queryLambda_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_list_query_lambda_versions(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.QueryLambdas.list_query_lambda_versions(
                query_lambda="queryLambda_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_list_query_lambdas_in_workspace(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.QueryLambdas.list_query_lambdas_in_workspace()
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_update_query_lambda(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.QueryLambdas.update_query_lambda(
                query_lambda="queryLambda_example",
                description="production version foo",
                is_public=True,
                sql=QueryLambdaSql(
                    default_parameters=[
                        QueryParameter(
                            name="_id",
                            type="string",
                            value="85beb391",
                        ),
                    ],
                    query="SELECT 'Foo'",
                ),
            )
        except EarlyExit as e:
            validate_call(e, request_validator)
