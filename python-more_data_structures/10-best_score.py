#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = 0
    value = None
    for k, v in a_dictionary.items():
        if v > max:
            value = k
            max = v
    return value
