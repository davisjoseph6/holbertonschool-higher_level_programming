#!/usr/bin/python3
"""Defines a function that writes a string to file (UTF8) and returns the number of char"""


def write_file(filename="", text=""):
    """the function tha read a file"""
    with open(filename, 'w', encoding='utf-8') as file:
        nb_characters = file.write(text)
    return nb_characters

