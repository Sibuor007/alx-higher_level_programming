#!/usr/bin/python3

"""writes an Object to a text file module """
import json

def save_to_json_file(my_obj, filename):
    """
        writes an Object to a text file, using a JSON representation
    """

    with open(filename, mode='w', encoding='utf-8') as file_:
        json.dump(my_obj, file_, ensure_ascii=False)
