#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.
    Args: my_list (list): The list
    x (int): The number of elements
    Returns: The number of elements
    """
    result = 0
    for item in range(x):
        try:
            print("{}".format(my_list[item]), end="")
            result += 1
        except IndexError:
            break
    print("")
    return (result)
