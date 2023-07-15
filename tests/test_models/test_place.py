#!/usr/bin/python3
"""
Unittest for Place
"""

import unittest
from models.place import Place
from datetime import datetime
from time import sleep


class testPlace(unittest.TestCase):
    """
    Test for Place
    """
    def test_str_city_id(self):
        """
        Check if city_id is a string
        """
        self.assertEqual(str, type(Place.city_id))

    def test_str_user_id(self):
        """
        Check if user_id is a string
        """
        self.assertEqual(str, type(Place.user_id))

    def test_str_name(self):
        """
        Check if name is a string
        """
        self.assertEqual(str, type(Place.name))

    def test_str_description(self):
        """
        Check if description is a string
        """
        self.assertEqual(str, type(Place.description))

    def test_int_number_rooms(self):
        """
        Check if number_rooms is a integer
        """
        self.assertEqual(int, type(Place.number_rooms))

    def test_int_number_bathrooms(self):
        """
        Check if number_bathrooms is a integer
        """
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_int_max_guest(self):
        """
        Check if max_guest is a integer
        """
        self.assertEqual(int, type(Place.max_guest))

    def test_int_price_by_night(self):
        """
        Check if price_by_night is a integer
        """
        self.assertEqual(int, type(Place.price_by_night))

    def test_float_latitude(self):
        """
        Check if latitude is a float
        """
        self.assertEqual(float, type(Place.latitude))

    def test_float_longitude(self):
        """
        Check if longitude is a float
        """
        self.assertEqual(float, type(Place.longitude))

    def test_list_amenity_ids(self):
        """
        Check if amenity_ids is a list of string
        """
        self.assertEqual(list, type(Place.amenity_ids))

    def test_unique_id(self):
        """
        Check if the review id in unique
        """
        instance1 = Place()
        instance2 = Place()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_instance_createdat(self):
        """
        Check if created_at is a intance of Place
        """
        self.assertTrue(hasattr(Place(), "created_at"), True)

    def test_instance(self):
        """
        Check if updated_at is a intance of Place
        """
        self.assertTrue(hasattr(Place(), "updated_at"), True)

    def test_public_datetime(self):
        """
        Test for a make public datetime
        """
        self.assertEqual(datetime, type(Place().created_at))

    def test_public_datetime_updated(self):
        """
        Test for a make public datetime
        """
        self.assertEqual(datetime, type(Place().updated_at))

    def test_less_time_createdat(self):
        """
        Check less time in created_at
        """
        instance1 = Place()
        sleep(0.2)
        instance2 = Place()
        self.assertLess(instance1.created_at, instance2.created_at)

    def test_less_time_updatedat(self):
        """
        Check less time in updated_at
        """
        instance1 = Place()
        sleep(0.2)
        instance2 = Place()
        self.assertLess(instance1.updated_at, instance2.updated_at)


if __name__ == '__main__':
    unittest.main()
