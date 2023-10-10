#!/usr/bin/python3


""" function read from a file"""


def read_file(filename=""):
    """
    read_file function , simple function read text from file
    the file is in filename argument
    """
    with open(filename, "r") as f:
        data = f.read()
    print(data)
