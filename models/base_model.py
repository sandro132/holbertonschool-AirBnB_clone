#!/usr/bin/python3

import uuid
from datetime import datetime
import models

'''BaseModel'''

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            protected_attrs = ["created_at", "updated_at"]
            #Function to pop tha value of the class
            kwargs.pop('__class__', None)
            for k, v in kwargs.items():
                if k in protected_attrs:
                    #Function to traslade the format in value
                    setattr(self, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    #Function to adding any property to the  object
                    setattr(self, k, v)
            models.storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        # very important, this is the output predeterminate
        return "[{}] ({}) ({})".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        #This methot is for save the datatime
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        #a copy of the dictionary is created so as not to modify the original 
        # one and a value is assigned to the keys which are the instances created
        #and return the dictionary with the new va
        my_dictionary = self.__dict__.copy()
        my_dictionary["__class__"] = self.__class__.__name__
        my_dictionary["created_at"] = self.created_at.isoformat()
        my_dictionary["updated_at"] = self.updated_at.isoformat()
        return my_dictionary
