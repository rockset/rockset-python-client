"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from unittest import mock

from rockset.models import *
from test.conftest import EarlyExit, validate_call


def test_create_azure_blob_storage_collection(
    get_client, mock_request, request_validator
):
    with mock_request:
        rs = get_client
        try:
            rs.Collections.create_azure_blob_storage_collection(
                clustering_key=[
                    FieldPartition(
                        field_name="address.city.zipcode",
                        keys=["value1", "value2"],
                        type="AUTO",
                    ),
                ],
                description="transactions from stores worldwide",
                event_time_info=EventTimeInfo(
                    field="timestamp",
                    format="seconds_since_epoch",
                    time_zone="UTC",
                ),
                field_mapping_query=FieldMappingQuery(
                    sql="sql",
                ),
                field_mappings=[
                    FieldMappingV2(
                        input_fields=[
                            InputField(
                                field_name="address.city.zipcode",
                                if_missing="SKIP",
                                is_drop=True,
                                param="zip",
                            ),
                        ],
                        name="myTestMapping",
                        output_field=OutputField(
                            field_name="zip_hash",
                            on_error="SKIP",
                            value=SqlExpression(
                                sql="SHA256()",
                            ),
                        ),
                    ),
                ],
                insert_only=True,
                name="global-transactions",
                retention_secs=1000000,
                sources=[
                    AzureBlobStorageSourceWrapper(
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
                        integration_name="aws-integration",
                        container="server-logs",
                        pattern="prefix/to/**/keys/*.format",
                        prefix="prefix/to/blobs",
                    ),
                ],
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_azure_event_hubs_collection(
    get_client, mock_request, request_validator
):
    with mock_request:
        rs = get_client
        try:
            rs.Collections.create_azure_event_hubs_collection(
                clustering_key=[
                    FieldPartition(
                        field_name="address.city.zipcode",
                        keys=["value1", "value2"],
                        type="AUTO",
                    ),
                ],
                description="transactions from stores worldwide",
                event_time_info=EventTimeInfo(
                    field="timestamp",
                    format="seconds_since_epoch",
                    time_zone="UTC",
                ),
                field_mapping_query=FieldMappingQuery(
                    sql="sql",
                ),
                field_mappings=[
                    FieldMappingV2(
                        input_fields=[
                            InputField(
                                field_name="address.city.zipcode",
                                if_missing="SKIP",
                                is_drop=True,
                                param="zip",
                            ),
                        ],
                        name="myTestMapping",
                        output_field=OutputField(
                            field_name="zip_hash",
                            on_error="SKIP",
                            value=SqlExpression(
                                sql="SHA256()",
                            ),
                        ),
                    ),
                ],
                insert_only=True,
                name="global-transactions",
                retention_secs=1000000,
                sources=[
                    AzureEventHubsSourceWrapper(
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
                        integration_name="aws-integration",
                        hub_id="event-hub-1",
                        offset_reset_policy="EARLIEST",
                    ),
                ],
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_azure_service_bus_collection(
    get_client, mock_request, request_validator
):
    with mock_request:
        rs = get_client
        try:
            rs.Collections.create_azure_service_bus_collection(
                clustering_key=[
                    FieldPartition(
                        field_name="address.city.zipcode",
                        keys=["value1", "value2"],
                        type="AUTO",
                    ),
                ],
                description="transactions from stores worldwide",
                event_time_info=EventTimeInfo(
                    field="timestamp",
                    format="seconds_since_epoch",
                    time_zone="UTC",
                ),
                field_mapping_query=FieldMappingQuery(
                    sql="sql",
                ),
                field_mappings=[
                    FieldMappingV2(
                        input_fields=[
                            InputField(
                                field_name="address.city.zipcode",
                                if_missing="SKIP",
                                is_drop=True,
                                param="zip",
                            ),
                        ],
                        name="myTestMapping",
                        output_field=OutputField(
                            field_name="zip_hash",
                            on_error="SKIP",
                            value=SqlExpression(
                                sql="SHA256()",
                            ),
                        ),
                    ),
                ],
                insert_only=True,
                name="global-transactions",
                retention_secs=1000000,
                sources=[
                    AzureServiceBusSourceWrapper(
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
                        integration_name="aws-integration",
                        subscription="rockset-subscription",
                        topic="rockset-topic",
                    ),
                ],
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_dynamodb_collection(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Collections.create_dynamodb_collection(
                clustering_key=[
                    FieldPartition(
                        field_name="address.city.zipcode",
                        keys=["value1", "value2"],
                        type="AUTO",
                    ),
                ],
                description="transactions from stores worldwide",
                event_time_info=EventTimeInfo(
                    field="timestamp",
                    format="seconds_since_epoch",
                    time_zone="UTC",
                ),
                field_mapping_query=FieldMappingQuery(
                    sql="sql",
                ),
                field_mappings=[
                    FieldMappingV2(
                        input_fields=[
                            InputField(
                                field_name="address.city.zipcode",
                                if_missing="SKIP",
                                is_drop=True,
                                param="zip",
                            ),
                        ],
                        name="myTestMapping",
                        output_field=OutputField(
                            field_name="zip_hash",
                            on_error="SKIP",
                            value=SqlExpression(
                                sql="SHA256()",
                            ),
                        ),
                    ),
                ],
                insert_only=True,
                name="global-transactions",
                retention_secs=1000000,
                sources=[
                    DynamodbSourceWrapper(
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
                        integration_name="aws-integration",
                        aws_region="us-east-2",
                        rcu=1000,
                        table_name="dynamodb_table_name",
                        use_scan_api=True,
                    ),
                ],
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_file_upload_collection(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Collections.create_file_upload_collection(
                clustering_key=[
                    FieldPartition(
                        field_name="address.city.zipcode",
                        keys=["value1", "value2"],
                        type="AUTO",
                    ),
                ],
                description="transactions from stores worldwide",
                event_time_info=EventTimeInfo(
                    field="timestamp",
                    format="seconds_since_epoch",
                    time_zone="UTC",
                ),
                field_mapping_query=FieldMappingQuery(
                    sql="sql",
                ),
                field_mappings=[
                    FieldMappingV2(
                        input_fields=[
                            InputField(
                                field_name="address.city.zipcode",
                                if_missing="SKIP",
                                is_drop=True,
                                param="zip",
                            ),
                        ],
                        name="myTestMapping",
                        output_field=OutputField(
                            field_name="zip_hash",
                            on_error="SKIP",
                            value=SqlExpression(
                                sql="SHA256()",
                            ),
                        ),
                    ),
                ],
                insert_only=True,
                name="global-transactions",
                retention_secs=1000000,
                sources=[
                    FileUploadSourceWrapper(
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
                        integration_name="aws-integration",
                        file_name="file1.json",
                        file_size=12345,
                        file_upload_time="2019-01-15T21:48:23Z",
                    ),
                ],
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_gcs_collection(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Collections.create_gcs_collection(
                clustering_key=[
                    FieldPartition(
                        field_name="address.city.zipcode",
                        keys=["value1", "value2"],
                        type="AUTO",
                    ),
                ],
                description="transactions from stores worldwide",
                event_time_info=EventTimeInfo(
                    field="timestamp",
                    format="seconds_since_epoch",
                    time_zone="UTC",
                ),
                field_mapping_query=FieldMappingQuery(
                    sql="sql",
                ),
                field_mappings=[
                    FieldMappingV2(
                        input_fields=[
                            InputField(
                                field_name="address.city.zipcode",
                                if_missing="SKIP",
                                is_drop=True,
                                param="zip",
                            ),
                        ],
                        name="myTestMapping",
                        output_field=OutputField(
                            field_name="zip_hash",
                            on_error="SKIP",
                            value=SqlExpression(
                                sql="SHA256()",
                            ),
                        ),
                    ),
                ],
                insert_only=True,
                name="global-transactions",
                retention_secs=1000000,
                sources=[
                    GcsSourceWrapper(
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
                        integration_name="aws-integration",
                        bucket="server-logs",
                        pattern="prefix/to/**/keys/*.format",
                        prefix="prefix/to/keys",
                    ),
                ],
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_kafka_collection(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Collections.create_kafka_collection(
                clustering_key=[
                    FieldPartition(
                        field_name="address.city.zipcode",
                        keys=["value1", "value2"],
                        type="AUTO",
                    ),
                ],
                description="transactions from stores worldwide",
                event_time_info=EventTimeInfo(
                    field="timestamp",
                    format="seconds_since_epoch",
                    time_zone="UTC",
                ),
                field_mapping_query=FieldMappingQuery(
                    sql="sql",
                ),
                field_mappings=[
                    FieldMappingV2(
                        input_fields=[
                            InputField(
                                field_name="address.city.zipcode",
                                if_missing="SKIP",
                                is_drop=True,
                                param="zip",
                            ),
                        ],
                        name="myTestMapping",
                        output_field=OutputField(
                            field_name="zip_hash",
                            on_error="SKIP",
                            value=SqlExpression(
                                sql="SHA256()",
                            ),
                        ),
                    ),
                ],
                insert_only=True,
                name="global-transactions",
                retention_secs=1000000,
                sources=[
                    KafkaSourceWrapper(
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
                        integration_name="aws-integration",
                        consumer_group_id="org-collection",
                        kafka_topic_name="example-topic",
                        offset_reset_policy="LATEST",
                        use_v3=True,
                    ),
                ],
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_kinesis_collection(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Collections.create_kinesis_collection(
                clustering_key=[
                    FieldPartition(
                        field_name="address.city.zipcode",
                        keys=["value1", "value2"],
                        type="AUTO",
                    ),
                ],
                description="transactions from stores worldwide",
                event_time_info=EventTimeInfo(
                    field="timestamp",
                    format="seconds_since_epoch",
                    time_zone="UTC",
                ),
                field_mapping_query=FieldMappingQuery(
                    sql="sql",
                ),
                field_mappings=[
                    FieldMappingV2(
                        input_fields=[
                            InputField(
                                field_name="address.city.zipcode",
                                if_missing="SKIP",
                                is_drop=True,
                                param="zip",
                            ),
                        ],
                        name="myTestMapping",
                        output_field=OutputField(
                            field_name="zip_hash",
                            on_error="SKIP",
                            value=SqlExpression(
                                sql="SHA256()",
                            ),
                        ),
                    ),
                ],
                insert_only=True,
                name="global-transactions",
                retention_secs=1000000,
                sources=[
                    KinesisSourceWrapper(
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
                        integration_name="aws-integration",
                        aws_region="us-east-2",
                        dms_primary_key=[
                            "dms_primary_key_example",
                        ],
                        offset_reset_policy="EARLIEST",
                        stream_name="click_stream",
                    ),
                ],
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_mongodb_collection(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Collections.create_mongodb_collection(
                clustering_key=[
                    FieldPartition(
                        field_name="address.city.zipcode",
                        keys=["value1", "value2"],
                        type="AUTO",
                    ),
                ],
                description="transactions from stores worldwide",
                event_time_info=EventTimeInfo(
                    field="timestamp",
                    format="seconds_since_epoch",
                    time_zone="UTC",
                ),
                field_mapping_query=FieldMappingQuery(
                    sql="sql",
                ),
                field_mappings=[
                    FieldMappingV2(
                        input_fields=[
                            InputField(
                                field_name="address.city.zipcode",
                                if_missing="SKIP",
                                is_drop=True,
                                param="zip",
                            ),
                        ],
                        name="myTestMapping",
                        output_field=OutputField(
                            field_name="zip_hash",
                            on_error="SKIP",
                            value=SqlExpression(
                                sql="SHA256()",
                            ),
                        ),
                    ),
                ],
                insert_only=True,
                name="global-transactions",
                retention_secs=1000000,
                sources=[
                    MongodbSourceWrapper(
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
                        integration_name="aws-integration",
                        collection_name="my_collection",
                        database_name="my_database",
                    ),
                ],
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_s3_collection(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Collections.create_s3_collection(
                clustering_key=[
                    FieldPartition(
                        field_name="address.city.zipcode",
                        keys=["value1", "value2"],
                        type="AUTO",
                    ),
                ],
                description="transactions from stores worldwide",
                event_time_info=EventTimeInfo(
                    field="timestamp",
                    format="seconds_since_epoch",
                    time_zone="UTC",
                ),
                field_mapping_query=FieldMappingQuery(
                    sql="sql",
                ),
                field_mappings=[
                    FieldMappingV2(
                        input_fields=[
                            InputField(
                                field_name="address.city.zipcode",
                                if_missing="SKIP",
                                is_drop=True,
                                param="zip",
                            ),
                        ],
                        name="myTestMapping",
                        output_field=OutputField(
                            field_name="zip_hash",
                            on_error="SKIP",
                            value=SqlExpression(
                                sql="SHA256()",
                            ),
                        ),
                    ),
                ],
                insert_only=True,
                name="global-transactions",
                retention_secs=1000000,
                sources=[
                    S3SourceWrapper(
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
                        integration_name="aws-integration",
                        bucket="s3://customer-account-info",
                        pattern="prefix/to/**/keys/*.format",
                        prefix="prefix/to/keys",
                        region="us-west-2",
                    ),
                ],
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_snowflake_collection(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Collections.create_snowflake_collection(
                clustering_key=[
                    FieldPartition(
                        field_name="address.city.zipcode",
                        keys=["value1", "value2"],
                        type="AUTO",
                    ),
                ],
                description="transactions from stores worldwide",
                event_time_info=EventTimeInfo(
                    field="timestamp",
                    format="seconds_since_epoch",
                    time_zone="UTC",
                ),
                field_mapping_query=FieldMappingQuery(
                    sql="sql",
                ),
                field_mappings=[
                    FieldMappingV2(
                        input_fields=[
                            InputField(
                                field_name="address.city.zipcode",
                                if_missing="SKIP",
                                is_drop=True,
                                param="zip",
                            ),
                        ],
                        name="myTestMapping",
                        output_field=OutputField(
                            field_name="zip_hash",
                            on_error="SKIP",
                            value=SqlExpression(
                                sql="SHA256()",
                            ),
                        ),
                    ),
                ],
                insert_only=True,
                name="global-transactions",
                retention_secs=1000000,
                sources=[
                    SnowflakeSourceWrapper(
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
                        integration_name="aws-integration",
                        database="NASDAQ",
                        schema="PUBLIC",
                        table_name="COMPANIES",
                        warehouse="COMPUTE_XL",
                    ),
                ],
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_delete(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Collections.delete(
                collection="collection_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_get(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Collections.get(
                collection="collection_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_list(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Collections.list()
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_workspace_collections(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Collections.workspace_collections()
        except EarlyExit as e:
            validate_call(e, request_validator)
