"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import rockset
from rockset.api.virtual_instances_api import VirtualInstancesApi  # noqa: E501


class TestVirtualInstancesApi(unittest.TestCase):
    """VirtualInstancesApi unit test stubs"""

    def setUp(self):
        self.api = VirtualInstancesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_virtual_instance(self):
        """Test case for get_virtual_instance

        Retrieve Virtual Instance  # noqa: E501
        """
        pass

    def test_list_virtual_instances(self):
        """Test case for list_virtual_instances

        List Virtual Instances  # noqa: E501
        """
        pass

    def test_set_virtual_instance(self):
        """Test case for set_virtual_instance

        Update Virtual Instance  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()