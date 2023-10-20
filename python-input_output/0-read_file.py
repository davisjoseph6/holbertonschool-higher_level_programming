#!/usr/bin/python3
"""Defines a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """the function tha read a file"""
    with open(filename, 'r', encoding='utf-8') as file:
        file_read = file.read()
        print(file_read, end='')
