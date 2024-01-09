#!/usr/bin/python3
""" checking inherited class """


def is_kind_of_class(obj, a_class):
    """Checking if an obj is an instance or inherited instance of a class.
    Args:
    obj: object
    a_class: class to compare
    Returns:
    Boolean
    """
    if isinstance(obj, a_class):
        return True
    return False
