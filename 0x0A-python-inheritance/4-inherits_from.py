#!/usr/bin/python3

"""Function that check if the object is an of class that inherited"""


def inherits_from(obj, a_class):
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
