#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    item = sorted(a_dictionary)
    for i in item:
        print("{}: {}".format(i, a_dictionary[i]))
