#!/usr/bin/python3
if __name__ == "__main__":
    """output all names in hidden_4 module."""
    import hidden_4

    items = dir(hidden_4)
    for i in items:
        if i[:2] != "__":
            print(i)
