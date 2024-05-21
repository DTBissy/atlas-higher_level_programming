#!/usr/bin/python3
"""This defines a function that creates from JSON fle"""


import json


def load_from_json_file(filename):
    """THis creats a object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
