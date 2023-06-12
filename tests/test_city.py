#!/usr/bin/python3
"""
unittest for the city
"""



from models.city import City
from datetime import datetime
from time import sleep
import unittest
import uuid

class Test_User(unittest.TestCase):
    """
    class test for city 
    """
     
    def test_state_id(self):
        self.assertEqual(str, type(City.state_id))

    def test_name(self):
        self.assertEqual(str, type(City.name))

