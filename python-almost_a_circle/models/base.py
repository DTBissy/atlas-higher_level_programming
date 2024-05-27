#!/usr/bin/python3
"""This will be my base class for almost_a_circle"""
import json


class Base:
    """This will be Base class ID keeper and i Initiate the
    Base.__nb_objects before i assign the self id to the number
    of instances there are"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id


    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "null"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as f:
            list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(list)
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return None
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list = cls.from_json_string(f.read())
                return [cls.create(**dictionary) for dictionary in list]
        except FileNotFoundError:
            return []
