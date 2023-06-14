#!/usr/bin/python3
'''Testing amenity.py'''
import unittest
from models.amenity import Amenity


class TestState(unittest.TestCase):
    '''Testing Amenity'''
    def test_name(self):
        '''Testing name attribute'''
        good = Amenity()
        self.assertEqual(str, type(good.name))
        self.assertIsNotNone(good.name)


if __name__ == "__main__":
    unittest.main()
