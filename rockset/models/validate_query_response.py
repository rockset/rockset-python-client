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


class ValidateQueryResponse(object):
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
        'collections': 'list[str]',
        'name': 'list[str]',
        'parameters': 'list[str]'
    }

    attribute_map = {
        'collections': 'collections',
        'name': 'name',
        'parameters': 'parameters'
    }

    def __init__(self, collections=None, name=None, parameters=None, local_vars_configuration=None):  # noqa: E501
        """ValidateQueryResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._collections = None
        self._name = None
        self._parameters = None
        self.discriminator = None

        self.collections = collections
        self.name = name
        self.parameters = parameters

    @property
    def collections(self):
        """Gets the collections of this ValidateQueryResponse.  # noqa: E501

        list of collection specified in query  # noqa: E501

        :return: The collections of this ValidateQueryResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this ValidateQueryResponse.

        list of collection specified in query  # noqa: E501

        :param collections: The collections of this ValidateQueryResponse.  # noqa: E501
        :type collections: list[str]
        """
        if self.local_vars_configuration.client_side_validation and collections is None:  # noqa: E501
            raise ValueError("Invalid value for `collections`, must not be `None`")  # noqa: E501

        self._collections = collections

    @property
    def name(self):
        """Gets the name of this ValidateQueryResponse.  # noqa: E501

        list of collection specified in query  # noqa: E501

        :return: The name of this ValidateQueryResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ValidateQueryResponse.

        list of collection specified in query  # noqa: E501

        :param name: The name of this ValidateQueryResponse.  # noqa: E501
        :type name: list[str]
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def parameters(self):
        """Gets the parameters of this ValidateQueryResponse.  # noqa: E501

        list of parameters specified in query  # noqa: E501

        :return: The parameters of this ValidateQueryResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ValidateQueryResponse.

        list of parameters specified in query  # noqa: E501

        :param parameters: The parameters of this ValidateQueryResponse.  # noqa: E501
        :type parameters: list[str]
        """
        if self.local_vars_configuration.client_side_validation and parameters is None:  # noqa: E501
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

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
        if not isinstance(other, ValidateQueryResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValidateQueryResponse):
            return True

        return self.to_dict() != other.to_dict()