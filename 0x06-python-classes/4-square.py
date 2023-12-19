#!/usr/bin/python3
"""a class Square that defines a square by: (based on 3-square.py)"""
class Square:
    """Representation of a square."""
    def __init__(self, size=0):
        """
        Args:
        size (int): the new square size.
        """
        self.size = size

    @property
    def size(self):
        """getter method for the size"""
        return (self.size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    def area(self):
        """Return: area of the square."""
        return (self.size * self.size)
