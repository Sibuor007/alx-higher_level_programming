#!/usr/bin/python3
"""
Rectangle class.
"""
class Rectangle:
    """Rectangle class: width and height."""

    def __init__(self, width=0, height=0):
        """Instantiation .
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width """
        return self.width__

    @width.setter
    def width(self, value):
        """Sets the width
        Args:
        value: value of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width__ = value

    @property
    def height(self):
        """Retrieves the height"""
        return self.height__

    @height.setter
    def height(self, value):
        """Sets the height
        Args:
        value: value of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height__ = value

    def area(self):
        """Calculates the area of a Rectangle
        Returns:
        Area of the the rectangle
        """
        return self.width__ * self.height__

    def perimeter(self):
        """Calculates the perimeter of a Rectangle
        Returns:
        Perimeter of the rectangle
        """
        if self.height__ == 0 or self.width__ == 0:
            return 0
        return 2 * (self.width__ + self.height__)
