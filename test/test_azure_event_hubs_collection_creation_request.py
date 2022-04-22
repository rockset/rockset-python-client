"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import rockset
from rockset.model.azure_event_hubs_source_wrapper import AzureEventHubsSourceWrapper
from rockset.model.event_time_info import EventTimeInfo
from rockset.model.field_mapping_query import FieldMappingQuery
from rockset.model.field_mapping_v2 import FieldMappingV2
from rockset.model.field_partition import FieldPartition
globals()['AzureEventHubsSourceWrapper'] = AzureEventHubsSourceWrapper
globals()['EventTimeInfo'] = EventTimeInfo
globals()['FieldMappingQuery'] = FieldMappingQuery
globals()['FieldMappingV2'] = FieldMappingV2
globals()['FieldPartition'] = FieldPartition
from rockset.model.azure_event_hubs_collection_creation_request import AzureEventHubsCollectionCreationRequest


class TestAzureEventHubsCollectionCreationRequest(unittest.TestCase):
    """AzureEventHubsCollectionCreationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAzureEventHubsCollectionCreationRequest(self):
        """Test AzureEventHubsCollectionCreationRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AzureEventHubsCollectionCreationRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
