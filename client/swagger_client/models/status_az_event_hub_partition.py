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


class StatusAzEventHubPartition(object):
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
        'partition_number': 'int',
        'partition_offset': 'int',
        'offset_lag': 'int'
    }

    attribute_map = {
        'partition_number': 'partition_number',
        'partition_offset': 'partition_offset',
        'offset_lag': 'offset_lag'
    }

    def __init__(self, partition_number=None, partition_offset=None, offset_lag=None, _configuration=None):  # noqa: E501
        """StatusAzEventHubPartition - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._partition_number = None
        self._partition_offset = None
        self._offset_lag = None
        self.discriminator = None

        if partition_number is not None:
            self.partition_number = partition_number
        if partition_offset is not None:
            self.partition_offset = partition_offset
        if offset_lag is not None:
            self.offset_lag = offset_lag

    @property
    def partition_number(self):
        """Gets the partition_number of this StatusAzEventHubPartition.  # noqa: E501

        The number of this partition  # noqa: E501

        :return: The partition_number of this StatusAzEventHubPartition.  # noqa: E501
        :rtype: int
        """
        return self._partition_number

    @partition_number.setter
    def partition_number(self, partition_number):
        """Sets the partition_number of this StatusAzEventHubPartition.

        The number of this partition  # noqa: E501

        :param partition_number: The partition_number of this StatusAzEventHubPartition.  # noqa: E501
        :type: int
        """

        self._partition_number = partition_number

    @property
    def partition_offset(self):
        """Gets the partition_offset of this StatusAzEventHubPartition.  # noqa: E501

        Latest offset of partition  # noqa: E501

        :return: The partition_offset of this StatusAzEventHubPartition.  # noqa: E501
        :rtype: int
        """
        return self._partition_offset

    @partition_offset.setter
    def partition_offset(self, partition_offset):
        """Sets the partition_offset of this StatusAzEventHubPartition.

        Latest offset of partition  # noqa: E501

        :param partition_offset: The partition_offset of this StatusAzEventHubPartition.  # noqa: E501
        :type: int
        """

        self._partition_offset = partition_offset

    @property
    def offset_lag(self):
        """Gets the offset_lag of this StatusAzEventHubPartition.  # noqa: E501

        Per partition lag for offset  # noqa: E501

        :return: The offset_lag of this StatusAzEventHubPartition.  # noqa: E501
        :rtype: int
        """
        return self._offset_lag

    @offset_lag.setter
    def offset_lag(self, offset_lag):
        """Sets the offset_lag of this StatusAzEventHubPartition.

        Per partition lag for offset  # noqa: E501

        :param offset_lag: The offset_lag of this StatusAzEventHubPartition.  # noqa: E501
        :type: int
        """

        self._offset_lag = offset_lag

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
        if issubclass(StatusAzEventHubPartition, dict):
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
        if not isinstance(other, StatusAzEventHubPartition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatusAzEventHubPartition):
            return True

        return self.to_dict() != other.to_dict()
