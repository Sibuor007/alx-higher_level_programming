#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    curr_list = []
    if my_list:
        for item in my_list:
            curr_list.append(False if item % 2 else True)
        return curr_list
