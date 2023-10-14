#!/usr/bin/python3

"""Define Square Class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    inisialize the attributes to 0 or None
    use super() to inherent some attribute property
    use __str__ magic method to display a Good looking output
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        name = "[Square]"
        v_id = "(" + str(self.id) + ")"
        x_y = str(self.x) + "/" + str(self.y)
        v_size = str(self.size)
        resu = name + " " + v_id + " " + x_y + " " + "-" + " " + v_size
        return resu

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
