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
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle is an inheretant from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initialize the inheret Class
        use the integer validator methods
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
