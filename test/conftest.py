import json
import logging
import yaml
from contextlib import contextmanager
from typing import Dict, Sequence
from unittest import mock

import pytest
from openapi_core import create_spec
from openapi_core.validation.request.datatypes import OpenAPIRequest, RequestParameters
from openapi_core.validation.request.validators import RequestValidator

from rockset import RocksetClient, Regions
from rockset.rest import RESTClientObject


REGION = Regions.use1a1


@pytest.fixture(scope="package")
def get_client():
    return RocksetClient(host=REGION, api_key="MOCK_KEY")


@pytest.fixture(scope="package")
def request_validator():
    with open("swagger/openapi-generated.yaml", "r") as spec_file:
        spec_dict = yaml.safe_load(spec_file)

    # The default for additionalProperties in OpenAPI 3 is True
    # additionalProperties should not be allowed under normal circumstances
    for obj in spec_dict["components"]["schemas"].values():
        if "additionalProperties" not in obj:
            obj["additionalProperties"] = False

    spec = create_spec(spec_dict)
    return RequestValidator(spec)


def early_exit_before_request(*args, **kwargs):
    raise EarlyExit(args=args, kwargs=kwargs)


@pytest.fixture
@contextmanager
def mock_request():
    with mock.patch.object(RESTClientObject, "request", early_exit_before_request):
        yield


class EarlyExit(Exception):
    args: Sequence
    kwargs: Dict

    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def validate_call(e: EarlyExit, validator: RequestValidator):
    method, url = e.args[1].lower(), e.args[2]

    mimetype = (
        e.kwargs["headers"]["Content-Type"]
        if "Content_Type" in e.kwargs["headers"]
        else e.kwargs["headers"]["Accept"]
    )

    request = OpenAPIRequest(
        mimetype=mimetype,
        full_url_pattern=url,
        method=method,
        parameters=RequestParameters(query=e.kwargs["query_params"]),
        body=json.dumps(e.kwargs["body"]) if "body" in e.kwargs else "",
    )

    result = validator.validate(request)
    result.raise_for_errors()
