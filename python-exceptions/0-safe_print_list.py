#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for k, v in enumerate(my_list):
            if k < x:
                print("{}".format(v), end="")
                count += 1
        print()
        return (count)
    except:
        return (0)
