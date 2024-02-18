#!/usr/bin/python3
"""BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime
import json


class BaseModel:
    """BaseModel of the project"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel"""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

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
        obj_dict['class'] = self.__class__.__name__
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
