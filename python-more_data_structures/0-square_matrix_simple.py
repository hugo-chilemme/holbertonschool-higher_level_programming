#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    string = "["
    i = 0
    for y in matrix:
        j = 0
        string += "["
        for x in y:
            string += str(x ** 2)
            if j < len(y) - 1:
                string += ", "
            j += 1
        string += "]"
        if i < len(matrix) - 1:
            string += ", "
        i += 1
    string += "]"
    return string
