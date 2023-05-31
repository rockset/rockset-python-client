"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
from rockset_v2.models import *


def test_patch_documents_request_init():
    PatchDocumentsRequest(
        data=[
            PatchDocument(
                id="ca2d6832-1bfd-f88f-0620-d2aa27a5d86c",
                patch=[
                    PatchOperation(
                        _from="_from_example",
                        op="ADD",
                        path="/foo/bar",
                        value={},
                    ),
                ],
            ),
        ],
    )
