#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or len(my_list) < idx:
        return None
    if my_list[idx]:
        return my_list[idx]
    return None
