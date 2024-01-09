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

    def to_json(self, attrs=None):

        if (type(attrs) == list and
                all(type(element_) == str for element_ in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        for m, q in json.items():
            setattr(self, m, q)
