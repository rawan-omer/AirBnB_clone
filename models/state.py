#!/usr/bin/python3
"""New class definition"""
from models.base_model import BaseModel


class State(BaseModel):
    """State CLASS """
    def __init__(self, *args, **kwargs):
        """ State's Initializes"""
        super().__init__(*args, **kwargs)
        self.name = ""
