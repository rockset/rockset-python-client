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


class QueryResponse(object):
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
        'query_id': 'str',
        'collections': 'list[str]',
        'results': 'list[object]',
        'stats': 'QueryResponseStats',
        'warnings': 'list[str]',
        'query_lambda_path': 'str',
        'query_errors': 'list[QueryError]',
        'column_fields': 'list[QueryFieldType]',
        'results_total_doc_count': 'int',
        'pagination': 'PaginationInfo',
        'last_offset': 'str'
    }

    attribute_map = {
        'query_id': 'query_id',
        'collections': 'collections',
        'results': 'results',
        'stats': 'stats',
        'warnings': 'warnings',
        'query_lambda_path': 'query_lambda_path',
        'query_errors': 'query_errors',
        'column_fields': 'column_fields',
        'results_total_doc_count': 'results_total_doc_count',
        'pagination': 'pagination',
        'last_offset': 'last_offset'
    }

    def __init__(self, query_id=None, collections=None, results=None, stats=None, warnings=None, query_lambda_path=None, query_errors=None, column_fields=None, results_total_doc_count=None, pagination=None, last_offset=None, _configuration=None):  # noqa: E501
        """QueryResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._query_id = None
        self._collections = None
        self._results = None
        self._stats = None
        self._warnings = None
        self._query_lambda_path = None
        self._query_errors = None
        self._column_fields = None
        self._results_total_doc_count = None
        self._pagination = None
        self._last_offset = None
        self.discriminator = None

        if query_id is not None:
            self.query_id = query_id
        if collections is not None:
            self.collections = collections
        if results is not None:
            self.results = results
        if stats is not None:
            self.stats = stats
        if warnings is not None:
            self.warnings = warnings
        if query_lambda_path is not None:
            self.query_lambda_path = query_lambda_path
        if query_errors is not None:
            self.query_errors = query_errors
        if column_fields is not None:
            self.column_fields = column_fields
        if results_total_doc_count is not None:
            self.results_total_doc_count = results_total_doc_count
        if pagination is not None:
            self.pagination = pagination
        if last_offset is not None:
            self.last_offset = last_offset

    @property
    def query_id(self):
        """Gets the query_id of this QueryResponse.  # noqa: E501

        Unique ID for this query.  # noqa: E501

        :return: The query_id of this QueryResponse.  # noqa: E501
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this QueryResponse.

        Unique ID for this query.  # noqa: E501

        :param query_id: The query_id of this QueryResponse.  # noqa: E501
        :type: str
        """

        self._query_id = query_id

    @property
    def collections(self):
        """Gets the collections of this QueryResponse.  # noqa: E501

        List of collections referenced in the query.  # noqa: E501

        :return: The collections of this QueryResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this QueryResponse.

        List of collections referenced in the query.  # noqa: E501

        :param collections: The collections of this QueryResponse.  # noqa: E501
        :type: list[str]
        """

        self._collections = collections

    @property
    def results(self):
        """Gets the results of this QueryResponse.  # noqa: E501

        Results from the query.  # noqa: E501

        :return: The results of this QueryResponse.  # noqa: E501
        :rtype: list[object]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this QueryResponse.

        Results from the query.  # noqa: E501

        :param results: The results of this QueryResponse.  # noqa: E501
        :type: list[object]
        """

        self._results = results

    @property
    def stats(self):
        """Gets the stats of this QueryResponse.  # noqa: E501

        Meta information about the query including execution latencies.  # noqa: E501

        :return: The stats of this QueryResponse.  # noqa: E501
        :rtype: QueryResponseStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this QueryResponse.

        Meta information about the query including execution latencies.  # noqa: E501

        :param stats: The stats of this QueryResponse.  # noqa: E501
        :type: QueryResponseStats
        """

        self._stats = stats

    @property
    def warnings(self):
        """Gets the warnings of this QueryResponse.  # noqa: E501

        Warnings generated by the query. Only populated if `generate_warnings` is specified in the query request.  # noqa: E501

        :return: The warnings of this QueryResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this QueryResponse.

        Warnings generated by the query. Only populated if `generate_warnings` is specified in the query request.  # noqa: E501

        :param warnings: The warnings of this QueryResponse.  # noqa: E501
        :type: list[str]
        """

        self._warnings = warnings

    @property
    def query_lambda_path(self):
        """Gets the query_lambda_path of this QueryResponse.  # noqa: E501

        The full path of the executed query lambda. Includes version information.  # noqa: E501

        :return: The query_lambda_path of this QueryResponse.  # noqa: E501
        :rtype: str
        """
        return self._query_lambda_path

    @query_lambda_path.setter
    def query_lambda_path(self, query_lambda_path):
        """Sets the query_lambda_path of this QueryResponse.

        The full path of the executed query lambda. Includes version information.  # noqa: E501

        :param query_lambda_path: The query_lambda_path of this QueryResponse.  # noqa: E501
        :type: str
        """

        self._query_lambda_path = query_lambda_path

    @property
    def query_errors(self):
        """Gets the query_errors of this QueryResponse.  # noqa: E501

        Errors encountered while executing the query.  # noqa: E501

        :return: The query_errors of this QueryResponse.  # noqa: E501
        :rtype: list[QueryError]
        """
        return self._query_errors

    @query_errors.setter
    def query_errors(self, query_errors):
        """Sets the query_errors of this QueryResponse.

        Errors encountered while executing the query.  # noqa: E501

        :param query_errors: The query_errors of this QueryResponse.  # noqa: E501
        :type: list[QueryError]
        """

        self._query_errors = query_errors

    @property
    def column_fields(self):
        """Gets the column_fields of this QueryResponse.  # noqa: E501

        Meta information about each column in the result set. Not populated in `SELECT *` queries.  # noqa: E501

        :return: The column_fields of this QueryResponse.  # noqa: E501
        :rtype: list[QueryFieldType]
        """
        return self._column_fields

    @column_fields.setter
    def column_fields(self, column_fields):
        """Sets the column_fields of this QueryResponse.

        Meta information about each column in the result set. Not populated in `SELECT *` queries.  # noqa: E501

        :param column_fields: The column_fields of this QueryResponse.  # noqa: E501
        :type: list[QueryFieldType]
        """

        self._column_fields = column_fields

    @property
    def results_total_doc_count(self):
        """Gets the results_total_doc_count of this QueryResponse.  # noqa: E501

        Number of results generated by the query  # noqa: E501

        :return: The results_total_doc_count of this QueryResponse.  # noqa: E501
        :rtype: int
        """
        return self._results_total_doc_count

    @results_total_doc_count.setter
    def results_total_doc_count(self, results_total_doc_count):
        """Sets the results_total_doc_count of this QueryResponse.

        Number of results generated by the query  # noqa: E501

        :param results_total_doc_count: The results_total_doc_count of this QueryResponse.  # noqa: E501
        :type: int
        """

        self._results_total_doc_count = results_total_doc_count

    @property
    def pagination(self):
        """Gets the pagination of this QueryResponse.  # noqa: E501

        Pagination information. Only populated if `paginate` is specified in the query request.  # noqa: E501

        :return: The pagination of this QueryResponse.  # noqa: E501
        :rtype: PaginationInfo
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this QueryResponse.

        Pagination information. Only populated if `paginate` is specified in the query request.  # noqa: E501

        :param pagination: The pagination of this QueryResponse.  # noqa: E501
        :type: PaginationInfo
        """

        self._pagination = pagination

    @property
    def last_offset(self):
        """Gets the last_offset of this QueryResponse.  # noqa: E501

        If this was a write query, this is the log offset the query was written to  # noqa: E501

        :return: The last_offset of this QueryResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_offset

    @last_offset.setter
    def last_offset(self, last_offset):
        """Sets the last_offset of this QueryResponse.

        If this was a write query, this is the log offset the query was written to  # noqa: E501

        :param last_offset: The last_offset of this QueryResponse.  # noqa: E501
        :type: str
        """

        self._last_offset = last_offset

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
        if issubclass(QueryResponse, dict):
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
        if not isinstance(other, QueryResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryResponse):
            return True

        return self.to_dict() != other.to_dict()
