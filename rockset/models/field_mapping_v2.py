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


class FieldMappingV2(object):
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
        'input_fields': 'list[InputField]',
        'is_drop_all_fields': 'bool',
        'name': 'str',
        'output_field': 'OutputField'
    }

    attribute_map = {
        'input_fields': 'input_fields',
        'is_drop_all_fields': 'is_drop_all_fields',
        'name': 'name',
        'output_field': 'output_field'
    }

    def __init__(self, input_fields=None, is_drop_all_fields=None, name=None, output_field=None, local_vars_configuration=None):  # noqa: E501
        """FieldMappingV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._input_fields = None
        self._is_drop_all_fields = None
        self._name = None
        self._output_field = None
        self.discriminator = None

        if input_fields is not None:
            self.input_fields = input_fields
        if is_drop_all_fields is not None:
            self.is_drop_all_fields = is_drop_all_fields
        if name is not None:
            self.name = name
        if output_field is not None:
            self.output_field = output_field

    @property
    def input_fields(self):
        """Gets the input_fields of this FieldMappingV2.  # noqa: E501

        A List of InputField for this mapping  # noqa: E501

        :return: The input_fields of this FieldMappingV2.  # noqa: E501
        :rtype: list[InputField]
        """
        return self._input_fields

    @input_fields.setter
    def input_fields(self, input_fields):
        """Sets the input_fields of this FieldMappingV2.

        A List of InputField for this mapping  # noqa: E501

        :param input_fields: The input_fields of this FieldMappingV2.  # noqa: E501
        :type input_fields: list[InputField]
        """

        self._input_fields = input_fields

    @property
    def is_drop_all_fields(self):
        """Gets the is_drop_all_fields of this FieldMappingV2.  # noqa: E501

        A boolean that determines whether to drop all fields in this document. If set, input and output fields should not be set  # noqa: E501

        :return: The is_drop_all_fields of this FieldMappingV2.  # noqa: E501
        :rtype: bool
        """
        return self._is_drop_all_fields

    @is_drop_all_fields.setter
    def is_drop_all_fields(self, is_drop_all_fields):
        """Sets the is_drop_all_fields of this FieldMappingV2.

        A boolean that determines whether to drop all fields in this document. If set, input and output fields should not be set  # noqa: E501

        :param is_drop_all_fields: The is_drop_all_fields of this FieldMappingV2.  # noqa: E501
        :type is_drop_all_fields: bool
        """

        self._is_drop_all_fields = is_drop_all_fields

    @property
    def name(self):
        """Gets the name of this FieldMappingV2.  # noqa: E501

        A user specified string that is a name for this mapping  # noqa: E501

        :return: The name of this FieldMappingV2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FieldMappingV2.

        A user specified string that is a name for this mapping  # noqa: E501

        :param name: The name of this FieldMappingV2.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def output_field(self):
        """Gets the output_field of this FieldMappingV2.  # noqa: E501


        :return: The output_field of this FieldMappingV2.  # noqa: E501
        :rtype: OutputField
        """
        return self._output_field

    @output_field.setter
    def output_field(self, output_field):
        """Sets the output_field of this FieldMappingV2.


        :param output_field: The output_field of this FieldMappingV2.  # noqa: E501
        :type output_field: OutputField
        """

        self._output_field = output_field

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
        if not isinstance(other, FieldMappingV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FieldMappingV2):
            return True

        return self.to_dict() != other.to_dict()
