#!/usr/bin/python3
"""FileStorage serializes instances to JSON and deserializes JSON """
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """FileStorage CLASS attribuets"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all function's definition"""
        return FileStorage.__objects

    def new(self, obj):
        """new function's definition"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """save function's definition"""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """reload function's definition"""
        with open(FileStorage.__file_path, 'r') as file:
            data = json.load(file)
            for key, obj_dict in data.items():
                class_name, obj_id = key.split('.')
                class_obj = globals().get(class_name)
                if class_obj:
                    obj = class_obj(**obj_dict)
                    FileStorage.__objects[key] = obj
                else:
                    raise ValueError("Class '" + class_name + "' not found.")
