#!/usr/bin/python3

"""Define Our Base Class """


class Base:
    """
    Insatiate private Class attribute nb_object to 0
    Verify if id is not None to assign id value to self.id
    if it fail increment nb_object assign the value to self.id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
