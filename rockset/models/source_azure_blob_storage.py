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


class SourceAzureBlobStorage(object):
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
        'blob_bytes_total': 'int',
        'blob_count_downloaded': 'int',
        'blob_count_total': 'int',
        'container': 'str',
        'pattern': 'str',
        'prefix': 'str'
    }

    attribute_map = {
        'blob_bytes_total': 'blob_bytes_total',
        'blob_count_downloaded': 'blob_count_downloaded',
        'blob_count_total': 'blob_count_total',
        'container': 'container',
        'pattern': 'pattern',
        'prefix': 'prefix'
    }

    def __init__(self, blob_bytes_total=None, blob_count_downloaded=None, blob_count_total=None, container=None, pattern=None, prefix=None, local_vars_configuration=None):  # noqa: E501
        """SourceAzureBlobStorage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._blob_bytes_total = None
        self._blob_count_downloaded = None
        self._blob_count_total = None
        self._container = None
        self._pattern = None
        self._prefix = None
        self.discriminator = None

        if blob_bytes_total is not None:
            self.blob_bytes_total = blob_bytes_total
        if blob_count_downloaded is not None:
            self.blob_count_downloaded = blob_count_downloaded
        if blob_count_total is not None:
            self.blob_count_total = blob_count_total
        if container is not None:
            self.container = container
        if pattern is not None:
            self.pattern = pattern
        if prefix is not None:
            self.prefix = prefix

    @property
    def blob_bytes_total(self):
        """Gets the blob_bytes_total of this SourceAzureBlobStorage.  # noqa: E501


        :return: The blob_bytes_total of this SourceAzureBlobStorage.  # noqa: E501
        :rtype: int
        """
        return self._blob_bytes_total

    @blob_bytes_total.setter
    def blob_bytes_total(self, blob_bytes_total):
        """Sets the blob_bytes_total of this SourceAzureBlobStorage.


        :param blob_bytes_total: The blob_bytes_total of this SourceAzureBlobStorage.  # noqa: E501
        :type blob_bytes_total: int
        """

        self._blob_bytes_total = blob_bytes_total

    @property
    def blob_count_downloaded(self):
        """Gets the blob_count_downloaded of this SourceAzureBlobStorage.  # noqa: E501


        :return: The blob_count_downloaded of this SourceAzureBlobStorage.  # noqa: E501
        :rtype: int
        """
        return self._blob_count_downloaded

    @blob_count_downloaded.setter
    def blob_count_downloaded(self, blob_count_downloaded):
        """Sets the blob_count_downloaded of this SourceAzureBlobStorage.


        :param blob_count_downloaded: The blob_count_downloaded of this SourceAzureBlobStorage.  # noqa: E501
        :type blob_count_downloaded: int
        """

        self._blob_count_downloaded = blob_count_downloaded

    @property
    def blob_count_total(self):
        """Gets the blob_count_total of this SourceAzureBlobStorage.  # noqa: E501


        :return: The blob_count_total of this SourceAzureBlobStorage.  # noqa: E501
        :rtype: int
        """
        return self._blob_count_total

    @blob_count_total.setter
    def blob_count_total(self, blob_count_total):
        """Sets the blob_count_total of this SourceAzureBlobStorage.


        :param blob_count_total: The blob_count_total of this SourceAzureBlobStorage.  # noqa: E501
        :type blob_count_total: int
        """

        self._blob_count_total = blob_count_total

    @property
    def container(self):
        """Gets the container of this SourceAzureBlobStorage.  # noqa: E501

        name of Azure blob Storage container you want to ingest from  # noqa: E501

        :return: The container of this SourceAzureBlobStorage.  # noqa: E501
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this SourceAzureBlobStorage.

        name of Azure blob Storage container you want to ingest from  # noqa: E501

        :param container: The container of this SourceAzureBlobStorage.  # noqa: E501
        :type container: str
        """

        self._container = container

    @property
    def pattern(self):
        """Gets the pattern of this SourceAzureBlobStorage.  # noqa: E501

        Glob-style pattern that selects keys to ingest. Only either prefix or pattern can be specified.  # noqa: E501

        :return: The pattern of this SourceAzureBlobStorage.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this SourceAzureBlobStorage.

        Glob-style pattern that selects keys to ingest. Only either prefix or pattern can be specified.  # noqa: E501

        :param pattern: The pattern of this SourceAzureBlobStorage.  # noqa: E501
        :type pattern: str
        """

        self._pattern = pattern

    @property
    def prefix(self):
        """Gets the prefix of this SourceAzureBlobStorage.  # noqa: E501

        Prefix that selects blobs to ingest.  # noqa: E501

        :return: The prefix of this SourceAzureBlobStorage.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this SourceAzureBlobStorage.

        Prefix that selects blobs to ingest.  # noqa: E501

        :param prefix: The prefix of this SourceAzureBlobStorage.  # noqa: E501
        :type prefix: str
        """

        self._prefix = prefix

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
        if not isinstance(other, SourceAzureBlobStorage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SourceAzureBlobStorage):
            return True

        return self.to_dict() != other.to_dict()