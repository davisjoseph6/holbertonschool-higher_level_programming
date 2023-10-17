#!/usr/bin/python3

def lookup(obj):
    attributes_and_methods = []
    for name in dir(obj):
        attr = getattr(obj, name)
        if callable(attr):
            attributes_and_methods.append(f"Method: {name}()")
        else:
            attributes_and_methods.append(f"Attribute: {name}")
    return attributes_and_methods
