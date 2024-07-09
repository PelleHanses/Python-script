#!/usr/bin/python3
'''
create_csv.py
Creates a CSV from an array.
The file also have a example function for saving some info

The function can be included in other scripts like this:
    from handle_csv import create_csv_file
    result, csv_file_name = create_csv_file(MY_FILE)
'''

import csv

def create_csv_file(csv_array, file_name, verbose=0):
    # Specify the CSV file name
    csv_file_name = "./" + file_name

    # Check if csv_array is not empty
    if not csv_array:
        if verbose > 0:
            print("Error: The csv_array is empty.")
        return "CSV creation failed: csv_array is empty.", None

    # Get the fieldnames from the first dictionary
    fieldnames = csv_array[0].keys()

    # Open the CSV file for writing
    with open(csv_file_name, mode='w', newline='') as file:
        # Create a DictWriter object
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header (field names)
        writer.writeheader()

        # Write the rows (data)
        for row in csv_array:
            writer.writerow(row)

    if verbose > 0:
        print(f"    Data saved in {report_file_name}")
    return "CSV created successfully: " + csv_file_name, csv_file_name


## Start
csv_array = [
    {"Name": "Alice", "Age": 23, "Grade": "A"},
    {"Name": "Bob", "Age": 22, "Grade": "B"},
    {"Name": "Charlie", "Age": 24, "Grade": "C"},
]
csv_file = "my_file.csv"
result, csv_file_name = create_csv_file(csv_array, csv_file)
