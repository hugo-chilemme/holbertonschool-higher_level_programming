#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = []
    for i in range(0, list_length):
        Result = 0
        try: 
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]
            if element_2 == 0:
                print("devision by 0")
                Result = 0
            else:
                try: 
                    Result = element_1 / element_2
                except:
                    print("wrong type")
                    Result = 0
        except:
            print("out of range")
        finally:
            list.append(Result)
    return list
