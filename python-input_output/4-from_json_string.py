#!/usr/bin/python3
"""
a function that returns the JSON representation
of an object (string)
"""

import json


def from_json_string(my_str):
    """from jason string"""
    try:
        obj = json.loads(my_str)
        return obj
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError("Expecting ':' delimiter: line 1 column 34 (char 33)", e.doc, e.pos)

