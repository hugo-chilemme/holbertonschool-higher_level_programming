#!/usr/bin/python3
MyTestClass = __import__('my_test_class_0').MyTestClass
class_to_json = __import__('8-class_to_json').class_to_json

def print_dict(d, t=0):
    keys = list(d.keys())
    keys.sort()
    for k in keys:
        v = d[k]
        if type(v) is dict:
            t += 1
            print_dict(v, t)
        else:
            print("{}{} => {} / {}".format("\t" * t, k, v, type(v)))


m = MyTestClass()
m.name = "John"
m.age = 89
mj = class_to_json(m)
print(type(mj) is dict)
print_dict(mj)