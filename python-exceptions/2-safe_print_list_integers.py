#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            element = my_list[i]
            try:
                print("{:d}".format(element), end="")
                count += 1
            except:
                pass
        except (RuntimeError, TypeError, NameError):
            pass
    print()
    return count
