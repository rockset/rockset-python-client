"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import rockset
from rockset.model.field_mask import FieldMask

globals()["FieldMask"] = FieldMask
from rockset.model.source_s3 import SourceS3


class TestSourceS3(unittest.TestCase):
    """SourceS3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSourceS3(self):
        """Test SourceS3"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SourceS3()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()