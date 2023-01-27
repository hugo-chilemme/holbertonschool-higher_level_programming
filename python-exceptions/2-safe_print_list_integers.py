#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for k, v in enumerate(my_list):
        if k < x:
            try:
                print("{:d}".format(v), end="")
                if type(v) is int:
                    count += 1
            except:
                continue
    print()
    return count
