#!/usr/bin/python3
def no_c(my_string):
    curr_string = ""
    for items in my_string:
        if items != "c" and items != "C":
            curr_string += items
    return curr_string
