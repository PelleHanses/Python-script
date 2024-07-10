#!/usr/bin/python3
"""
env.php
Example of handling .env file and get values from it.

The function can be included in other scripts like this:
    from env import get_value
    result = get_value()
"""

import os
from dotenv import load_dotenv

def get_value(argument_to_fetch, verbose=False):
    """
    Function to fetch value from .env file based on argument_to_fetch
    """
    try:
        load_dotenv() #laddar.env
        fetched_value = os.getenv(argument_to_fetch)
        if fetched_value is None:
            raise ValueError(f"Value for '{argument_to_fetch}' not found in .env file.")
        return fetched_value
    except Exception as e:
        if verbose:
            print(f"An error occurred while fetching value for '{argument_to_fetch}': {e}")
        return None

## Start
argument_to_fetch = "SMTP_PORT"
result = get_value(argument_to_fetch)
print()
print(f"  Fetched value for {argument_to_fetch}: {result}")
