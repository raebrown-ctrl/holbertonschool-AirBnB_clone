#!/usr/bin/python3
"""
uinitest for the Amenity
"""



from models.amenity import Amenity
from datetime import datetime
from time import sleep
import unittest
import uuid

class Test_User(unittest.TestCase):
    """
    calss Test for User 
    """
     
    def test_name_is_public_str(self):
        self.assertEqual(str, type(Amenity.name))
