import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the value of the KEY key from the .env file
key_value = os.getenv('KEY')

# Print the value to the console
print(key_value)