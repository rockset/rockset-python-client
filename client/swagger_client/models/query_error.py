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


class QueryError(object):
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
        'type': 'str',
        'message': 'str',
        'status_code': 'int'
    }

    attribute_map = {
        'type': 'type',
        'message': 'message',
        'status_code': 'status_code'
    }

    def __init__(self, type=None, message=None, status_code=None, _configuration=None):  # noqa: E501
        """QueryError - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._message = None
        self._status_code = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if message is not None:
            self.message = message
        if status_code is not None:
            self.status_code = status_code

    @property
    def type(self):
        """Gets the type of this QueryError.  # noqa: E501

        The type of error  # noqa: E501

        :return: The type of this QueryError.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QueryError.

        The type of error  # noqa: E501

        :param type: The type of this QueryError.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def message(self):
        """Gets the message of this QueryError.  # noqa: E501

        A message associated with the error, containing more information about it  # noqa: E501

        :return: The message of this QueryError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this QueryError.

        A message associated with the error, containing more information about it  # noqa: E501

        :param message: The message of this QueryError.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def status_code(self):
        """Gets the status_code of this QueryError.  # noqa: E501

        The HTTP status code associated with this error, had it been sent as the response status code  # noqa: E501

        :return: The status_code of this QueryError.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this QueryError.

        The HTTP status code associated with this error, had it been sent as the response status code  # noqa: E501

        :param status_code: The status_code of this QueryError.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

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
        if issubclass(QueryError, dict):
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
        if not isinstance(other, QueryError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryError):
            return True

        return self.to_dict() != other.to_dict()
