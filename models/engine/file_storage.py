#!/usr/bin/python3
'''Python AirBnB Console Project'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    '''Serializes instances to a JSON file and
    deserializes JSON file to instances'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key
         <obj class name>.id'''
        obj_key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[obj_key] = obj

    def save(self):
        '''Serializes __objects to the JSON file'''
        dict_data = {}
        for k, v in self.__objects.items():
            dict_data[k] = v.to_dict()
        with open(self.__file_path, mode="w") as f:
            json.dump(dict_data, f)

    def reload(self):
        '''Deserializes the JSON file to __objects'''
        class_dict = {'BaseModel': BaseModel,
                      'User': User,
                      'State': State,
                      'City': City,
                      'Amenity': Amenity,
                      'Place': Place,
                      'Review': Review}
        try:
            with open(self.__file_path, mode="r") as f:
                json_dict = json.load(f)
                self.__objects = {}
                for k, v in json_dict.items():
                    self.__objects[k] = class_dict[v['__class__']](**v)
        except FileNotFoundError:
            pass
