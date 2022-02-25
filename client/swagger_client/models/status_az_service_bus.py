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


class StatusAzServiceBus(object):
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
        'first_processed_at': 'datetime',
        'records_processed': 'int',
        'last_processed_at': 'datetime'
    }

    attribute_map = {
        'first_processed_at': 'first_processed_at',
        'records_processed': 'records_processed',
        'last_processed_at': 'last_processed_at'
    }

    def __init__(self, first_processed_at=None, records_processed=None, last_processed_at=None, _configuration=None):  # noqa: E501
        """StatusAzServiceBus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._first_processed_at = None
        self._records_processed = None
        self._last_processed_at = None
        self.discriminator = None

        if first_processed_at is not None:
            self.first_processed_at = first_processed_at
        if records_processed is not None:
            self.records_processed = records_processed
        if last_processed_at is not None:
            self.last_processed_at = last_processed_at

    @property
    def first_processed_at(self):
        """Gets the first_processed_at of this StatusAzServiceBus.  # noqa: E501

        Service Bus first message processed time in ISO-8601 format  # noqa: E501

        :return: The first_processed_at of this StatusAzServiceBus.  # noqa: E501
        :rtype: datetime
        """
        return self._first_processed_at

    @first_processed_at.setter
    def first_processed_at(self, first_processed_at):
        """Sets the first_processed_at of this StatusAzServiceBus.

        Service Bus first message processed time in ISO-8601 format  # noqa: E501

        :param first_processed_at: The first_processed_at of this StatusAzServiceBus.  # noqa: E501
        :type: datetime
        """

        self._first_processed_at = first_processed_at

    @property
    def records_processed(self):
        """Gets the records_processed of this StatusAzServiceBus.  # noqa: E501

        Number of records processed  # noqa: E501

        :return: The records_processed of this StatusAzServiceBus.  # noqa: E501
        :rtype: int
        """
        return self._records_processed

    @records_processed.setter
    def records_processed(self, records_processed):
        """Sets the records_processed of this StatusAzServiceBus.

        Number of records processed  # noqa: E501

        :param records_processed: The records_processed of this StatusAzServiceBus.  # noqa: E501
        :type: int
        """

        self._records_processed = records_processed

    @property
    def last_processed_at(self):
        """Gets the last_processed_at of this StatusAzServiceBus.  # noqa: E501

        ISO-8601 date when the last message was processed  # noqa: E501

        :return: The last_processed_at of this StatusAzServiceBus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_processed_at

    @last_processed_at.setter
    def last_processed_at(self, last_processed_at):
        """Sets the last_processed_at of this StatusAzServiceBus.

        ISO-8601 date when the last message was processed  # noqa: E501

        :param last_processed_at: The last_processed_at of this StatusAzServiceBus.  # noqa: E501
        :type: datetime
        """

        self._last_processed_at = last_processed_at

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
        if issubclass(StatusAzServiceBus, dict):
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
        if not isinstance(other, StatusAzServiceBus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatusAzServiceBus):
            return True

        return self.to_dict() != other.to_dict()
