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


class SourceAzureBlobStorage(object):
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
        'container': 'str',
        'prefix': 'str',
        'pattern': 'str',
        'blob_count_downloaded': 'int',
        'blob_count_total': 'int',
        'blob_bytes_total': 'int'
    }

    attribute_map = {
        'container': 'container',
        'prefix': 'prefix',
        'pattern': 'pattern',
        'blob_count_downloaded': 'blob_count_downloaded',
        'blob_count_total': 'blob_count_total',
        'blob_bytes_total': 'blob_bytes_total'
    }

    def __init__(self, container=None, prefix=None, pattern=None, blob_count_downloaded=None, blob_count_total=None, blob_bytes_total=None, _configuration=None):  # noqa: E501
        """SourceAzureBlobStorage - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._container = None
        self._prefix = None
        self._pattern = None
        self._blob_count_downloaded = None
        self._blob_count_total = None
        self._blob_bytes_total = None
        self.discriminator = None

        if container is not None:
            self.container = container
        if prefix is not None:
            self.prefix = prefix
        if pattern is not None:
            self.pattern = pattern
        if blob_count_downloaded is not None:
            self.blob_count_downloaded = blob_count_downloaded
        if blob_count_total is not None:
            self.blob_count_total = blob_count_total
        if blob_bytes_total is not None:
            self.blob_bytes_total = blob_bytes_total

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
        :type: str
        """

        self._container = container

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
        :type: str
        """

        self._prefix = prefix

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
        :type: str
        """

        self._pattern = pattern

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
        :type: int
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
        :type: int
        """

        self._blob_count_total = blob_count_total

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
        :type: int
        """

        self._blob_bytes_total = blob_bytes_total

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
        if issubclass(SourceAzureBlobStorage, dict):
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
        if not isinstance(other, SourceAzureBlobStorage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SourceAzureBlobStorage):
            return True

        return self.to_dict() != other.to_dict()
