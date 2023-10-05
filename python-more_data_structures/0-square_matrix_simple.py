#!/usr/bin/python3
def square(line):
    result = []
    for i in line:
       result.append(i ** 2)
    return result

def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    new_mat = map(square, matrix)
    result_mat = list(new_mat)
    return (result_mat)
