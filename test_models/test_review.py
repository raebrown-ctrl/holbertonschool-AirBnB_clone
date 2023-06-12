#!/usr/bin/python3
"""
uinitest for the Review
"""



from models.review import Review
from datetime import datetime
from time import sleep
import unittest
import uuid

class Test_User(unittest.TestCase):
    """
    calss Test for Review
    """
     
    def test_place_id(self):
        self.assertEqual(str, type(Review.place_id))

    def test_user_id(self):
        self.assertEqual(str, type(Review.user_id))


    def test_text(self):
        self.assertEqual(str, type(Review.text))

