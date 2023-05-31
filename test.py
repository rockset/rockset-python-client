from rockset_v2 import RocksetClient
from rockset_v2.models import S3SourceWrapper
from rockset_v2.exceptions import NotFoundException


rs = RocksetClient(api_key="9AG9yeBVdql1LedvaDdSvuD03bYXy8bc3LGTTmqxK3ejaY2KigP37l9J0RiwMGS9", host="staging-api.usw2a1.dev.rockset.com")

c = rs.Collections.get(
                    collection="aliasCollection1")

print(c)         
