#!/usr/bin/python3
"""Review class difinition"""
from models.base_model import BaseModel

class Review(BaseModel):
    """ClASS that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """Reviw's init"""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
