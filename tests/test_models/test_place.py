#!/usr/bin/python3
'''Testing place.py'''
import unittest
from models.place import Place


class testPlace(unittest.TestCase):
    '''Testing Place'''
    def test_city_id(self):
        '''Testing city_id attribute'''
        apt = Place()
        self.assertEqual(str, type(apt.city_id))
        self.assertIsNotNone(apt)

    def test_user_id(self):
        '''Testing user_id attribute'''
        apt = Place()
        self.assertEqual(str, type(apt.user_id))
        self.assertIsNotNone(apt.user_id)

    def test_name(self):
        '''Testing name attribute'''
        apt = Place()
        self.assertEqual(str, type(apt.name))
        self.assertIsNotNone(apt.name)

    def test_description(self):
        '''Testing description attribute'''
        apt = Place()
        self.assertEqual(str, type(apt.description))
        self.assertIsNotNone(apt.description)

    def test_number_rooms(self):
        '''Testing number_rooms attribute'''
        apt = Place()
        self.assertEqual(int, type(apt.number_rooms))
        self.assertIsNotNone(apt.number_rooms)

    def test_number_bathrooms(self):
        '''Testing number_bathrooms attribute'''
        apt = Place()
        self.assertEqual(int, type(apt.number_bathrooms))
        self.assertIsNotNone(apt.number_bathrooms)

    def test_max_guest(self):
        '''Testing max_guest attribute'''
        apt = Place()
        self.assertEqual(int, type(apt.max_guest))
        self.assertIsNotNone(apt.max_guest)

    def test_price_by_night(self):
        '''Testing price_by_night attribute'''
        apt = Place()
        self.assertEqual(int, type(apt.price_by_night))
        self.assertIsNotNone(apt.price_by_night)

    def test_latitude(self):
        '''Testing latitude attribute'''
        apt = Place()
        self.assertEqual(float, type(apt.latitude))
        self.assertIsNotNone(apt.latitude)

    def test_longitude(self):
        '''Testing longitude attribute'''
        apt = Place()
        self.assertEqual(float, type(apt.longitude))
        self.assertIsNotNone(apt.longitude)

    def test_amenity_ids(self):
        '''Testing amenity_ids attribute'''
        apt = Place()
        for i in apt.amenity_ids:
            self.assertEqual(str, type(apt.amenity_ids[i]))
        self.assertIsNotNone(apt.amenity_ids)


if __name__ == "__main__":
    unittest.main()
