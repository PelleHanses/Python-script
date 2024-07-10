#!/usr/bin/python3
"""
subcommands.py
Examples of subcommands.
This will work even if Python < 3.7 are used.

The function can be included in other scripts like this:
    from suncommands import get_curl_command
    result = get_curl_command(address)
"""
import subprocess
import shlex  # For safe shell command splitting

def get_curl_result(address_to_get, allow_insecure=False, verbose=True):
    """
    Function to fetch a URL using curl and return the result.

    Parameters:
    - address_to_get (str): The URL to fetch.
    - allow_insecure (bool): Whether to allow insecure connections (default: False).
    - verbose (bool): Whether to print verbose output (default: True).

    Returns:
    - str or False: The result of the curl command as a string, or False if the command failed.
    """

    insecure_flag = "--insecure" if allow_insecure else ""
    curl_command = f'curl {insecure_flag} -L "{address_to_get}"'

    if verbose:
        print(f"Running curl command: {curl_command}")

    try:
        # Use shlex.split for safe splitting of the command
        args = shlex.split(curl_command)
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        output = result.stdout.decode('utf-8')
        return output
    except subprocess.CalledProcessError as e:
        if verbose:
            print(f"Error running curl command: {e}")
        return False
    except Exception as e:
        if verbose:
            print(f"An error occurred: {e}")
        return False


## Start
# Example address
address_to_get = "https://github.com/PelleHanses"
allow_insecure = False
address_result = get_curl_result(address_to_get, allow_insecure)
print()
print(f"The fetched result from {address_to_get}")
print()
print(str(address_result))
print()
