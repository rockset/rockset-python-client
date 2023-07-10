"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from unittest import mock

from rockset.models import *
from test.conftest import EarlyExit, validate_call


def test_create_source(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Sources.create_source(
                collection="collection_example",
                azure_blob_storage=SourceAzureBlobStorage(
                    container="server-logs",
                    pattern="prefix/to/**/keys/*.format",
                    prefix="prefix/to/blobs",
                ),
                azure_event_hubs=SourceAzureEventHubs(
                    hub_id="event-hub-1",
                    offset_reset_policy="EARLIEST",
                ),
                azure_service_bus=SourceAzureServiceBus(
                    subscription="rockset-subscription",
                    topic="rockset-topic",
                ),
                dynamodb=SourceDynamoDb(
                    aws_region="us-east-2",
                    rcu=1000,
                    table_name="dynamodb_table_name",
                    use_scan_api=True,
                ),
                file_upload=SourceFileUpload(
                    file_name="file1.json",
                    file_size=12345,
                    file_upload_time="2019-01-15T21:48:23Z",
                ),
                format_params=FormatParams(
                    csv=CsvParams(
                        column_names=["c1", "c2", "c3"],
                        column_types=["BOOLEAN", "INTEGER", "FLOAT", "STRING"],
                        encoding="UTF-8",
                        escape_char="\\",
                        first_line_as_column_names=True,
                        quote_char='"',
                        separator=",",
                    ),
                    json=True,
                    mssql_dms=True,
                    mysql_dms=True,
                    oracle_dms=True,
                    postgres_dms=True,
                    xml=XmlParams(
                        attribute_prefix="_attr",
                        doc_tag="row",
                        encoding="UTF-8",
                        root_tag="root",
                        value_tag="value",
                    ),
                ),
                gcs=SourceGcs(
                    bucket="server-logs",
                    pattern="prefix/to/**/keys/*.format",
                    prefix="prefix/to/keys",
                ),
                id="a1df483c-734e-485b-8005-f46386ef42f6",
                integration_name="aws-integration",
                kafka=SourceKafka(
                    consumer_group_id="org-collection",
                    kafka_topic_name="example-topic",
                    offset_reset_policy="EARLIEST",
                    use_v3=True,
                ),
                kinesis=SourceKinesis(
                    aws_region="us-east-2",
                    dms_primary_key=[
                        "dms_primary_key_example",
                    ],
                    offset_reset_policy="EARLIEST",
                    stream_name="click_stream",
                ),
                mongodb=SourceMongoDb(
                    collection_name="my_collection",
                    database_name="my_database",
                    retrieve_full_document=True,
                ),
                s3=SourceS3(
                    bucket="s3://customer-account-info",
                    pattern="prefix/to/**/keys/*.format",
                    prefix="prefix/to/keys",
                    region="us-west-2",
                ),
                snowflake=SourceSnowflake(
                    database="NASDAQ",
                    schema="PUBLIC",
                    table_name="COMPANIES",
                    warehouse="COMPUTE_XL",
                ),
                system=SourceSystem(
                    type="QUERY_LOGS",
                ),
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_delete(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Sources.delete(
                collection="collection_example",
                source="source_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_get(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Sources.get(
                collection="collection_example",
                source="source_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_list_collection_sources(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Sources.list_collection_sources(
                collection="collection_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)
