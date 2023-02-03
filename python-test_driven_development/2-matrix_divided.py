#!/usr/bin/python3
"""matrix_divided"""


def matrix_divided(matrix=[], div=1):
    """Return new matrix with value divided by @div"""
    if not isinstance(div, (int, float)) or div is None:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    error = "matrix must be a matrix (list of lists) of integers/floats"
    size = None
    new_matrix = []
    j = 0
    for i in matrix:
        new_matrix.append([])
        if size and size != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        size = len(i)
        for element in i:
            if not isinstance(element, (int, float)):
                raise TypeError(error)
            new_matrix[j].append(round(element / div, 2))
        j += 1
    return new_matrix
