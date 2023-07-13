#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """A base class for all hbnb models"""
    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        storage.save()
        storage.new(self)

    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        storage.new(self)
        
    def __str__(self):
        return "[{}] ({}) ({})".format(self.__class__.__name__, self.id, self.__dict__)
    
    
    def to_dict(self):
        my_dictionary = self.__dict__.copy()
        my_dictionary["__class__"] = self.__class__.__name__
        my_dictionary["created_at"] = self.created_at.isoformat()
        my_dictionary["updated_at"] = self.updated_at.isoformat()
        return my_dictionary
