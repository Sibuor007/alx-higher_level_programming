#!/usr/bin/python3
"""function that prints a square with the character #"""

def print_square(size):
    """Print a square with #
    Args:
    The height/width of the square.
    Raises:
    TypeError
    ValueError
    """
    if not isinstance(size, int):
    raise TypeError("size must be an integer")
    if size < 0:
    raise ValueError("size must be >= 0")

    for item in range(size):
    [print("#", end="") for item_0 in range(size)]
    print("")
