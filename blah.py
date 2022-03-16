from rockset.rockset_client import RocksetClient
from rockset.api_client import ApiClient
from rockset.models import QueryRequestSql
import rockset
import asyncio


rs = RocksetClient(api_key="vjbBqS95TN8SmFhcZ3FDh6vHCXYVJqxSZ9FIiVmawuMuLuP1zgYSbDR7ry9avBjp")

async def blah():
    res = await rs.CollectionsApi.list_collections(async_req=True)
    return res


loop = asyncio.get_event_loop()
all = asyncio.gather(blah())

print(loop.run_until_complete(all))