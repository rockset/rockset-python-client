"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from unittest import mock

from rockset.models import *
from test.conftest import EarlyExit, validate_call


def test_create_user(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Users.create_user(
                email="hello@rockset.com",
                roles=["admin", "member", "read-only"],
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_delete_user(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Users.delete_user(
                user="user_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_get_current_user(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Users.get_current_user()
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_get_user(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Users.get_user(
                user="user_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_list_unsubscribe_preferences(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Users.list_unsubscribe_preferences()
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_list_users(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Users.list_users()
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_update_unsubscribe_preferences(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Users.update_unsubscribe_preferences(
                data=[
                    UnsubscribePreference(
                        notification_type="create_apikey",
                    ),
                ],
            )
        except EarlyExit as e:
            validate_call(e, request_validator)
