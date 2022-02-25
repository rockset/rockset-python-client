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


class Alias(object):
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
        'name': 'str',
        'description': 'str',
        'workspace': 'str',
        'creator_email': 'str',
        'collections': 'list[str]',
        'state': 'str',
        'created_at': 'str',
        'modified_at': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'workspace': 'workspace',
        'creator_email': 'creator_email',
        'collections': 'collections',
        'state': 'state',
        'created_at': 'created_at',
        'modified_at': 'modified_at'
    }

    def __init__(self, name=None, description=None, workspace=None, creator_email=None, collections=None, state=None, created_at=None, modified_at=None, _configuration=None):  # noqa: E501
        """Alias - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._description = None
        self._workspace = None
        self._creator_email = None
        self._collections = None
        self._state = None
        self._created_at = None
        self._modified_at = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if workspace is not None:
            self.workspace = workspace
        if creator_email is not None:
            self.creator_email = creator_email
        if collections is not None:
            self.collections = collections
        if state is not None:
            self.state = state
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at

    @property
    def name(self):
        """Gets the name of this Alias.  # noqa: E501

        name of the alias  # noqa: E501

        :return: The name of this Alias.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Alias.

        name of the alias  # noqa: E501

        :param name: The name of this Alias.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Alias.  # noqa: E501

        alias description  # noqa: E501

        :return: The description of this Alias.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Alias.

        alias description  # noqa: E501

        :param description: The description of this Alias.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def workspace(self):
        """Gets the workspace of this Alias.  # noqa: E501

        name of the workspace  # noqa: E501

        :return: The workspace of this Alias.  # noqa: E501
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this Alias.

        name of the workspace  # noqa: E501

        :param workspace: The workspace of this Alias.  # noqa: E501
        :type: str
        """

        self._workspace = workspace

    @property
    def creator_email(self):
        """Gets the creator_email of this Alias.  # noqa: E501

        email of the creator  # noqa: E501

        :return: The creator_email of this Alias.  # noqa: E501
        :rtype: str
        """
        return self._creator_email

    @creator_email.setter
    def creator_email(self, creator_email):
        """Sets the creator_email of this Alias.

        email of the creator  # noqa: E501

        :param creator_email: The creator_email of this Alias.  # noqa: E501
        :type: str
        """

        self._creator_email = creator_email

    @property
    def collections(self):
        """Gets the collections of this Alias.  # noqa: E501

        list of fully qualified collection names referenced by alias  # noqa: E501

        :return: The collections of this Alias.  # noqa: E501
        :rtype: list[str]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this Alias.

        list of fully qualified collection names referenced by alias  # noqa: E501

        :param collections: The collections of this Alias.  # noqa: E501
        :type: list[str]
        """

        self._collections = collections

    @property
    def state(self):
        """Gets the state of this Alias.  # noqa: E501

        state of the alias  # noqa: E501

        :return: The state of this Alias.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Alias.

        state of the alias  # noqa: E501

        :param state: The state of this Alias.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREATED", "DELETED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                state not in allowed_values):
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def created_at(self):
        """Gets the created_at of this Alias.  # noqa: E501

        ISO-8601 date  # noqa: E501

        :return: The created_at of this Alias.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Alias.

        ISO-8601 date  # noqa: E501

        :param created_at: The created_at of this Alias.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this Alias.  # noqa: E501

        ISO-8601 date  # noqa: E501

        :return: The modified_at of this Alias.  # noqa: E501
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this Alias.

        ISO-8601 date  # noqa: E501

        :param modified_at: The modified_at of this Alias.  # noqa: E501
        :type: str
        """

        self._modified_at = modified_at

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
        if issubclass(Alias, dict):
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
        if not isinstance(other, Alias):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Alias):
            return True

        return self.to_dict() != other.to_dict()
