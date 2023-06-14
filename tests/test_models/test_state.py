#!/usr/bin/python3
'''Testing state.py'''
import unittest
from models.state import State


class TestState(unittest.TestCase):
    '''Testing State'''
    def test_name(self):
        '''Testing state attribute'''
        texas = State()
        self.assertEqual(str, type(texas.name))
        self.assertIsNotNone(texas.name)


if __name__ == "__main__":
    unittest.main()
