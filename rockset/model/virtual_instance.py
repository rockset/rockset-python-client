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
    from rockset.model.auto_scaling_policy import AutoScalingPolicy
    from rockset.model.virtual_instance_stats import VirtualInstanceStats
    globals()['AutoScalingPolicy'] = AutoScalingPolicy
    globals()['VirtualInstanceStats'] = VirtualInstanceStats


class VirtualInstance(ModelNormal):
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
        ('current_size',): {
            'FREE': "FREE",
            'NANO': "NANO",
            'SHARED': "SHARED",
            'MILLI': "MILLI",
            'XSMALL': "XSMALL",
            'SMALL': "SMALL",
            'MEDIUM': "MEDIUM",
            'LARGE': "LARGE",
            'XLARGE': "XLARGE",
            'XLARGE2': "XLARGE2",
            'XLARGE4': "XLARGE4",
            'XLARGE8': "XLARGE8",
            'XLARGE16': "XLARGE16",
        },
        ('desired_size',): {
            'FREE': "FREE",
            'NANO': "NANO",
            'SHARED': "SHARED",
            'MILLI': "MILLI",
            'XSMALL': "XSMALL",
            'SMALL': "SMALL",
            'MEDIUM': "MEDIUM",
            'LARGE': "LARGE",
            'XLARGE': "XLARGE",
            'XLARGE2': "XLARGE2",
            'XLARGE4': "XLARGE4",
            'XLARGE8': "XLARGE8",
            'XLARGE16': "XLARGE16",
        },
        ('mount_type',): {
            'LIVE': "LIVE",
            'STATIC': "STATIC",
        },
        ('state',): {
            'INITIALIZING': "INITIALIZING",
            'PROVISIONING_RESOURCES': "PROVISIONING_RESOURCES",
            'REBALANCING_COLLECTIONS': "REBALANCING_COLLECTIONS",
            'ACTIVE': "ACTIVE",
            'SUSPENDING': "SUSPENDING",
            'SUSPENDED': "SUSPENDED",
            'RESUMING': "RESUMING",
            'DELETED': "DELETED",
            'ENABLING_DEDICATED_SERVICES': "ENABLING_DEDICATED_SERVICES",
            'DISABLING_DEDICATED_SERVICES': "DISABLING_DEDICATED_SERVICES",
        },
    }

    validations = {
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
            'name': (str,),  # noqa: E501
            'auto_scaling_policy': (AutoScalingPolicy, none_type),  # noqa: E501
            'auto_suspend_seconds': (int, none_type),  # noqa: E501
            'created_at': (str, none_type),  # noqa: E501
            'created_by': (str, none_type),  # noqa: E501
            'current_size': (str, none_type),  # noqa: E501
            'default_pod_count': (int, none_type),  # noqa: E501
            'default_vi': (bool, none_type),  # noqa: E501
            'description': (str, none_type),  # noqa: E501
            'desired_size': (str, none_type),  # noqa: E501
            'enable_remount_on_resume': (bool, none_type),  # noqa: E501
            'id': (str, none_type),  # noqa: E501
            'monitoring_enabled': (bool, none_type),  # noqa: E501
            'mount_refresh_interval_seconds': (int, none_type),  # noqa: E501
            'mount_type': (str, none_type),  # noqa: E501
            'resumed_at': (str, none_type),  # noqa: E501
            'rrn': (str, none_type),  # noqa: E501
            'scaled_pod_count': (int, none_type),  # noqa: E501
            'state': (str, none_type),  # noqa: E501
            'stats': (VirtualInstanceStats, none_type),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name': 'name',  # noqa: E501
        'auto_scaling_policy': 'auto_scaling_policy',  # noqa: E501
        'auto_suspend_seconds': 'auto_suspend_seconds',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'created_by': 'created_by',  # noqa: E501
        'current_size': 'current_size',  # noqa: E501
        'default_pod_count': 'default_pod_count',  # noqa: E501
        'default_vi': 'default_vi',  # noqa: E501
        'description': 'description',  # noqa: E501
        'desired_size': 'desired_size',  # noqa: E501
        'enable_remount_on_resume': 'enable_remount_on_resume',  # noqa: E501
        'id': 'id',  # noqa: E501
        'monitoring_enabled': 'monitoring_enabled',  # noqa: E501
        'mount_refresh_interval_seconds': 'mount_refresh_interval_seconds',  # noqa: E501
        'mount_type': 'mount_type',  # noqa: E501
        'resumed_at': 'resumed_at',  # noqa: E501
        'rrn': 'rrn',  # noqa: E501
        'scaled_pod_count': 'scaled_pod_count',  # noqa: E501
        'state': 'state',  # noqa: E501
        'stats': 'stats',  # noqa: E501
    }

    read_only_vars = {
        'current_size',  # noqa: E501
        'desired_size',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, name, *args, **kwargs):  # noqa: E501
        """VirtualInstance - a model defined in OpenAPI

        Args:
            name (str): Virtual instance name.

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
            auto_scaling_policy (AutoScalingPolicy): [optional]  # noqa: E501
            auto_suspend_seconds (int): Number of seconds without queries after which the VI is suspended. [optional]  # noqa: E501
            created_at (str): ISO-8601 date of when virtual instance was created.. [optional]  # noqa: E501
            created_by (str): Creator of requested virtual instance.. [optional]  # noqa: E501
            current_size (str): Virtual instance current size.. [optional]  # noqa: E501
            default_pod_count (int): [optional]  # noqa: E501
            default_vi (bool): [optional]  # noqa: E501
            description (str): Virtual instance description.. [optional]  # noqa: E501
            desired_size (str): Virtual instance desired size.. [optional]  # noqa: E501
            enable_remount_on_resume (bool): When a Virtual Instance is resumed, it will remount all collections that were mounted when the Virtual Instance was suspended.. [optional]  # noqa: E501
            id (str): Unique identifier for virtual instance.. [optional]  # noqa: E501
            monitoring_enabled (bool): [optional]  # noqa: E501
            mount_refresh_interval_seconds (int): DEPRECATED. Number of seconds between data refreshes for mounts on this Virtual Instance. [optional]  # noqa: E501
            mount_type (str): The mount type of collections that this Virtual Instance will query. Live mounted collections stay up-to-date with the underlying collection in real-time. Static mounted collections do not stay up-to-date. See https://docs.rockset.com/documentation/docs/virtual-instances#virtual-instance-configuration. [optional]  # noqa: E501
            resumed_at (str): ISO-8601 date of when virtual instance was created.. [optional]  # noqa: E501
            rrn (str): Virtual Instance RRN.. [optional]  # noqa: E501
            scaled_pod_count (int): [optional]  # noqa: E501
            state (str): Virtual instance state.. [optional]  # noqa: E501
            stats (VirtualInstanceStats): [optional]  # noqa: E501
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

        self.name = name
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
    def __init__(self, *, name, **kwargs):  # noqa: E501
        """VirtualInstance - a model defined in OpenAPI

        Keyword Args:
            name (str): Virtual instance name.
            auto_scaling_policy (AutoScalingPolicy): [optional]  # noqa: E501
            auto_suspend_seconds (int): Number of seconds without queries after which the VI is suspended. [optional]  # noqa: E501
            created_at (str): ISO-8601 date of when virtual instance was created.. [optional]  # noqa: E501
            created_by (str): Creator of requested virtual instance.. [optional]  # noqa: E501
            default_pod_count (int): [optional]  # noqa: E501
            default_vi (bool): [optional]  # noqa: E501
            description (str): Virtual instance description.. [optional]  # noqa: E501
            enable_remount_on_resume (bool): When a Virtual Instance is resumed, it will remount all collections that were mounted when the Virtual Instance was suspended.. [optional]  # noqa: E501
            id (str): Unique identifier for virtual instance.. [optional]  # noqa: E501
            monitoring_enabled (bool): [optional]  # noqa: E501
            mount_refresh_interval_seconds (int): DEPRECATED. Number of seconds between data refreshes for mounts on this Virtual Instance. [optional]  # noqa: E501
            mount_type (str): The mount type of collections that this Virtual Instance will query. Live mounted collections stay up-to-date with the underlying collection in real-time. Static mounted collections do not stay up-to-date. See https://docs.rockset.com/documentation/docs/virtual-instances#virtual-instance-configuration. [optional]  # noqa: E501
            resumed_at (str): ISO-8601 date of when virtual instance was created.. [optional]  # noqa: E501
            rrn (str): Virtual Instance RRN.. [optional]  # noqa: E501
            scaled_pod_count (int): [optional]  # noqa: E501
            state (str): Virtual instance state.. [optional]  # noqa: E501
            stats (VirtualInstanceStats): [optional]  # noqa: E501
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

        self.name = name
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
