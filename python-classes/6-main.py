#!/usr/bin/python3
Square = __import__('6-square').Square

try:
    my_square = Square(3, "Position")
except Exception as e:
    print(e)