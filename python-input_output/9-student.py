#!/usr/bin/python3
"""A class for student"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Instantation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return vars(self)
