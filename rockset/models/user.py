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


class User(object):
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
        'created_at': 'str',
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'roles': 'list[str]',
        'state': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'email': 'email',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'roles': 'roles',
        'state': 'state'
    }

    def __init__(self, created_at=None, email=None, first_name=None, last_name=None, roles=None, state=None, local_vars_configuration=None):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._roles = None
        self._state = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if roles is not None:
            self.roles = roles
        if state is not None:
            self.state = state

    @property
    def created_at(self):
        """Gets the created_at of this User.  # noqa: E501

        ISO-8601 date  # noqa: E501

        :return: The created_at of this User.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this User.

        ISO-8601 date  # noqa: E501

        :param created_at: The created_at of this User.  # noqa: E501
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501

        user email  # noqa: E501

        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        user email  # noqa: E501

        :param email: The email of this User.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501

        user first name  # noqa: E501

        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.

        user first name  # noqa: E501

        :param first_name: The first_name of this User.  # noqa: E501
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501

        user last name  # noqa: E501

        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.

        user last name  # noqa: E501

        :param last_name: The last_name of this User.  # noqa: E501
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def roles(self):
        """Gets the roles of this User.  # noqa: E501

        List of roles for a given user  # noqa: E501

        :return: The roles of this User.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this User.

        List of roles for a given user  # noqa: E501

        :param roles: The roles of this User.  # noqa: E501
        :type roles: list[str]
        """

        self._roles = roles

    @property
    def state(self):
        """Gets the state of this User.  # noqa: E501

        state of user - NEW / ACTIVE  # noqa: E501

        :return: The state of this User.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this User.

        state of user - NEW / ACTIVE  # noqa: E501

        :param state: The state of this User.  # noqa: E501
        :type state: str
        """

        self._state = state

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
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()
