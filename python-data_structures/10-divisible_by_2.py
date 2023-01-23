#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    callback = []
    for num in my_list:
        if num % 2 == 0:
            callback.append(True)
        else:
            callback.append(False)
    return callback
