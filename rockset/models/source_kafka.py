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


class SourceKafka(object):
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
        'kafka_topic_name': 'str',
        'offset_reset_policy': 'str',
        'status': 'StatusKafka',
        'use_v3': 'bool'
    }

    attribute_map = {
        'kafka_topic_name': 'kafka_topic_name',
        'offset_reset_policy': 'offset_reset_policy',
        'status': 'status',
        'use_v3': 'use_v3'
    }

    def __init__(self, kafka_topic_name=None, offset_reset_policy=None, status=None, use_v3=None, local_vars_configuration=None):  # noqa: E501
        """SourceKafka - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._kafka_topic_name = None
        self._offset_reset_policy = None
        self._status = None
        self._use_v3 = None
        self.discriminator = None

        self.kafka_topic_name = kafka_topic_name
        if offset_reset_policy is not None:
            self.offset_reset_policy = offset_reset_policy
        if status is not None:
            self.status = status
        if use_v3 is not None:
            self.use_v3 = use_v3

    @property
    def kafka_topic_name(self):
        """Gets the kafka_topic_name of this SourceKafka.  # noqa: E501

        The Kafka topic to be tailed  # noqa: E501

        :return: The kafka_topic_name of this SourceKafka.  # noqa: E501
        :rtype: str
        """
        return self._kafka_topic_name

    @kafka_topic_name.setter
    def kafka_topic_name(self, kafka_topic_name):
        """Sets the kafka_topic_name of this SourceKafka.

        The Kafka topic to be tailed  # noqa: E501

        :param kafka_topic_name: The kafka_topic_name of this SourceKafka.  # noqa: E501
        :type kafka_topic_name: str
        """
        if self.local_vars_configuration.client_side_validation and kafka_topic_name is None:  # noqa: E501
            raise ValueError("Invalid value for `kafka_topic_name`, must not be `None`")  # noqa: E501

        self._kafka_topic_name = kafka_topic_name

    @property
    def offset_reset_policy(self):
        """Gets the offset_reset_policy of this SourceKafka.  # noqa: E501


        :return: The offset_reset_policy of this SourceKafka.  # noqa: E501
        :rtype: str
        """
        return self._offset_reset_policy

    @offset_reset_policy.setter
    def offset_reset_policy(self, offset_reset_policy):
        """Sets the offset_reset_policy of this SourceKafka.


        :param offset_reset_policy: The offset_reset_policy of this SourceKafka.  # noqa: E501
        :type offset_reset_policy: str
        """
        allowed_values = ["LATEST", "EARLIEST"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and offset_reset_policy not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `offset_reset_policy` ({0}), must be one of {1}"  # noqa: E501
                .format(offset_reset_policy, allowed_values)
            )

        self._offset_reset_policy = offset_reset_policy

    @property
    def status(self):
        """Gets the status of this SourceKafka.  # noqa: E501


        :return: The status of this SourceKafka.  # noqa: E501
        :rtype: StatusKafka
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SourceKafka.


        :param status: The status of this SourceKafka.  # noqa: E501
        :type status: StatusKafka
        """

        self._status = status

    @property
    def use_v3(self):
        """Gets the use_v3 of this SourceKafka.  # noqa: E501


        :return: The use_v3 of this SourceKafka.  # noqa: E501
        :rtype: bool
        """
        return self._use_v3

    @use_v3.setter
    def use_v3(self, use_v3):
        """Sets the use_v3 of this SourceKafka.


        :param use_v3: The use_v3 of this SourceKafka.  # noqa: E501
        :type use_v3: bool
        """

        self._use_v3 = use_v3

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
        if not isinstance(other, SourceKafka):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SourceKafka):
            return True

        return self.to_dict() != other.to_dict()
