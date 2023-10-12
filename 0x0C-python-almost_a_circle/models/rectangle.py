#!/usr/bin/python3

"""Define New Class Rectancle Inheret from base """
from models.base import Base


class Rectangle(Base):
    """
    instatiate all rectangle attributes & make them private attribute
    use the super() to get from id value from base
    setup all private attribute Getter & setter one by one
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width_get(self):
        return self.__width

    @width_get.setter
    def width_get(self, newwidth):
        self.__width = newwidth

    @property
    def height_get(self):
        return self.__height

    @height_get.setter
    def height_get(self, newheight):
        self.__height = newheight

    @property
    def x_get(self):
        return self.__x

    @x_get.setter
    def x_get(self, new_x):
        self.__x = new_x

    @property
    def y_get(self):
        return self.__y

    @y_get.setter
    def y_get(self, new_y):
        self.__y = new_y
