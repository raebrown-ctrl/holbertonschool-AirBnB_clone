#!/usr/bin/python3
'''Testing review.py'''
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    '''Testing Review'''
    def test_place_id(self):
        '''Testing place_id attribute'''
        rev = Review()
        self.assertEqual(str, type(rev.place_id))
        self.assertIsNotNone(rev.place_id)

    def test_user_id(self):
        '''Testing user_id attribute'''
        rev = Review()
        self.assertEqual(str, type(rev.user_id))
        self.assertIsNotNone(rev.user_id)

    def test_text(self):
        '''Testing text attribute'''
        rev = Review()
        self.assertEqual(str, type(rev.text))
        self.assertIsNotNone(rev.text)


if __name__ == "__main__":
    unittest.main()
