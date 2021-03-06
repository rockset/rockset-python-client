"""
    REST API

    Rockset's REST API allows for creating and managing all resources in Rockset. Each supported endpoint is documented below.  All requests must be authorized with a Rockset API key, which can be created in the [Rockset console](https://console.rockset.com). The API key must be provided as `ApiKey <api_key>` in the `Authorization` request header. For example: ``` Authorization: ApiKey aB35kDjg93J5nsf4GjwMeErAVd832F7ad4vhsW1S02kfZiab42sTsfW5Sxt25asT ```  All endpoints are only accessible via https.  Build something awesome!  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from unittest import mock

from rockset.models import *
from test.conftest import EarlyExit, validate_call


def test_create_azure_blob_storage_integration(
    get_client, mock_request, request_validator
):
    with mock_request:
        rs = get_client
        try:
            rs.Integrations.create_azure_blob_storage_integration(
                azure_blob_storage=AzureBlobStorageIntegration(
                    connection_string="connection_string_example",
                ),
                description="AWS account with event data for the data science team.",
                name="event-logs",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_azure_event_hubs_integration(
    get_client, mock_request, request_validator
):
    with mock_request:
        rs = get_client
        try:
            rs.Integrations.create_azure_event_hubs_integration(
                azure_event_hubs=AzureEventHubsIntegration(),
                description="AWS account with event data for the data science team.",
                name="event-logs",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_dynamodb_integration(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Integrations.create_dynamodb_integration(
                description="AWS account with event data for the data science team.",
                dynamodb=DynamodbIntegration(
                    aws_access_key=AwsAccessKey(
                        aws_access_key_id="AKIAIOSFODNN7EXAMPLE",
                        aws_secret_access_key="wJal....",
                    ),
                    aws_role=AwsRole(
                        aws_role_arn="arn:aws:iam::2378964092:role/rockset-role",
                    ),
                    s3_export_bucket_name="s3_export_bucket_name_example",
                ),
                name="event-logs",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_gcs_integration(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Integrations.create_gcs_integration(
                description="AWS account with event data for the data science team.",
                gcs=GcsIntegration(
                    gcp_service_account=GcpServiceAccount(
                        service_account_key_file_json="service_account_key_file_json_example",
                    ),
                ),
                name="event-logs",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_kafka_integration(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Integrations.create_kafka_integration(
                description="AWS account with event data for the data science team.",
                kafka=KafkaIntegration(
                    bootstrap_servers="bootstrap_servers_example",
                    kafka_data_format="JSON",
                    kafka_topic_names=[
                        "kafka_topic_names_example",
                    ],
                    schema_registry_config=SchemaRegistryConfig(
                        key="key_example",
                        secret="secret_example",
                        url="url_example",
                    ),
                    security_config=KafkaV3SecurityConfig(
                        api_key="api_key_example",
                        secret="secret_example",
                    ),
                    use_v3=True,
                ),
                name="event-logs",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_kinesis_integration(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Integrations.create_kinesis_integration(
                description="AWS account with event data for the data science team.",
                kinesis=KinesisIntegration(
                    aws_access_key=AwsAccessKey(
                        aws_access_key_id="AKIAIOSFODNN7EXAMPLE",
                        aws_secret_access_key="wJal....",
                    ),
                    aws_role=AwsRole(
                        aws_role_arn="arn:aws:iam::2378964092:role/rockset-role",
                    ),
                ),
                name="event-logs",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_mongodb_integration(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Integrations.create_mongodb_integration(
                description="AWS account with event data for the data science team.",
                mongodb=MongoDbIntegration(
                    connection_uri="mongodb+srv://<username>:<password>@server.example.com/",
                ),
                name="event-logs",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_s3_integration(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Integrations.create_s3_integration(
                description="AWS account with event data for the data science team.",
                name="event-logs",
                s3=S3Integration(
                    aws_access_key=AwsAccessKey(
                        aws_access_key_id="AKIAIOSFODNN7EXAMPLE",
                        aws_secret_access_key="wJal....",
                    ),
                    aws_role=AwsRole(
                        aws_role_arn="arn:aws:iam::2378964092:role/rockset-role",
                    ),
                ),
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_segment_integration(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Integrations.create_segment_integration(
                description="AWS account with event data for the data science team.",
                name="event-logs",
                segment=SegmentIntegration(),
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_create_snowflake_integration(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Integrations.create_snowflake_integration(
                description="AWS account with event data for the data science team.",
                name="event-logs",
                snowflake=SnowflakeIntegration(
                    aws_access_key=AwsAccessKey(
                        aws_access_key_id="AKIAIOSFODNN7EXAMPLE",
                        aws_secret_access_key="wJal....",
                    ),
                    aws_role=AwsRole(
                        aws_role_arn="arn:aws:iam::2378964092:role/rockset-role",
                    ),
                    default_warehouse="default_warehouse_example",
                    password="password_example",
                    s3_export_path="s3://bucket/prefix",
                    snowflake_url="acme-marketing-test-account.snowflakecomputing.com",
                    user_role="user_role_example",
                    username="username_example",
                ),
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_delete(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Integrations.delete(
                integration="integration_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_get(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Integrations.get(
                integration="integration_example",
            )
        except EarlyExit as e:
            validate_call(e, request_validator)


def test_list(get_client, mock_request, request_validator):
    with mock_request:
        rs = get_client
        try:
            rs.Integrations.list()
        except EarlyExit as e:
            validate_call(e, request_validator)
