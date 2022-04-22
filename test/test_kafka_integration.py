"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import rockset
from rockset.model.kafka_v3_security_config import KafkaV3SecurityConfig
from rockset.model.schema_registry_config import SchemaRegistryConfig
from rockset.model.status_kafka import StatusKafka
globals()['KafkaV3SecurityConfig'] = KafkaV3SecurityConfig
globals()['SchemaRegistryConfig'] = SchemaRegistryConfig
globals()['StatusKafka'] = StatusKafka
from rockset.model.kafka_integration import KafkaIntegration


class TestKafkaIntegration(unittest.TestCase):
    """KafkaIntegration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testKafkaIntegration(self):
        """Test KafkaIntegration"""
        # FIXME: construct object with mandatory attributes with example values
        # model = KafkaIntegration()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
