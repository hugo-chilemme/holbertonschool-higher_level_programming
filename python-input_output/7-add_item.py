#!/usr/bin/python3
"""import"""

import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
arguments = sys.argv[1:]

f = open(filename, "a+")
f.close()

datas = []
try:
    datas = load_from_json_file(filename)
except:
    pass

for value in arguments:
    datas.append(value)
    
save_to_json_file(datas, filename)