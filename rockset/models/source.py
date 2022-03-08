# coding: utf-8

"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from rockset.configuration import Configuration


class Source(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "format_params": "FormatParams",
        "integration_name": "str",
        "status": "Status",
    }

    attribute_map = {
        "format_params": "format_params",
        "integration_name": "integration_name",
        "status": "status",
    }

    def __init__(
        self,
        format_params=None,
        integration_name=None,
        status=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Source - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._format_params = None
        self._integration_name = None
        self._status = None
        self.discriminator = None

        if format_params is not None:
            self.format_params = format_params
        self.integration_name = integration_name
        if status is not None:
            self.status = status

    @property
    def format_params(self):
        """Gets the format_params of this Source.  # noqa: E501


        :return: The format_params of this Source.  # noqa: E501
        :rtype: FormatParams
        """
        return self._format_params

    @format_params.setter
    def format_params(self, format_params):
        """Sets the format_params of this Source.


        :param format_params: The format_params of this Source.  # noqa: E501
        :type format_params: FormatParams
        """

        self._format_params = format_params

    @property
    def integration_name(self):
        """Gets the integration_name of this Source.  # noqa: E501

        name of integration to use  # noqa: E501

        :return: The integration_name of this Source.  # noqa: E501
        :rtype: str
        """
        return self._integration_name

    @integration_name.setter
    def integration_name(self, integration_name):
        """Sets the integration_name of this Source.

        name of integration to use  # noqa: E501

        :param integration_name: The integration_name of this Source.  # noqa: E501
        :type integration_name: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and integration_name is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `integration_name`, must not be `None`"
            )  # noqa: E501

        self._integration_name = integration_name

    @property
    def status(self):
        """Gets the status of this Source.  # noqa: E501


        :return: The status of this Source.  # noqa: E501
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Source.


        :param status: The status of this Source.  # noqa: E501
        :type status: Status
        """

        self._status = status

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(lambda item: (item[0], convert(item[1])), value.items())
                )
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Source):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Source):
            return True

        return self.to_dict() != other.to_dict()
