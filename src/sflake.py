from snowflake.connector import connect, SnowflakeConnection

def get_connection(user: str, password: str, account: str) -> SnowflakeConnection:
    return connect(user=user, password=password, account=account)
