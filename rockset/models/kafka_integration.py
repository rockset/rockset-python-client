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


class KafkaIntegration(object):
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
        'bootstrap_servers': 'str',
        'connection_string': 'str',
        'kafka_data_format': 'str',
        'kafka_topic_names': 'list[str]',
        'security_config': 'KafkaV3SecurityConfig',
        'source_status_by_topic': 'dict(str, StatusKafka)',
        'use_v3': 'bool'
    }

    attribute_map = {
        'bootstrap_servers': 'bootstrap_servers',
        'connection_string': 'connection_string',
        'kafka_data_format': 'kafka_data_format',
        'kafka_topic_names': 'kafka_topic_names',
        'security_config': 'security_config',
        'source_status_by_topic': 'source_status_by_topic',
        'use_v3': 'use_v3'
    }

    def __init__(self, bootstrap_servers=None, connection_string=None, kafka_data_format=None, kafka_topic_names=None, security_config=None, source_status_by_topic=None, use_v3=None, local_vars_configuration=None):  # noqa: E501
        """KafkaIntegration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._bootstrap_servers = None
        self._connection_string = None
        self._kafka_data_format = None
        self._kafka_topic_names = None
        self._security_config = None
        self._source_status_by_topic = None
        self._use_v3 = None
        self.discriminator = None

        if bootstrap_servers is not None:
            self.bootstrap_servers = bootstrap_servers
        if connection_string is not None:
            self.connection_string = connection_string
        if kafka_data_format is not None:
            self.kafka_data_format = kafka_data_format
        if kafka_topic_names is not None:
            self.kafka_topic_names = kafka_topic_names
        if security_config is not None:
            self.security_config = security_config
        if source_status_by_topic is not None:
            self.source_status_by_topic = source_status_by_topic
        if use_v3 is not None:
            self.use_v3 = use_v3

    @property
    def bootstrap_servers(self):
        """Gets the bootstrap_servers of this KafkaIntegration.  # noqa: E501


        :return: The bootstrap_servers of this KafkaIntegration.  # noqa: E501
        :rtype: str
        """
        return self._bootstrap_servers

    @bootstrap_servers.setter
    def bootstrap_servers(self, bootstrap_servers):
        """Sets the bootstrap_servers of this KafkaIntegration.


        :param bootstrap_servers: The bootstrap_servers of this KafkaIntegration.  # noqa: E501
        :type bootstrap_servers: str
        """

        self._bootstrap_servers = bootstrap_servers

    @property
    def connection_string(self):
        """Gets the connection_string of this KafkaIntegration.  # noqa: E501

        kafka connection string  # noqa: E501

        :return: The connection_string of this KafkaIntegration.  # noqa: E501
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """Sets the connection_string of this KafkaIntegration.

        kafka connection string  # noqa: E501

        :param connection_string: The connection_string of this KafkaIntegration.  # noqa: E501
        :type connection_string: str
        """

        self._connection_string = connection_string

    @property
    def kafka_data_format(self):
        """Gets the kafka_data_format of this KafkaIntegration.  # noqa: E501

        The format of the Kafka topics being tailed  # noqa: E501

        :return: The kafka_data_format of this KafkaIntegration.  # noqa: E501
        :rtype: str
        """
        return self._kafka_data_format

    @kafka_data_format.setter
    def kafka_data_format(self, kafka_data_format):
        """Sets the kafka_data_format of this KafkaIntegration.

        The format of the Kafka topics being tailed  # noqa: E501

        :param kafka_data_format: The kafka_data_format of this KafkaIntegration.  # noqa: E501
        :type kafka_data_format: str
        """
        allowed_values = ["JSON", "AVRO"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and kafka_data_format not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `kafka_data_format` ({0}), must be one of {1}"  # noqa: E501
                .format(kafka_data_format, allowed_values)
            )

        self._kafka_data_format = kafka_data_format

    @property
    def kafka_topic_names(self):
        """Gets the kafka_topic_names of this KafkaIntegration.  # noqa: E501

        Kafka topics to tail  # noqa: E501

        :return: The kafka_topic_names of this KafkaIntegration.  # noqa: E501
        :rtype: list[str]
        """
        return self._kafka_topic_names

    @kafka_topic_names.setter
    def kafka_topic_names(self, kafka_topic_names):
        """Sets the kafka_topic_names of this KafkaIntegration.

        Kafka topics to tail  # noqa: E501

        :param kafka_topic_names: The kafka_topic_names of this KafkaIntegration.  # noqa: E501
        :type kafka_topic_names: list[str]
        """

        self._kafka_topic_names = kafka_topic_names

    @property
    def security_config(self):
        """Gets the security_config of this KafkaIntegration.  # noqa: E501


        :return: The security_config of this KafkaIntegration.  # noqa: E501
        :rtype: KafkaV3SecurityConfig
        """
        return self._security_config

    @security_config.setter
    def security_config(self, security_config):
        """Sets the security_config of this KafkaIntegration.


        :param security_config: The security_config of this KafkaIntegration.  # noqa: E501
        :type security_config: KafkaV3SecurityConfig
        """

        self._security_config = security_config

    @property
    def source_status_by_topic(self):
        """Gets the source_status_by_topic of this KafkaIntegration.  # noqa: E501

        The status of the Kafka source by topic  # noqa: E501

        :return: The source_status_by_topic of this KafkaIntegration.  # noqa: E501
        :rtype: dict(str, StatusKafka)
        """
        return self._source_status_by_topic

    @source_status_by_topic.setter
    def source_status_by_topic(self, source_status_by_topic):
        """Sets the source_status_by_topic of this KafkaIntegration.

        The status of the Kafka source by topic  # noqa: E501

        :param source_status_by_topic: The source_status_by_topic of this KafkaIntegration.  # noqa: E501
        :type source_status_by_topic: dict(str, StatusKafka)
        """

        self._source_status_by_topic = source_status_by_topic

    @property
    def use_v3(self):
        """Gets the use_v3 of this KafkaIntegration.  # noqa: E501


        :return: The use_v3 of this KafkaIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._use_v3

    @use_v3.setter
    def use_v3(self, use_v3):
        """Sets the use_v3 of this KafkaIntegration.


        :param use_v3: The use_v3 of this KafkaIntegration.  # noqa: E501
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
        if not isinstance(other, KafkaIntegration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KafkaIntegration):
            return True

        return self.to_dict() != other.to_dict()