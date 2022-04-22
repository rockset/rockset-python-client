import inspect
import re
from enum import Enum
from functools import wraps
from types import FunctionType
from typing import Union

from rockset.api_client import ApiClient
from rockset.apis import (
    AliasesApi,
    APIKeysApi,
    CollectionsApi,
    DocumentsApi,
    IntegrationsApi,
    OrganizationsApi,
    QueriesApi,
    QueryLambdasApi,
    UsersApi,
    ViewsApi,
    VirtualInstancesApi,
    WorkspacesApi,
)
from rockset.configuration import Configuration
from rockset.exceptions import ApiTypeError, ApiValueError, InitializationException


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
        try:
            body = req_type(**body_args)
        except ApiTypeError as e:
            raise ApiValueError(f"Body for the request ({req_type}) could not be created because of an incorrect type: {e}") from e
        except TypeError as e:
            raise ApiValueError(f"Body for the request ({req_type}) could not be created because of a missing argument: {e}") from e

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


class DocumentsApiWrapper(DocumentsApi, metaclass=ApiMetaclass):
    pass


class IntegrationsApiWrapper(IntegrationsApi, metaclass=ApiMetaclass):
    pass


class OrganizationsApiWrapper(OrganizationsApi, metaclass=ApiMetaclass):
    pass


class QueriesApiWrapper(QueriesApi, metaclass=ApiMetaclass):
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
    """
    The class that is used to make requests to the Rockset API.

    Usage:
        rs = RocksetClient(api_key=APIKEY, host=Regions.use1a1)

        # Synchronous request
        response = rs.DocumentsApi.add_documents(
            collection=collection,
            data=[{"column": "value"}],
        )
        dict = response.to_dict()

        # Asynchronous request
        future = rs.DocumentsApi.add_documents(
            collection=collection,
            data=[{"column": "value"}],
            async_req=True,
        )
        result = await future
    """
    def __init__(self, host: Union[str, Regions, DevRegions] = None, api_key: str = None, max_workers: int=4, config: Configuration=None):
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
        if isinstance(host, Enum):
            host = host.value
        else:
            if host.startswith("http://"):
                host = f"https://{host[7:]}"
            elif not host.startswith("https://"):
                host = f"https://{host}"

            if host.endswith("/"):
                host = host[:-1]

        if not re.match(APISERVER_PATTERN, host):
            raise InitializationException("The provided host was invalid and could not be parsed into a valid host.")

        if not config:
            config = Configuration(host=host, api_key=api_key)

        if not config.api_key:
            raise InitializationException("An api key must be provided as a parameter to the RocksetClient or the Configuration object.")

        self.api_client = ApiClient(config, max_workers=max_workers)

        self.AliasesApi = AliasesApiWrapper(self.api_client)
        self.APIKeysApi = APIKeysApiWrapper(self.api_client)
        self.CollectionsApi = CollectionsApiWrapper(self.api_client)
        self.DocumentsApi = DocumentsApiWrapper(self.api_client)
        self.IntegrationsApi = IntegrationsApiWrapper(self.api_client)
        self.OrganizationsApi = OrganizationsApiWrapper(self.api_client)
        self.QueriesApi = QueriesApiWrapper(self.api_client)
        self.QueryLambdasApi = QueryLambdasApiWrapper(self.api_client)
        self.UsersApi = UsersApiWrapper(self.api_client)
        self.ViewsApi = ViewsApiWrapper(self.api_client)
        self.VirtualInstancesApi = VirtualInstancesApiWrapper(self.api_client)
        self.WorkspacesApi = WorkspacesApiWrapper(self.api_client)
