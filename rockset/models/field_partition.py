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


class FieldPartition(object):
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
        'field_name': 'str',
        'keys': 'list[str]',
        'type': 'str'
    }

    attribute_map = {
        'field_name': 'field_name',
        'keys': 'keys',
        'type': 'type'
    }

    def __init__(self, field_name=None, keys=None, type=None, local_vars_configuration=None):  # noqa: E501
        """FieldPartition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._field_name = None
        self._keys = None
        self._type = None
        self.discriminator = None

        if field_name is not None:
            self.field_name = field_name
        if keys is not None:
            self.keys = keys
        if type is not None:
            self.type = type

    @property
    def field_name(self):
        """Gets the field_name of this FieldPartition.  # noqa: E501

        The name of a field, parsed as a SQL qualified name  # noqa: E501

        :return: The field_name of this FieldPartition.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this FieldPartition.

        The name of a field, parsed as a SQL qualified name  # noqa: E501

        :param field_name: The field_name of this FieldPartition.  # noqa: E501
        :type field_name: str
        """

        self._field_name = field_name

    @property
    def keys(self):
        """Gets the keys of this FieldPartition.  # noqa: E501

        The values for partitioning of a field  # noqa: E501

        :return: The keys of this FieldPartition.  # noqa: E501
        :rtype: list[str]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this FieldPartition.

        The values for partitioning of a field  # noqa: E501

        :param keys: The keys of this FieldPartition.  # noqa: E501
        :type keys: list[str]
        """

        self._keys = keys

    @property
    def type(self):
        """Gets the type of this FieldPartition.  # noqa: E501

        The type of partitions on a field  # noqa: E501

        :return: The type of this FieldPartition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FieldPartition.

        The type of partitions on a field  # noqa: E501

        :param type: The type of this FieldPartition.  # noqa: E501
        :type type: str
        """
        allowed_values = ["AUTO"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
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
        if not isinstance(other, FieldPartition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FieldPartition):
            return True

        return self.to_dict() != other.to_dict()