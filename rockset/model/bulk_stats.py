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



class BulkStats(ModelNormal):
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
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
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
        return {
            'data_downloaded_bytes': (int, none_type),  # noqa: E501
            'data_indexed_bytes': (int, none_type),  # noqa: E501
            'documents_downloaded': (int, none_type),  # noqa: E501
            'download_compute_ms': (int, none_type),  # noqa: E501
            'downloading_stage_done_at': (str, none_type),  # noqa: E501
            'finalizing_stage_done_at': (str, none_type),  # noqa: E501
            'index_compute_ms': (int, none_type),  # noqa: E501
            'indexing_stage_done_at': (str, none_type),  # noqa: E501
            'initializing_stage_done_at': (str, none_type),  # noqa: E501
            'provisioning_stage_done_at': (str, none_type),  # noqa: E501
            'started_at': (str, none_type),  # noqa: E501
            'total_index_size_bytes': (int, none_type),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'data_downloaded_bytes': 'data_downloaded_bytes',  # noqa: E501
        'data_indexed_bytes': 'data_indexed_bytes',  # noqa: E501
        'documents_downloaded': 'documents_downloaded',  # noqa: E501
        'download_compute_ms': 'download_compute_ms',  # noqa: E501
        'downloading_stage_done_at': 'downloading_stage_done_at',  # noqa: E501
        'finalizing_stage_done_at': 'finalizing_stage_done_at',  # noqa: E501
        'index_compute_ms': 'index_compute_ms',  # noqa: E501
        'indexing_stage_done_at': 'indexing_stage_done_at',  # noqa: E501
        'initializing_stage_done_at': 'initializing_stage_done_at',  # noqa: E501
        'provisioning_stage_done_at': 'provisioning_stage_done_at',  # noqa: E501
        'started_at': 'started_at',  # noqa: E501
        'total_index_size_bytes': 'total_index_size_bytes',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """BulkStats - a model defined in OpenAPI

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
            data_downloaded_bytes (int): Size in bytes of documents downloaded from source during an ongoing or completed bulk ingest. This includes documents that are dropped and reingested.. [optional]  # noqa: E501
            data_indexed_bytes (int): Size in bytes of documents indexed. This is the total size of documents after transformations and dropping before indexes are built.. [optional]  # noqa: E501
            documents_downloaded (int): Number of documents downloaded from source during an ongoing or completed bulk ingest. This includes documents that are dropped and reingested.. [optional]  # noqa: E501
            download_compute_ms (int): Bulk ingest compute units in milliseconds used for downloading documents.. [optional]  # noqa: E501
            downloading_stage_done_at (str): ISO-8601 date of when the downloading stage was completed.. [optional]  # noqa: E501
            finalizing_stage_done_at (str): ISO-8601 date of when the finalizing stage was completed.. [optional]  # noqa: E501
            index_compute_ms (int): Bulk ingest compute units in milliseconds used for indexing documents.. [optional]  # noqa: E501
            indexing_stage_done_at (str): ISO-8601 date of when the indexing stage was completed.. [optional]  # noqa: E501
            initializing_stage_done_at (str): ISO-8601 date of when the initializing stage was completed.. [optional]  # noqa: E501
            provisioning_stage_done_at (str): ISO-8601 date of when the provisioning stage was completed.. [optional]  # noqa: E501
            started_at (str): ISO-8601 date of when the bulk ingest was started.. [optional]  # noqa: E501
            total_index_size_bytes (int): Total size of indexes after the completed bulk ingest. This is the same as collection size.. [optional]  # noqa: E501
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
        """BulkStats - a model defined in OpenAPI

        Keyword Args:
            data_downloaded_bytes (int): Size in bytes of documents downloaded from source during an ongoing or completed bulk ingest. This includes documents that are dropped and reingested.. [optional]  # noqa: E501
            data_indexed_bytes (int): Size in bytes of documents indexed. This is the total size of documents after transformations and dropping before indexes are built.. [optional]  # noqa: E501
            documents_downloaded (int): Number of documents downloaded from source during an ongoing or completed bulk ingest. This includes documents that are dropped and reingested.. [optional]  # noqa: E501
            download_compute_ms (int): Bulk ingest compute units in milliseconds used for downloading documents.. [optional]  # noqa: E501
            downloading_stage_done_at (str): ISO-8601 date of when the downloading stage was completed.. [optional]  # noqa: E501
            finalizing_stage_done_at (str): ISO-8601 date of when the finalizing stage was completed.. [optional]  # noqa: E501
            index_compute_ms (int): Bulk ingest compute units in milliseconds used for indexing documents.. [optional]  # noqa: E501
            indexing_stage_done_at (str): ISO-8601 date of when the indexing stage was completed.. [optional]  # noqa: E501
            initializing_stage_done_at (str): ISO-8601 date of when the initializing stage was completed.. [optional]  # noqa: E501
            provisioning_stage_done_at (str): ISO-8601 date of when the provisioning stage was completed.. [optional]  # noqa: E501
            started_at (str): ISO-8601 date of when the bulk ingest was started.. [optional]  # noqa: E501
            total_index_size_bytes (int): Total size of indexes after the completed bulk ingest. This is the same as collection size.. [optional]  # noqa: E501
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