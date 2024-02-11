#!/usr/bin/python3
"""new class that define more attribuets"""
from models.base_model import BaseModel


class User(BaseModel):
    """OUR User CLASS"""
    def __init__(self, *args, **kwargs):
        """The instance of User class"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
