#!/usr/bin/python3
""" Check """
from models.square import Square

s = Square(12)
if s is None:
    print("Can't create Square")
    exit(1)

for attribute in list(s.__dict__.keys()):
    if "size" in attribute:
        print("You are not allowed to add any new attribute for size: {}".format(attribute))
        exit(1)

if s.size != 12:
    print("Wrong size getter: {}".format(s.size))
    exit(1)

s.size = 5

if s.size != 5:
    print("Wrong size getter: {}".format(s.size))
    exit(1)

print("OK", end="")