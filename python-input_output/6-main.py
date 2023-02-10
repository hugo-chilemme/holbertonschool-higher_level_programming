#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filemame = "file_0"
data = load_from_json_file(filemame)
print(type(data))
print(data)