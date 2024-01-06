#!/usr/bin/python3
"""
Rectangle class.
"""
class Rectangle:
    """Rectangle class: width and height."""
    num_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiation .
        """
        self.width = width
        self.height = height
        Rectangle.num_instances += 1

    def __str__(self):
        """informal string representation
        """
        if self.height__ == 0 or self.width__ == 0:
            return ''
        rect_ = ''
        for item in range(self.height__):
            for k in range(self.width__):
                rect_ += '#'
            rect_ += '\n'
        return rect_[:-1]

    def __repr__(self):
        """internal string rep
        """
        return "rectangle({}, {})".format(self.width__, self.height__)

    def __del__(self):
        """Deletes the instance."""
        print("Bye rectangle...")
        Rectangle.num_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the biggest Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
    @classmethod
    def square(cls, size=0):
        """ new Rectangle instance: width == height == size
        """
        return cls(size, size)
