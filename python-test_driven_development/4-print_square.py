#!/usr/bin/python3
'''Write a function that print a square with the character #'''


def print_square(size):
    '''def and print square of size'''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print("#" * size)
