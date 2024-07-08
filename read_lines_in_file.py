#!/usr/bin/python3
'''
read_lines_in_file.py

Reads lines in a file and store it in a array.
Ignoring empty lines and lines starting with #

The function can be included in other scripts like this:
    from read_lines_in_file import read_lines
    lines = read_lines(MY_FILE)

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

# Usage example:
file_content = read_lines('your_file.txt', 1)
print(file_content)
