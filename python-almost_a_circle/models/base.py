#!/usr/bin/python3
"""This will be my base class for almost_a_circle"""
import json


class Base:
    """This will be Base class ID keeper and i Initiate the
    Base.__nb_objects before i assign the self id to the number
    of instances there are"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            json_string = []

        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as f:
            list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(list)
            f.write(json_string)
