#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)"""

def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
    """
    with open(filename, "w", encoding="utf-8") as file_:
        return file_.write(text)
