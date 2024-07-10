#!/usr/bin/python3
'''
handle_yaml.py

Reads a Yaml file store it in a variable.
The file also have a example function for printing some info

The function can be included in other scripts like this:
    from handle_yaml import read_yaml
    yaml_data = read_yaml(MY_FILE)
    result = save_to_yaml_file('output.yaml', yaml_data)

'''

import os
import yaml

def read_yaml(filename, verbose=0):
    # Reads data from Yaml file and return it
    if not os.path.exists(filename):
        if verbose > 0:
            print(f"Error: The file '{filename}' does not exist.")
        return None

    try:
        with open(filename, 'r') as file:
            data = yaml.safe_load(file)
    except yaml.YAMLError as e:
        print(f"Error: The file '{filename}' is not a valid YAML file. {e}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

    return data

def save_to_yaml_file(filename, datai, verbose=0):
    # Saves data to file
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
    # Example function to print som info
    if data is None:
        return

    quiz = data.get("quiz", {})
    index = 1
    for category, questions in quiz.items():
        print(f"  Category: {category}")
        for qid, qdata in questions.items():
            question = qdata.get("question", "No question found")
            options = qdata.get("options", [])
            print(f"    Questioni {index}: {question}")
            print("    Options:")
            for option in options:
                print(f"      - {option}")
            index = index + 1
        print()  # Add a blank line between categories

## Start
if __name__ == "__main__":
    yaml_data = read_yaml('your_file.yml')
    print_questions_and_options(yaml_data)
    save_to_yaml_file('output.yaml', {"key": "value", "list": [1, 2, 3]})
