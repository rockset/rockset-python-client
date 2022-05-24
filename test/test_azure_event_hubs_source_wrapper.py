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
from rockset.model.source_azure_event_hubs import SourceAzureEventHubs
from rockset.model.status import Status

globals()["FormatParams"] = FormatParams
globals()["SourceAzureEventHubs"] = SourceAzureEventHubs
globals()["Status"] = Status
from rockset.model.azure_event_hubs_source_wrapper import AzureEventHubsSourceWrapper


class TestAzureEventHubsSourceWrapper(unittest.TestCase):
    """AzureEventHubsSourceWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAzureEventHubsSourceWrapper(self):
        """Test AzureEventHubsSourceWrapper"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AzureEventHubsSourceWrapper()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
