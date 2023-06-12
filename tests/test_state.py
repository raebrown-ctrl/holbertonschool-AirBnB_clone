#!/usr/bin/python3
"""
uinitest for the State
"""



from models.state import State
from datetime import datetime
from time import sleep
import unittest
import uuid

class Test_User(unittest.TestCase):
    """
    calss Test for User 
    """
     
    def test_name_is_public_str(self):
        self.assertEqual(str, type(State.name))
