#!/usr/bin/python3
"""THis returns a JSON file from a string"""


import json


def from_json_string(my_str):
    """THis will do it"""
    json_string = json.loads(my_str)
    return json_string