#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    curr_dict = dict(a_dictionary)
    for i, j in curr_dict.items():
        curr_dict[i] = j * 2
    return curr_dict
