#!/usr/bin/python3

""" converting from json module """
import json


def from_json_string(my_str):
    """
    func that returns a JSON object
    """
    return json.loads(my_str)
