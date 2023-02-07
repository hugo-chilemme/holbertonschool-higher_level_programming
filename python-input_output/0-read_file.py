#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            print("{}".format(line))
