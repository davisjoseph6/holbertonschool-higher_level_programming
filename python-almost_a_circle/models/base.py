#!/usr/bin/python3
"""Base module"""

import json


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ from jason strong"""
        if json_string is None or json_string == "":
            return[]
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save to file
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_str = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
                )

        with open(filename, "w") as file:
            file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """ Create a dummy instance with mandatory attributes """
        if cls.__name__ == "Rectangle":
            obj = cls(2, 3)
        else:
            obj = cls(3)
        obj.update(**dictionary)
        return obj
