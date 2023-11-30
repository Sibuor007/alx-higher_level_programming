f __name__ == "__main__":
    """Print infinite addition of args."""
    import sys

    result = 0
    for i in range(len(sys.argv) - 1):
        result += int(sys.argv[i + 1])
    print("{}".format(result))
