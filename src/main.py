import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the value of the KEY key from the .env file
# Get all the keys from the .env file
keys = os.environ.keys()

# Print the values of all the keys to the console
for key in keys:
    print(os.getenv(key))