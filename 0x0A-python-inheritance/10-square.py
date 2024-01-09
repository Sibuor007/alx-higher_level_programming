#!/usr/bin/python3

""" a class Square that inherits from Rectangle (9-rectangle.py) """
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ the square class body """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.s_size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        return self.s_size * self.s_size
