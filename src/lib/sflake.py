from snowflake.connector import connect, SnowflakeConnection
from snowflake.core import Root
from snowflake.core.database import Database
from snowflake.core import CreateMode


def get_connection(user: str, password: str, account: str) -> SnowflakeConnection:
    return connect(user=user, password=password, account=account)


def get_root(conn: SnowflakeConnection) -> Root:
    return Root(conn)


def create_database(conn: SnowflakeConnection, name: str) -> Root:
    db = Database(name=name)
    root = get_root(conn=conn)
    root.databases.create(database=db, mode=CreateMode.or_replace)


def display_connection_details(conn: SnowflakeConnection):
    print(f"---------- Connection details -----------")
    print(f"Account: {conn.account}")
    print(f"User: {conn.user}")
    print(f"Role: {conn.role}")
    print(f"Warehouse: {conn.warehouse}")
    print("-" * 40)
