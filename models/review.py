#!/usr/bin/python3
"""
hbnb clone
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review"""
    place_id = ""
    user_id = ""
    text = ""
