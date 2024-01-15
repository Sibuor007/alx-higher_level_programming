#!/usr/bin/python3
""" introducing the Rectangle class """
from models.base import Base

class Rectangle(Base):
    """ Rectangle class that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Used to initialize a new Rectangle - instance

        Args:
            width (int): The width
            height (int): The height
            x (int): The x coordinate
            y (int): The y coordinate
            id (int): The identity
        Raises:
            TypeError: width or height must be an int.
            ValueError: width or height <= 0.
            TypeError: x or y must be an int.
            ValueError: x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, number):
        if type(number) != int:
            raise TypeError("width must be an integer")
        if number <= 0:
            raise ValueError("width must be > 0")
        self.__width = number

    @property
    def height(self):
        """getter the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, number):
        if type(number) != int:
            raise TypeError("height must be an integer")
        if number <= 0:
            raise ValueError("height must be > 0")
        self.__height = number

    @property
    def x(self):
        """getter the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, number):
        if type(number) != int:
            raise TypeError("x must be an integer")
        if number < 0:
            raise ValueError("x must be >= 0")
        self.__x = number

    @property
    def y(self):
        """getter the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, number):
        if type(number) != int:
            raise TypeError("y must be an integer")
        if number < 0:
            raise ValueError("y must be >= 0")
        self.__y = number

    def area(self):
        """ method to get area of rectangle """
        return self.width * self.height

    def display(self):
        """ method to print rect in `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for item in range(self.y)]
        for item_ in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update for the Rectangle.

        Args:
            *args (ints): New attribute numbers.
                - 1st argument = id attribute
                - 2nd argument = width attribute
                - 3rd argument = height attribute
                - 4th argument = x attribute
                - 5th argument = y attribute
            **kwargs (dict): key/number pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for item in args:
                if a == 0:
                    if item is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = item
                elif a == 1:
                    self.width = item
                elif a == 2:
                    self.height = item
                elif a == 3:
                    self.x = item
                elif a == 4:
                    self.y = item
                a += 1

        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    if j is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = j
                elif i == "width":
                    self.width = j
                elif i == "height":
                    self.height = j
                elif i == "x":
                    self.x = j
                elif k == "y":
                    self.y = j

    def to_dictionary(self):
        """Return the dictionary representation """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """ print() and str() representation of the Rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
