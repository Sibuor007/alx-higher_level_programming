#!/usr/bin/python3
""" a class MyInt that inherits from int """

class MyInt(int):
    """ the MyInt class body """

    def _equal(self, item_):
        """ == is inverted """
        return self.real != item_

    def n_equal(self, item_):
        """ != is inverted """
        return self.real == item_
