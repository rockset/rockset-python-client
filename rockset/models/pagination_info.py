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


class PaginationInfo(object):
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
        'current_page_doc_count': 'int',
        'next_cursor': 'str',
        'next_cursor_offset': 'int',
        'start_cursor': 'str'
    }

    attribute_map = {
        'current_page_doc_count': 'current_page_doc_count',
        'next_cursor': 'next_cursor',
        'next_cursor_offset': 'next_cursor_offset',
        'start_cursor': 'start_cursor'
    }

    def __init__(self, current_page_doc_count=None, next_cursor=None, next_cursor_offset=None, start_cursor=None, local_vars_configuration=None):  # noqa: E501
        """PaginationInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._current_page_doc_count = None
        self._next_cursor = None
        self._next_cursor_offset = None
        self._start_cursor = None
        self.discriminator = None

        if current_page_doc_count is not None:
            self.current_page_doc_count = current_page_doc_count
        if next_cursor is not None:
            self.next_cursor = next_cursor
        if next_cursor_offset is not None:
            self.next_cursor_offset = next_cursor_offset
        if start_cursor is not None:
            self.start_cursor = start_cursor

    @property
    def current_page_doc_count(self):
        """Gets the current_page_doc_count of this PaginationInfo.  # noqa: E501

        Number of documents returned in this result set  # noqa: E501

        :return: The current_page_doc_count of this PaginationInfo.  # noqa: E501
        :rtype: int
        """
        return self._current_page_doc_count

    @current_page_doc_count.setter
    def current_page_doc_count(self, current_page_doc_count):
        """Sets the current_page_doc_count of this PaginationInfo.

        Number of documents returned in this result set  # noqa: E501

        :param current_page_doc_count: The current_page_doc_count of this PaginationInfo.  # noqa: E501
        :type current_page_doc_count: int
        """

        self._current_page_doc_count = current_page_doc_count

    @property
    def next_cursor(self):
        """Gets the next_cursor of this PaginationInfo.  # noqa: E501

        Cursor to use to get the list of documents  # noqa: E501

        :return: The next_cursor of this PaginationInfo.  # noqa: E501
        :rtype: str
        """
        return self._next_cursor

    @next_cursor.setter
    def next_cursor(self, next_cursor):
        """Sets the next_cursor of this PaginationInfo.

        Cursor to use to get the list of documents  # noqa: E501

        :param next_cursor: The next_cursor of this PaginationInfo.  # noqa: E501
        :type next_cursor: str
        """

        self._next_cursor = next_cursor

    @property
    def next_cursor_offset(self):
        """Gets the next_cursor_offset of this PaginationInfo.  # noqa: E501

        The doc offset that next_cursor starts at.  # noqa: E501

        :return: The next_cursor_offset of this PaginationInfo.  # noqa: E501
        :rtype: int
        """
        return self._next_cursor_offset

    @next_cursor_offset.setter
    def next_cursor_offset(self, next_cursor_offset):
        """Sets the next_cursor_offset of this PaginationInfo.

        The doc offset that next_cursor starts at.  # noqa: E501

        :param next_cursor_offset: The next_cursor_offset of this PaginationInfo.  # noqa: E501
        :type next_cursor_offset: int
        """

        self._next_cursor_offset = next_cursor_offset

    @property
    def start_cursor(self):
        """Gets the start_cursor of this PaginationInfo.  # noqa: E501

        Cursor used to retrieve the first set of documents.  # noqa: E501

        :return: The start_cursor of this PaginationInfo.  # noqa: E501
        :rtype: str
        """
        return self._start_cursor

    @start_cursor.setter
    def start_cursor(self, start_cursor):
        """Sets the start_cursor of this PaginationInfo.

        Cursor used to retrieve the first set of documents.  # noqa: E501

        :param start_cursor: The start_cursor of this PaginationInfo.  # noqa: E501
        :type start_cursor: str
        """

        self._start_cursor = start_cursor

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
        if not isinstance(other, PaginationInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaginationInfo):
            return True

        return self.to_dict() != other.to_dict()