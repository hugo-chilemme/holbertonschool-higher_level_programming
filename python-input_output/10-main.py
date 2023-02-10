#!/usr/bin/python3
Student = __import__('10-student').Student

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

student = Student("Tom", "Smith", 89)

j_student = student.to_json([])
print(type(j_student))
print_dict(j_student)