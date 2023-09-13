#!/usr/bin/python3

def uniq_sum(my_list=[]):
    new_set = set(my_list)
    res = 0
    for element in new_set:
        res += element
    return res
