#!/usr/bin/python3
"""
a function that returns the JSON representation
of an object (string)
"""

import json


def save_to_json_file(my_obj, filename):
    """
    save an object to a JSON file.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
