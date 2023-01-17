#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num = 0
    if len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
    elif len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for arg in sys.argv:
        num += 1
        if num > 1:
            print("{}: {}".format(num - 1, arg))
