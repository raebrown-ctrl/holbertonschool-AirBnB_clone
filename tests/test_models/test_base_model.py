#!/usr/bin/python3
'''Testing base_model.py'''
import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep


class TestBaseModel(unittest.TestCase):
    '''testing BaseModel'''
    def test_init(self):
        '''testing instances'''
        test_base = BaseModel()
        self.assertEqual(str, type(test_base.id))
        self.assertEqual(datetime, type(test_base.created_at))
        self.assertEqual(datetime, type(test_base.updated_at))

    def test_str(self):
        '''Testing __str__ method'''
        test_base = BaseModel()
        self.assertEqual(str(test_base), f"[BaseModel]\
 ({test_base.id}) {test_base.__dict__}")

    def test_to_dict(self):
        '''Testing to_dict method'''
        test_base = BaseModel()
        test_base_dict = test_base.to_dict()
        self.assertEqual(test_base_dict["created_at"],
                         test_base.created_at.isoformat())

    def test_save(self):
        """Testing to save method"""
        test_base = BaseModel()
        update = test_base.updated_at
        test_base.save()
        self.assertNotEqual(test_base.updated_at, update)


if __name__ == "__main__":
    unittest.main()
