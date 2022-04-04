
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.api_keys_api import APIKeysApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from rockset.api.api_keys_api import APIKeysApi
from rockset.api.aliases_api import AliasesApi
from rockset.api.collections_api import CollectionsApi
from rockset.api.custom_roles_api import CustomRolesApi
from rockset.api.documents_api import DocumentsApi
from rockset.api.integrations_api import IntegrationsApi
from rockset.api.organizations_api import OrganizationsApi
from rockset.api.queries_api import QueriesApi
from rockset.api.query_lambdas_api import QueryLambdasApi
from rockset.api.users_api import UsersApi
from rockset.api.views_api import ViewsApi
from rockset.api.virtual_instances_api import VirtualInstancesApi
from rockset.api.workspaces_api import WorkspacesApi
