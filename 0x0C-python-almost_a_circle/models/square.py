#!/usr/bin/python3
""" introducing the Square class """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ representing the Square class body"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of Square class
        Args:
            size (int): The size
            x (int): The x coordinate
            y (int): The y coordinate
            id (int): The identity
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter the size of the Square."""
        return self.width

    @size.setter
    def size(self, number_):
        self.width = number_
        self.height = number_

    def update(self, *args, **kwargs):
        """for Updating the Square.

        Args:
            *args (ints): New attribute sizes
                - 1st argument = id attribute
                - 2nd argument = size attribute
                - 3rd argument = x attribute
                - 4th argument = y attribute
            **kwargs (dict): New key/value pairs
        """
        if args and len(args) != 0:
            num = 0
            for arg in args:
                if num == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif num == 1:
                    self.size = arg
                elif num == 2:
                    self.x = arg
                elif num == 3:
                    self.y = arg
                num += 1

        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    if j is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = j
                elif i == "size":
                    self.size = j
                elif i == "x":
                    self.x = j
                elif i == "y":
                    self.y = j

    def to_dictionary(self):
        """ return the dictionary representation """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """ the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
