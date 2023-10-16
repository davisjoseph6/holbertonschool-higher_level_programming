#!/usr/bin/python3
""" say_my_name prints back the parameters
first_name followed by last_name
last_name is defaulted to an empty string
"""


def say_my_name(first_name, last_name=""):
    """Write a function that prints My name is <first name> <last name>"""
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))
