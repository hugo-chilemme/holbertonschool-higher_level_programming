#!/usr/bin/python3
Student = __import__('11-student').Student

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


student = Student("John", "Snow", 25)
j_student = student.to_json()
print_dict(j_student)

f_student = Student("J", "S", 1)
j_f_student = f_student.to_json()
print_dict(j_f_student)

f_student.reload_from_json(j_student)
j_f_student = f_student.to_json()
print_dict(j_f_student)
print_dict(f_student.__dict__)