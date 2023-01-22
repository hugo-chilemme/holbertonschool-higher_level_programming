#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        i = 0
        for y in x:
            if i != len(x) - 1:
                print("{:d}".format(y), end=" ")
            else:
                print("{:d}".format(y), end="")
            i+=1
        print("")
