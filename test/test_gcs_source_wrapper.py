"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import rockset
from rockset.model.format_params import FormatParams
from rockset.model.source_gcs import SourceGcs
from rockset.model.status import Status
globals()['FormatParams'] = FormatParams
globals()['SourceGcs'] = SourceGcs
globals()['Status'] = Status
from rockset.model.gcs_source_wrapper import GcsSourceWrapper


class TestGcsSourceWrapper(unittest.TestCase):
    """GcsSourceWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGcsSourceWrapper(self):
        """Test GcsSourceWrapper"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GcsSourceWrapper()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
