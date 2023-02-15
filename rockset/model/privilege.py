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



class Privilege(ModelNormal):
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
        ('action',): {
            'ALL_GLOBAL_ACTIONS': "ALL_GLOBAL_ACTIONS",
            'GET_ORG_GLOBAL': "GET_ORG_GLOBAL",
            'GET_CURRENT_USER_GLOBAL': "GET_CURRENT_USER_GLOBAL",
            'INVITE_USER_GLOBAL': "INVITE_USER_GLOBAL",
            'DELETE_USER_GLOBAL': "DELETE_USER_GLOBAL",
            'LIST_USERS_GLOBAL': "LIST_USERS_GLOBAL",
            'GET_BILLING_GLOBAL': "GET_BILLING_GLOBAL",
            'UPDATE_BILLING_GLOBAL': "UPDATE_BILLING_GLOBAL",
            'UPDATE_SETTINGS_GLOBAL': "UPDATE_SETTINGS_GLOBAL",
            'GET_METRICS_GLOBAL': "GET_METRICS_GLOBAL",
            'CREATE_VI_GLOBAL': "CREATE_VI_GLOBAL",
            'UPDATE_VI_GLOBAL': "UPDATE_VI_GLOBAL",
            'LIST_VI_GLOBAL': "LIST_VI_GLOBAL",
            'CREATE_WS_GLOBAL': "CREATE_WS_GLOBAL",
            'LIST_WS_GLOBAL': "LIST_WS_GLOBAL",
            'CREATE_INTEGRATION_GLOBAL': "CREATE_INTEGRATION_GLOBAL",
            'DELETE_INTEGRATION_GLOBAL': "DELETE_INTEGRATION_GLOBAL",
            'LIST_INTEGRATIONS_GLOBAL': "LIST_INTEGRATIONS_GLOBAL",
            'UPDATE_RESOURCE_OWNER_GLOBAL': "UPDATE_RESOURCE_OWNER_GLOBAL",
            'CREATE_API_KEY_GLOBAL': "CREATE_API_KEY_GLOBAL",
            'CREATE_ROLE_GLOBAL': "CREATE_ROLE_GLOBAL",
            'UPDATE_ROLE_GLOBAL': "UPDATE_ROLE_GLOBAL",
            'DELETE_ROLE_GLOBAL': "DELETE_ROLE_GLOBAL",
            'LIST_ROLES_GLOBAL': "LIST_ROLES_GLOBAL",
            'GRANT_REVOKE_ROLE_GLOBAL': "GRANT_REVOKE_ROLE_GLOBAL",
            'ALL_INTEGRATION_ACTIONS': "ALL_INTEGRATION_ACTIONS",
            'CREATE_COLLECTION_INTEGRATION': "CREATE_COLLECTION_INTEGRATION",
            'ALL_WORKSPACE_ACTIONS': "ALL_WORKSPACE_ACTIONS",
            'DELETE_WS': "DELETE_WS",
            'QUERY_DATA_WS': "QUERY_DATA_WS",
            'WRITE_DATA_WS': "WRITE_DATA_WS",
            'CREATE_COLLECTION_WS': "CREATE_COLLECTION_WS",
            'DELETE_COLLECTION_WS': "DELETE_COLLECTION_WS",
            'CREATE_ALIAS_WS': "CREATE_ALIAS_WS",
            'DELETE_ALIAS_WS': "DELETE_ALIAS_WS",
            'LIST_RESOURCES_WS': "LIST_RESOURCES_WS",
            'CREATE_QUERY_LAMBDA_WS': "CREATE_QUERY_LAMBDA_WS",
            'DELETE_QUERY_LAMBDA_WS': "DELETE_QUERY_LAMBDA_WS",
            'EXECUTE_QUERY_LAMBDA_WS': "EXECUTE_QUERY_LAMBDA_WS",
            'CREATE_SCHEDULED_LAMBDA_WS': "CREATE_SCHEDULED_LAMBDA_WS",
            'DELETE_SCHEDULED_LAMBDA_WS': "DELETE_SCHEDULED_LAMBDA_WS",
            'CREATE_VIEW_WS': "CREATE_VIEW_WS",
            'DELETE_VIEW_WS': "DELETE_VIEW_WS",
            'ALL_VI_ACTIONS': "ALL_VI_ACTIONS",
            'QUERY_VI': "QUERY_VI",
            'UPDATE_VI': "UPDATE_VI",
            'SUSPEND_RESUME_VI': "SUSPEND_RESUME_VI",
            'DELETE_VI': "DELETE_VI",
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
            'action': (str, none_type),  # noqa: E501
            'cluster': (str, none_type),  # noqa: E501
            'resource_name': (str, none_type),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'action': 'action',  # noqa: E501
        'cluster': 'cluster',  # noqa: E501
        'resource_name': 'resource_name',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Privilege - a model defined in OpenAPI

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
            action (str): The action allowed by this privilege.. [optional]  # noqa: E501
            cluster (str): Cluster ID (`usw2a1` for us-west-2, `use1a1` for us-east-1, `euc1a1` for eu-central-1) for which the action is allowed. Defaults to '*All*' if not specified.. [optional]  # noqa: E501
            resource_name (str): The resources on which the action is allowed. Defaults to '*All*' if not specified.. [optional]  # noqa: E501
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
        """Privilege - a model defined in OpenAPI

        Keyword Args:
            action (str): The action allowed by this privilege.. [optional]  # noqa: E501
            cluster (str): Cluster ID (`usw2a1` for us-west-2, `use1a1` for us-east-1, `euc1a1` for eu-central-1) for which the action is allowed. Defaults to '*All*' if not specified.. [optional]  # noqa: E501
            resource_name (str): The resources on which the action is allowed. Defaults to '*All*' if not specified.. [optional]  # noqa: E501
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
