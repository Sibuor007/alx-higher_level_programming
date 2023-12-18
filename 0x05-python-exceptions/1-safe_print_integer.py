#!/usr/bin/python3

def safe_print_integer(value):
    """Print with "{:d}".format().
    Args: value (int): The integer
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
