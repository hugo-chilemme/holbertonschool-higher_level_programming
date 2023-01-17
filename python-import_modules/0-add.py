#!/usr/bin/python3
add = __import__('add_0').add

a = 1
b = 2

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
