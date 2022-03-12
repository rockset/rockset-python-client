"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import rockset
from rockset.api.integrations_api import IntegrationsApi  # noqa: E501


class TestIntegrationsApi(unittest.TestCase):
    """IntegrationsApi unit test stubs"""

    def setUp(self):
        self.api = IntegrationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_integration(self):
        """Test case for create_integration

        Create Integration  # noqa: E501
        """
        pass

    def test_delete_integration(self):
        """Test case for delete_integration

        Delete Integration  # noqa: E501
        """
        pass

    def test_get_integration(self):
        """Test case for get_integration

        Retrieve Integration  # noqa: E501
        """
        pass

    def test_list_integrations(self):
        """Test case for list_integrations

        List Integrations  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()