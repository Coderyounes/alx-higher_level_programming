#!/usr/bin/python3

"""BaseGeometry is New Class """


class BaseGeometry:
    """
    Class has area() method that Raise an Exception
    """
    def area(self):
        raise Exception("area() is not implemented")
    """
    integer_validator function to validate integer
    Check if the value is int if not raise a TypeError
    Check if the value is less or equal zero if True raise ValueError
    """
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")