#!/usr/bin/python3
"""
try_except.py
Handles failures in a function.

The function can be included in other scripts like this:
    from try_except import read_file
    result = read_file(MY_FILE)
"""

def read_file(file_path, verbose=1):
    """
    Function to read a file and print its contents.
    If the file does not exist or other errors occur, an error message is printed.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
            return content
    except FileNotFoundError:
        if verbose > 0:
            print(f"Error: The file '{file_path}' does not exist.")
        return f"Error: The file '{file_path}' does not exist."
    except IOError:
        if verbose > 0:
            print(f"Error: An IOError occurred while trying to read the file '{file_path}'.")
        return f"Error: An IOError occurred while trying to read the file '{file_path}'."
    except Exception as e:
        if verbose > 0:
            print(f"An unexpected error occurred: {e}")
        return f"An unexpected error occurred: {e}"

## Start
if __name__ == "__main__":
    file_path = 'not_your_file.txt'
    result = read_file(file_path, 0)
    print("")
    print(f"The result: {result}")
    print("")
