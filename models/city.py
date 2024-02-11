#!/usr/bin/python3
from models.base_model import BaseModel
"""City class model"""


class City(BaseModel):
    """City class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
