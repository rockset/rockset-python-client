import os
from typing import Dict, List

import swagger_client as client

APISERVERS = {
    "DEV": "https://master-api.dev.rockset.com",
    "RS2": "https://api.rs2.usw2.rockset.com",
}


def create_query_parameters(parameters: List[Dict[str, any]]):
    return [client.QueryParameter(**param) for param in parameters]


class RocksetClient:
    def __init__(self, host: str, apikey: str = None):
        apikey = apikey or os.environ.get("APIKEY", None)

        if not apikey:
            # Just generic exceptions for now
            raise Exception("Apikey must be provided in the constructor for the client or provided in the env.")
    
        config = client.Configuration()
        config.host = APISERVERS[host] if host in APISERVERS else host
        self.api_client = client.ApiClient(configuration=config)
        self.api_client.set_default_header("Authorization", f"apikey {apikey}")

        self.queries_api = client.QueriesApi(self.api_client)
        self.query_lambdas_api = client.QueryLambdasApi(self.api_client)

    def execute_query(self, body: Dict[str, any]):
        """
        Body is a dictionary containing all the fields of QueryRequestSql:
        {
            'query': 'str',
            'generate_warnings': 'bool',
            'profiling_enabled': 'bool',
            'default_row_limit': 'int',
            "parameters": [{"name": name, "type": type, "value": value}],
        }
        Note: pagination is currently hidden in the swagger spec.
        """
        if "parameters" in body and isinstance(body["parameters"], list):
            body["parameters"] = create_query_parameters(body["parameters"])
        
        req = client.QueryRequestSql(**body)
        return self.queries_api.query(client.QueryRequest(sql=req))

    def execute_query_lambda(self, workspace, query_lambda, version, body):
        if "parameters" in body and isinstance(body["parameters"], list):
            body["parameters"] = create_query_parameters(body["parameters"])

        req = client.ExecuteQueryLambdaRequest(**body)
        return self.query_lambdas_api.execute_query_lambda(workspace, query_lambda, version, body=req)
