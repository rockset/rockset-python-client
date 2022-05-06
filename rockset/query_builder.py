"""
DEPRECATION NOTICE: The query builder will not receive updates in the future.
It has been brought over from the old Rockset python client for ease-of-use
but there are no guarantees on it.

Usage
-----

Query module contains a set of APIs that allows you to compose powerful
queries over collections.

This module comprises of two major components:

``Q`` : Query Builder
Used to compose complex and powerful queries.

>>> from rockset import Q
>>> q = Q('hello-world').limit(10)
>>> (sqltxt, sqlargs) = q.sql()
>>> print(sqltxt)
SELECT *
FROM "hello-world"
LIMIT 10
>>>

``F`` : Field Reference
Used to construct field expressions that refer to particular fields within a document.

>>> from rockset import F
>>> (F['answer'] == 42).sqlexpression()
'"answer" = 42'
>>>

Example
-------
::

    from rockset import Client, Q, F

    # connect to Rockset
    rs = Client()

    # fetch user whose "_id" == "u42"
    u = rs.sql(Q('users').where(F["_id"] == "u42"))

    # fetch the 100 oldest users in the 'users' collection
    q = Q('users').highest(100, F["age"])
    old100 = rs.sql(q)

    # find the average rating of all songs by "The Beatles"
    q = Q('songs').where(F["artist"] == "The Beatles").select(F["rating"].avg())
    avg_rating = rs.sql(q)

Query Operators: Overview
-------------------------

.. autofunction:: rockset.Q

* Constructor

  * ``Q``: Specify the collection to be queried

  >>> # return all documents in the logins collection.
  >>> q = Q('logins')

* Filter queries

  * ``where``: Classic selection operator to only return documents that match \
the given criteria. Use ``F`` to construct field expressions to specify the \
selection criteria.

  >>> # return all docs in logins where field "user_id" is equal to "u42"
  >>> q = Q('logins').where(F['user_id'] == 'u42')

* Projection

  * ``select``: Specify the list of desired fields to be returned

  >>> # will return the fields "user_id" and "login_ip" from all docs in logins
  >>> q = Q('logins').select(F['user_id'], F['login_ip'])

* Pagination

  * ``limit`` : Specify limit with skip support

  >>> # return 10 documents from logins after skipping the first 40 results
  >>> q = Q('logins').limit(10, skip=40)

* Sorting

  * ``highest``, ``lowest``: Find the top N or the bottom N

  >>> # will return 10 documents with the most recent "login_time"
  >>> q = Q('logins').highest(10, F['login_time'])

* Aggregation

  * ``aggregate``: Group by and aggregate fields

  >>> # will aggregate all documents in logins by "user_id",
  >>> # and return "user_id", max("login_time") and count(*) after aggregation.
  >>> Q('logins').aggregate(F['user_id'], F['login_time'].max(), F.count())


Query Operator: Filters
-----------------------

=========================
Where operator
=========================
    Syntax:
    ``<Query>.where(<Query>)``

    ``where`` allows you to chain a new query object as a conjuntion.
    In most cases, field reference expressions are sufficient, but
    ``where`` comes in especially handy when you want to sub-select
    documents following another operation such as a sort or an aggregation.

    Examples:
    ::

      # find all "Jim"s who are in the top 100 highest scorers
      Q('players')  \\
      .highest(100, F["score"])  \\
      .where(F["first_name"] == "Jim")

.. automethod:: Query.where

Query Operator: Projection
--------------------------

=========================
Select operator
=========================
    Syntax:
    ``<Query>.select(<field_ref> [, <field_ref> [, ...]])``

    Allows you to specify the fields that you wish to include in the
    query results.

    Examples:
    ::

      Q('authors') \\
      .where(F["last_name"] == "Gray")  \\
      .select(F["first_name"], F["last_name"], F["age"])

.. automethod:: Query.select

Query Operator: Pagination
--------------------------

=========================
Limit operator
=========================
    Syntax:
    ``<Query>.limit(<max_results> [, <skip_count>])``

    Limit operator allows you to perform pagination queries and positional
    filters.

    Examples:
    ::

      # find the "_id" field of the 5 most recently uploaded documents
      # since the default sorting is more recently updated first,
      # this query will simply be:
      Q('uploads').limit(5)

      # fetch a third batch of 100 results, for all users older than 18
      # i.e., skip the first 200 results
      Q('uploads').where(F["age"] >= 18).limit(100, skip=200)

.. automethod:: Query.limit

Query Operator: Sorting
-----------------------

=========================
Highest, Lowest operators
=========================
    Syntax:
    ``<Query>.highest(N, <field_ref> [, <field_ref> [, ...]])``,
    ``<Query>.lowest(N, <field_ref> [, <field_ref> [, ...]])``

    Examples:
    ::

      Q(F["last_name"] == "Gray").highest(5, F["score"], F["first_name"])
      Q(F["last_name"] == "Gray").lowest(10, F["salary"])

.. automethod:: Query.highest
.. automethod:: Query.lowest


Query Operator: JOINs
---------------------

=====
JOINS
=====
    Syntax:
    ``<Query>.join(<Query>, on=<field_ref expression>)``
    ``<Query>.left_outer_join(<Query>, on=<field_ref expression>)``
    ``<Query>.right_outer_join(<Query>, on=<field_ref expression>)``

    Examples:
    ::

      Q('emails') \\
      .join(Q('users'), on=(F['emails']['from'] == F['users']['email']))

      Q('emails', alias='e') \\
      .left_outer_join(Q('users', alias='u'), on=(F['e']['from'] == F['u']['email']))

.. automethod: Query.join
.. automethod: Query.left_outer_join
.. automethod: Query.right_outer_join

Query Operator: Unnest - to expand nested array fields
------------------------------------------------------

================
Unnest operators
================
    Syntax:
    ``<Query>.unnest(<field_ref>)``

    Examples:
    ::

      Q('emails').unnest(F['to'])
      (Q('linkedin_people', 'p')
      .unnest(F['p']['experiences'], alias='exp')
      .where(F['exp']['company_name'] == 'Rockset'))

.. automethod:: Query.unnest


Query Operator: Aggregation
---------------------------

====================================================
Aggregate operator and field ref aggregate functions
====================================================
    Syntax:
    ``<Query>.aggregate(<field_ref> [, <field_ref> [, ...]])``

    Field reference objects can also include any of the following aggregation
    functions:

    * ``min``
    * ``max``
    * ``avg``
    * ``sum``
    * ``count``
    * ``countdistinct``
    * ``approximatecountdistinct``
    * ``collect``

    You can also optionally provide a field name alias in the
    field reference using the ``named`` function. This comes in
    especially handy for the aggregated fields.

    Examples:
    ::

      # find min and max salaries broken down by age
      Q('employees').aggregate(F["age"], F["salary"].min(), F["salary"].max())
      # will return documents such as:
      # {"age", "18", "min(salary)": 50000, "max(salary)": 150000}
      # {"age", "19", "min(salary)": 50000, "max(salary)": 152000}

      # example using field name alias
      Q('employees').aggregate(F["age"], F["salary"].avg().named("avg_salary"))
      # will return documents such as:
      # {"age", "18", "avg_salary": 82732}

.. automethod:: Query.aggregate

.. automethod:: FieldRef.min
.. automethod:: FieldRef.max
.. automethod:: FieldRef.avg
.. automethod:: FieldRef.sum
.. automethod:: FieldRef.count
.. automethod:: FieldRef.countdistinct
.. automethod:: FieldRef.approximatecountdistinct
.. automethod:: FieldRef.collect

--------------

Field Expressions Overview
--------------------------

.. autodata:: rockset.F

* Value comparators

  * ``==``, ``!=``, ``<``, ``<=``, ``>``, ``>=``:

  >>> # match all docs where "first_name" is equal to "Jim"
  >>> F["first_name"] == "Jim"
  >>> # match all docs where "rating" is greater than or equal to 4.5
  >>> F["rating"] >= 4.5
  >>> # match all docs where "title" text is lexographcially greater than "Star Wars"
  >>> F["title"] >= "Star Wars"

* String functions

  * ``startswith``, ``like``: Prefix and classic SQL LIKE expressions

  >>> # match all docs where "title" starts with "Star Wars"
  >>> F["title"].startswith("Stars Wars")
  >>> # match all docs where "title" contains the word "Wars"
  >>> F["title"].like("% Wars %")

* Boolean compositions

  * ``&``, ``|``, ``~``: AND, OR and NOT expressions

  >>> # match all records with "rating" >= 4.5 AND "title" starts with "Star Wars"
  >>> e1 = (F["rating"] >= 4.5) & F["title"].startswith("Star Wars")
  >>> # match all records with "director" == "George Lucas" OR "title" starts with "Star Wars"
  >>> e2 = (F["director"] == 'George Lucas') | F["title"].startswith("Star Wars")
  >>> # match all records that are not included in expressions e1 or e2
  >>> e1e2_complement = ~(e1 | e2)

* IN and EXISTS operators

  * ``exists``: Construct a query of the form ``SELECT ... WHERE <field> IN <subquery>``

  Can also be used to just check if a subquery returns one or more results

  * ``exists``: Construct a query of the form ``SELECT ... WHERE EXISTS (<subquery>)``

  >>> # find records where "source_ip" is one of the "ip"s in "wolves" collection
  >>> e1 = F["source_ip"].exists(Q("wolves").select(F["ip"]))
  >>> # match all such records in the "logins" collection
  >>> q = Q("logins").where(e1)
  >>> # another way to write the same query
  >>> q = (Q("logins")
  >>>         .where(
  >>>             F.exists(
  >>>                 Q("wolves")
  >>>                 .where(F["wolves"]["ip"] = F["logins"]["source_ip"])
  >>>             )
  >>>         )
  >>>     )

* Field aggregations

  * ``avg``, ``collect``, ``count``, ``countdistinct``, ``max``, ``min``, ``sum``

  >>> # count(*)
  >>> F.count()
  >>> # min(login_time)
  >>> F["login_time"].min()
  >>> # max(login_time) as last_login_time
  >>> F["login_time"].max().named('last_login_time')

* Nested documents and arrays

  * ``[]``: The ``[]`` notation can be used to refer to fields within nested documents and arrays.

  * Consider a collection where documents looked like this example below.

  ::

    {
      "_id": {"u42"},
      "name": {
          "first": "James",
          "middle": "Nicholas",
          "last": "Gray" },
      "tags": [
          "ACID",
          "database locking",
          "two phase commits",
          "five-minute rule",
          "data cube",
          "turing award" ]
     }

  * Example field references to access nested documents and arrays:

  >>> # expression to find all documents where field "name" contains a
  >>> # nested field "middle" with value equal to "Nicholas"
  >>> F["name"]["middle"] == "Nicholas"
  >>>
  >>> # similarly, for array fields, you can specify the array offset.
  >>> # expression to find all documents where the first "tags" field
  >>> # is equal to "ACID"
  >>> F["tags"][0] == "ACID"

  * In order to match against any element within an array field, you can use
    Python's empty slice ``[:]`` notation.

  >>> # expression to find all documents where the "tags" array field
  >>> # contains "ACID" as one of the elements
  >>> F["tags"][:] == "ACID"
  >>> # find all documents where one of the "tags" is "turing award"
  >>> F["tags"][:] == "turing award"


Field Expression: Value Comparators
-----------------------------------

=========================
Equality operator: ``==``
=========================
    Supported types: ``int``, ``float``, ``bool``, ``str``

    Syntax:
    ``<field_ref> == <value>``

    Examples:
    ::

      F["first_name"] == "Jim"
      F["year"] == 2017
      F["score"] == 5.0
      F["tags"][:] == 'critical'

===============================================
Value comparators: ``<``, ``<=``, ``>=``, ``>``
===============================================
    Supported types: ``int``, ``float``, ``str``

    Syntax:
    ``<field_ref> < <value>``,
    ``<field_ref> <= <value>``,
    ``<field_ref> >= <value>``,
    ``<field_ref> > <value>``

    Examples:
    ::

      F["year"] < 2000
      F["year"] >= 2007
      F["rating"] >= 4.5
      F["title"] >= "Star Wars"

===============================
Prefix operator: ``startswith``
===============================
    Supported types: ``str``

    Syntax:
    ``<field_ref>.startswith(<prefix>)``

    Examples:
    ::

      F["first_name"].startswith("Ben")

===============================
Like operator: ``like``
===============================
    Supported types: ``str``

    Syntax:
    ``<field_ref>.like(<pattern>)``

    Examples:
    ::

      F["address"].like("%State St%")

===============================
Field alias: ``named``
===============================
    Supported types: All field references

    Syntax:
    ``<field_ref>.named(<new-field-name>)``

    Examples:
    ::

      F["full_name"].named("name")
      F["login_time"].max().named("last_login_time")

===============================
Field existence: ``is_defined``
===============================
    Supported types: All

    Syntax:
    ``<field_ref>.is_defined()``

    Field existence tested with ``<field_ref>.is_defined()`` will match all
    documents where the field is defined, even if it has a null value.

================================
Null comparison: ``is_not_null``
================================
    Supported types: All

    Syntax:
    ``<field_ref>.is_not_null()``

    Field expression ``<field_ref>.is_not_null()`` will match all documents
    where the field is defined and has a non-null value.

.. tip:: There is no ``is_null()`` because of the potential confusion of \
calling ``is_null()`` on an undefined field. Use \
``~<field_ref>.is_not_null()`` or ``<field_ref>.is_defined() & \
~<field_ref>.is_not_null()`` depending on your use case.


Field Expression: Boolean Compositions
--------------------------------------

Three different boolean operators (``&``, ``|``, and ``~``) are
overloaded to allow easy composition of boolean operators.

.. note:: The boolean operators are **NOT** ``and``, ``or``, and ``not``, \
as those are special and cannot be overridden in Python.

==================================
AND operator: ``&`` (intersection)
==================================
    Syntax:
    ``<Query object> & <Query object>``

    Examples:
    ::

      # find all documents where field tags contains the "turing award"
      # and the age is greater than 40
      (F["tags"][:] == "turing award") & (F["age"] > 40)

==========================
OR operator: ``|`` (union)
==========================
    Syntax:
    ``<Query object> | <Query object>``

    Examples:
    ::

      # find all documents where the first_name is "jim"
      # or last_name is "gray"
      (F["first_name"] == "jim") | (F["last_name"] == "gray")

==============================
NOT operator: ``~`` (negation)
==============================
    Syntax:
    ``~<Query object>``

    Examples:
    ::

      # find all documents whose title does not contain the term "confidential"
      ~F["title"][:] == "confidential"


Field Expression: Array operators
---------------------------------

=========================
nested operator
=========================
    syntax:
    ``<field_ref>.nested(<query>)``

    ``nested`` operator makes it easy to work with nested array of documents.

    example:
    ::

        # find all books authored by 'jim gray'
        F["authors"].nested((F["first_name") == "jim") \
& (F["last_name"] == "gray"))

        # find all users who logged in from given ip on june 06, 2006
        F["logins"].nested((F["ipv4"] == "10.6.6.6") \
& (F["login_date"] == "2006-06-06"))

=========================
Unnest operator
=========================
    Syntax:
    ``<field_ref>.unnest(alias=None)``

    ``unnest`` operator should be called only on array fields and will
    return the a query object to represent the SQL expression of
    the form UNNEST(<field_ref>)

    Example:
    ::

        # unnest all authors from the books collection, so that
        # there is a record for every (book x book's author)
        Q("books).join(F["authors"].unnest())

        # find all books authored by 'jim gray'
        (Q("books")
            .join(Q(F["authors"].unnest(), alias="a"))
            .where((F["a"]["first_name"] == "jim") \
& (F["a"]["last_name"] == "gray"))
        )


"""
import copy
import datetime
import json

from rockset.value import decode, py_type


class Query(object):
    def __init__(self, source=None, alias=None, child=None, children=None):
        self._source = source
        if child:
            self._source = child.get_source()

        self._alias = alias
        if child and not self._alias:
            self._alias = child.get_alias()

        if children:
            for c in children:
                if c.get_source() and not self.get_source():
                    self._source = c.get_source()
                if (
                    self.get_source()
                    and c.get_source()
                    and self.get_source() != c.get_source()
                ):
                    raise ValueError(
                        "cannot combine multiple sub-queries "
                        "bound to different target collections. "
                    )

        # if query is bound to a collection, then init FieldRef
        # so one can do q.F['name']
        if self.get_source():
            self.F = FieldRef(source=(self.get_alias() or self.get_source()))
        else:
            self.F = FieldRef()

        # init params to empty map
        self.P = ParamDict()  # params explicitly set by user

    def __and__(self, other):
        if not isinstance(other, Query):
            return NotImplemented
        return AndQuery([self, other])

    def __or__(self, other):
        if not isinstance(other, Query):
            return NotImplemented
        return OrQuery([self, other])

    def __sub__(self, other):
        if not isinstance(other, Query):
            return NotImplemented
        return DifferenceQuery(self, other)

    def __invert__(self):
        return NotQuery(self)

    # property getters
    def get_source(self):
        return self._source

    def get_alias(self):
        return self._alias

    def select(self, *fields):
        """Returns a new query object that when executed will only include
        the list of fields provided as input.

        Args:
            fields (list of FieldRef): fields you wish to select

        Returns:
            Query: new query object that includes the desired field selection
        """
        return SelectQuery(fields, self)

    def where(self, query):
        """Returns a new query object that when executed will only return
        documents that match the current query object AND the query object
        provided as input.

        Args:
            query (Query): the conjunct query object

        Returns:
            Query: new query object that returns documents in
            **self** AND **query**
        """
        return WhereQuery(query, self)

    def highest(self, limit, *fields):
        """Returns a new query object that when executed will sort the results
        from the current query object by the list of fields provided as input
        in descending order and return top N defined by the limit parameter.

        Args:
            limit (int): top N results you wish to fetch
            fields (list of FieldRef): fields you wish to sort
            descending by

        Returns:
            Query: new query object that returns top N descending
        """
        return SortQuery("desc", fields, self).limit(limit)

    def lowest(self, limit, *fields):
        """Returns a new query object that when executed will sort the results
        from the current query object by the list of fields provided as input
        in ascending order and return top N defined by the limit parameter.

        Args:
            limit (int): top N results you wish to fetch
            fields (list of FieldRef): fields you wish to sort
            ascending by

        Returns:
            Query: new query object that returns top N ascending
        """
        return SortQuery("asc", fields, self).limit(limit)

    def aggregate(self, *fields):
        """Returns a new query object that when executed will aggregate
        results from the current query object by the list of fields
        provided as input.

        Field reference objects can include one of the supported aggregate
        functions such as ``max``, ``min``, ``avg``, ``sum``,
        ``count``, ``countdistinct``, ``approximatecountdistinct``, ``collect``
        as follows: ``<field_ref>.max()``, ``<field_ref>.min()``, ... .

        The list of fields provided as input can contain a mix of field
        references that include an aggregate function and field references
        that does not.

        Args:
            fields (list of FieldRef): fields you wish to aggregate by

        Returns:
            Query: new query object that includes the desired field aggregations
        """
        return AggregateQuery(fields, self)

    def join(self, query, on=None, join_type="JOIN"):
        """Returns a new query object that when executed will do an
        INNER JOIN of the current query object with the input query object
        based on the given join predicate.

        Args:
            query (Query): the right hand side of the JOIN
            on (Query): the join predicate expressed as a field expression.
            This field is optional and does not need to provided for a
            CROSS JOIN.

        Returns:
            Query: new query object that incorporates the join
        """
        if not on:
            join_type = "CROSS JOIN"
        return JoinQuery(join_type, query, on, child=self)

    def left_outer_join(self, query, on):
        """Returns a new query object that when executed will do a
        LEFT OUTER JOIN of the current query object with the input query
        object based on the given join predicate.

        Args:
            query (Query): the right hand side of the LEFT OUTER JOIN
            on (Query): the join predicate expressed as a field expression.
            This field is optional and does not need to provided for a
            CROSS PRODUCT JOIN.

        Returns:
            Query: new query object that incorporates the left outer join
        """
        return self.join(query, on, join_type="LEFT OUTER JOIN")

    def right_outer_join(self, query, on):
        """Returns a new query object that when executed will do a
        RIGHT OUTER JOIN of the current query object with the input query
        object based on the given join predicate.

        Args:
            query (Query): the right hand side of the RIGHT OUTER JOIN
            on (Query): the join predicate expressed as a field expression.
            This field is optional and does not need to provided for a
            CROSS PRODUCT JOIN.

        Returns:
            Query: new query object that incorporates the right outer join
        """
        return self.join(query, on, join_type="RIGHT OUTER JOIN")

    def unnest(self, field, field_alias=None, alias=None):
        """Returns a new query object that when executed will unnest the
        specified array field present in the results of the current
        query object.

        Args:
            field (FieldRef): array field that you wish to unnest
            field_alias (str): This field is required if the specified
            array field holds an array of scalar values. This field is
            optional if the specified array field holds an array of objects.
            alias (str): subquery alias name for the unnested fields.
            This field is optional and defaults to the input array field name.

        Returns:
            Query: new query object for the unnested query
        """
        return UnnestQuery(field, self, field_alias=field_alias, alias=alias)

    def limit(self, limit, skip=0):
        """Returns a new query object that when executed will only return
        a subset of the results. The query when executed will return no more
        than ``limit`` results after skipping the first ``skip`` number of
        results. The limit operator is most commonly used for pagination.

        Args:
            limit (int): maximum number of results to return
            skip (int): the number of results to skip

        Returns:
            Query: new query object that only returns the desired subset
        """
        return LimitQuery(limit=limit, skip=skip, child=self)

    def __str__(self):
        try:
            return self.sql()[0]
        except NotImplementedError:
            return repr(self)

    def sqlprepare(self, sqlsel):
        """Returns an SQLSelect object, which can be used to build
        the SQL version of the query.
        """
        return sqlsel

    def sqlbuild(self, sqlsel):
        """Returns an SQLSelect object, which can be used to generate
        the SQL text for the query.
        """
        raise NotImplementedError(
            "Class {} does not implement sqlbuild()".format(type(self))
        )

    def sqlexpression(self, **kwargs):
        """Returns a text SQL fragment for the underlying query expression."""
        raise NotImplementedError(
            "Class {} does not implement sqlexpression()".format(type(self))
        )

    def sql(self, **kwargs):
        """Returns a tuple of (SQL, params) for the underlying query
        expression.
        """
        # step 1: prepare and get all sql params
        params = ParamDict()
        params.update(self.P)
        sqlsel = self.sqlprepare(SQLSelect(params=params))
        sqlsel.P.update(self.P)  # merge with user set params

        # step 2: build the SQL expression into sqlsel
        sqlsel = self.sqlbuild(sqlsel)

        # step 3:
        # translate sqlsel into sql text and return sql params from step 1
        return (sqlsel.sqlexpression(**kwargs), sqlsel.P)


def _sqlexp(s, delim=" ", **kwargs):
    s = decode(s)
    if isinstance(s, list) or isinstance(s, tuple):
        return delim.join([_sqlexp(x, **kwargs) for x in s])
    if isinstance(s, set):
        return delim.join(sorted(set([_sqlexp(x, **kwargs) for x in s])))
    if isinstance(s, (bool, int, float)):
        return str(s)
    if isinstance(s, str):
        return json.dumps(s)
    if isinstance(s, slice):
        return Symbol("[*]")
    if isinstance(s, (datetime.datetime, datetime.date, datetime.time)):
        return s.isoformat()
    if isinstance(s, datetime.timedelta):
        return str(s.total_seconds())
    if isinstance(s, SubQuery):
        kwargs["level"] = kwargs.get("level", 0) + 1
    return s.sqlexpression(**kwargs)


def _sqlprep(sqlsel, *args, **kwargs):
    for arg in args:
        if not hasattr(arg, "sqlprepare"):
            continue
        if not callable(arg.sqlprepare):
            continue
        sqlsel = arg.sqlprepare(sqlsel)
    return sqlsel


def _escape_chars(v, chars=set()):
    for c in set(chars):
        v = v.replace(c, r"\{}".format(c))
    return v


class SQLSelect(object):
    def __init__(self, params=None, default_alias=None):
        self._select_list = []
        self._from_list = []
        self._join_list = []
        self._where_list = []
        self._groupby_list = []
        self._orderby_list = []
        self._limit = None
        self._skip = None
        self._build_order = 0
        self.P = params or ParamDict()
        self._default_alias = default_alias or "subq"
        self._sqltext = None

    def default_alias(self):
        """return a best guess alias for the current SELECT statement.
        used when the current SELECT statement suddently gets wrapped
        as a sub-query and the new sub-query needs an alias
        """
        return self._default_alias

    def _set_build_order(self, build_order):
        if self._build_order < build_order:
            self._build_order = build_order
        return self

    def _enforce_build_order(self, build_order, coalesce=False):
        """use to automatically nest and build inner subquery in
        cases such as Q().aggregate().limit().where()
        """
        if self._build_order < build_order:
            return self._set_build_order(build_order)
        if coalesce and self._build_order == build_order:
            return self
        return (
            SQLSelect(params=self.P, default_alias=self.default_alias())
            .add_from(
                [Symbol("("), self, Symbol(")"), Symbol(" as "), self.default_alias()],
                alias=self.default_alias(),
            )
            ._set_build_order(build_order)
        )

    def add_select(self, *f):
        # allow select from any order, so default to current
        build_order = self._build_order
        # unless select list is non-empty, then force a nested sub query
        if len(self._select_list) > 0:
            build_order = 0
        # if sqltext was initialized, then force a nested sub query too
        if build_order == 99:
            build_order = 0
        this = self._enforce_build_order(build_order, coalesce=True)
        this._select_list += f
        return this

    def add_from(self, t, alias=None):
        if alias:
            self._default_alias = alias
        this = self._enforce_build_order(1)
        this._from_list += [t]
        return this

    def add_join(self, r, p=None, join_type="JOIN"):
        this = self._enforce_build_order(1, coalesce=True)
        this._join_list.append((Symbol(join_type), r, p))
        return this

    def add_cross_join(self, r):
        return self.add_join(r, p=None, join_type="CROSS JOIN")

    def add_left_outer_join(self, r, p):
        return self.add_join(r, p, join_type="LEFT OUTER JOIN")

    def add_where(self, *op):
        this = self._enforce_build_order(2, coalesce=True)
        this._where_list += op
        return this

    def add_groupby(self, *f):
        this = self._enforce_build_order(3)
        this._groupby_list += f
        return this

    def add_orderby(self, mode, *fields):
        this = self._enforce_build_order(4)
        this._orderby_list += [(field, Symbol(mode)) for field in fields]
        return this

    def add_limit(self, limit, skip=0):
        this = self._enforce_build_order(5)
        this._limit = limit
        this._skip = skip
        return this

    def add_sqltext(self, sqltext, alias):
        if self._build_order != 0:
            raise ValueError("SQL text not supported in this mode")
        this = self._enforce_build_order(99)
        this._sqltext = Symbol(sqltext)
        if alias:
            this._default_alias = alias
        return this

    def sqlexpression(self, **kwargs):
        if self._sqltext:
            return _sqlexp(self._sqltext, **kwargs)

        linesep = "\n" + (" " * kwargs.get("level", 0) * 7)
        ret = ""
        select_list = self._select_list or [F]
        ret += "SELECT {} ".format(_sqlexp(select_list, delim=", ", **kwargs))
        if self._from_list:
            ret += linesep
            ret += "  FROM {} ".format(_sqlexp(self._from_list, delim=", ", **kwargs))
        if self._join_list:
            ret += linesep
            for (join_type, relation, predicate) in self._join_list:
                ret += "    {} {} ".format(
                    _sqlexp(join_type, **kwargs), _sqlexp(relation, **kwargs)
                )
                if predicate:
                    ret += " ON {} ".format(_sqlexp(predicate, **kwargs))
        if self._where_list:
            ret += linesep
            ret += " WHERE {} ".format(
                _sqlexp(self._where_list, delim=" AND ", **kwargs)
            )
        if self._groupby_list:
            ret += linesep
            ret += " GROUP BY {} ".format(
                _sqlexp(self._groupby_list, delim=", ", **kwargs)
            )
        if self._orderby_list:
            ret += linesep
            ret += " ORDER BY {} ".format(
                _sqlexp(self._orderby_list, delim=", ", **kwargs)
            )
        if self._limit:
            ret += linesep
            ret += " LIMIT {} ".format(_sqlexp(self._limit, **kwargs))
            if self._skip:
                ret += " OFFSET {} ".format(_sqlexp(self._skip, **kwargs))
        return ret

    def __str__(self):
        return self.sqlexpression()


def _QueryString(qs, alias):
    # detect if input string is collection-path, collection-name or SQL
    if len(qs.strip().split()) == 1:
        if "." not in qs:
            # case 1: exactly one token without a path delimiter means it is a resource name
            return QueryStringResource(qs.strip(), alias=alias)
        else:
            # case 2: exactly one token with path delimiters means it is a collection path
            # the collection path can have multiple nested workspaces
            # so a.b.c.d will be: collection name = d, workspaces = [a, b, c]
            parts = qs.strip().split(".")
            workspaces, resource = parts[:-1], parts[-1]

            return QueryStringResource(resource, alias=alias, workspaces=workspaces)
    else:
        # case 3: not s-expr, not resource name -> assume SQL
        return QueryStringSQLText(qs, alias=alias)


class QueryStringResource(Query):
    def __init__(self, qs, alias=None, workspaces=[]):
        self._resource = qs
        alias = alias or qs
        # Plural workspaces because we can have nested workspaces.
        self._workspaces = workspaces
        super(QueryStringResource, self).__init__(source=qs, alias=alias)

    def sqlbuild(self, sqlsel):
        return sqlsel.add_from(self, self.get_alias())

    def sqlexpression(self, **kwargs):
        return _sqlexp(
            [*self._workspaces, self._resource], delim=".", **kwargs
        ) + _sqlexp([Symbol(" as "), self.get_alias()], delim="", **kwargs)


class QueryStringSQLText(Query):
    def __init__(self, sqltext, alias=None):
        self._sqltext = sqltext
        super(QueryStringSQLText, self).__init__(alias=alias)

    def sqlbuild(self, sqlsel):
        return sqlsel.add_sqltext(self._sqltext, self.get_alias())


class SubQuery(Query):
    def __init__(self, child, alias=None):
        if not isinstance(child, Query):
            raise TypeError("invalid query type " + type(child))
        super(SubQuery, self).__init__(child=child, alias=alias)
        self.child = child
        self.alias = alias

    def sqlprepare(self, sqlsel):
        return _sqlprep(sqlsel, self.child)

    def sqlbuild(self, sqlsel):
        alias = self.alias
        self.alias = self.alias or "subq"
        sqltxt = self.sqlexpression()
        self.alias = alias
        return sqlsel.add_from(Symbol(sqltxt), alias)

    def sqlexpression(self, **kwargs):
        sqlsel = SQLSelect(params=self.P, default_alias=self.alias)
        sqlsel = self.child.sqlbuild(sqlsel)
        t = [
            Symbol("\n" + " " * ((kwargs.get("level", 0) * 7) - 1) + "("),
            sqlsel,
            Symbol(")"),
        ]
        if self.alias:
            t += [Symbol("as"), self.alias]
        return _sqlexp(t, **kwargs)


class MultiTermQuery(Query):
    def __init__(self, children=[], **kwargs):
        super(MultiTermQuery, self).__init__(children=children, **kwargs)
        self.children = children

    def sqlprepare(self, sqlsel):
        return _sqlprep(sqlsel, *self.children)


class AndQuery(MultiTermQuery):
    def __and__(self, other):
        if isinstance(other, AndQuery):
            children = self.children + other.children
            if len(children) == 1:
                return children.pop()
            return AndQuery(children)
        if not isinstance(other, Query):
            return NotImplemented
        if len(self.children) == 0:
            return other
        return AndQuery(self.children + [other])

    def sqlexpression(self, **kwargs):
        return _sqlexp(self.children, delim=" AND ", **kwargs)


class OrQuery(MultiTermQuery):
    def __or__(self, other):
        if isinstance(other, OrQuery):
            children = self.children + other.children
            if len(children) == 1:
                return children.pop()
            return OrQuery(children)
        if not isinstance(other, Query):
            return NotImplemented
        if len(self.children) == 0:
            return other
        return OrQuery(self.children + [other])

    def sqlexpression(self, **kwargs):
        return _sqlexp(self.children, delim=" OR ", **kwargs)


class NotQuery(Query):
    def __init__(self, negated):
        super(NotQuery, self).__init__(child=negated)
        self.negated = negated

    def __invert__(self):
        return self.negated

    def sqlprepare(self, sqlsel):
        return _sqlprep(sqlsel, self.negated)

    def sqlexpression(self, **kwargs):
        return _sqlexp(
            [Symbol("NOT"), Symbol("("), self.negated, Symbol(")")], **kwargs
        )


class DifferenceQuery(Query):
    def __init__(self, base, diminisher):
        super(DifferenceQuery, self).__init__(child=base)
        self.base = base
        self.diminisher = diminisher


def checked_decode(x, ty=None):
    x = decode(x)
    if ty:
        assert isinstance(x, ty)
    return x


class FieldOpQuery(Query):
    def __init__(self, field, v, sqlop):
        super(FieldOpQuery, self).__init__()
        self.field = _fref(field)
        self.value = v
        if isinstance(v, (BaseRef, Query)):
            self.value_p = v
        else:
            self.value_p = Literal(v)
        self.sqlop = sqlop
        self.nested_field_expr = self._init_nested_field_op_query()

    def _init_nested_field_op_query(self):
        if not self.field._is_array_field():
            return None
        # turn F['foo'][:]['bar'][:]['baz'] == 10
        # into F['foo'].nested(F['bar'].nested(F['baz'] == 10))
        fparts = self._split_array_path(self.field)
        fop_q = FieldOpQuery(fparts.pop(), self.value_p, self.sqlop)
        for fpart in reversed(fparts):
            fop_q = fpart.nested(fop_q)
        return fop_q

    def _split_array_path(self, field):
        parts = []
        tp = FieldRef()
        for fp in field._path():
            if isinstance(fp, slice):
                parts.append(tp)
                tp = FieldRef()
                continue
            tp = tp[fp]
        parts.append(tp)
        return parts

    def sqlprepare(self, sqlsel):
        sqlsel = _sqlprep(sqlsel, self.field, self.value)
        """
        FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME

        Disabling auto-params feature for now.
        Remove this once issue #1506 is fixed.

        FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME FIXME

        if not isinstance(self.value, (BaseRef, Query)):
            # replace value with param ref, stash the value in sqlsel
            pname = sqlsel.P.new_param(self.field)
            sqlsel.P[pname] = self.value
            self.value_p = ParamRef(pname)
        """
        return sqlsel

    def sqlexpression(self, **kwargs):
        if self.nested_field_expr:
            return _sqlexp(self.nested_field_expr, **kwargs)
        return _sqlexp([self.field, Symbol(self.sqlop), self.value_p], **kwargs)


class FieldEqQuery(FieldOpQuery):
    def __init__(self, field, v):
        if isinstance(v, (type(None), dict, list)):
            raise TypeError(
                "Invalid FieldRef op / type combination: {}, {}".format(
                    "==",
                    type(v),
                )
            )
        super(FieldEqQuery, self).__init__(field, v, "=")


def _make_ne(field, v):
    return NotQuery(FieldEqQuery(field, v))


class FieldIntOpQuery(FieldOpQuery):
    def __init__(self, field, v, sqlop):
        super(FieldIntOpQuery, self).__init__(field, checked_decode(v, int), sqlop)


class FieldFloatOpQuery(FieldOpQuery):
    def __init__(self, field, v, sqlop):
        super(FieldFloatOpQuery, self).__init__(field, checked_decode(v, float), sqlop)


class FieldStringOpQuery(FieldOpQuery):
    def __init__(self, field, v, sqlop):
        super(FieldStringOpQuery, self).__init__(field, checked_decode(v, str), sqlop)


class FieldDateTimeOpQuery(FieldOpQuery):
    def __init__(self, field, v, sqlop):
        dt_types = (datetime.datetime, datetime.date, datetime.time, datetime.timedelta)
        super(FieldDateTimeOpQuery, self).__init__(
            field, checked_decode(v, dt_types), sqlop
        )


class FieldBaseRefOpQuery(FieldOpQuery):
    def __init__(self, field, v, sqlop):
        super(FieldBaseRefOpQuery, self).__init__(
            field, checked_decode(v, BaseRef), sqlop
        )


class FieldLikeQuery(FieldOpQuery):
    def __init__(self, field, v):
        # v could be str or Literal
        v = decode(v)
        super().__init__(field, v, "LIKE")


class FieldPrefixQuery(FieldOpQuery):
    def __init__(self, field, v):
        # v could be str or Literal
        v = decode(v)

        # need to escape '%_' since sql query is re-written with LIKE
        if isinstance(v, str):
            v = _escape_chars(v, "%_")
            v = v + "%"
        elif isinstance(v, Literal):
            v = Literal(_escape_chars(v.value, "%_"))
            v = Literal(v.value + "%")

        super(FieldPrefixQuery, self).__init__(field, v, "LIKE")


class FieldUnaryOpQuery(Query):
    def __init__(self, field, pre_sqlop=None, post_sqlop=None):
        super(FieldUnaryOpQuery, self).__init__()
        self.field = _fref(field)
        self.pre_sqlop = pre_sqlop
        self.post_sqlop = post_sqlop

    def sqlprepare(self, sqlsel):
        return _sqlprep(sqlsel, self.field)

    def sqlexpression(self, **kwargs):
        exp = []
        self.pre_sqlop and exp.append(Symbol(self.pre_sqlop))
        exp.append(self.field)
        self.post_sqlop and exp.append(Symbol(self.post_sqlop))
        return _sqlexp(exp, **kwargs)


class FieldIsNullQuery(FieldUnaryOpQuery):
    def __init__(self, field):
        super(FieldIsNullQuery, self).__init__(field, post_sqlop="IS NULL")


class FieldIsNotNullQuery(FieldUnaryOpQuery):
    def __init__(self, field):
        super(FieldIsNotNullQuery, self).__init__(field, post_sqlop="IS NOT NULL")


class FieldIsDefinedQuery(FieldUnaryOpQuery):
    def __init__(self, field):
        super(FieldIsDefinedQuery, self).__init__(field)

    def sqlexpression(self, **kwargs):
        return _sqlexp(
            FieldIsNotNullQuery(self.field)
            & FieldOpQuery(self.field, Symbol("NULL_VALUE"), "IS DISTINCT FROM"),
            **kwargs
        )


class FieldExistsQuery(Query):
    def __init__(self, inner_query):
        super(FieldExistsQuery, self).__init__()
        self.inner_query = SubQuery(inner_query)

    def sqlprepare(self, sqlsel):
        return _sqlprep(sqlsel, self.inner_query)

    def sqlexpression(self, **kwargs):
        return _sqlexp([Symbol("EXISTS"), self.inner_query])


class FieldIsInQuery(FieldOpQuery):
    def __init__(self, field, inner_query):
        inner_query = SubQuery(inner_query)
        super(FieldIsInQuery, self).__init__(field, inner_query, "IN")


class FieldNestedQuery(FieldExistsQuery):
    def __init__(self, field, field_alias, nested_query, alias):
        field_unnest = _fref(field).unnest(field_alias)
        alias = alias or "uq"
        inner_query = (
            Q(field_unnest, alias=alias).where(nested_query).select(Literal(1))
        )
        super(FieldNestedQuery, self).__init__(inner_query)


class AggregateQuery(Query):
    def __init__(self, fields, child):
        super(AggregateQuery, self).__init__(child=child)
        self.dimension_fields = []
        self.aggregate_fields = []
        for f in fields:
            fr = _fref(f)
            if isinstance(fr, AggFieldRef):
                self.aggregate_fields += [fr]
            else:
                self.dimension_fields += [fr]
        self.child = child

    def sqlprepare(self, sqlsel):
        all_fields = self.dimension_fields + self.aggregate_fields
        return _sqlprep(sqlsel, self.child, *all_fields)

    def sqlbuild(self, sqlsel):
        all_fields = self.dimension_fields + self.aggregate_fields
        sqlsel = self.child.sqlbuild(sqlsel)
        sqlsel = sqlsel.add_select(*all_fields)
        sqlsel = sqlsel.add_groupby(*self.dimension_fields)
        return sqlsel


class SortQuery(Query):
    def __init__(self, mode, fields, child):
        super(SortQuery, self).__init__(child=child)
        self.mode = mode
        self.fields = [_fref(f) for f in fields]
        self.child = child

    def sqlprepare(self, sqlsel):
        return _sqlprep(sqlsel, self.child, *self.fields)

    def sqlbuild(self, sqlsel):
        sqlsel = self.child.sqlbuild(sqlsel)
        return sqlsel.add_orderby(self.mode, *self.fields)


class LimitQuery(Query):
    def __init__(self, limit, skip, child):
        super(LimitQuery, self).__init__(child=child)
        self.max_results = limit
        self.skip_results = skip
        self.child = child

    def sqlprepare(self, sqlsel):
        return _sqlprep(sqlsel, self.child, self.max_results, self.skip_results)

    def sqlbuild(self, sqlsel):
        sqlsel = self.child.sqlbuild(sqlsel)
        return sqlsel.add_limit(limit=self.max_results, skip=self.skip_results)


class JoinQuery(Query):
    def __init__(self, join_type, query, on, child):
        super(JoinQuery, self).__init__(child=child)
        self.join_type = join_type
        # see if we need to wrap the right side of the join in a SubQuery
        if isinstance(query, QueryStringResource):
            # right side is just a collection
            self.right_query = query
        else:
            # right side is complicated ... wrap SubQuery with same alias
            self.right_query = SubQuery(query, alias=query.get_alias())
        self.join_predicate = on
        self.child = child

    def sqlbuild(self, sqlsel):
        sqlsel = self.child.sqlbuild(sqlsel)
        return sqlsel.add_join(self.right_query, self.join_predicate, self.join_type)


class UnnestQuery(Query):
    def __init__(self, field, child, alias=None, field_alias=None):
        alias = alias or list(field)[-1]
        super(UnnestQuery, self).__init__(child=child, alias=alias)
        self.field_unnest = _fref(field).unnest(field_alias)
        self.child = child

    def sqlbuild(self, sqlsel):
        sqlsel = self.child.sqlbuild(sqlsel)
        uf = [self.field_unnest, Symbol("as"), self.get_alias()]
        return sqlsel.add_cross_join(uf)


class SelectQuery(Query):
    def __init__(self, fields, child):
        super(SelectQuery, self).__init__(child=child)
        if not isinstance(child, Query):
            return NotImplemented
        self.fields = [_fref(f) for f in fields]
        self.child = child

    def sqlprepare(self, sqlsel):
        return _sqlprep(sqlsel, self.child, *self.fields)

    def sqlbuild(self, sqlsel):
        sqlsel = self.child.sqlbuild(sqlsel)
        return sqlsel.add_select(*self.fields)


class WhereQuery(Query):
    def __init__(self, pred, child):
        super(WhereQuery, self).__init__(child=child)
        if not isinstance(child, Query) or not isinstance(pred, Query):
            return NotImplemented
        self.pred = pred
        self.child = child

    def sqlprepare(self, sqlsel):
        return _sqlprep(sqlsel, self.child, self.pred)

    def sqlbuild(self, sqlsel):
        sqlsel = self.child.sqlbuild(sqlsel)
        return sqlsel.add_where(self.pred)


def _fref(f):
    if isinstance(f, BaseRef):
        return f
    if type(f) is str:
        return FieldRef()[f]
    return NotImplemented


class BaseRef(object):
    def sqlexpression(self, **kwargs):
        raise NotImplementedError(
            "Class {} does not implement sqlexpression()".format(type(self))
        )


class Symbol(BaseRef):
    def __init__(self, v):
        self.value = v

    def __str__(self):
        return str(self.value)

    def sqlexpression(self, **kwargs):
        return self.value


class Literal(BaseRef):
    def __init__(self, v):
        self.value = v

    def sqlexpression(self, **kwargs):
        if isinstance(self.value, str):
            return "'{}'".format(self.value.replace("'", "''"))
        elif isinstance(self.value, datetime.datetime):
            if self.value.tzinfo is None:
                return "DATETIME '{}'".format(_sqlexp(self.value))
            else:
                return "TIMESTAMP '{}'".format(_sqlexp(self.value))
        elif isinstance(self.value, datetime.date):
            return "DATE '{}'".format(_sqlexp(self.value))
        elif isinstance(self.value, datetime.time):
            return "TIME '{}'".format(_sqlexp(self.value))
        elif isinstance(self.value, datetime.timedelta):
            return "INTERVAL '{}' SECOND".format(_sqlexp(self.value))

        return _sqlexp(self.value)


class FieldPathPartRef(BaseRef):
    def __init__(self, fp, level=0):
        self.fp = fp
        self.level = level

    def sqlexpression(self, **kwargs):
        if self.level == 0:
            ret = [self.fp]
        elif isinstance(self.fp, slice):
            ret = [Symbol(".*")]
        elif isinstance(self.fp, int):
            ret = [Symbol("[{}]".format(self.fp))]
        else:
            ret = [Symbol("."), self.fp]
        return _sqlexp(ret, delim="", **kwargs)


class FieldRef(BaseRef):
    def __init__(self, name=None, parent=None, source=None):
        if isinstance(name, slice):
            if not (name.start is None and name.stop is None and name.step is None):
                raise ValueError('Only empty slices (":") are supported')
        elif isinstance(name, str):
            if name == "*":
                name = slice(None)
        elif isinstance(name, int):
            pass
        elif name is None:
            assert parent is None
            pass
        else:
            raise TypeError("Invalid FieldRef type " + type(name))

        # if parent is None it means that name also needs to be None
        assert parent is not None or name is None

        self._name = name
        self._parent = parent
        self._source = source
        self._alias = None

    def __getitem__(self, name):
        if isinstance(name, FieldRef):
            this = self
            for fp in name._path():
                this = FieldRef(fp, this)
        else:
            this = FieldRef(name, self)
        return this

    def __getattr__(self, name):
        if name.startswith("_"):
            raise AttributeError("Field reference has no attribute {}", name)
        return FieldRef(name, self)

    def __iter__(self):
        for part in self._path():
            if isinstance(part, slice):
                yield "*"
                continue
            yield part

    def _concat(self, suffix):
        self._name += suffix

    def _path(self):
        r = self
        p = []
        while r._parent is not None:
            p.append(r._name)
            r = r._parent
        p.reverse()
        return p

    def _is_simple_field_lookup(self):
        return isinstance(self._name, str) and len(self._path()) == 1

    def _is_root_field(self):
        if self._name is None and self._parent is None:
            return True
        if isinstance(self._name, slice) and self._parent is not None:
            return self._parent._is_root_field()
        return False

    def _is_array_field(self):
        return "*" in list(self)

    def _get_source(self):
        if self._parent:
            return self._parent._get_source()
        return self._source

    def named(self, alias):
        self._alias = alias
        return self

    def min(self):
        """Returns a new FieldRef that represents a MIN() aggregation
        of the given field.

        Returns:
           AggFieldRef: FieldRef object that represents the desired ``min``
           aggregation.
        """
        return AggFieldRef("MIN", self)

    def max(self):
        """Returns a new FieldRef that represents a MAX() aggregation
        of the given field.

        Returns:
           AggFieldRef: FieldRef object that represents the desired ``max``
           aggregation.
        """
        return AggFieldRef("MAX", self)

    def avg(self):
        """Returns a new FieldRef that represents an AVG() aggregation
        of the given field.

        Returns:
           AggFieldRef: FieldRef object that represents the desired ``avg``
           aggregation.
        """
        return AggFieldRef("AVG", self)

    def sum(self):
        """Returns a new FieldRef that represents a SUM() aggregation
        of the given field.

        Returns:
           AggFieldRef: FieldRef object that represents the desired ``sum``
           aggregation.
        """
        return AggFieldRef("SUM", self)

    def count(self):
        """Returns a new FieldRef that represents a COUNT() aggregation
        of the given field.

        When called from a field, say F['username'].count(), then the
        SQL expression generated will be of the following form, which when
        executed will return the number of rows where "username" IS NOT NULL:

            COUNT("username")

        When called on the root field, say F.count(), then the SQL expression
        generated will be of the form:

            COUNT(*)

        Returns:
          AggFieldRef: FieldRef object that represents the desired ``count``
          aggregation.
        """
        return AggFieldRef("COUNT", self, allow_root=True, root_field=FieldRef())

    def countdistinct(self):
        """Returns a new FieldRef that represents COUNT(DISTINCT <field_ref>)
        aggregation of the given field.

        Returns:
          AggFieldRef: FieldRef object that represents the desired
          ``countdistinct`` aggregation.
        """
        return AggFieldRef("COUNT", [Symbol("DISTINCT"), self])

    def array_agg(self):
        """Returns a new FieldRef that represents a ARRAY_AGG()
        aggregation of the given field.

        Returns:
          AggFieldRef: FieldRef object that represents the desired
          ``collect`` aggregation.
        """
        return AggFieldRef("ARRAY_AGG", self)

    def map_agg(self, fvalue):
        """Returns a new FieldRef that represents a MAP_AGG() such that
        MAP_AGG(key=<self>, value=<fvalue>) aggregation of the given fields.

        Returns:
          AggFieldRef: FieldRef object that represents the desired
          ``collect`` aggregation.
        """
        return AggFieldRef("MAP_AGG", [self, Symbol(","), fvalue])

    def exists(self, inner_query):
        """Returns a new query object that represents a SQL expression
        as an IN clause or an EXISTS clause.

        If the current field ref is just ``F`` and represents the root field,
        then the SQL expression will be of the form:

            EXISTS (<inner_query>)

        If the current field ref represents a field within the collection,
        then the SQL expression will be of the form:

            <field_ref> IN (<inner_query>)

        Example usage:

            Q("logins").where(F["source_ip"].exists(Q("wolves").select(F["ip"])))

            will construct the following SQL:

            SELECT *
            FROM   "logins"
            WHERE  "source_ip" IN (SELECT "ip" FROM "wolves")

        Args:
            inner_query (Query): query object that represents the nested subquery

        Returns:
            Query: query object that represents the desired SQL expression
        """
        if self._is_root_field():
            return FieldExistsQuery(inner_query)
        return FieldIsInQuery(self, inner_query)

    def nested(self, nested_query, field_alias=None, alias=None):
        """ Returns a new query object that matches all documents
        where the given inner query matches on one or more individual
        nested documents present within the field path of the given field.

        Useful to run complex query expressions on fields that contain
        an nested array of documents.

        Example:
          Say you have a collection where every document describes a book,
          and each document has an "authors" field that is a nested array of
          documents describing each author::

            {"title": "Transaction Processing: Concepts and Techniques",
             "authors": [
                 {"first_name": "Jim", "last_name": "Gray"},
                 {"first_name": "Andreas", "last_name": "Reuter"},
             ],
             "publisher": ... }

        If you want to do find all books where 'Jim Gray' was one of the
        authors, you can use the following query::

            F["authors"].nested((F["first_name"] == 'Jim') \
& (F["last_name"] == 'Gray'))

        Note: Constructing the same query as follows is incorrect::

            # CAUTION: This is not same as the query above
            (F["authors"][:]["first_name"] == 'Jim') \
& (F["authors"][:]["last_name"] == 'Gray')

        The incorrect version will return all books which has at least one
        author with first name 'Jim' and at least one author with last name
        'Gray', but it need not be the same author. A book with two authors
        named 'Jim Smith' and 'Alice Gray' will also match, which is not what
        is intended.

        Args:
            nested_query (Query): query expression to run on every nested \
            document present within the given field path

        Returns:
            Query: query object that represents desired nested operations
        """
        return FieldNestedQuery(self, field_alias, nested_query, alias)

    def unnest(self, alias=None):
        """Returns a new query object that represents a SQL expression
        of the form:

            UNNEST(<field_ref>)

            or, when alias is not None

            UNNEST(<field_ref> as <alias>)

        Example usage:

            Q("books").join(F["authors"].unnest())

            will construct the following SQL:

            SELECT *
            FROM   "books" CROSS JOIN UNNEST("books"."authors")

        Args:
            alias (str): Required when the fied ref is an array of scalars
            such as ['vacation', 'beach', 'sand', 'dog']
            Not required if the field is an array of objects.

        Returns:
            Query: query object that represents the desired UNNEST() expression
        """
        resource = "{}".format(_sqlexp(self))
        if alias:
            resource += " as {}".format(_sqlexp(alias))
        return Symbol("UNNEST({})".format(resource))

    def sqlexpression(self, **kwargs):
        # for root_fields just use '*'
        # eg: SELECT count(*) FROM employees;
        terms = []
        if self._get_source():
            terms += [self._get_source(), Symbol(".")]
        if self._is_root_field():
            terms += [Symbol("*")]
        else:
            terms += [FieldPathPartRef(p, i) for i, p in enumerate(self._path())]
        if self._alias:
            terms += [Symbol(" as "), self._alias]
        return _sqlexp(terms, delim="", **kwargs)

    def __str__(self):
        try:
            return self.sqlexpression()
        except NotImplementedError:
            return repr(self)


class AggFieldRef(BaseRef):
    def __init__(self, agg_op, field, allow_root=False, root_field=None):
        self._field = field
        self._aggregate_op = agg_op
        self._alias = None
        if (
            not allow_root
            and hasattr(field, "_is_root_field")
            and field._is_root_field()
        ):
            raise ValueError(
                "aggregation function {} is not allowed on "
                "the root field reference".format(agg_op)
            )
        if allow_root and field._is_root_field() and root_field is not None:
            self._field = root_field

    def __str__(self):
        try:
            return self.sqlexpression()
        except NotImplementedError:
            return repr(self)

    def named(self, alias):
        self._alias = alias
        return self

    def sqlexpression(self, **kwargs):
        t = [Symbol(self._aggregate_op), Symbol("("), self._field, Symbol(")")]
        if self._alias:
            t += [Symbol(" as "), self._alias]
        return _sqlexp(t, delim="", **kwargs)


def _gen_param_name(field):
    if isinstance(field, FieldRef):
        fpath = list(field)
        fpath.reverse()
    elif isinstance(field, str):
        fpath = [field]
    else:
        raise TypeError('invalid field type "{}"'.format(type(field)))
    fname = None
    for fname in fpath:
        if isinstance(fname, int) or (fname == "*") or (fname == ""):
            continue
        # found a good fname in fpath to seed new param; bail
        break

    # a is for apple, p is for param
    fname = fname or "p"
    # replace all non alphanumeric with '_'
    fname = [c.isalnum() and c or "_" for c in fname]
    # strip all consecutive '_' with a single '_'
    fname = [
        c
        for i, c in enumerate(fname)
        if ((i == 0) or (c != "_") or (fname[i] != fname[i - 1]))
    ]
    fname = "".join(fname)
    return fname


class ParamRef(BaseRef):
    def __init__(self, name=""):
        self._name = name
        self._pname = _gen_param_name(name)

    def _symbol(self):
        return ":" + self._pname

    def __getitem__(self, name):
        if self._name != "":
            raise ValueError("nested parameters are not supported")
        return ParamRef(name)

    def __setitem__(self, name, value):
        raise ValueError("cannot assign values to ParamRef. " "use ParamDict instead")

    def __str__(self):
        return self._symbol()

    def sqlexpression(self, **kwargs):
        return _sqlexp(Symbol(self._symbol()), **kwargs)


class ParamDict(dict):
    def __setitem__(self, name, value):
        k = _gen_param_name(name)
        v = value
        _ = self._type_map(value)  # ensure value type is supported
        super(ParamDict, self).__setitem__(k, v)

    def _to_value_str(self, v):
        if isinstance(v, datetime.datetime):
            return v.isoformat()
        return v

    def _type_map(self, v):
        # map Python types to Rockset type
        if isinstance(v, bool):
            return "bool"
        elif isinstance(v, int):
            return "int"
        elif isinstance(v, float):
            return "float"
        elif isinstance(v, str):
            return "string"
        # this check needs to be first because `date` is also a `datetime`
        elif isinstance(v, datetime.datetime):
            return "datetime"
        elif isinstance(v, datetime.date):
            return "date"
        raise TypeError("parameter value of type {} is not supported".format(type(v)))

    def new_param(self, field):
        fname = _gen_param_name(field)
        for i in range(1, 1001):
            candidate = fname
            if i > 1:
                candidate += str(i)
            if candidate not in self:
                return candidate
        raise ValueError('too many parameters bound with name "{}"'.format(fname))

    def sqlparams(self):
        params = []
        for k in sorted(self):
            v = self._to_value_str(self[k])
            vtype = self._type_map(self[k])
            params.append({"name": k, "value": str(v), "type": vtype})
        return params


_arg_ops = [
    ("__eq__", {}, FieldEqQuery),
    ("__ne__", {}, _make_ne),
    ("startswith", {str: FieldPrefixQuery, Literal: FieldPrefixQuery}, None),
    ("like", {str: FieldLikeQuery, Literal: FieldLikeQuery}, None),
]

for (pyop, sqlop) in (
    ("__lt__", "<"),
    ("__le__", "<="),
    ("__gt__", ">"),
    ("__ge__", ">="),
):

    def f_int(field, v, sqlop=sqlop):
        return FieldIntOpQuery(field, v, sqlop)

    def f_float(field, v, sqlop=sqlop):
        return FieldFloatOpQuery(field, v, sqlop)

    def f_string(field, v, sqlop=sqlop):
        return FieldStringOpQuery(field, v, sqlop)

    def f_datetime(field, v, sqlop=sqlop):
        return FieldDateTimeOpQuery(field, v, sqlop)

    def f_baseref(field, v, sqlop=sqlop):
        return FieldBaseRefOpQuery(field, v, sqlop)

    type_map = {
        int: f_int,
        float: f_float,
        str: f_string,
        datetime.datetime: f_datetime,
        datetime.date: f_datetime,
        datetime.time: f_datetime,
        datetime.timedelta: f_datetime,
        FieldRef: f_baseref,
        ParamRef: f_baseref,
    }
    _arg_ops.append((pyop, type_map, None))

_no_arg_ops = [
    ("is_null", FieldIsNullQuery),
    ("is_not_null", FieldIsNotNullQuery),
    ("is_defined", FieldIsDefinedQuery),
]


def _agg_ni(self, x, op=None):
    raise TypeError(
        "Operator {} is not supported for aggregated " "field references".format(op)
    )


for op, type_map, default_ctor in _arg_ops:

    def f(self, x, op=op, type_map=type_map, default_ctor=default_ctor):
        ty = py_type(x)
        ctor = type_map.get(ty, default_ctor)
        if ctor is None:
            raise TypeError(
                "Invalid FieldRef op / type combination: {}, {}".format(op, ty)
            )
        return ctor(self, x)

    setattr(FieldRef, op, f)
    setattr(AggFieldRef, op, _agg_ni)

for op, ctor in _no_arg_ops:

    def f(self, ctor=ctor):
        return ctor(self)

    setattr(FieldRef, op, f)
    setattr(AggFieldRef, op, _agg_ni)

F = FieldRef()
F.__doc__ = """``F`` is a field reference object that helps in building
query expressions natively using Python language expressions.
``F`` uses Python operator overloading heavily and operations on field
references generate Query_ objects that can be used in conjunction with
``Q`` to build compose complex queries."""

P = ParamRef()
P.__doc__ = """``P`` is a query parameter reference object used to define
query parameters within query expressions."""


def Q(query, alias=None):
    """All query objects are constructed using the ``Q(<collection-name>)``
    query builder construct and are then followed by a chain of query
    operators to build the full query expression."""
    if isinstance(query, Query):
        return SubQuery(query, alias=alias)
    elif type(query) == str:
        return _QueryString(query, alias=alias)
    elif isinstance(query, Symbol):
        return QueryStringResource(query, alias=alias)
    return NotImplemented
