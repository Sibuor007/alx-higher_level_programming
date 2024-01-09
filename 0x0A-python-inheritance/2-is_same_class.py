#!/usr/bin/python3
""" check if obj is instance of the class """

def is_same_class(obj, a_class):
    """ chekcing for instance of a specified class
    Args: 
        obj: the objecte to be checked
        a_class: the class in question

    return: boolean value
    """
    return type(obj) is a_class
