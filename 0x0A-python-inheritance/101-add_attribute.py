#!/usr/bin/python3
""" a function that adds a new attribute to an object if it’s possible """

def add_attribute(object, attr_, value_):
    """add a new attribute to an object if possible.
    Raises:
        TypeError:  if the object can’t have new attribute
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attr_, value_)
