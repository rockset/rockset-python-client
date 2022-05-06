# flake8: noqa

"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


__version__ = "1.0.0"

# import ApiClient
from rockset.api_client import ApiClient

# import Configuration
from rockset.configuration import Configuration

# import exceptions
from rockset.exceptions import RocksetException
from rockset.exceptions import ApiAttributeError
from rockset.exceptions import ApiTypeError
from rockset.exceptions import ApiValueError
from rockset.exceptions import ApiKeyError
from rockset.exceptions import ApiException

from rockset.rockset_client import DevRegions, Regions, RocksetClient
from rockset.document import Document
from rockset.query_builder import Q, F, P, ParamDict
