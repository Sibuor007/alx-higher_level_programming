#!/usr/bin/python3
"""a class Square that defines a square by: (based on 4-square.py)"""

class Square:
    """Representation of a square."""
    def __init__(self, size):
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

    def print_code(self):
        """prints in stdout the square with the character #"""
        for k in range(0, self.size):
            [print("#", end="") for l in range(self.size)]
            print("")
        if self.size == 0:
            print("")
