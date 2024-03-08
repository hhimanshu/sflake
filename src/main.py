import os
from dotenv import load_dotenv
from sflake import create_database, display_connection_details, get_connection
from snowflake.connector import SnowflakeConnection
from snowflake.core import Root
from snowflake.core.database import Database

# Load the .env file
load_dotenv()


def main():
    endpoint = os.getenv("SNOWFLAKE_ENDPOINT")
    user = os.getenv("SNOWFLAKE_USER")
    password = os.getenv("SNOWFLAKE_PASSWORD")
    conn = get_connection(user=user, password=password, account=endpoint)
    create_database(conn=conn, name="DEMO_DB")

    display_connection_details(conn)


if __name__ == "__main__":
    main()
