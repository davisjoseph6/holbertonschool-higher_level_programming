#!/usr/bin/python3
"""
a function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean)
"""


def class_to_json(obj):
    """
    class to json
    """
    if isinstance(obj, object):
        # Get all attributes of the object
        obj_dict = {}
        for attr_name in dir(obj):
            attr = getattr(obj, attr_name)
            # Check if the attribute is of a serializable type
            if isinstance(attr, (int, str, bool, list, dict)):
                obj_dict[attr_name] = attr
        return obj_dict
    else:
        raise ValueError("Input is not an instance of a class")
