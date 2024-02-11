#!/usr/bin/python3
"""BaseModel class"""
import uuid
from datetime import datetime
import json
import models

class BaseModel:
    """BaseModel of the project"""
    def __init__(self, *args, **kwargs):
        """__init__ method of class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """should print the following"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """dictionary containing all keys/values """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        if 'created_at' in obj_dict:
            obj_dict['created_at'] = self.created_at.isoformat()
        if 'updated_at' in obj_dict:
            obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    @staticmethod
    def load_from_file():
        """Load instances from JSON file"""
        try:
            with open("file.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
