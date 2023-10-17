#!/usr/bin/python3


def inherits_from(obj, a_class):
    obj_class = type(obj)

    while obj_class is not None:
        if obj_class is a_class:
            return True
        obj_class = obj_class.__base__  # Get the base class
    return False
