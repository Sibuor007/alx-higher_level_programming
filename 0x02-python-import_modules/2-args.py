#!/usr/bin/python3
if __name__ == "__main__":
    """Print the var_1 of and vector of arguments."""
    import sys

    var_1 = len(sys.argv) - 1
    if var_1 == 0:
        print("Arguments: 0")
    elif var_1 == 1:
        print("Arguments: 1")
    else:
        print("Arguments: {}".format(var_1))
    for i in range(var_1):
        rint("{}: {}".format(i + 1, sys.argv[i + 1]))
