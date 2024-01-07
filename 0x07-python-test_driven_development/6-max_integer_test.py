#!/usr/bin/python3
"""find the max integer in a list
"""

def max_integer(list=[]):
    """Function to find and return the max integer
    """
    if len(list) == 0:
        return None
    outcome = list[0]
    i = 1
    while i < len(list):
        if list[i] > outcome:
            outcome = list[i]
            i += 1
    return outcome
