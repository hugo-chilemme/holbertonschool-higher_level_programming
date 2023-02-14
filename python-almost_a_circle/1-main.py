#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(12, 14, 4, 5, 10)
if r is None:
    print("Can't create Rectangle")
    exit(1)

if r._Rectangle__x != 4:
    print("Wrong private x: {}".format(r._Rectangle__x))
    exit(1)

if r.x != 4:
    print("Wrong x getter: {}".format(r._Rectangle__x))
    exit(1)

r.x = 5

if r._Rectangle__x != 5:
    print("Wrong private x: {}".format(r._Rectangle__x))
    exit(1)

if r.x != 5:
    print("Wrong x getter: {}".format(r._Rectangle__x))
    exit(1)

print("OK", end="")