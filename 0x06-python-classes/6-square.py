#!/usr/bin/python3
"""a class Square that defines a square by: (based on 5-square.py)"""
class Square:
    """Representation of a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
        size (int): the new square size.
        position (int, int): position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter"""
        return (self.size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    @property
    def position(self):
        """getter"""
        return (self.position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(item, int) for item in value) or
                not all(item >= 0 for item in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value

    def area(self):
        """Return:  area of the square."""
        return (self.size * self.size)

    def my_print(self):
        """square with the # character."""
        if self.size == 0:
            print("")
            return

        [print("") for k in range(0, self.position[1])]
        for k in range(0, self.size):
            [print(" ", end="") for l in range(0, self.position[0])]
            [print("#", end="") for m in range(0, self.size)]
            print("")
