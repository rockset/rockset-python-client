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


class Role(object):
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
        'role_name': 'str',
        'description': 'str',
        'owner_email': 'str',
        'created_by': 'str',
        'privileges': 'list[Privilege]',
        'created_at': 'str'
    }

    attribute_map = {
        'role_name': 'role_name',
        'description': 'description',
        'owner_email': 'owner_email',
        'created_by': 'created_by',
        'privileges': 'privileges',
        'created_at': 'created_at'
    }

    def __init__(self, role_name=None, description=None, owner_email=None, created_by=None, privileges=None, created_at=None, _configuration=None):  # noqa: E501
        """Role - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._role_name = None
        self._description = None
        self._owner_email = None
        self._created_by = None
        self._privileges = None
        self._created_at = None
        self.discriminator = None

        if role_name is not None:
            self.role_name = role_name
        if description is not None:
            self.description = description
        if owner_email is not None:
            self.owner_email = owner_email
        if created_by is not None:
            self.created_by = created_by
        if privileges is not None:
            self.privileges = privileges
        if created_at is not None:
            self.created_at = created_at

    @property
    def role_name(self):
        """Gets the role_name of this Role.  # noqa: E501

        Unique identifier for the role.  # noqa: E501

        :return: The role_name of this Role.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this Role.

        Unique identifier for the role.  # noqa: E501

        :param role_name: The role_name of this Role.  # noqa: E501
        :type: str
        """

        self._role_name = role_name

    @property
    def description(self):
        """Gets the description of this Role.  # noqa: E501

        Description for the role.  # noqa: E501

        :return: The description of this Role.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Role.

        Description for the role.  # noqa: E501

        :param description: The description of this Role.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def owner_email(self):
        """Gets the owner_email of this Role.  # noqa: E501

        Email of the user who currently owns the role.  # noqa: E501

        :return: The owner_email of this Role.  # noqa: E501
        :rtype: str
        """
        return self._owner_email

    @owner_email.setter
    def owner_email(self, owner_email):
        """Sets the owner_email of this Role.

        Email of the user who currently owns the role.  # noqa: E501

        :param owner_email: The owner_email of this Role.  # noqa: E501
        :type: str
        """

        self._owner_email = owner_email

    @property
    def created_by(self):
        """Gets the created_by of this Role.  # noqa: E501

        Email of the user who created the role.  # noqa: E501

        :return: The created_by of this Role.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Role.

        Email of the user who created the role.  # noqa: E501

        :param created_by: The created_by of this Role.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def privileges(self):
        """Gets the privileges of this Role.  # noqa: E501

        List of privileges associated with the role.  # noqa: E501

        :return: The privileges of this Role.  # noqa: E501
        :rtype: list[Privilege]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this Role.

        List of privileges associated with the role.  # noqa: E501

        :param privileges: The privileges of this Role.  # noqa: E501
        :type: list[Privilege]
        """

        self._privileges = privileges

    @property
    def created_at(self):
        """Gets the created_at of this Role.  # noqa: E501

        ISO-8601 date of when the role was created.  # noqa: E501

        :return: The created_at of this Role.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Role.

        ISO-8601 date of when the role was created.  # noqa: E501

        :param created_at: The created_at of this Role.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

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
        if issubclass(Role, dict):
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
        if not isinstance(other, Role):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Role):
            return True

        return self.to_dict() != other.to_dict()
