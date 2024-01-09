#!/usr/bin/python3
""" inheritance from list class """

class MyList(list):
    """inheritance from list"""
    def print_sorted(self):
        """ print sorted list """
        print(sorted(self))
