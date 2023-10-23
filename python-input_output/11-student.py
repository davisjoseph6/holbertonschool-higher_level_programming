#!/usr/bin/python3
""" student class define """


class Student:
    """class define"""

    def __init__(self, first_name, last_name, age):
        """define parametre"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """define attr select"""
        if attrs is None:
            return self.__dict__
        else:
            new_attr = {}
            for i in attrs:
                if i in self.__dict__:
                    new_attr[i] = self.__dict__[i]
            return new_attr

    def reload_from_json(self, json):
        """ reload from json """
        for elem, value in json.items():
            setattr(self, elem, value)
