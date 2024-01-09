#!/usr/bin/python3
"""adds all arguments to a Python list module """
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        file__ = load_from_json_file("add_item.json")
    except FileNotFoundError:
        file__ = []
    file__.extend(sys.argv[1:])
    save_to_json_file(file__, "add_item.json")
