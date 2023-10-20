#!/usr/bin/python3
"""
a function that returns the JSON representation
of an object (string)
"""

import json


def load_from_json_file(filename):
    """Loads an object from a JSON file and returns the object."""
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
