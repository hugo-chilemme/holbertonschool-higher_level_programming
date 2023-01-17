#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = 0
    for i in range(1, len(sys.argv)):
        count += int(sys.argv[i])
    print(count)
