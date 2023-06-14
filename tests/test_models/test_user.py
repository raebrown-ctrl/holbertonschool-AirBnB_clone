#!/usr/bin/python3
'''Testing user.py'''
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    '''Testing User'''
    def test_email(self):
        '''Testing email attribute'''
        saitama = User()
        self.assertEqual(str, type(User.email))
        self.assertTrue(hasattr(saitama, 'email'))

    def test_password(self):
        '''Testing password attribute'''
        saitama = User()
        self.assertEqual(str, type(User.password))
        self.assertTrue(hasattr(saitama, 'password'))

    def test_first_name(self):
        '''Testing first_name'''
        saitama = User()
        self.assertEqual(str, type(User.first_name))
        self.assertTrue(hasattr(saitama, 'first_name'))

    def test_last_name(self):
        '''Testing last_name attribute'''
        saitama = User()
        self.assertEqual(str, type(User.last_name))
        self.assertTrue(hasattr(saitama, 'last_name'))


if __name__ == "__main__":
    unittest.main()
