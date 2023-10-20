#!/usr/bin/python3
"""A function that writes a string to file utf8 returns the number of char"""


def write_file(filename="", text=""):
    """the function tha read a file"""
    with open(filename, 'w', encoding='utf-8') as file:
        nb_characters = file.write(text)
    return nb_characters
