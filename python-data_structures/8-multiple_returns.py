#!/usr/bin/python3
def multiple_returns(sentence):
    first_letter = None
    if sentence[0]:
        first_letter = sentence[0]
    return len(sentence), first_letter
