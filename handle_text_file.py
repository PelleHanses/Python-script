#!/usr/bin/python3
'''
handle_text_file.py

Reads lines in a file and store it in a array.
Ignoring empty lines and lines starting with #

The function can be included in other scripts like this:
    from handle_text_file import read_lines
    lines = read_lines(MY_FILE)
    result = save_to_text_file('output.txt', lines)

'''

import os

def read_lines(filename, verbose=0):
    # Check if the file exists
    if not os.path.exists(filename):
        if verbose > 0:
            print(f"Error: The file '{filename}' does not exist.")
        return []

    lines = []
    with open(filename, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line and not stripped_line.startswith('#'):
                lines.append(stripped_line)
    return lines

def save_to_text_file(filename, data, verbose=0):
    try:
        with open(filename, 'w') as file:
            for line in data:
                file.write(f"{line}\n")
        if verbose > 0:
            print(f"Data successfully written to {filename}")
        return True
    except Exception as e:
        if verbose > 0:
            print(f"An error occurred while writing to the file: {e}")
        return False

# Usage example:
file_content = read_lines('your_file.txt', 1)
print(file_content)
result = save_to_text_file('output.txt', ['Line 1', 'Line 2', 'Line 3'])
