import inspect
from functools import wraps
from types import FunctionType

from rockset.api_client import ApiClient
from rockset.apis import (
    AliasesApi,
    APIKeysApi,
    CollectionsApi,
    # DocumentsApi,
    IntegrationsApi,
    OrganizationsApi,
    # QueriesApi,
    QueryLambdasApi,
    UsersApi,
    ViewsApi,
    VirtualInstancesApi,
    WorkspacesApi,
)
from rockset.configuration import Configuration
from rockset.exceptions import InitializationException

# todo: change module-level docstrings in templates


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

        body = req_type(**body_args)
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


class AliasesApiWrapper(AliasesApi, metaclass=ApiMetaclass):
    pass


class APIKeysApiWrapper(APIKeysApi, metaclass=ApiMetaclass):
    pass


class CollectionsApiWrapper(CollectionsApi, metaclass=ApiMetaclass):
    pass


class IntegrationsApiWrapper(IntegrationsApi, metaclass=ApiMetaclass):
    pass


class OrganizationsApiWrapper(OrganizationsApi, metaclass=ApiMetaclass):
    pass


class QueryLambdasApiWrapper(QueryLambdasApi, metaclass=ApiMetaclass):
    pass


class UsersApiWrapper(UsersApi, metaclass=ApiMetaclass):
    pass


class ViewsApiWrapper(ViewsApi, metaclass=ApiMetaclass):
    pass


class VirtualInstancesApiWrapper(VirtualInstancesApi, metaclass=ApiMetaclass):
    pass


class WorkspacesApiWrapper(WorkspacesApi, metaclass=ApiMetaclass):
    pass


class RocksetClient:
    # todo: should user create Config object or pass in each config var as arguments?
    def __init__(self, host: str = None, apikey: str = None, max_workers=4):
        self.api_client = ApiClient(Configuration(host=host), max_workers=max_workers)

        if not apikey:
            raise InitializationException("an api key must be provided")
        self.api_client.default_headers["Authorization"] = f"apikey {apikey}"

        self.Alias = AliasesApiWrapper(self.api_client)
        self.ApiKey = APIKeysApiWrapper(self.api_client)
        self.Collection = CollectionsApiWrapper(self.api_client)
        # self.Document = DocumentsApi(self.api_client)
        self.Integration = IntegrationsApiWrapper(self.api_client)
        self.Organization = OrganizationsApiWrapper(self.api_client)
        # self.Query = QueriesApi(self.api_client)
        self.QueryLambda = QueryLambdasApiWrapper(self.api_client)
        self.User = UsersApiWrapper(self.api_client)
        self.View = ViewsApiWrapper(self.api_client)
        self.VirtualInstance = VirtualInstancesApiWrapper(self.api_client)
        self.Workspace = WorkspacesApiWrapper(self.api_client)
