# coding: utf-8

"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class GcsIntegration(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'gcp_service_account': 'GcpServiceAccount'
    }

    attribute_map = {
        'gcp_service_account': 'gcp_service_account'
    }

    def __init__(self, gcp_service_account=None, _configuration=None):  # noqa: E501
        """GcsIntegration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._gcp_service_account = None
        self.discriminator = None

        if gcp_service_account is not None:
            self.gcp_service_account = gcp_service_account

    @property
    def gcp_service_account(self):
        """Gets the gcp_service_account of this GcsIntegration.  # noqa: E501

        credentials for an AWS key integration  # noqa: E501

        :return: The gcp_service_account of this GcsIntegration.  # noqa: E501
        :rtype: GcpServiceAccount
        """
        return self._gcp_service_account

    @gcp_service_account.setter
    def gcp_service_account(self, gcp_service_account):
        """Sets the gcp_service_account of this GcsIntegration.

        credentials for an AWS key integration  # noqa: E501

        :param gcp_service_account: The gcp_service_account of this GcsIntegration.  # noqa: E501
        :type: GcpServiceAccount
        """

        self._gcp_service_account = gcp_service_account

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GcsIntegration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GcsIntegration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GcsIntegration):
            return True

        return self.to_dict() != other.to_dict()
