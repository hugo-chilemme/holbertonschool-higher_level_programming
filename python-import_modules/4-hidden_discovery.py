#!/usr/bin/python3
import statistics  
import hidden_4

for name in dir(hidden_4):
    if name[:2] != "__":
        print(name)
