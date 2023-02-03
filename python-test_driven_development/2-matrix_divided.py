#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    size = None
    new_matrix = []
    j = 0
    for i in matrix:
        new_matrix.append([])
        if size and size != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        size = len(i)
        for element in i:
            if not isinstance(div, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix[j].append(round(element / div, 2))
        j += 1 
    return new_matrix
    