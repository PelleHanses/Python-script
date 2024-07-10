#!/usr/bin/python3
'''
handle_json.py

Reads a Json file store it in a variable.
The file also have a example function for printing some info

The function can be included in other scripts like this:
    from handle_json import read_json
    json_data = read_json(MY_FILE)
    result = save_to_yaml_file(MY_FILE, json_data)

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

def save_to_yaml_file(filename, data, verbose=1):
    try:
        with open(filename, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
        if verbose > 0:
            print(f"Data successfully written to {filename}")
        return True
    except Exception as e:
        if verbose > 0:
            print(f"An error occurred while writing to the file: {e}")
        return False

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

### Start
if __name__ == "__main__":
    json_data = read_json('your_file.json')
    #print(json_data)
    print_questions_and_options(json_data)
    result = save_to_json_file('output.json', {"key": "value", "list": [1, 2, 3]})
