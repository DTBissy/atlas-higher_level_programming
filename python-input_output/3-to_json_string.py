#!/usr/bin/python3
"""This is a JSON file"""


import json

def to_json_string(my_obj):
    json_object = json.dump(my_obj)
    return json_object
