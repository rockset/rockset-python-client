"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from rockset.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from rockset.exceptions import ApiAttributeError


def lazy_import():
    from rockset.model.alias import Alias
    from rockset.model.bulk_stats import BulkStats
    from rockset.model.collection_stats import CollectionStats
    from rockset.model.field_mapping_query import FieldMappingQuery
    from rockset.model.field_mapping_v2 import FieldMappingV2
    from rockset.model.field_partition import FieldPartition
    from rockset.model.source import Source
    globals()['Alias'] = Alias
    globals()['BulkStats'] = BulkStats
    globals()['CollectionStats'] = CollectionStats
    globals()['FieldMappingQuery'] = FieldMappingQuery
    globals()['FieldMappingV2'] = FieldMappingV2
    globals()['FieldPartition'] = FieldPartition
    globals()['Source'] = Source


class Collection(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """
    
    allowed_values = {
        ('status',): {
            'INITIALIZED': "INITIALIZED",
            'CREATED': "CREATED",
            'READY': "READY",
            'PAUSED': "PAUSED",
            'DELETED': "DELETED",
            'PAUSING': "PAUSING",
            'RESUMING': "RESUMING",
            'PREPARING_BULK': "PREPARING_BULK",
            'BULK_INGEST_MODE': "BULK_INGEST_MODE",
            'EXITING_BULK_INGEST_MODE': "EXITING_BULK_INGEST_MODE",
            'ENCRYPTION_KEY_ERROR': "ENCRYPTION_KEY_ERROR",
            'UNKNOWN': "UNKNOWN",
        },
        ('storage_compression_type',): {
            'LZ4': "LZ4",
            'ZSTD': "ZSTD",
            'UNKNOWN': "UNKNOWN",
        },
    }

    validations = {
        ('name',): {
            'regex': {
                'pattern': r'^[A-Za-z0-9_\-.]+$',  # noqa: E501
            },
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'aliases': ([Alias], none_type),  # noqa: E501
            'bulk_stats': ([BulkStats], none_type),  # noqa: E501
            'clustering_key': ([FieldPartition], none_type),  # noqa: E501
            'created_at': (str, none_type),  # noqa: E501
            'created_by': (str, none_type),  # noqa: E501
            'created_by_apikey_name': (str, none_type),  # noqa: E501
            'description': (str, none_type),  # noqa: E501
            'field_mapping_query': (FieldMappingQuery, none_type),  # noqa: E501
            'field_mappings': ([FieldMappingV2], none_type),  # noqa: E501
            'insert_only': (bool, none_type),  # noqa: E501
            'name': (str, none_type),  # noqa: E501
            'read_only': (bool, none_type),  # noqa: E501
            'retention_secs': (int, none_type),  # noqa: E501
            'rrn': (str, none_type),  # noqa: E501
            'sources': ([Source], none_type),  # noqa: E501
            'stats': (CollectionStats, none_type),  # noqa: E501
            'status': (str, none_type),  # noqa: E501
            'storage_compression_type': (str, none_type),  # noqa: E501
            'workspace': (str, none_type),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'aliases': 'aliases',  # noqa: E501
        'bulk_stats': 'bulk_stats',  # noqa: E501
        'clustering_key': 'clustering_key',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'created_by_apikey_name': 'created_by_apikey_name',  # noqa: E501
        'description': 'description',  # noqa: E501
        'field_mapping_query': 'field_mapping_query',  # noqa: E501
        'field_mappings': 'field_mappings',  # noqa: E501
        'insert_only': 'insert_only',  # noqa: E501
        'name': 'name',  # noqa: E501
        'read_only': 'read_only',  # noqa: E501
        'retention_secs': 'retention_secs',  # noqa: E501
        'rrn': 'rrn',  # noqa: E501
        'sources': 'sources',  # noqa: E501
        'stats': 'stats',  # noqa: E501
        'status': 'status',  # noqa: E501
        'storage_compression_type': 'storage_compression_type',  # noqa: E501
        'workspace': 'workspace',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Collection - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            aliases ([Alias]): List of aliases for a collection.. [optional]  # noqa: E501
            bulk_stats ([BulkStats]): [optional]  # noqa: E501
            clustering_key ([FieldPartition]): List of clustering fields for a collection.. [optional]  # noqa: E501
            created_at (str): ISO-8601 date.. [optional]  # noqa: E501
            created_by (str): Email of user who created the collection.. [optional]  # noqa: E501
            created_by_apikey_name (str): Name of the API key that was used to create this collection if one was used.. [optional]  # noqa: E501
            description (str): Text describing the collection.. [optional]  # noqa: E501
            field_mapping_query (FieldMappingQuery): [optional]  # noqa: E501
            field_mappings ([FieldMappingV2]): List of mappings applied on all documents in a collection.. [optional]  # noqa: E501
            insert_only (bool): Whether the collection is insert only or not.. [optional]  # noqa: E501
            name (str): Unique identifer for collection, can contain alphanumeric or dash characters.. [optional]  # noqa: E501
            read_only (bool): Whether the collection is read-only or not.. [optional]  # noqa: E501
            retention_secs (int): Number of seconds after which data is purged based on event time.. [optional]  # noqa: E501
            rrn (str): Collection RRN.. [optional]  # noqa: E501
            sources ([Source]): List of sources from which collection ingests.. [optional]  # noqa: E501
            stats (CollectionStats): [optional]  # noqa: E501
            status (str): Current status of collection.. [optional]  # noqa: E501
            storage_compression_type (str): RocksDB storage compression type.. [optional]  # noqa: E501
            workspace (str): Name of the workspace that the collection is in.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, **kwargs):  # noqa: E501
        """Collection - a model defined in OpenAPI

        Keyword Args:
            aliases ([Alias]): List of aliases for a collection.. [optional]  # noqa: E501
            bulk_stats ([BulkStats]): [optional]  # noqa: E501
            clustering_key ([FieldPartition]): List of clustering fields for a collection.. [optional]  # noqa: E501
            created_at (str): ISO-8601 date.. [optional]  # noqa: E501
            created_by (str): Email of user who created the collection.. [optional]  # noqa: E501
            created_by_apikey_name (str): Name of the API key that was used to create this collection if one was used.. [optional]  # noqa: E501
            description (str): Text describing the collection.. [optional]  # noqa: E501
            field_mapping_query (FieldMappingQuery): [optional]  # noqa: E501
            field_mappings ([FieldMappingV2]): List of mappings applied on all documents in a collection.. [optional]  # noqa: E501
            insert_only (bool): Whether the collection is insert only or not.. [optional]  # noqa: E501
            name (str): Unique identifer for collection, can contain alphanumeric or dash characters.. [optional]  # noqa: E501
            read_only (bool): Whether the collection is read-only or not.. [optional]  # noqa: E501
            retention_secs (int): Number of seconds after which data is purged based on event time.. [optional]  # noqa: E501
            rrn (str): Collection RRN.. [optional]  # noqa: E501
            sources ([Source]): List of sources from which collection ingests.. [optional]  # noqa: E501
            stats (CollectionStats): [optional]  # noqa: E501
            status (str): Current status of collection.. [optional]  # noqa: E501
            storage_compression_type (str): RocksDB storage compression type.. [optional]  # noqa: E501
            workspace (str): Name of the workspace that the collection is in.. [optional]  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """
        
        args = []
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            # todo: remove these comments - this stops the user from setting read only vars but we need this now to address a bug
            # if var_name in self.read_only_vars:
            #     raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
            #                          f"class with read only attributes.")
