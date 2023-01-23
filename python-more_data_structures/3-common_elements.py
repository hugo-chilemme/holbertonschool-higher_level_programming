#!/usr/bin/python3
def common_elements(set_1, set_2):
    callback = []
    for i in set_1:
         for j in set_2:
             if j == i:
                callback.append(i)
    return callback
