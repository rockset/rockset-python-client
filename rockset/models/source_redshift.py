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


class SourceRedshift(object):
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
        'database': 'str',
        'incremental_field': 'str',
        'schema': 'str',
        'table_name': 'str'
    }

    attribute_map = {
        'database': 'database',
        'incremental_field': 'incremental_field',
        'schema': 'schema',
        'table_name': 'table_name'
    }

    def __init__(self, database=None, incremental_field=None, schema=None, table_name=None, local_vars_configuration=None):  # noqa: E501
        """SourceRedshift - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._database = None
        self._incremental_field = None
        self._schema = None
        self._table_name = None
        self.discriminator = None

        self.database = database
        if incremental_field is not None:
            self.incremental_field = incremental_field
        self.schema = schema
        self.table_name = table_name

    @property
    def database(self):
        """Gets the database of this SourceRedshift.  # noqa: E501

        name of the database in Redshift Cluster  # noqa: E501

        :return: The database of this SourceRedshift.  # noqa: E501
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this SourceRedshift.

        name of the database in Redshift Cluster  # noqa: E501

        :param database: The database of this SourceRedshift.  # noqa: E501
        :type database: str
        """
        if self.local_vars_configuration.client_side_validation and database is None:  # noqa: E501
            raise ValueError("Invalid value for `database`, must not be `None`")  # noqa: E501

        self._database = database

    @property
    def incremental_field(self):
        """Gets the incremental_field of this SourceRedshift.  # noqa: E501

        field in Redshift source table to monitor for updates  # noqa: E501

        :return: The incremental_field of this SourceRedshift.  # noqa: E501
        :rtype: str
        """
        return self._incremental_field

    @incremental_field.setter
    def incremental_field(self, incremental_field):
        """Sets the incremental_field of this SourceRedshift.

        field in Redshift source table to monitor for updates  # noqa: E501

        :param incremental_field: The incremental_field of this SourceRedshift.  # noqa: E501
        :type incremental_field: str
        """

        self._incremental_field = incremental_field

    @property
    def schema(self):
        """Gets the schema of this SourceRedshift.  # noqa: E501

        schema which contains the Redshift table  # noqa: E501

        :return: The schema of this SourceRedshift.  # noqa: E501
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this SourceRedshift.

        schema which contains the Redshift table  # noqa: E501

        :param schema: The schema of this SourceRedshift.  # noqa: E501
        :type schema: str
        """
        if self.local_vars_configuration.client_side_validation and schema is None:  # noqa: E501
            raise ValueError("Invalid value for `schema`, must not be `None`")  # noqa: E501

        self._schema = schema

    @property
    def table_name(self):
        """Gets the table_name of this SourceRedshift.  # noqa: E501

        name of Redshift table containing data  # noqa: E501

        :return: The table_name of this SourceRedshift.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this SourceRedshift.

        name of Redshift table containing data  # noqa: E501

        :param table_name: The table_name of this SourceRedshift.  # noqa: E501
        :type table_name: str
        """
        if self.local_vars_configuration.client_side_validation and table_name is None:  # noqa: E501
            raise ValueError("Invalid value for `table_name`, must not be `None`")  # noqa: E501

        self._table_name = table_name

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
        if not isinstance(other, SourceRedshift):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SourceRedshift):
            return True

        return self.to_dict() != other.to_dict()
