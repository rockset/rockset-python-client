from client import RocksetClient


rs = RocksetClient("DEV", "mPxfooyfovW4t9BuCCkzwKQf3Qh0Jjny5HAelp1jeiB35M7vcit8xAMSj8OuuIMr")

# print(
#     rs.execute_query(
#         {
#             "query": "SELECT * FROM _events LIMIT :limit",
#             "default_row_limit": 100,
#             "parameters": [{"name": "limit", "type": "int", "value": 100}]
#         }
#     )
# )

print(rs.execute_query_lambda(
    "commons", "myQueryLambda", "5424426cfbd2c26c", {
        "parameters": [{"name": "target_type", "type": "string", "value": "INFO"}],
        "default_row_limit": 2,
    }
))