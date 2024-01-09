#!/usr/bin/python3
""" dictionary description module """

def class_to_json(obj):
    """ function that returns the dictionary description """
    return obj.__dict__
