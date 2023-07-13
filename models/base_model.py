#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage

'''BaseModel'''

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            protected_attrs = ["created_at", "updated_at"]
            kwargs.pop('__class__', None)
            for k, v in kwargs.items():
                if k in protected_attrs:
                    setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        storage.new(self)

    def __str__(self):
        return "[{}] ({}) ({})".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        my_dictionary = self.__dict__.copy()
        my_dictionary["__class__"] = self.__class__.__name__
        my_dictionary["created_at"] = self.created_at.isoformat()
        my_dictionary["updated_at"] = self.updated_at.isoformat()
        return my_dictionary
