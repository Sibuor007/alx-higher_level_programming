#!/usr/bin/python3
"""  a function that appends a string at the end of a text file """

def append_write(filename="", text=""):
    """Appends a string.
    """
    with open(filename, "a", encoding="utf-8") as file_:
        return file_.write(text)
