#!/usr/bin/python3
""" Check """
from models.base import Base
import json


res = Base.from_json_string(None)

if res is None:
    print("from_json_string doesn't return a list of dictionaries: {}".format(res))
    exit(1)

if type(res) is not list:
    print("from_json_string2 doesn't return a list of dictionaries: {}".format(res))
    exit(1)

if len(res) != 0:
    print("from_json_string3 doesn't return a list of dictionaries: {}".format(res))
    exit(1)

print("OK", end="")