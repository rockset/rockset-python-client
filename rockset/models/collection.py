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


class Collection(object):
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
        'aliases': 'list[Alias]',
        'clustering_key': 'list[FieldPartition]',
        'created_at': 'str',
        'created_by': 'str',
        'description': 'str',
        'enable_exactly_once_writes': 'bool',
        'field_partitions': 'list[FieldPartition]',
        'field_mapping_query': 'FieldMappingQuery',
        'field_mappings': 'list[FieldMappingV2]',
        'field_schemas': 'list[FieldSchema]',
        'insert_only': 'bool',
        'inverted_index_group_encoding_options': 'InvertedIndexGroupEncodingOptions',
        'name': 'str',
        'retention_secs': 'int',
        'sources': 'list[Source]',
        'stats': 'CollectionStats',
        'status': 'str',
        'workspace': 'str'
    }

    attribute_map = {
        'aliases': 'aliases',
        'clustering_key': 'clustering_key',
        'created_at': 'created_at',
        'created_by': 'created_by',
        'description': 'description',
        'enable_exactly_once_writes': 'enable_exactly_once_writes',
        'field_partitions': 'fieldPartitions',
        'field_mapping_query': 'field_mapping_query',
        'field_mappings': 'field_mappings',
        'field_schemas': 'field_schemas',
        'insert_only': 'insert_only',
        'inverted_index_group_encoding_options': 'inverted_index_group_encoding_options',
        'name': 'name',
        'retention_secs': 'retention_secs',
        'sources': 'sources',
        'stats': 'stats',
        'status': 'status',
        'workspace': 'workspace'
    }

    def __init__(self, aliases=None, clustering_key=None, created_at=None, created_by=None, description=None, enable_exactly_once_writes=None, field_partitions=None, field_mapping_query=None, field_mappings=None, field_schemas=None, insert_only=None, inverted_index_group_encoding_options=None, name=None, retention_secs=None, sources=None, stats=None, status=None, workspace=None, local_vars_configuration=None):  # noqa: E501
        """Collection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._aliases = None
        self._clustering_key = None
        self._created_at = None
        self._created_by = None
        self._description = None
        self._enable_exactly_once_writes = None
        self._field_partitions = None
        self._field_mapping_query = None
        self._field_mappings = None
        self._field_schemas = None
        self._insert_only = None
        self._inverted_index_group_encoding_options = None
        self._name = None
        self._retention_secs = None
        self._sources = None
        self._stats = None
        self._status = None
        self._workspace = None
        self.discriminator = None

        if aliases is not None:
            self.aliases = aliases
        if clustering_key is not None:
            self.clustering_key = clustering_key
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if description is not None:
            self.description = description
        if enable_exactly_once_writes is not None:
            self.enable_exactly_once_writes = enable_exactly_once_writes
        if field_partitions is not None:
            self.field_partitions = field_partitions
        if field_mapping_query is not None:
            self.field_mapping_query = field_mapping_query
        if field_mappings is not None:
            self.field_mappings = field_mappings
        if field_schemas is not None:
            self.field_schemas = field_schemas
        if insert_only is not None:
            self.insert_only = insert_only
        if inverted_index_group_encoding_options is not None:
            self.inverted_index_group_encoding_options = inverted_index_group_encoding_options
        if name is not None:
            self.name = name
        if retention_secs is not None:
            self.retention_secs = retention_secs
        if sources is not None:
            self.sources = sources
        if stats is not None:
            self.stats = stats
        if status is not None:
            self.status = status
        if workspace is not None:
            self.workspace = workspace

    @property
    def aliases(self):
        """Gets the aliases of this Collection.  # noqa: E501

        list of aliases for a collection  # noqa: E501

        :return: The aliases of this Collection.  # noqa: E501
        :rtype: list[Alias]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this Collection.

        list of aliases for a collection  # noqa: E501

        :param aliases: The aliases of this Collection.  # noqa: E501
        :type aliases: list[Alias]
        """

        self._aliases = aliases

    @property
    def clustering_key(self):
        """Gets the clustering_key of this Collection.  # noqa: E501

        list of clustering fields for a collection  # noqa: E501

        :return: The clustering_key of this Collection.  # noqa: E501
        :rtype: list[FieldPartition]
        """
        return self._clustering_key

    @clustering_key.setter
    def clustering_key(self, clustering_key):
        """Sets the clustering_key of this Collection.

        list of clustering fields for a collection  # noqa: E501

        :param clustering_key: The clustering_key of this Collection.  # noqa: E501
        :type clustering_key: list[FieldPartition]
        """

        self._clustering_key = clustering_key

    @property
    def created_at(self):
        """Gets the created_at of this Collection.  # noqa: E501

        ISO-8601 date  # noqa: E501

        :return: The created_at of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Collection.

        ISO-8601 date  # noqa: E501

        :param created_at: The created_at of this Collection.  # noqa: E501
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Collection.  # noqa: E501

        email of user who created the collection  # noqa: E501

        :return: The created_by of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Collection.

        email of user who created the collection  # noqa: E501

        :param created_by: The created_by of this Collection.  # noqa: E501
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def description(self):
        """Gets the description of this Collection.  # noqa: E501

        text describing the collection  # noqa: E501

        :return: The description of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Collection.

        text describing the collection  # noqa: E501

        :param description: The description of this Collection.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def enable_exactly_once_writes(self):
        """Gets the enable_exactly_once_writes of this Collection.  # noqa: E501

        If true, exactly-once write semantics is enabled.  # noqa: E501

        :return: The enable_exactly_once_writes of this Collection.  # noqa: E501
        :rtype: bool
        """
        return self._enable_exactly_once_writes

    @enable_exactly_once_writes.setter
    def enable_exactly_once_writes(self, enable_exactly_once_writes):
        """Sets the enable_exactly_once_writes of this Collection.

        If true, exactly-once write semantics is enabled.  # noqa: E501

        :param enable_exactly_once_writes: The enable_exactly_once_writes of this Collection.  # noqa: E501
        :type enable_exactly_once_writes: bool
        """

        self._enable_exactly_once_writes = enable_exactly_once_writes

    @property
    def field_partitions(self):
        """Gets the field_partitions of this Collection.  # noqa: E501


        :return: The field_partitions of this Collection.  # noqa: E501
        :rtype: list[FieldPartition]
        """
        return self._field_partitions

    @field_partitions.setter
    def field_partitions(self, field_partitions):
        """Sets the field_partitions of this Collection.


        :param field_partitions: The field_partitions of this Collection.  # noqa: E501
        :type field_partitions: list[FieldPartition]
        """

        self._field_partitions = field_partitions

    @property
    def field_mapping_query(self):
        """Gets the field_mapping_query of this Collection.  # noqa: E501


        :return: The field_mapping_query of this Collection.  # noqa: E501
        :rtype: FieldMappingQuery
        """
        return self._field_mapping_query

    @field_mapping_query.setter
    def field_mapping_query(self, field_mapping_query):
        """Sets the field_mapping_query of this Collection.


        :param field_mapping_query: The field_mapping_query of this Collection.  # noqa: E501
        :type field_mapping_query: FieldMappingQuery
        """

        self._field_mapping_query = field_mapping_query

    @property
    def field_mappings(self):
        """Gets the field_mappings of this Collection.  # noqa: E501

        list of mappings applied on all documents in a collection  # noqa: E501

        :return: The field_mappings of this Collection.  # noqa: E501
        :rtype: list[FieldMappingV2]
        """
        return self._field_mappings

    @field_mappings.setter
    def field_mappings(self, field_mappings):
        """Sets the field_mappings of this Collection.

        list of mappings applied on all documents in a collection  # noqa: E501

        :param field_mappings: The field_mappings of this Collection.  # noqa: E501
        :type field_mappings: list[FieldMappingV2]
        """

        self._field_mappings = field_mappings

    @property
    def field_schemas(self):
        """Gets the field_schemas of this Collection.  # noqa: E501

        list of field schemas   # noqa: E501

        :return: The field_schemas of this Collection.  # noqa: E501
        :rtype: list[FieldSchema]
        """
        return self._field_schemas

    @field_schemas.setter
    def field_schemas(self, field_schemas):
        """Sets the field_schemas of this Collection.

        list of field schemas   # noqa: E501

        :param field_schemas: The field_schemas of this Collection.  # noqa: E501
        :type field_schemas: list[FieldSchema]
        """

        self._field_schemas = field_schemas

    @property
    def insert_only(self):
        """Gets the insert_only of this Collection.  # noqa: E501

        Whether the collection is insert only or not  # noqa: E501

        :return: The insert_only of this Collection.  # noqa: E501
        :rtype: bool
        """
        return self._insert_only

    @insert_only.setter
    def insert_only(self, insert_only):
        """Sets the insert_only of this Collection.

        Whether the collection is insert only or not  # noqa: E501

        :param insert_only: The insert_only of this Collection.  # noqa: E501
        :type insert_only: bool
        """

        self._insert_only = insert_only

    @property
    def inverted_index_group_encoding_options(self):
        """Gets the inverted_index_group_encoding_options of this Collection.  # noqa: E501


        :return: The inverted_index_group_encoding_options of this Collection.  # noqa: E501
        :rtype: InvertedIndexGroupEncodingOptions
        """
        return self._inverted_index_group_encoding_options

    @inverted_index_group_encoding_options.setter
    def inverted_index_group_encoding_options(self, inverted_index_group_encoding_options):
        """Sets the inverted_index_group_encoding_options of this Collection.


        :param inverted_index_group_encoding_options: The inverted_index_group_encoding_options of this Collection.  # noqa: E501
        :type inverted_index_group_encoding_options: InvertedIndexGroupEncodingOptions
        """

        self._inverted_index_group_encoding_options = inverted_index_group_encoding_options

    @property
    def name(self):
        """Gets the name of this Collection.  # noqa: E501

        unique identifer for collection, can contain alphanumeric or dash characters  # noqa: E501

        :return: The name of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Collection.

        unique identifer for collection, can contain alphanumeric or dash characters  # noqa: E501

        :param name: The name of this Collection.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[A-Za-z0-9_\-.]+$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[A-Za-z0-9_\-.]+$/`")  # noqa: E501

        self._name = name

    @property
    def retention_secs(self):
        """Gets the retention_secs of this Collection.  # noqa: E501

        number of seconds after which data is purged based on event time  # noqa: E501

        :return: The retention_secs of this Collection.  # noqa: E501
        :rtype: int
        """
        return self._retention_secs

    @retention_secs.setter
    def retention_secs(self, retention_secs):
        """Sets the retention_secs of this Collection.

        number of seconds after which data is purged based on event time  # noqa: E501

        :param retention_secs: The retention_secs of this Collection.  # noqa: E501
        :type retention_secs: int
        """

        self._retention_secs = retention_secs

    @property
    def sources(self):
        """Gets the sources of this Collection.  # noqa: E501

        list of sources from which collection ingests  # noqa: E501

        :return: The sources of this Collection.  # noqa: E501
        :rtype: list[Source]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this Collection.

        list of sources from which collection ingests  # noqa: E501

        :param sources: The sources of this Collection.  # noqa: E501
        :type sources: list[Source]
        """

        self._sources = sources

    @property
    def stats(self):
        """Gets the stats of this Collection.  # noqa: E501


        :return: The stats of this Collection.  # noqa: E501
        :rtype: CollectionStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this Collection.


        :param stats: The stats of this Collection.  # noqa: E501
        :type stats: CollectionStats
        """

        self._stats = stats

    @property
    def status(self):
        """Gets the status of this Collection.  # noqa: E501

        current status of collection, one of: CREATED, READY, DELETED  # noqa: E501

        :return: The status of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Collection.

        current status of collection, one of: CREATED, READY, DELETED  # noqa: E501

        :param status: The status of this Collection.  # noqa: E501
        :type status: str
        """
        allowed_values = ["INITIALIZED", "CREATED", "READY", "PAUSED", "DELETED", "PAUSING", "RESUMING", "PREPARING_BULK", "BULK_INGEST_MODE", "EXITING_BULK_INGEST_MODE", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def workspace(self):
        """Gets the workspace of this Collection.  # noqa: E501

        name of the workspace that the collection is in  # noqa: E501

        :return: The workspace of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this Collection.

        name of the workspace that the collection is in  # noqa: E501

        :param workspace: The workspace of this Collection.  # noqa: E501
        :type workspace: str
        """

        self._workspace = workspace

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
        if not isinstance(other, Collection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Collection):
            return True

        return self.to_dict() != other.to_dict()
