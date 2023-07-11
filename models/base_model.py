#!/usr/bin/python3

import uuid
from datetime import datetime

'''BaseModel'''

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()
        
        '''if len(kwargs) != 0:
            for x, y in kwargs.items():
                if x == "created_at" or x == "updated_at":
                    self.__dict__[x] = datetime.strptime(y, x)
                else:
                    self.__dict__[x] = y
        else:'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()
        
    def __str__(self):
        return [{}] ({}) ({}).format(self.class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.update_at = datetime.now()
    
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