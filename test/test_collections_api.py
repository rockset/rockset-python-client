"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import rockset
from rockset.api.collections_api import CollectionsApi  # noqa: E501


class TestCollectionsApi(unittest.TestCase):
    """CollectionsApi unit test stubs"""

    def setUp(self):
        self.api = CollectionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_azure_blob_collection(self):
        """Test case for create_azure_blob_collection

        Create azure blob collection  # noqa: E501
        """
        pass

    def test_create_gcs_collection(self):
        """Test case for create_gcs_collection

        Create gcs collection  # noqa: E501
        """
        pass

    def test_delete_collection(self):
        """Test case for delete_collection

        Delete Collection  # noqa: E501
        """
        pass

    def test_get_collection(self):
        """Test case for get_collection

        Retrieve Collection  # noqa: E501
        """
        pass

    def test_list_collections(self):
        """Test case for list_collections

        List Collections  # noqa: E501
        """
        pass

    def test_workspace_collections(self):
        """Test case for workspace_collections

        List Collections in Workspace  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()