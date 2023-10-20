#!/usr/bin/python3
"""
Script to add arguments to a Python list and save it as JSON
"""

import sys
import os

# Name of the JSON file to save the list
json_filename = 'add_item.json'

# Check if the JSON file exists and load its content, if any
if os.path.exists(json_filename):
    with open(json_filename, 'r') as file:
        my_list = eval(file.read())
else:
    my_list = []

# Append all command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
with open(json_filename, 'w') as file:
    file.write(repr(my_list))
