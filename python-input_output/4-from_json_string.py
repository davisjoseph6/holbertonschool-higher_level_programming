#!/usr/bin/python3
"""
a function that returns the JSON representation
of an object (string)
"""

import json


def from_json_string(my_str):
    """from jason"""
    return json.loads(my_str)
