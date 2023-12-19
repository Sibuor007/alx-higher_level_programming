#!/usr/bin/python3
"""a class Square that defines a square by: (based on 2-square.py)"""
class Square:
    """Representation of a square."""

    def __init__(self, size=0):
        """
        size (int):the new square size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    def area(self):
        """ area of the square."""
        return (self.size * self.size)
