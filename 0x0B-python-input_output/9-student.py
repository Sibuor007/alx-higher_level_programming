#!/usr/bin/python3
"""class Student module"""

class Student:
    """ the class body """

    def __init__(self, first_name, last_name, age):
        """initializing the constructor
        """
        self.s_first_name = first_name
        self.s_last_name = last_name
        self.s_age = age

    def to_json(self):
        return self.__dict__
