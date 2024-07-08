#!/usr/bin/python3
'''
read_json_file.py

Reads a Json file store it in a array.
The file also have a example function for printing some info

The function can be included in other scripts like this:
    from read_json_file import read_json
    lines = read_json(MY_FILE)

'''

import os
import json

def read_json(filename, verbose=0):
    # Reads the Json file and return it
    # Check if the file exists
    if not os.path.exists(filename):
        if verbose > 0:
            print(f"Error: The file '{filename}' does not exist.")
        return None

    # Read the JSON file
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print(f"Error: The file '{filename}' is not a valid JSON file.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

    return data

def print_questions_and_options(data):
    # Sample print of some info in the Json file
    if data is None:
        return

    quiz = data.get("quiz", {})
    index = 1
    for category, questions in quiz.items():
        print(f"  Category: {category}")
        for qid, qdata in questions.items():
            question = qdata.get("question", "No question found")
            options = qdata.get("options", [])
            print(f"    Question {index}: {question}")
            print("    Options:")
            for option in options:
                print(f"      - {option}")
            index = index + 1
        print()  # Add a blank line between categories

# Usage example:
json_data = read_json('your_file.json')
#print(json_data)
print_questions_and_options(json_data)

