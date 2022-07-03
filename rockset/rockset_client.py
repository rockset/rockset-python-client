import datetime
import inspect
import re
from enum import Enum
from functools import wraps
from types import FunctionType
from typing import Any, Dict, Union

from rockset.api_client import ApiClient
from rockset.apis import (
    Aliases,
    APIKeys,
    Collections,
    CustomRoles,
    Documents,
    Integrations,
    Organizations,
    Queries,
    QueryLambdas,
    Users,
    Views,
    VirtualInstances,
    Workspaces,
)
from rockset.configuration import Configuration
from rockset.exceptions import ApiTypeError, ApiValueError, InitializationException
from rockset.models import QueryParameter, QueryRequestSql, QueryResponse


APISERVER_PATTERN = re.compile(r"^https:\/\/(\w|-|\.)+\.rockset\.com$")


class Regions(str, Enum):
    rs2 = "https://api.rs2.usw2.rockset.com"
    use1a1 = "https://api.use1a1.rockset.com"
    euc1a1 = "https://api.euc1a1.rockset.com"


class DevRegions(str, Enum):
    dev = "https://master-api.dev.rockset.com"
    use1a1 = "https://staging-api.use1a1.dev.rockset.com"
    usw2a1 = "https://staging-api.usw2a1.dev.rockset.com"


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


class AliasesApiWrapper(Aliases, metaclass=ApiMetaclass):
    pass


class APIKeysApiWrapper(APIKeys, metaclass=ApiMetaclass):
    pass


class CollectionsApiWrapper(Collections, metaclass=ApiMetaclass):
    pass


class CustomRolesApiWrapper(CustomRoles, metaclass=ApiMetaclass):
    pass


class DocumentsApiWrapper(Documents, metaclass=ApiMetaclass):
    pass


class IntegrationsApiWrapper(Integrations, metaclass=ApiMetaclass):
    pass


class OrganizationsApiWrapper(Organizations, metaclass=ApiMetaclass):
    pass


class QueriesApiWrapper(Queries, metaclass=ApiMetaclass):
    pass


class QueryLambdasApiWrapper(QueryLambdas, metaclass=ApiMetaclass):
    pass


class UsersApiWrapper(Users, metaclass=ApiMetaclass):
    pass


class ViewsApiWrapper(Views, metaclass=ApiMetaclass):
    pass


class VirtualInstancesApiWrapper(VirtualInstances, metaclass=ApiMetaclass):
    pass


class WorkspacesApiWrapper(Workspaces, metaclass=ApiMetaclass):
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
        host: Union[str, Regions, DevRegions] = None,
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
        elif host:
            if host.startswith("http://"):
                host = f"https://{host[7:]}"
            elif not host.startswith("https://"):
                host = f"https://{host}"

            if host.endswith("/"):
                host = host[:-1]

            if not re.match(APISERVER_PATTERN, host):
                raise InitializationException(
                    "The provided host was invalid and could not be parsed into a valid host."
                )

        if not config:
            config = Configuration(host=host, api_key=api_key)
        else:
            config.host = host

        if not config.api_key:
            raise InitializationException(
                "An api key must be provided as a parameter to the RocksetClient or the Configuration object."
            )

        self.api_client = ApiClient(config, max_workers=max_workers)

        self.Aliases = AliasesApiWrapper(self.api_client)
        self.APIKeys = APIKeysApiWrapper(self.api_client)
        self.Collections = CollectionsApiWrapper(self.api_client)
        self.CustomRoles = CustomRolesApiWrapper(self.api_client)
        self.Documents = DocumentsApiWrapper(self.api_client)
        self.Integrations = IntegrationsApiWrapper(self.api_client)
        self.Organizations = OrganizationsApiWrapper(self.api_client)
        self.Queries = QueriesApiWrapper(self.api_client)
        self.QueryLambdas = QueryLambdasApiWrapper(self.api_client)
        self.Users = UsersApiWrapper(self.api_client)
        self.Views = ViewsApiWrapper(self.api_client)
        self.VirtualInstances = VirtualInstancesApiWrapper(self.api_client)
        self.Workspaces = WorkspacesApiWrapper(self.api_client)

    def sql(self, query: str, params: Dict[str, Any] = None) -> QueryResponse:
        """Convenience method for making queries."""
        if params:
            params = [
                QueryParameter(
                    name=param, value=str(val), type=convert_to_rockset_type(val)
                )
                for param, val in params.items()
            ]

        return self.Queries.query(sql=QueryRequestSql(query=query, parameters=params))
