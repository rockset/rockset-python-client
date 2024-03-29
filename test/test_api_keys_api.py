"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from unittest import mock

from rockset.models import *
from test.conftest import EarlyExit, validate_call


def test_create(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.APIKeys.create(
                created_by="string_example",
                expiry_time="2001-08-28T00:23:41Z",
                name="my-app",
                role="string_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_delete(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.APIKeys.delete(
                name="my-key",
                user="admin@me.com",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_get(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.APIKeys.get(
                user="admin@me.com",
                name="my-key",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_list(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.APIKeys.list(
                user="admin@me.com",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_update(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.APIKeys.update(
                name="my-key",
                user="admin@me.com",
                clear_expiry_time=True,
                expiry_time="2001-08-28T00:23:41Z",
                state="ACTIVE",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)
