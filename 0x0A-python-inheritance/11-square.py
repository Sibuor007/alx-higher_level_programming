#!/usr/bin/python3
""" importing Rectangle class """
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """the square class body """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.s_size = size
