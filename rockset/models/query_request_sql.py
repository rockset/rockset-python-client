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


class QueryRequestSql(object):
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
        'default_row_limit': 'int',
        'generate_warnings': 'bool',
        'initial_paginate_response_doc_count': 'int',
        'paginate': 'bool',
        'parameters': 'list[QueryParameter]',
        'profiling_enabled': 'bool',
        'query': 'str'
    }

    attribute_map = {
        'default_row_limit': 'default_row_limit',
        'generate_warnings': 'generate_warnings',
        'initial_paginate_response_doc_count': 'initial_paginate_response_doc_count',
        'paginate': 'paginate',
        'parameters': 'parameters',
        'profiling_enabled': 'profiling_enabled',
        'query': 'query'
    }

    def __init__(self, default_row_limit=None, generate_warnings=None, initial_paginate_response_doc_count=None, paginate=None, parameters=None, profiling_enabled=None, query=None, local_vars_configuration=None):  # noqa: E501
        """QueryRequestSql - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._default_row_limit = None
        self._generate_warnings = None
        self._initial_paginate_response_doc_count = None
        self._paginate = None
        self._parameters = None
        self._profiling_enabled = None
        self._query = None
        self.discriminator = None

        if default_row_limit is not None:
            self.default_row_limit = default_row_limit
        if generate_warnings is not None:
            self.generate_warnings = generate_warnings
        if initial_paginate_response_doc_count is not None:
            self.initial_paginate_response_doc_count = initial_paginate_response_doc_count
        if paginate is not None:
            self.paginate = paginate
        if parameters is not None:
            self.parameters = parameters
        if profiling_enabled is not None:
            self.profiling_enabled = profiling_enabled
        self.query = query

    @property
    def default_row_limit(self):
        """Gets the default_row_limit of this QueryRequestSql.  # noqa: E501

        Row limit to use. Limits specified in the query text will override this default.  # noqa: E501

        :return: The default_row_limit of this QueryRequestSql.  # noqa: E501
        :rtype: int
        """
        return self._default_row_limit

    @default_row_limit.setter
    def default_row_limit(self, default_row_limit):
        """Sets the default_row_limit of this QueryRequestSql.

        Row limit to use. Limits specified in the query text will override this default.  # noqa: E501

        :param default_row_limit: The default_row_limit of this QueryRequestSql.  # noqa: E501
        :type default_row_limit: int
        """

        self._default_row_limit = default_row_limit

    @property
    def generate_warnings(self):
        """Gets the generate_warnings of this QueryRequestSql.  # noqa: E501

        Flag to enable warnings. Warnings can help debug query issues but negatively affect performance.  # noqa: E501

        :return: The generate_warnings of this QueryRequestSql.  # noqa: E501
        :rtype: bool
        """
        return self._generate_warnings

    @generate_warnings.setter
    def generate_warnings(self, generate_warnings):
        """Sets the generate_warnings of this QueryRequestSql.

        Flag to enable warnings. Warnings can help debug query issues but negatively affect performance.  # noqa: E501

        :param generate_warnings: The generate_warnings of this QueryRequestSql.  # noqa: E501
        :type generate_warnings: bool
        """

        self._generate_warnings = generate_warnings

    @property
    def initial_paginate_response_doc_count(self):
        """Gets the initial_paginate_response_doc_count of this QueryRequestSql.  # noqa: E501

        Number of documents to return in addition to paginating for this query call. Only relevant if `paginate` flag is also set.  # noqa: E501

        :return: The initial_paginate_response_doc_count of this QueryRequestSql.  # noqa: E501
        :rtype: int
        """
        return self._initial_paginate_response_doc_count

    @initial_paginate_response_doc_count.setter
    def initial_paginate_response_doc_count(self, initial_paginate_response_doc_count):
        """Sets the initial_paginate_response_doc_count of this QueryRequestSql.

        Number of documents to return in addition to paginating for this query call. Only relevant if `paginate` flag is also set.  # noqa: E501

        :param initial_paginate_response_doc_count: The initial_paginate_response_doc_count of this QueryRequestSql.  # noqa: E501
        :type initial_paginate_response_doc_count: int
        """

        self._initial_paginate_response_doc_count = initial_paginate_response_doc_count

    @property
    def paginate(self):
        """Gets the paginate of this QueryRequestSql.  # noqa: E501

        Flag to paginate and store the results of this query for later / sequential retrieval.  # noqa: E501

        :return: The paginate of this QueryRequestSql.  # noqa: E501
        :rtype: bool
        """
        return self._paginate

    @paginate.setter
    def paginate(self, paginate):
        """Sets the paginate of this QueryRequestSql.

        Flag to paginate and store the results of this query for later / sequential retrieval.  # noqa: E501

        :param paginate: The paginate of this QueryRequestSql.  # noqa: E501
        :type paginate: bool
        """

        self._paginate = paginate

    @property
    def parameters(self):
        """Gets the parameters of this QueryRequestSql.  # noqa: E501

        List of named parameters.  # noqa: E501

        :return: The parameters of this QueryRequestSql.  # noqa: E501
        :rtype: list[QueryParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this QueryRequestSql.

        List of named parameters.  # noqa: E501

        :param parameters: The parameters of this QueryRequestSql.  # noqa: E501
        :type parameters: list[QueryParameter]
        """

        self._parameters = parameters

    @property
    def profiling_enabled(self):
        """Gets the profiling_enabled of this QueryRequestSql.  # noqa: E501

        Flag to generate a performance profile for this query.  # noqa: E501

        :return: The profiling_enabled of this QueryRequestSql.  # noqa: E501
        :rtype: bool
        """
        return self._profiling_enabled

    @profiling_enabled.setter
    def profiling_enabled(self, profiling_enabled):
        """Sets the profiling_enabled of this QueryRequestSql.

        Flag to generate a performance profile for this query.  # noqa: E501

        :param profiling_enabled: The profiling_enabled of this QueryRequestSql.  # noqa: E501
        :type profiling_enabled: bool
        """

        self._profiling_enabled = profiling_enabled

    @property
    def query(self):
        """Gets the query of this QueryRequestSql.  # noqa: E501

        SQL query string.  # noqa: E501

        :return: The query of this QueryRequestSql.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this QueryRequestSql.

        SQL query string.  # noqa: E501

        :param query: The query of this QueryRequestSql.  # noqa: E501
        :type query: str
        """
        if self.local_vars_configuration.client_side_validation and query is None:  # noqa: E501
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

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
        if not isinstance(other, QueryRequestSql):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryRequestSql):
            return True

        return self.to_dict() != other.to_dict()