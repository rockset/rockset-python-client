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


class QueryLambdaSql(object):
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
        'query': 'str',
        'default_parameters': 'list[QueryParameter]'
    }

    attribute_map = {
        'query': 'query',
        'default_parameters': 'default_parameters'
    }

    def __init__(self, query=None, default_parameters=None, _configuration=None):  # noqa: E501
        """QueryLambdaSql - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._query = None
        self._default_parameters = None
        self.discriminator = None

        self.query = query
        if default_parameters is not None:
            self.default_parameters = default_parameters

    @property
    def query(self):
        """Gets the query of this QueryLambdaSql.  # noqa: E501

        SQL text  # noqa: E501

        :return: The query of this QueryLambdaSql.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this QueryLambdaSql.

        SQL text  # noqa: E501

        :param query: The query of this QueryLambdaSql.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def default_parameters(self):
        """Gets the default_parameters of this QueryLambdaSql.  # noqa: E501

        default parameters for this Query Lambda  # noqa: E501

        :return: The default_parameters of this QueryLambdaSql.  # noqa: E501
        :rtype: list[QueryParameter]
        """
        return self._default_parameters

    @default_parameters.setter
    def default_parameters(self, default_parameters):
        """Sets the default_parameters of this QueryLambdaSql.

        default parameters for this Query Lambda  # noqa: E501

        :param default_parameters: The default_parameters of this QueryLambdaSql.  # noqa: E501
        :type: list[QueryParameter]
        """

        self._default_parameters = default_parameters

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
        if issubclass(QueryLambdaSql, dict):
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
        if not isinstance(other, QueryLambdaSql):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryLambdaSql):
            return True

        return self.to_dict() != other.to_dict()
