#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""


import json
from models.base_model import BaseModel

class FileStorage():
    """This class manages storage of hbnb models in JSON forma"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the list of objects of one type of class.
        it's an optional filtering"""
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Loads storage dictionary from file"""

        classes = {
                'BaseModel': BaseModel
                }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
