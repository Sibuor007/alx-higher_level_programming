#!/usr/bin/python3
def search_replace(my_list, search, replace):
    curr_list = list(my_list)
    for i in range(len(curr_list)):
        if curr_list[i] == search:
            curr_list[i] = replace
    return curr_list
