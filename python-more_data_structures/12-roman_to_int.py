#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_manuals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    if roman_string is None:
        return None
    roman_number = 0
    for letter in roman_string:
        if roman_manuals[letter]:
            roman_number += roman_manuals[letter]
    return roman_number
