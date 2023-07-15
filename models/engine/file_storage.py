#!/usr/bin/python3


from models.base_model import BaseModel
import json
from models.user import User


class FileStorage:
    '''CLass File storage'''
    def __init__(self):
        #a private class instance is created 
        # that fetches the json file we created
        self.__file_path = "file.json"
        #a empty dict is created in  a private class instance
        self.__objects = dict()

    def all(self):
        '''Return the dictionary'''
        return self.__objects

    def new(self, obj):
        '''The obj paramether is the base model'''
        # get propertys
        name_clase = type(obj).__name__
        id_obj = obj.id
        self.__objects[f"{name_clase}.{id_obj}"] = obj

    def save(self):
        '''save the file in the  __file__path'''
        #create a new empty dictionary
        new_dic = dict()
        #iteration the __objects items
        for k, v in self.__objects.items():
            #get the copy of the original dictionary
            obj_dict = v.to_dict()
            #adds the copy to new dict
            new_dic[k] = obj_dict
        #serialization the objects that is BaseModel
        serialized_obj = json.dumps(new_dic)
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            file.write(serialized_obj)

    def reload(self):
        '''load json and reload Model'''
        try:
            #open the file
            with open(self.__file_path, encoding="utf-8") as file:
                dict_data = json.loads(file.read())
                #iteration the items of the dict_data
                for k, v in dict_data.items():
                    #search the name of the class
                    class_name = v["__class__"]
                    self.__objects[k] = globals()[class_name](**v)
        except FileNotFoundError:
            pass
