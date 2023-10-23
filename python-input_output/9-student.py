#!/usr/bin/python3
""" def class student """


class Student:
    """ write parametre student class """
    def __init__(self, first_name, last_name, age):
        """ def attribut """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """def dict return """
        return self.__dict__
