#!/usr/bin/python3
"""
unittest for the review
"""



from models.review import Review
from datetime import datetime
from time import sleep
import unittest
import uuid

class Test_User(unittest.TestCase):
    """
    class test for review
    """
     
    def test_place_id(self):
        self.assertEqual(str, type(Review.place_id))

    def test_user_id(self):
        self.assertEqual(str, type(Review.user_id))


    def test_text(self):
        self.assertEqual(str, type(Review.text))
