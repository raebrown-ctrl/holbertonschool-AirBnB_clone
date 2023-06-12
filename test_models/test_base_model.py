#!/usr/bin/python3
"""
uinitest for the base moodel
"""

import unittest
import uuid
from datetime import datetime
from time import sleep

from models.base_model import BaseModel

class Test_BaseModel(unittest.TestCase):
    """
    calss Test for Base Model 
    """

    def test_id(self):
        """test the id"""
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1.id, id2.id)
    
    def test_save(self):
        """
        test save 
        """
        bm = BaseModel()
        sleep(0.1)
        update = bm.updated_at
        bm.save()
        self.assertLess(update, bm.updated_at)

    def test_tow_save(self):
        """
        test save if tow  
        """
        bm = BaseModel()
        sleep(0.1)
        update = bm.updated_at
        bm.save()
        update2 = bm.updated_at
        self.assertLess(update, bm.updated_at)
        sleep(0.1)
        bm.save()
        self.assertLess(update2, bm.updated_at)

    def test_three_save(self):
        """
        test save if tow  
        """
        bm = BaseModel()
        sleep(0.1)
        update = bm.updated_at
        bm.save()
        self.assertNotEqual(update, datetime.utcnow())

        
    def test_to_dict(self):
        """
        test to dict
        """
        bm = BaseModel()
        sleep(0.1)
        bm2 = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm2.to_dict())

    def test___str__(self):
        """
        test str 
        """
        bm = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm.__str__(), bm2.__str__())
        


if __name__ =='__main__':
    unittest.main()
