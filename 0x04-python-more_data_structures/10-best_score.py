#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    num = 0
    for i, j in a_dictionary.items():
        if j > num:
            num = j
    for i, j in a_dictionary.items():
        if j == num:
            return i
