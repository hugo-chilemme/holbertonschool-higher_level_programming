#!/usr/bin/python3
def uniq_add(my_list=[]):
    redlist = []
    for num in my_list:
        find = False
        for val in redlist:
            if val == num:
                find = True
        if find is False:
            redlist.append(num)
    res = 0
    for val in redlist:
        res += val
    return res
