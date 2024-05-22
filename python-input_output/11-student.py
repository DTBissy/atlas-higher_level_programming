#!/usr/bin/python3
"""A class for student"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Instantation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Converts the current instance into a dictionary"""

        if attrs is None:
            attrs = ['first_name', 'last_name', 'age']

        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)

        return result

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)