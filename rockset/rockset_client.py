"""Generated file. Make changes by editing templates/rockset_client.mustache."""

import datetime
import inspect
import re
from enum import Enum
from functools import wraps
from types import FunctionType
from typing import Any, Dict, Union

import rockset.apis as apis
from rockset.api_client import ApiClient
from rockset.configuration import Configuration
from rockset.exceptions import (ApiTypeError, ApiValueError,
                                InitializationException)
from rockset.models import QueryParameter, QueryRequestSql, QueryResponse

APISERVER_PATTERN = re.compile(r"^https:\/\/(\w|-|\.)+\.rockset\.com$")


class Clusters(str, Enum):
    STAGING = "https://staging-api.rockset-0s.internal.api.openai.org"


def wrapper(method):
    @wraps(method)
    def wrapped(*args, **kwargs):
        req_type = inspect.getmro(args[0].__class__)[1].return_types_dict.get(
            method.__name__, None
        )
        body_param_name = inspect.getmro(args[0].__class__)[1].body_params_dict.get(
            method.__name__, None
        )

        if not req_type:
            return method(*args, **kwargs)

        body_fields = req_type.attribute_map.keys()
        body_args = dict(filter(lambda item: item[0] in body_fields, kwargs.items()))
        other_args = kwargs

        body = None
        if body_args:
            try:
                body = req_type(**body_args)
            except ApiTypeError as e:
                raise ApiValueError(
                    f"Body for the request ({req_type}) could not be created because of an incorrect type: {e}"
                ) from e
            except TypeError as e:
                raise ApiValueError(
                    f"Body for the request ({req_type}) could not be created because of a missing argument: {e}"
                ) from e

            other_args[body_param_name] = body

        # A way to pass in arguments that will make it to the body.
        # This is not officially supported, arguments sent in this way have no compatability gaurentees.
        if "add_raw_args_to_body" in other_args:
            for raw_key, raw_value in other_args["add_raw_args_to_body"].items():
                other_args[body_param_name][raw_key] = raw_value
            del other_args["add_raw_args_to_body"]

        return method(*args, **other_args)

    return wrapped


class ApiMetaclass(type):
    def __new__(cls, className, bases, classDict):
        child = super().__new__(cls, className, bases, classDict)
        for base in bases:
            for field_name, field in base.__dict__.items():
                if (
                    not field_name.startswith("__")
                    and isinstance(field, FunctionType)
                    and field_name not in classDict
                ):
                    setattr(child, field_name, wrapper(field))
        return child


def convert_to_rockset_type(v):
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
    raise TypeError(
        "Parameter value of type {} is not supported by Rockset".format(type(v))
    )


class APIKeysApiWrapper(apis.APIKeys, metaclass=ApiMetaclass):
    pass


class AliasesApiWrapper(apis.Aliases, metaclass=ApiMetaclass):
    pass


class BoxApiWrapper(apis.Box, metaclass=ApiMetaclass):
    pass


class CollectionsApiWrapper(apis.Collections, metaclass=ApiMetaclass):
    pass


class CustomRolesApiWrapper(apis.CustomRoles, metaclass=ApiMetaclass):
    pass


class DeploymentSettingsApiWrapper(apis.DeploymentSettings, metaclass=ApiMetaclass):
    pass


class DeploymentsApiWrapper(apis.Deployments, metaclass=ApiMetaclass):
    pass


class DocumentsApiWrapper(apis.Documents, metaclass=ApiMetaclass):
    pass


class IntegrationsApiWrapper(apis.Integrations, metaclass=ApiMetaclass):
    pass


class OrganizationsApiWrapper(apis.Organizations, metaclass=ApiMetaclass):
    pass


class QueriesApiWrapper(apis.Queries, metaclass=ApiMetaclass):
    pass


class QueryLambdasApiWrapper(apis.QueryLambdas, metaclass=ApiMetaclass):
    pass


class ScheduledLambdasApiWrapper(apis.ScheduledLambdas, metaclass=ApiMetaclass):
    pass


class SearchApiWrapper(apis.Search, metaclass=ApiMetaclass):
    pass


class SharedLambdasApiWrapper(apis.SharedLambdas, metaclass=ApiMetaclass):
    pass


class SourcesApiWrapper(apis.Sources, metaclass=ApiMetaclass):
    pass


class UsersApiWrapper(apis.Users, metaclass=ApiMetaclass):
    pass


class ViewsApiWrapper(apis.Views, metaclass=ApiMetaclass):
    pass


class VirtualInstancesApiWrapper(apis.VirtualInstances, metaclass=ApiMetaclass):
    pass


class WorkspacesApiWrapper(apis.Workspaces, metaclass=ApiMetaclass):
    pass


class RocksetClient:
    """
    The class that is used to make requests to the Rockset API.

    Usage:
        rs = RocksetClient(api_key=APIKEY, host=Regions.use1a1)

        # Synchronous request
        response = rs.Documents.add_documents(
            collection=collection,
            data=[{"column": "value"}],
        )
        dict = response.to_dict()

        # Asynchronous request
        future = rs.Documents.add_documents(
            collection=collection,
            data=[{"column": "value"}],
            async_req=True,
        )
        result = await future
    """

    def __init__(
        self,
        host: Union[str, Clusters] = None,
        api_key: str = None,
        max_workers: int = 4,
        config: Configuration = None,
    ):
        """
        Keyword Args:
            host (str, Regions, DevRegions): Base url of the Rockset apiserver that should be used.
                The Regions enum can be used instead of a string.
                Can be specified here or within the Configuration object.
                If no host is specified, the client will default to us-west-2.
                us-west-2: https://api.rs2.usw2.rockset.com
                us-east-1: https://api.use1a1.rockset.com
                eu-central-1: https://api.euc1a1.rockset.com
            api_key (str): The api key to use for authorization when making requests.
                The api key must be provided here or within the configuration object
            max_workers (int): The max number of workers that the ThreadPoolExecutor
                should use when making asynchronous requests. [optional]
        """
        if not host and config and config.host:
            host = config.host

        if isinstance(host, Enum):
            host = host.value

        if not config:
            config = Configuration(host=host, api_key=api_key)
        else:
            config.host = host

        if not config.api_key:
            raise InitializationException(
                "An api key must be provided as a parameter to the RocksetClient or the Configuration object."
            )

        self.api_client = ApiClient(config, max_workers=max_workers)

        self.APIKeys = APIKeysApiWrapper(self.api_client)
        self.Aliases = AliasesApiWrapper(self.api_client)
        self.Box = BoxApiWrapper(self.api_client)
        self.Collections = CollectionsApiWrapper(self.api_client)
        self.CustomRoles = CustomRolesApiWrapper(self.api_client)
        self.DeploymentSettings = DeploymentSettingsApiWrapper(self.api_client)
        self.Deployments = DeploymentsApiWrapper(self.api_client)
        self.Documents = DocumentsApiWrapper(self.api_client)
        self.Integrations = IntegrationsApiWrapper(self.api_client)
        self.Organizations = OrganizationsApiWrapper(self.api_client)
        self.Queries = QueriesApiWrapper(self.api_client)
        self.QueryLambdas = QueryLambdasApiWrapper(self.api_client)
        self.ScheduledLambdas = ScheduledLambdasApiWrapper(self.api_client)
        self.Search = SearchApiWrapper(self.api_client)
        self.SharedLambdas = SharedLambdasApiWrapper(self.api_client)
        self.Sources = SourcesApiWrapper(self.api_client)
        self.Users = UsersApiWrapper(self.api_client)
        self.Views = ViewsApiWrapper(self.api_client)
        self.VirtualInstances = VirtualInstancesApiWrapper(self.api_client)
        self.Workspaces = WorkspacesApiWrapper(self.api_client)
        

    def set_application(self, value):
        self.api_client.set_application(value)

    def sql(self, query: str, params: Dict[str, Any] = None) -> QueryResponse:
        """Convenience method for making queries."""
        if params is not None:
            params = [
                QueryParameter(
                    name=param, value=str(val), type=convert_to_rockset_type(val)
                )
                for param, val in params.items()
            ]

        return self.Queries.query(sql=QueryRequestSql(query=query, parameters=params))
