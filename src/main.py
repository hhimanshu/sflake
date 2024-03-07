import os
from dotenv import load_dotenv
from sflake import get_connection
from snowflake.connector import SnowflakeConnection

# Load the .env file
load_dotenv()


def main():
    endpoint = os.getenv("SNOWFLAKE_ENDPOINT")
    user = os.getenv("SNOWFLAKE_USER")
    password = os.getenv("SNOWFLAKE_PASSWORD")
    conn = get_connection(user=user, password=password, account=endpoint)
    display_connection_details(conn)

def display_connection_details(conn: SnowflakeConnection):
    print(f"---------- Connection details -----------")
    print(f"Account: {conn.account}")
    print(f"User: {conn.user}")
    print(f"Role: {conn.role}")
    print(f"Warehouse: {conn.warehouse}")
    print("-"*40)

if __name__ == "__main__":
    main()
