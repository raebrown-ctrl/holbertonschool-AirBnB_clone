#!/usr/bin/python3
'''Testing user.py'''
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    '''Testing City'''
    def test_state_id(self):
        '''Testing state_id attribute'''
        tulsa = City()
        self.assertEqual(str, type(tulsa.state_id))
        self.assertIsNotNone(tulsa.state_id)

    def test_name(self):
        '''Testing name attribute'''
        tulsa = City()
        self.assertEqual(str, type(tulsa.name))
        self.assertIsNotNone(tulsa.name)


if __name__ == "__main__":
    unittest.main()
