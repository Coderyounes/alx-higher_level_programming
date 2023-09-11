#!/usr/bin/python3

def max_integer(my_list=[]):
    max_num = my_list[0]
    if len(my_list) == 0:
        return None
    for i, num in enumerate(my_list):
        if num > max_num:
            max_num = num
    return max_num
