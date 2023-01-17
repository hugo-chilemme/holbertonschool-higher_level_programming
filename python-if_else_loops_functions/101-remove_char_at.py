#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    start_witch = str[0:n]
    end_witch = str[n+1:len(str)]
    return start_witch + end_witch
