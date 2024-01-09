#!/usr/bin/python3
""" creates an Object from a “JSON file” """
import json

def load_from_json_file(filename):
    """from json to file"""
    with open(filename, encoding="utf-8") as file_:
        return json.load(file_)
