#!/usr/bin/python3
""" Class BaseModel """

import uuid
from datetime import datetime
import models


class BaseModel:
    """ Define the class BaseModel """

    def __init__(self, *args, **kwargs):
        """ Initialize the class BaseModel """
        dt_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for x, y in kwargs.items():
                if x == "created_at" or x == "updated_at":
                    self.__dict__[x] = datetime.strptime(y, dt_format)
                else:
                    self.__dict__[x] = y
        else:
            models.storage.new(self)

    def __str__(self):
        """ Return a string representation """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """ Updates the public instance attribute """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        my_dictionary = self.__dict__.copy()
        my_dictionary["__class__"] = self.__class__.__name__
        my_dictionary["created_at"] = self.created_at.isoformat()
        my_dictionary["updated_at"] = self.updated_at.isoformat()
        return (my_dictionary)