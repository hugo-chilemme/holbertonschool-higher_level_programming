#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    res = 0
    for i in my_list:
        in_array = False
        for i, val in enumerate(new_list):
            if val == i:
                in_array = True
        if in_array == False:
            res += i
            new_list.append(i)
    return res - 1

