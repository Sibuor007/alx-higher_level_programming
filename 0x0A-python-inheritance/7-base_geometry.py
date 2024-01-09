#!/usr/bin/python3
""" an empty class BaseGeometry """

class BaseGeometry:
    """ class body """
    def area(self):
        """ area not implemented """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """validates value:
            you can assume name is always a string
            TypeError: value must be an integer
            ValueError: value must be greater than or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
