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


class FormatParams(object):
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
        'json': 'bool',
        'csv': 'CsvParams',
        'xml': 'XmlParams',
        'mysql_dms': 'bool',
        'postgres_dms': 'bool'
    }

    attribute_map = {
        'json': 'json',
        'csv': 'csv',
        'xml': 'xml',
        'mysql_dms': 'mysql_dms',
        'postgres_dms': 'postgres_dms'
    }

    def __init__(self, json=None, csv=None, xml=None, mysql_dms=None, postgres_dms=None, _configuration=None):  # noqa: E501
        """FormatParams - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._json = None
        self._csv = None
        self._xml = None
        self._mysql_dms = None
        self._postgres_dms = None
        self.discriminator = None

        if json is not None:
            self.json = json
        if csv is not None:
            self.csv = csv
        if xml is not None:
            self.xml = xml
        if mysql_dms is not None:
            self.mysql_dms = mysql_dms
        if postgres_dms is not None:
            self.postgres_dms = postgres_dms

    @property
    def json(self):
        """Gets the json of this FormatParams.  # noqa: E501

        source data is in json format  # noqa: E501

        :return: The json of this FormatParams.  # noqa: E501
        :rtype: bool
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this FormatParams.

        source data is in json format  # noqa: E501

        :param json: The json of this FormatParams.  # noqa: E501
        :type: bool
        """

        self._json = json

    @property
    def csv(self):
        """Gets the csv of this FormatParams.  # noqa: E501


        :return: The csv of this FormatParams.  # noqa: E501
        :rtype: CsvParams
        """
        return self._csv

    @csv.setter
    def csv(self, csv):
        """Sets the csv of this FormatParams.


        :param csv: The csv of this FormatParams.  # noqa: E501
        :type: CsvParams
        """

        self._csv = csv

    @property
    def xml(self):
        """Gets the xml of this FormatParams.  # noqa: E501


        :return: The xml of this FormatParams.  # noqa: E501
        :rtype: XmlParams
        """
        return self._xml

    @xml.setter
    def xml(self, xml):
        """Sets the xml of this FormatParams.


        :param xml: The xml of this FormatParams.  # noqa: E501
        :type: XmlParams
        """

        self._xml = xml

    @property
    def mysql_dms(self):
        """Gets the mysql_dms of this FormatParams.  # noqa: E501


        :return: The mysql_dms of this FormatParams.  # noqa: E501
        :rtype: bool
        """
        return self._mysql_dms

    @mysql_dms.setter
    def mysql_dms(self, mysql_dms):
        """Sets the mysql_dms of this FormatParams.


        :param mysql_dms: The mysql_dms of this FormatParams.  # noqa: E501
        :type: bool
        """

        self._mysql_dms = mysql_dms

    @property
    def postgres_dms(self):
        """Gets the postgres_dms of this FormatParams.  # noqa: E501


        :return: The postgres_dms of this FormatParams.  # noqa: E501
        :rtype: bool
        """
        return self._postgres_dms

    @postgres_dms.setter
    def postgres_dms(self, postgres_dms):
        """Sets the postgres_dms of this FormatParams.


        :param postgres_dms: The postgres_dms of this FormatParams.  # noqa: E501
        :type: bool
        """

        self._postgres_dms = postgres_dms

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
        if issubclass(FormatParams, dict):
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
        if not isinstance(other, FormatParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FormatParams):
            return True

        return self.to_dict() != other.to_dict()
