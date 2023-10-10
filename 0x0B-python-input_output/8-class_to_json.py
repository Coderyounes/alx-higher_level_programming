#!/usr/bin/python3
""" Define our function & Import all modules needed"""
import json


def class_to_json(obj):
    """
    Class to json function is function that take instance
    of class and convert into json represetation
    using json.dumps.
    we take:
        obj: the instace of the classe
        __dict__ : to be selective & include only object that has
        dictionnary representation
    """
    return json.dumps(obj.__dict__)
