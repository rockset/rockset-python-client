from rockset.rockset_client import RocksetClient
from rockset.api_client import ApiClient
from rockset.models import *
import rockset
import asyncio


rs = RocksetClient(api_key="vjbBqS95TN8SmFhcZ3FDh6vHCXYVJqxSZ9FIiVmawuMuLuP1zgYSbDR7ry9avBjp")

async def blah():
    api_response = await rs.CollectionsApi.create_azure_blob_storage_collection(
        description="transactions from stores worldwide",
        event_time_info=EventTimeInfo(
        field="timestamp",
        format="seconds_since_epoch",
        time_zone="UTC",
    ),
        field_schemas=[
        FieldSchema(
            field_name="address.city.zipcode",
            field_options=FieldOptions(
                column_index_mode="store",
                index_mode="index",
                range_index_mode="v1_index",
                type_index_mode="index",
            ),
        ),
    ],
        insert_only=False,
        inverted_index_group_encoding_options=InvertedIndexGroupEncodingOptions(
        doc_id_codec="doc_id_codec_example",
        event_time_codec="event_time_codec_example",
        format_version=1,
        group_size=1,
        restart_length=1,
    ),
        name="global-transactions",
        retention_secs=1000000,
        sources=[
        AzureBlobStorageSourceWrapper(
            azure_blob_storage=SourceAzureBlobStorage(
                container="server-logs",
                pattern="prefix/to/**/keys/*.format",
                prefix="prefix/to/blobs",
            ),
            format_params=FormatParams(
                csv=CsvParams(
                    column_names=["c1","c2","c3"],
                    column_types=["BOOLEAN","INTEGER","FLOAT","STRING"],
                    encoding="UTF-8",
                    escape_char="\\",
                    first_line_as_column_names=True,
                    quote_char="\"",
                    separator=",",
                ),
                json=True,
                xml=XmlParams(
                    attribute_prefix="_attr",
                    doc_tag="row",
                    encoding="UTF-8",
                    root_tag="root",
                    value_tag="value",
                ),
            ),
            integration_name="aws-integration",
        ),
    ],
        time_partition_resolution_secs=1,
        async_req=True,
    )


loop = asyncio.get_event_loop()
all = asyncio.gather(blah())

print(loop.run_until_complete(all))