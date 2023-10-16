#!/usr/bin/python3
"""
   This module contains a matrix_divided(matrix, div)
   function witch divides all elements of a matrix,
   if matrix contains a non integer or float element
   a TypeError is raised. If rows are not of the same
   size, a TypeError is raised. If div is 0, a ZeroDivisionError
   is raised.
"""


def matrix_divided(matrix, div):
    """ Divides a matrix and returns a new matrix """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)
    return new_matrix
