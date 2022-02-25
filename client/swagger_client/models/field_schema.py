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


class FieldSchema(object):
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
        'field_name': 'str',
        'field_options': 'FieldOptions'
    }

    attribute_map = {
        'field_name': 'field_name',
        'field_options': 'field_options'
    }

    def __init__(self, field_name=None, field_options=None, _configuration=None):  # noqa: E501
        """FieldSchema - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._field_name = None
        self._field_options = None
        self.discriminator = None

        if field_name is not None:
            self.field_name = field_name
        if field_options is not None:
            self.field_options = field_options

    @property
    def field_name(self):
        """Gets the field_name of this FieldSchema.  # noqa: E501

        The name of a field, parsed as a SQL qualified name  # noqa: E501

        :return: The field_name of this FieldSchema.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this FieldSchema.

        The name of a field, parsed as a SQL qualified name  # noqa: E501

        :param field_name: The field_name of this FieldSchema.  # noqa: E501
        :type: str
        """

        self._field_name = field_name

    @property
    def field_options(self):
        """Gets the field_options of this FieldSchema.  # noqa: E501

        The indexing options for a field  # noqa: E501

        :return: The field_options of this FieldSchema.  # noqa: E501
        :rtype: FieldOptions
        """
        return self._field_options

    @field_options.setter
    def field_options(self, field_options):
        """Sets the field_options of this FieldSchema.

        The indexing options for a field  # noqa: E501

        :param field_options: The field_options of this FieldSchema.  # noqa: E501
        :type: FieldOptions
        """

        self._field_options = field_options

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
        if issubclass(FieldSchema, dict):
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
        if not isinstance(other, FieldSchema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FieldSchema):
            return True

        return self.to_dict() != other.to_dict()
