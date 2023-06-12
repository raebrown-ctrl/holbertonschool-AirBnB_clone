#!/usr/bin/python3
"""
    import module
"""
from models.base_model import BaseModel


"""
    User class File
"""


class User(BaseModel):
    """
        class User inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
