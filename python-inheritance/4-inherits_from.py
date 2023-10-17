#!/usr/bin/python3
""" a function that returns True if the object"""
"""is an instance of a class that inherited (directly or indirectly)"""
"""from the specified class ; otherwise False."""


def inherits_from(obj, a_class):
    """Get the class of the object"""
    obj_class = type(obj)

    """Check if the object's class is the same as the specified class"""
    if obj_class is a_class:
        return False

    return issubclass(obj_class, a_class)
