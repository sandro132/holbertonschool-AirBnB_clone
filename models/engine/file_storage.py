#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""


#!/usr/bin/python3
""" Class FileStorage """

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json

classtype = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review,
}


class FileStorage:
    """ Define the class FileStorage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key """
        n_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(n_name, obj.id)] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        dict = {}
        for key, value in self.__objects.items():
            dict.update({key: value.to_dict()})
        with open(FileStorage.__file_path, "w") as file:
            json.dump(dict, file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    search = classtype[value["__class__"]](**value)
                    dict = {key: search}
                    self.__objects.update(dict)
        except Exception:
            pass

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
