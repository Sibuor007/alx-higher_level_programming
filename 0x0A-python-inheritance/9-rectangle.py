#!/usr/bin/python3

""" import the BaseGeometry class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Body of rectangle class """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.s_width = width
        self.s_height = height

    def area(self):
        return self.s_width * self.s_height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.s_width, self.s_height)
