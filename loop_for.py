#!/usr/bin/python3
"""
loop_for.py
Examples of loops with for.

The function can be included in other scripts like this:
    from loop_for import loop_array, loop_array_dict, loop_list, loop_n
    result = loop_array(array_to_loop)
    result = loop_array_dict(array_to_loop)
    result = loop_list(list_to_loop)
    result = loop_n(nr_of_loops)
"""

import array

def loop_array(array_to_loop):
    """
    Loops through an array
    """
    print("Loops array")
    for element in my_array:
        print(f"  {element}")
    return True

def loop_array_dict(array_to_loop):
    """
    Loops through an array of dictionaries
    """
    print("Loops array of dictionaries")
    for element in array_to_loop:
        for key, value in element.items():
            print(f"  {key}: {value}")
        print()  # Add a blank line between each dictionary for readability
    return True

def loop_list(list_to_loop):
    """
    Loop through the list
    """
    print("Loops through a list")
    for element in list_to_loop:
        print(f"  {element}")
    return True

def loop_n(nr_of_loops):
    """
    Loop n times
    """
    print(f"Loops {nr_of_loops} times")
    for i in range(nr_of_loops):
        print(f"  Iteration {i + 1}")
    return True


## Start
# Define an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])
loop_array(my_array)

# Define an array of dictionaries
my_arraydict = [
    {"Name": "Alice", "Age": 23, "Grade": "A"},
    {"Name": "Bob", "Age": 22, "Grade": "B"},
    {"Name": "Charlie", "Age": 24, "Grade": "C"},
]
loop_array_dict(my_array_dict)

# Define a list of strings
my_list = ["apple", "banana", "cherry", "date", "elderberry"]
loop_list(my_list)

# Define number of loops
nr_of_loops = 10
loop_n(nr_of_loops)
