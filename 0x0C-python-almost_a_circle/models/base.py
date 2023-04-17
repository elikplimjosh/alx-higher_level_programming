#!/usr/bin/python3
"""
    Base Class Module for Object-Oriented Programming
"""

import json
import os.path


class Base:
    """
        Base Class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Instantiating an object of the Base Class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Converts a list of dictionaries to a list of objects as a JSON string
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
            Converts a JSON string of a list to a Python list of dictionaries
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Saves a list of objects as a JSON string to a file of class name
        """
        file_name = cls.__name__ + ".json"
        my_list = []
        if list_objs is not None:
            for obj in list_objs:
                my_list.append(obj.to_dictionary())
        with open(file_name, mode='w', encoding='utf-8') as my_file:
            my_file.write(cls.to_json_string(my_list))

    @classmethod
    def create(cls, **dictionary):
        """
            Creates an instance of a class from a dictionary of class data
        """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        else:
            obj = None
        if obj:
            obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
            Gets JSON string from file of class name,
            String is decoded to a list of dictionaries in Python.
            Each dictionary is used to create an instance of the class,
            a list of instances is returned
        """
        file_name = cls.__name__ + ".json"
        obj_list = []
        if os.path.exists(file_name):
            with open(file_name, 'r') as my_file:
                obj_list = cls.from_json_string(my_file.read())
            for i, obj_dict in enumerate(obj_list):
                obj_list[i] = cls.create(**obj_dict)
        return obj_list

