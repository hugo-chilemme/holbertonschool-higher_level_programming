#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

list = [1, 2, 3]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(list, idx)))