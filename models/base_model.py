#!/usr/bin/python3
"""BaseModel class"""
import uuid
from datetime import datetime
import models
import json


class BaseModel:
    """BaseModel of the project"""
    def __init__(self, *args, **kwargs):
        """Initialization method"""
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
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def str(self):
        """String representation of the instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """Updates the public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Dictionary containing all keys/values"""
        obj_dict = self.dict.copy()
        obj_dict['class'] = self.__class__.__name__
        for key, value in obj_dict.items():
            if isinstance(value, datetime):
                obj_dict[key] = value.isoformat()
        return obj_dict

    @staticmethod
    def load_from_file():
        """Load instances from JSON file"""
        try:
            with open(models.storage.__file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
