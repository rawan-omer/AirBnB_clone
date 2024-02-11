#!/usr/bin/python3
from models.base_model import BaseModel
"""class Amenity model """


class Amenity(BaseModel):
    """class Amenity"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
