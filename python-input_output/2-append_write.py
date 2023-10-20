#!/usr/bin/python3
"""
a function that appends a string at the end
of a text file
(UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """append and write"""

    with open(filename, 'a', encoding='utf-8') as file:
        nb_characters_added = file.write(text)
    return nb_characters_added
