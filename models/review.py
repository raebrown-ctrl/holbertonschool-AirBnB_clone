#!/usr/bin/python3
"""
    import module
"""
from models.base_model import BaseModel


"""
    Review class file
"""


class Review(BaseModel):
    """
        Review class inherit from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
