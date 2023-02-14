#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(12, 14, 4, 5, 10)
if r is None:
    print("Can't create Rectangle")
    exit(1)

if r._Rectangle__height != 14:
    print("Wrong private height: {}".format(r._Rectangle__height))
    exit(1)

print(r.height)
if r.height != 14:
    print("Wrong height getter: {}".format(r._Rectangle__height))
    exit(1)

r.height = 5

if r._Rectangle__height != 5:
    print("Wrong private height: {}".format(r._Rectangle__height))
    exit(1)

if r.height != 5:
    print("Wrong height getter: {}".format(r._Rectangle__height))
    exit(1)

print("OK", end="")