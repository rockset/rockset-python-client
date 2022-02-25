# coding: utf-8

"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.create_integration_request import CreateIntegrationRequest  # noqa: E501
from swagger_client.rest import ApiException


class TestCreateIntegrationRequest(unittest.TestCase):
    """CreateIntegrationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateIntegrationRequest(self):
        """Test CreateIntegrationRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.create_integration_request.CreateIntegrationRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
